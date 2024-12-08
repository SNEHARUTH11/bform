from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_students, name='upload_students'),
    path('generate-bform/', views.generate_bform, name='generate_bform'),
]
