from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^play/$', views.play_game),
    url(r'^register-players/$', views.register_players),
    url(r'^getcard/$', views.GetCards.as_view()),
]