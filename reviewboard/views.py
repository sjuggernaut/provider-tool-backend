from .serializers import *
import copy
from documents.serializers import ReviewBoardReferralFormsDocumentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
import json
from rest_framework import generics
from documents.models import ReviewBoardReferralFormsDocuments
from providertool.errors import default_error_response
from clientpatient.models import Client
from authentication.serializers import RegistrationSerializer
import string
import random
from providertool.errors import default_error_response
from authentication.models import User


class ClientReferralList(generics.ListCreateAPIView):
    """
    List all client referral.
    """
    queryset = ClientReferral.objects.all()
    serializer_class = ClientReferralSerializer


class ClientReferralListUserFilter(generics.ListAPIView):
    """
    List all client referral by user.
    """
    queryset = ClientReferral.objects.all()
    serializer_class = ClientReferralSerializer

    def get_queryset(self):
        try:
            queryset = super(ClientReferralListUserFilter, self).get_queryset()
            review_board_user = self.kwargs['pk']
            return queryset.filter(review_board_user=review_board_user)
        except Exception as e:
            print(e)
            return []

    def list(self, request, *args, **kwargs):
        retrieve_response = super().list(request, *args, **kwargs)
        if retrieve_response:
            return Response({
                'status': 200,
                'data': retrieve_response.data
            })
        else:
            return Response({
                'status': 200,
                'data': []
            })


class ClientReferralRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve client referral detail.
    """
    queryset = ClientReferral.objects.all()
    serializer_class = ClientReferralSerializer

    def retrieve(self, request, *args, **kwargs):
        referral = super().get_object()

        retrieve_response = super().retrieve(request, *args, **kwargs)
        return Response({
            'status': 200,
            'data': retrieve_response.data
        })

    def update(self, request, *args, **kwargs):
        retrieve_response = super().update(request, *args, **kwargs)

        if retrieve_response.status_code == 200:
            if 'referral_forms' in request.data:
                referral_forms = request.data['referral_forms']
                client_referral_id = kwargs.get('pk')
                client_referral_object = ClientReferral.objects.get(referral_id=client_referral_id)
                ReviewBoardReferralFormsDocuments.objects.filter(client_referral=client_referral_object).delete()
                ClientReferralCreate.create_referral_forms(client_referral_object, referral_forms)

        return Response({
            'status': 200,
            'data': retrieve_response.data
        })


class ClientReferralCreate(APIView):
    """
    Create a new client referral.
    """

    def password_generator(self, length=8):
        '''
        Generates a random password having the specified length
        :length -> length of password to be generated. Defaults to 8
            if nothing is specified.
        :returns string <class 'str'>
        '''
        LETTERS = string.ascii_letters
        NUMBERS = string.digits

        # create alphanumerical from string constants
        printable = f'{LETTERS}{NUMBERS}'

        # convert printable from string to list and shuffle
        printable = list(printable)
        random.shuffle(printable)

        # generate random password and convert to string
        random_password = random.choices(printable, k=length)
        random_password = ''.join(random_password)
        return random_password

    def post(self, request):
        try:
            if 'data' not in request.data:
                return Response({
                    'result': False,
                    'message': 'Invalid client referral request data'
                }, status=HTTP_400_BAD_REQUEST)

            serializer = ClientReferralSerializer(data=request.data['data'])
            if serializer.is_valid():
                client_referral = serializer.save()

                if client_referral:
                    forms_request_data = request.data["referral_forms"]
                    forms_create_result = ClientReferralCreate.create_referral_forms(client_referral,
                                                                                     forms_request_data)

                    if forms_create_result:
                        """
                        Based on Decision value - 
                        POTENTIAL_CLIENT: create client account in inactive status
                        ACTIVE_CLIENT: 
                        DISCHARGED_CLIENT:
                        """
                        client_referral_data = ClientReferralSerializer(client_referral).data
                        client_referral_decision = client_referral_data.get('decision')
                        client_email = client_referral_data.get('client_email')
                        client_username = client_email.split("@")[0]

                        registration_data = {
                            "email": client_email,
                            "username": client_username,
                            "first_name": client_referral_data.get('client_first_name'),
                            "last_name": client_referral_data.get('client_last_name'),
                            "password": self.password_generator(16),
                            "user_type": "TYPE_CLIENT"
                        }
                        client_creation_serializer = RegistrationSerializer(data=registration_data)

                        if client_creation_serializer.is_valid():
                            client_creation_serializer.save()
                            client_user = User.objects.get(email=client_email).clientuser
                            client_user.client_status = client_referral_decision
                            client_user.save()

                            return Response({
                                'result': True,
                                'data': {
                                    'referral': ClientReferralSerializer(client_referral).data,
                                    'client': client_creation_serializer.data
                                },
                                'message': 'Client Referral record created.'
                            }, status=HTTP_201_CREATED)
                        else:
                            client_referral.delete()
                            return Response({
                                'result': False,
                                'message': default_error_response(client_creation_serializer)
                            }, status=HTTP_201_CREATED)
                    else:
                        client_referral.delete()
                        return Response({
                            'result': True,
                            'message': 'Failed to create referral forms. Try to create the referral again later.'
                        }, status=HTTP_500_INTERNAL_SERVER_ERROR)
                else:
                    return Response({
                        'result': False,
                        'message': 'Failed to create Client Referral record. '
                    }, status=HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({
                    'result': False,
                    'message': default_error_response(serializer)
                }, status=HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                'result': False,
                'message': str(e)
            }, status=HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def create_referral_forms(client_referral, forms_request_data):
        referralFormsCreate = True
        if isinstance(forms_request_data, dict):
            for form in forms_request_data:
                print(form)
                if isinstance(forms_request_data[form], list):
                    for form_document in forms_request_data[form]:
                        serializer_data = {
                            "document": form_document,
                            "client_referral": client_referral.referral_id,
                            "category": form
                        }
                        form_document_serializer = ReviewBoardReferralFormsDocumentsSerializer(data=serializer_data)
                        if form_document_serializer.is_valid():
                            form_document_serializer.save()
                        else:
                            referralFormsCreate = False
        else:
            return False

        return referralFormsCreate
