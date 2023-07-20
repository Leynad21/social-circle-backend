from rest_framework import serializers
from .models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):

    question_count = serializers.SerializerMethodField("getQuestionCount")
    author_username = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'author',
            'author_username',
            'question_count',
            'slug',
            'created_at',
        ]
        read_only_fields = ['author']

    def getQuestionCount(self, obj):
        return obj.question_count
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
    



class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    quiz = QuizSerializer(read_only=True)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = [
            'quiz',
            'title',
            'id',
            'method',
            'answers',
        ]

    def create(self, validated_data):
        answers_data = validated_data.pop('answers', [])
        question = Question.objects.create(**validated_data)

        for answer_data in answers_data:
            Answer.objects.create(question=question, **answer_data)

        return question
    
    def update(self, instance, validated_data):
        # Update the instance fields
        instance.title = validated_data.pop('title', instance.title)
        instance.method = validated_data.pop('method', instance.method)

        # Update the associated answers
        answers_data = validated_data.pop('answers', [])
        instance.answers.all().delete()  # Delete existing answers
        for answer_data in answers_data:
            Answer.objects.create(question=instance, **answer_data)

        instance.save()
        return instance
    

class PlayQuizSerializer(serializers.ModelSerializer):
    question_count = serializers.SerializerMethodField("get_question_count")
    author_username = serializers.CharField(source="author.username", read_only=True)
    questions = serializers.SerializerMethodField("get_quiz_questions")

    class Meta:
        model = Quiz
        fields = [
            'id',
            'title',
            'author',
            'author_username',
            'question_count',
            'slug',
            'created_at',
            'questions',
        ]
        read_only_fields = ['author']

    def get_question_count(self, obj):
        return obj.question_count

    def get_quiz_questions(self, obj):
        questions = obj.questions.all()
        question_data = []
        for question in questions:
            answers = question.answers.all()
            answer_data = []
            for answer in answers:
                answer_data.append({
                    'id': answer.id,
                    'answer_text': answer.answer_text,
                    'is_right': answer.is_right,
                })
            question_data.append({
                'id': question.id,
                'title': question.title,
                'method': question.method,
                'date_created': question.date_created,
                'answers': answer_data,
            })
        return question_data

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

