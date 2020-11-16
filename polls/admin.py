from django.contrib import admin

from .models import Poll, Questions, Answer


@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    pass


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass