from django.urls import path
from .views import *

urlpatterns = [

    path('quizzes/', QuizListCreateView.as_view(), name='quiz-create'),
    path('quizzes/<int:pk>/', QuizRetrieveView.as_view(), name='quiz-retrieve'),
    path('participants/', ParticipantListView.as_view(), name='participant-list'),
    path('questions/', QuestionCreateView.as_view(), name='question-create'),
    path('answers/', AnswersCreateView.as_view(), name='question-create'),
    path('quizzes/<int:quiz_id>/attempt/', QuizAttemptView.as_view(), name='quiz-attempt'),
    path('quizzes/<int:quiz_id>/scores/', QuizScoresView.as_view(), name='quiz-scores'),


]
