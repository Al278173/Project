from django.shortcuts import render

# Create your views here.

from catalog.models import Student, Counselor, School, Exam

def index(request):

    num_students = Student.objects.all().count()
    num_exams = Exam.objects.all().count()
    num_schools = School.objects.all().count()
    
    num_counselors = Counselor.objects.count()
    
    context = {
        'num_students': num_students,
        'num_exams': num_exams,
        'num_schools': num_schools,
    }

    return render(request, 'index.html', context=context)

from django.views import generic

class BookListView(generic.ListView):
    model = Student