from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer, PlayQuizSerializer
from rest_framework.views import APIView
from django.http import Http404

# Create your views here.

class ListCreateQuiz(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    

class RetrieveUpdateDestroyQuiz(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = 'slug'

class QuizQuestion(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(quiz__slug=kwargs['slug'])
        serializer = QuestionSerializer(question, many=True)

        return Response(serializer.data)
    
    def post(self, request, format=None, **kwargs):
        quiz = Quiz.objects.get(slug=kwargs['slug'])
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(quiz=quiz) # Assign the quiz to the question
            return Response({"message": "Question created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuizQuestionDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Question.objects.get(id=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    
    def patch(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response({"message": "Question deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    

class PlayQuiz(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PlayQuizSerializer

    def get_queryset(self):
        slug = self.kwargs['slug'] 
        queryset = Quiz.objects.filter(slug=slug)
        return queryset
