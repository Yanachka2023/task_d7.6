from django.contrib import admin
from django.urls import path, include
from .views import SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', SignUp.as_view(), name='signup'),
    path('', include('allauth.urls')),
]
