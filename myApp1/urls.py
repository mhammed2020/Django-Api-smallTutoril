from django.urls import path
from  . import views
app_name="myApp1"
urlpatterns = [
path('',views.show,name = "show"),

]