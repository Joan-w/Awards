from django.conf.urls import url
from . import views as accounts_views

app_name = 'accounts'

urlpatterns = [
    url(r'^register/', accounts_views.register, name='register'),
    url(r'^login/', accounts_views.login_user, name='login'),
    url(r'^logout/', accounts_views.logout_user, name='logout'),
]