from argparse import Namespace
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view_main,name="homepagemain"),
    path('proceed/',views.home_view,name="homepage"),
    path('sendagain/',views.send_again,name="main"),
    path('sendmails/',views.with_body,name="sendmails"),
    path('about/',views.about_view,name="about"),
]