from core.paginations import CustomPagination
from core.models import QuestionPage
from core.serializer import SurveyQuestionsSerializer
from rest_framework.generics import ListAPIView


class SurveyQuestionsAPIView(ListAPIView):
    serializer_class = SurveyQuestionsSerializer
    pagination_class = CustomPagination
    # lookup_field = "uuid"

    def get_queryset(self):
        slug = self.kwargs["uuid"]
        queryset = QuestionPage.objects.filter(survey__uuid=slug)
        print(queryset)
        return queryset
