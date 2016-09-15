from categories.models import Category
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category)
    question = models.TextField()
    description = models.TextField()
    answer_a = models.CharField(max_length=255)
    answer_b = models.CharField(max_length=255)
    answer_c = models.CharField(max_length=255)
    answer_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    class Meta:
        ordering = ('category',
                    'question',
                    )

    def __str__(self):
        return u'%s' % self.question
