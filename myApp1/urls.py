from django.urls import path,include
from rest_framework import routers
from  . import views
r = routers.DefaultRouter()
r.register('blog',views.BlogerViewSet)
urlpatterns = [
path('',include(r.urls)),

]