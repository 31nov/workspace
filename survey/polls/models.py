from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField('Poll Question', max_length=200)
    pub_date = models.DateTimeField('Poll Open Date')
    
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField('Choice Text', max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return "%s -> %s" % (self.poll.question, self.choice_text)