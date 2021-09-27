from core.models import MCQQuestionOption, Question, QuestionPage
from django.db.models import fields
from django_countries.serializer_fields import CountryField
from rest_framework import serializers

class MCQOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQQuestionOption
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = '__all__'
    
    def get_options(self,obj):
        options = obj.options.all()
        return MCQOptionsSerializer(options,many=True).data

class SurveyQuestionsSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    class Meta:
        model = QuestionPage
        fields = "__all__"
    
    def get_question(self, obj):
        return QuestionsSerializer(Question.objects.filter(questionpage = obj), many=True).data
