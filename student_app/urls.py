from django.conf.urls import url
from student_app import views

app_name = 'student_app'

urlpatterns = [
    url(r'^$', views.StudentsListView.as_view(),name='list'),
    url(r'^$', views.StudentsListView.as_view(),name='detail'),
    url(r'^create/',views.StudentsCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$',views.StudentsUpdateView.as_view(),name='update'),
    url(r'^delete/(?P<pk>\d+)/$',views.StudentDeleteView.as_view(),name='delete'),
]
