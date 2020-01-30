from . import views
from django.urls import path,include


app_name = "design"

urlpatterns = [
    path('',views.index,name="index")
]
