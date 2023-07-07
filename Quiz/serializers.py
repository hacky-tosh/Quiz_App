from rest_framework import serializers
from .models import Quiz, Question, Answer, Participant

class QuizSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields =['id', 'title', 'creator', 'questions']
    
    def get_questions(self, obj):
        questions = obj.question_set.all()
        return QuestionSerializer(questions, many=True).data

class ParticipantSerializer(serializers.ModelSerializer):
    quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())

    class Meta:
        model = Participant
        fields = ['id', 'user', 'quiz', 'score']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'text', 'creator']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'text','is_correct']


