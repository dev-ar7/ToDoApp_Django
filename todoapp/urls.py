from django.conf.urls import url
from . import views

app_name = 'todoapp'

urlpatterns = [
    url(r'^$', views.tasks, name='tasks'),
    url(r'^complete/<int:id>/', views.complete, name='complete_task'),
    url(r'^delete/<int:id>/', views.delete, name='delete_task'),
]
