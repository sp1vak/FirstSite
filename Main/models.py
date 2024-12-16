from django.db import models

# Create your models here.

class Notes(models.Model):
	title = models.CharField('Name', max_length = 50)
	note = models.TextField('Note')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Note'
		verbose_name_plural = 'Notes'