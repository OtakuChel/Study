from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FeedbackView.as_view()),
    #path('<int:id_feedback>', views.FeedBackUpdateView.as_view()),
    path('update/<int:pk>', views.FeedBackUpdateView.as_view()),
    path('done', views.DoneView.as_view()),
    path('list', views.ListFeedBack.as_view()),
    path('detail/<int:pk>', views.DetailFeedBack.as_view(), name='feedback-detail'),
]