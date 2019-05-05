from django.urls import path
from .views import RegistrationView, LoginView, LogoutView
from rest_framework.authtoken import views

from .views import sample_api


urlpatterns = [
	path('sampleapi', sample_api),
	path('register', RegistrationView.as_view(), name='registation'),
	# path('login', views.obtain_auth_token, name='login'),
	path('login', LoginView.as_view(), name='Login'),
	path('logout', LogoutView.as_view(), name='logout')
]