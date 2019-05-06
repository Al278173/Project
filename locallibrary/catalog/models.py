from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a school name')
    
    def __str__(self):
        return self.name

class Exam(models.Model):
    name = models.CharField(max_length=200, help_text='Enter an exam')
    
    def __str__(self):
        return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    School = models.OneToOneField('School', on_delete = models.CASCADE)
    Counselor = models.OneToOneField('Counselor', on_delete = models.CASCADE)

    class Meta:
        unique_together = ["first_name", "last_name", "School", "Counselor"]
    
    exam = models.ManyToManyField(Exam, help_text='Select an exam')
    
    def __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def display_school(self):
        """return ', '.join(School.name for school in School.all()[:3])"""

    display_school.short_description = 'School'

from django.db.models.signals import m2m_changed    
from django.core.exceptions import ValidationError

def too_many_exams(sender, **kwargs):
        if kwargs['instance'].exam.count() > 3:
            raise ValidationError("You can't assign more than three exams")

m2m_changed.connect(too_many_exams, sender = Student.exam.through)

class Counselor (models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length = 20)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('counselor-contact', args=[str(self.id)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

