from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Poll, Questions, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('answer', 'answer_text', 'user',)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('poll', 'question_text', 'question_type',)


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'title', 'start_date', 'end_date')
        #read_only_fields = 'start_date'



class PollStatistic(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    
    class Meta:
        model = Poll
        fields = ('id', 'title', 'start_date', 'end_date', 'user_id')
        read_only_fields = ('id', 'title', 'start_date', 'end_date', 'user_id')


