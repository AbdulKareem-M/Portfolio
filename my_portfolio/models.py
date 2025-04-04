from django.db import models

class ContactMessage(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  message = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
     return f'Message from {self.name}'
   
class Project(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField()
  tech_stack = models.CharField(max_length=200)
  github_link = models.URLField(blank=True, null=True)
  demo_link = models.URLField(blank=True, null=True)
  image = models.ImageField(upload_to='project_images/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.title