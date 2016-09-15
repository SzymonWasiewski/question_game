from rest_framework import serializers
from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Question
        fields = (
            'id',
            'category',
            'question',
            'description',
            'answer_a',
            'answer_b',
            'answer_c',
            'answer_d',
            'correct_answer',
        )
