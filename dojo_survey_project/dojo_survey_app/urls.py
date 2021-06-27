from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_form),
    path('posted', views.user_form_post),
    path('result', views.survey_result),
    path('goHome', views.homeButton)
]