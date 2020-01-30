from . import views
from django.urls import path,include
from .views import registration


app_name = "apilogin"

urlpatterns = [
    path('register/',views.registration,name="registration"),

]
