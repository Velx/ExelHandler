from django.urls import path
from rest_framework import routers

from .views import FileUploadView, Data, Send

router = routers.SimpleRouter()
router.register(r'data', Data, 'Data')

urlpatterns = [
	path('upload', FileUploadView.as_view(), name='upload'),
	path('email', Send.as_view(), name='send' )
	# path('data', Data.as_view(), name='Data')
]
urlpatterns += router.urls
