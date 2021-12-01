from django.db import models
from django.utils import timezone

# Create your models here.
class QuizModelForm(models.Model):
    title = models.CharField('タイトル', max_length=255)
    text = models.CharField('本文', max_length=511)
    hint = models.CharField('ヒント', max_length=255)
    input1 = models.CharField('入力例1', max_length=255, null=True)
    output1 = models.CharField('出力例1', max_length=255, null=True)
    input2 = models.CharField('入力例2', max_length=255, null=True)
    output2 = models.CharField('出力例2', max_length=255, null=True)
    input3 = models.CharField('入力例3', max_length=255, null=True)
    output3 = models.CharField('出力例3', max_length=255, null=True)

    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.title + '>'

class SubModelForm(models.Model):
    user_id = models.CharField('ユーザID', max_length=255)
    quiz_id = models.IntegerField('クイズID', default=0)
    text = models.CharField('テキスト', max_length=8192)
    create_at = models.DateField('提出日', default = timezone.now)

    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.user_id + ',' + str(self.quiz_id) + '>'
