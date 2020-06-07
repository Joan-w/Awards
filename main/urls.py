from django.conf.urls import url
from . import views

app_name = 'main'

urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'^details/<int:id>/', views.detail, name="detail")
]