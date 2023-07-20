from django.urls import path
from .views import ListCreateQuiz, QuizQuestion, RetrieveUpdateDestroyQuiz, QuizQuestionDetail, PlayQuiz


urlpatterns = [
    path("", ListCreateQuiz.as_view(), name="quiz_list"),
    path("<str:slug>", RetrieveUpdateDestroyQuiz.as_view(), name="quiz_detail"),
    path("question/<str:slug>", QuizQuestion.as_view(), name='questions'),
    path("question/detail/<int:pk>", QuizQuestionDetail.as_view(), name='question-detail'),
    path("play/<str:slug>", PlayQuiz.as_view(), name="quiz_play"),
]