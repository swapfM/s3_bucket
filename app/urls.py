from django.urls import path
from app import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('', views.DataList.as_view()),
    path('data/<int:pk>/', views.DataList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
