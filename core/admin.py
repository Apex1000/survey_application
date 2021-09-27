from django.contrib import admin
from core import models

admin.site.register(models.Survey)
admin.site.register(models.QuestionPage)
admin.site.register(models.MCQQuestionOption)
admin.site.register(models.Question)