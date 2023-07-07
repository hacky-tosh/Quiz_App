from django.shortcuts import render

# Create your views here.

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Quiz, Question, Answer, Participant
from .serializers import *
from django.contrib.sites.shortcuts import get_current_site
   
class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
   
    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"error": "Only admin users can create quizzes."}, status=status.HTTP_403_FORBIDDEN)
    
        request.data["creator"] = self.request.user.id
        response = super().create(request, *args, **kwargs)
        quiz_id = response.data["id"]
        current_site = get_current_site(request)
        current_hostname = current_site.domain
        quiz_url = f"http://{current_hostname}/api/quizzez/{quiz_id}/attempt/ "
        response.data["url"] = quiz_url

        return response



class QuizRetrieveView(generics.RetrieveAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Quiz.objects.all()


class ParticipantListView(generics.ListCreateAPIView):
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Participant.objects.filter(quiz__creator_id=user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        quiz_id = self.request.data.get('quiz_id')
        quiz = Quiz.objects.get(id=quiz_id)
        serializer.save(quiz=quiz, creator=self.request.user)


class AnswersCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class QuizAttemptView(generics.CreateAPIView):
    serializer_class = ParticipantSerializer

    def create(self, request, *args, **kwargs):
        quiz_id = kwargs.get('quiz_id')
        try:
            quiz = Quiz.objects.get(id=quiz_id)
        except Quiz.DoesNotExist:
            return Response({'detail': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)

        user_id = request.data.get('user')
        answers_data = request.data.get('answers', [])

        if not user_id:
            return Response({'detail': 'User ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not isinstance(answers_data, list):
            return Response({'detail': 'Answers data should be a list'}, status=status.HTTP_400_BAD_REQUEST)

        participant_data = {'user': user_id, 'quiz': quiz_id}
        participant_serializer = self.get_serializer(data=participant_data)
        participant_serializer.is_valid(raise_exception=True)
        participant = participant_serializer.save()

        answer_errors = []
        for answer_data in answers_data:
            question_id = answer_data.get('question')
            selected_answer_id = answer_data.get('selected_answer')

            try:
                question = Question.objects.get(id=question_id, quiz_id=quiz_id)
            except Question.DoesNotExist:
                answer_errors.append(f"Question with ID {question_id} not found for the quiz")
                continue

            try:
                answer = Answer.objects.get(id=selected_answer_id, question=question)
            except Answer.DoesNotExist:
                answer_errors.append(f"Answer with ID {selected_answer_id} not found for the question")
                continue

            participant.answers.add(answer)

        if answer_errors:
            return Response({'detail': answer_errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'participant_id': participant.id}, status=status.HTTP_201_CREATED)


class QuizScoresView(generics.ListAPIView):
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        quiz_id = self.kwargs.get('quiz_id')
        return Participant.objects.filter(quiz_id=quiz_id)