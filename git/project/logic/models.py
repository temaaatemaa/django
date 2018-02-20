from django.db import models
from django.utils import timezone
       
class Users(models.Model):
	user_id = models.IntegerField()
	fio = models.CharField(max_length=50)
	phone = models.CharField(max_length=11)
	email = models.CharField(max_length=100)
	position = models.CharField(max_length=100)
	
	def __str__(self):
		return self.fio
	
class Systems(models.Model):
	system_id = models.IntegerField()
	name = models.CharField(max_length=40)
	
	def __str__(self):
		return self.name

class Priority(models.Model):
	priority_id = models.IntegerField()
	name = models.CharField(max_length=30)
	
	def __str__(self):
		return self.name
	
class Time(models.Model):
	time_id = models.IntegerField()
	description = models.CharField(max_length=30)
	
	def __str__(self):
		return self.description
        
class FullTable(models.Model):
	user = models.ManyToManyField(Users)
	system = models.ManyToManyField(Systems)
	priotiry = models.ManyToManyField(Priority)
	time = models.ManyToManyField(Time)
	
	def __str__(self):
		a = ""
		for us in self.user.all():
			a+=us.fio
		return a