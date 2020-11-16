from django.conf.urls import url
from django.urls import path, include
from .views import PollViewSet, QuestionViewSet, AnswerViewSet, StatisticVIewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')
router.register('questions', QuestionViewSet, basename='questions')
router.register('answers', AnswerViewSet, basename='answers')
router.register('statistic', StatisticVIewSet, basename='statistic')

urlpatterns = [
    url('', include(router.urls))
    ]
