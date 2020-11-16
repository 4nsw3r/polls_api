from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from polls.models import Poll, Questions, Answer

from polls.serializers import PollSerializer, QuestionSerializer, AnswerSerializer, PollStatistic

class PermissionViewSet(ModelViewSet):
    methods = ('POST', 'PUT', 'DELETE', 'PATCH')

    def get_permissions(self):
        if self.request.method in self.methods:
            permission_classes = [IsAdminUser, IsAuthenticated]
            return [permission() for permission in permission_classes]
        return [AllowAny()]


class PollViewSet(PermissionViewSet):
    serializer_class = PollSerializer

    def get_queryset(self):
        queryset = Poll.objects.all()
        user = self.request.user
        if user.id is None:
            return queryset.exclude(status=False)
        else:
            return queryset


class QuestionViewSet(PermissionViewSet):

    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()


class AnswerViewSet(PermissionViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class StatisticVIewSet(PermissionViewSet):
    serializer_class = PollStatistic
    queryset = Poll.objects.all()