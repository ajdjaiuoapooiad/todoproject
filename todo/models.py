from django.db import models

PRIORITY=(('danger','high'),('info','normal'),('success','low'))

class Post(models.Model):
    title=models.CharField('タイトル',max_length=30)
    text=models.TextField('本文')
    priority=models.CharField(
        '優先度',
        max_length=50,
        choices=PRIORITY,
        null=True
    )
    duedate=models.DateField('期限',null=True)
    
    def __str__(self):
        return self.title
    