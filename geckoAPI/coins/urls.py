from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_graph, name="show graph"),
    path("/get_coins", views.get_all_coins, name="get coins"),
    path("/update_coins", views.update_coins, name="update coins"),
]
