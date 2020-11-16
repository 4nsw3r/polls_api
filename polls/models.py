from django.db import models
from django.contrib.auth.models import User


# ОПРОС
class Poll(models.Model):
    title = models.CharField(max_length=100, unique=True)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


# ВОПРОС
class Questions(models.Model):
    type = (
        ("text", "text"),
        ("single_answer", "single_answer"),
        ("multi_answer", "multi_answer"),
    )
    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=100)
    question_type = models.CharField(choices=type, max_length=20, blank=False)

    def __str__(self):
        return self.question_text


# ОТВЕТ
class Answer(models.Model):
    answer = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text
