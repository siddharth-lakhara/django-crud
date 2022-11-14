from django.db import models
  
class StudentsList(models.Model):
  name = models.TextField(max_length=100)
  age = models.IntegerField()
  
  def __str__(self) -> str:
    return f"Student {self.name}, {self.age} years old"
  