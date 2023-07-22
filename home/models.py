from django.db import models

class Menu(models.Model):
	route = models.CharField(
		max_length = 50,
		blank = True,
		null = True,
		verbose_name = ('Ссылка')
	)
	text = models.CharField(
		max_length = 50,
		verbose_name = ('Текст')
	)
	def __str__(self):
		return self.text

class Advantage(models.Model):
	name = models.CharField(
		max_length = 50,
		verbose_name = ('Примущество')
	)
	number = models.CharField(
		max_length = 50,
		verbose_name = ('Цифра')
	)
	description = models.CharField(
		max_length = 50,
		verbose_name = ('Описание')
	)
	def __str__(self):
		return self.name