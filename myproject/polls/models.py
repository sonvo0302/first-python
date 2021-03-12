from djongo import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub=models.DateTimeField()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question=models.ForeignKey(Question,null=True, on_delete= models.SET_NULL)
    choice_text = models.CharField(max_length=100)
    vote=models.IntegerField(default=0)
    def __str__(self):
        return self.question.question_text


