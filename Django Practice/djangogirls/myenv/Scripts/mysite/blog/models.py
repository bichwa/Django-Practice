from django.db import models
from django.utils import timezone

#defining our model, Post using keyword  'class'
class Post (models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length = 200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now())
	published_date = models.DateTimeField(blank = True, null = True)

# Method to publish our posts!
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title







