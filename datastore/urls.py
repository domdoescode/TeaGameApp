from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^player', views.PlayerList.as_view(), name='player-list'),
    url(r'^round', views.RoundList.as_view(), name='round-list'),
    url(r'^drink', views.DrinkList.as_view(), name='drink-list'),
]