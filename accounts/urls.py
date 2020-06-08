from django.conf.urls import url
from . import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    url(r'^register/', accounts_views.register, name='register'),
]