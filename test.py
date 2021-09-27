from core import models
from datetime import date, timedelta

for obj in range(1,10):
    survey_obj = models.Survey.objects.create(
        name = "Survey:"+str(obj),
        description = "DEMO",
        startdate = date.today(),
        enddate = date.today()+timedelta(10)
    )
    for page in range(1,6):
        question_page_obj = models.QuestionPage.objects.create(
            title = "QuestionPage"+str(page),
            description = "QuestionPage"+str(page),
            survey = survey_obj
        )
        for question in range(1,10):
            if question%2==0:
                models.Question.objects.create(
                    survey = survey_obj,
                    questionpage = question_page_obj,
                    title = "Question"+str(question),
                    description = "Question"+str(question),
                    type = "SUB",
                    variant = None,
                    is_required = True if question%2 == 0 else False,
                    is_visible = True if question%2 == 0 else False
                )
            else:
                questionobj = models.Question.objects.create(
                    survey = survey_obj,
                    questionpage = question_page_obj,
                    title = "Question"+str(question),
                    description = "Question"+str(question),
                    type = "MCQ",
                    variant = "RADIO",
                    is_required = True if question%2 == 0 else False,
                    is_visible = True if question%2 == 0 else False
                )
                for obj in range(4):
                    mcqobj = models.MCQQuestionOption.objects.create(
                        name = "MCQ"+str(obj)
                    )
                    questionobj.options.add(mcqobj)
                    questionobj.save()

        

