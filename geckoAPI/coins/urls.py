from django.urls import path

from . import views

urlpatterns = [
    path("/get_coins", views.get_coins, name="get coins"),
    path("/update_coins", views.update_coins, name="update coins"),
]
