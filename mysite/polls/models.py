# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

## 每一个模型都用一个类表示
class Poll(models.Model):
        questions = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.questions

class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length = 200)
	votes = models.IntegerField()

	def __unicode__(self):
		return self.choice
