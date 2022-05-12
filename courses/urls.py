import django


from django.urls import path
from .views import (
    CourseCreateView,
    CourseView,
    my_course,
    CourseListView,
    ChildListView,
    CourseUpdateView,
    CourseDeleteView,
)

app_name = 'courses'
urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('child', ChildListView.as_view(), name='child-course'),

    # path('', CourseView.as_view(template_name="about.html"), name='courses-list'),
    # path('', my_course, name='courses-list'),
    path("<int:id>/", CourseView.as_view(), name='course-detail'),

    path('create/', CourseCreateView.as_view(), name='course-create'),
    path("<int:id>/update/", CourseUpdateView.as_view(), name='course-update'),
    path("<int:id>/delete/", CourseDeleteView.as_view(), name='course-delete'),
]