from core.paginations import CustomPagination
from core.models import QuestionPage
from core.serializer import SurveyQuestionsSerializer
from django.db.models import Q
import io
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListCreateAPIView,
)
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import json
import random
import re
import uuid
import base64
from django.core.files.base import ContentFile


class SurveyQuestionsAPIView(ListAPIView):
    serializer_class = SurveyQuestionsSerializer
    pagination_class = CustomPagination
    # lookup_field = "uuid"

    def get_queryset(self):
        slug = self.kwargs["uuid"]
        queryset = QuestionPage.objects.filter(survey__uuid = slug)
        print(queryset)
        return queryset
