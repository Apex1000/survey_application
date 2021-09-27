from os import name
from django.db import models
from django.db.models.deletion import DO_NOTHING
import uuid

QUESTION_TYPE = (
    ("MCQ","MCQ"),
    ("SUB","SUBJECTIVE"),
)

QUESTION_PROPERTY_TYPE = (
    ("BL",)
)

QUESTION_VARIANT_TYPE = (
    ("RADIO","RADIO"),
    ("CHECKBOX","CHECKBOX"),
)

class Survey(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.name)

class QuestionPage(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    survey = models.ForeignKey(Survey,on_delete=DO_NOTHING,related_name="survey_question_page")
    
    def __str__(self):
        return "%s" % (self.title)

class MCQQuestionOption(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return "%s" % (self.name)
    

class Question(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    survey = models.ForeignKey(Survey,on_delete=DO_NOTHING,related_name="survey_question")
    questionpage = models.ForeignKey(QuestionPage,on_delete=DO_NOTHING,related_name="questionpage",blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    placeholder = models.TextField(blank=True, null=True)
    type = models.CharField(choices=QUESTION_TYPE,blank=True, null=True,max_length=50,default=None)
    options = models.ManyToManyField(MCQQuestionOption,blank=True)
    variant = models.CharField(choices=QUESTION_VARIANT_TYPE,blank=True, null=True,max_length=50,default=None)
    is_required = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    
    def __str__(self):
        return "%s" % (self.title)
