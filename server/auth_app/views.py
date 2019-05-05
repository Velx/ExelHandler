from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
# from rest_framework.exceptions import NotFound

UserModel = get_user_model()


class RegistrationView(APIView):

	permission_classes = (AllowAny,)

	def post(self, request, *args, **kwargs):
		username = request.data.get("username")
		password = request.data.get("password")
		if username is None or password is None:
			return Response({'error': 'Please provide both username and password'},
                        	status=HTTP_400_BAD_REQUEST)
		if UserModel.objects.filter(username=username).exists():
			return Response({'error': 'This user already exist'},
                        	status=HTTP_400_BAD_REQUEST)
		else:
			user = UserModel.objects.create(username=username)
			user.set_password(password)
			user.save()
			return Response({}, status=HTTP_200_OK)


class LoginView(APIView):

	permission_classes = (AllowAny,)

	def post(self, request):
		username = request.data.get("username")
		password = request.data.get("password")
		if username is None or password is None:
			return Response({'error': 'Please provide both username and password'},
                        	status=HTTP_400_BAD_REQUEST)
		user = authenticate(username=username, password=password)
		if not user:
			return Response({'data': 'Wrong username or password'}, #TODO: edit this, not throw error
                        	status=HTTP_404_NOT_FOUND)
		token, _ = Token.objects.get_or_create(user=user)
		return Response({'token': token.key, 'username':username},
    					status=HTTP_200_OK)


class LogoutView(APIView):

	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
        # simply delete the token to force a login
		request.user.auth_token.delete()
		return Response({}, status=HTTP_200_OK)

class CustomAuthToken(ObtainAuthToken):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


@csrf_exempt
@api_view(["GET"])
def sample_api(request):

	data = {'sample_data': 123}
	return Response(data, status=HTTP_200_OK)