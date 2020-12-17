from django.urls import path
from . import views



app_name = "authorization"

urlpatterns = [
    path('', views.login_view, name="login"),
    path('redirect', views.authorization, name="redirectAuth"),
    path('logout', views.logout_view, name="logout"),
]