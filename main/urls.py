from django.conf.urls import url
from . import views as main_views

app_name = 'main'

urlpatterns = [
    url(r'^$', main_views.home, name='home'),
    url(r'^details/<int:id>/', main_views.detail, name="detail"),
    url(r'^addprojects/', main_views.add_projects, name="add_projects"),
    url(r'^editprojects/<int:id>/', main_views.edit_projects, name="edit_projects"),
    url(r'^deleteprojects/<int:id>/', main_views.delete_projects, name="delete_projects"),
    url(r'^addreview/<int:id>/', main_views.add_review, name="add_review"),
    url(r'^editreview/<int:project_id>/<int:review_id/', main_views.edit_review, name="edit_review"),
]