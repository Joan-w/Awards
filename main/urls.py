from django.conf.urls import url
from . import views as main_views

app_name = 'main'

urlpatterns = [
    url(r'^$', main_views.home, name='home'),
    url(r'^details/<int:id>/', main_views.detail, name="detail"),
    url(r'^addprojects/', main_views.add_projects, name="add_projects"),
    url(r'^editprojects/<int:id>/', main_views.edit_projects, name="edit_projects"),
]