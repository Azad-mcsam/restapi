from http.client import HTTPResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# model object - single student data


def student_details():
    stu = Student.objects.get(Student)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HTTPResponse(json_data)


def student_list(request):
    stu = Student.objects.all()
    print(stu)
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HTTPResponse(json_data, content_type='application/json')
