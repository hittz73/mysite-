from django.shortcuts import render
from django.http import HttpResponse
from ads.models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'ads/try.html', {'students': students})