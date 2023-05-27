from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView,ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.
'''
class StudentView(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

class CreateStudentView(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)
'''
class RUDStudentView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
'''
class UpdateStudentView(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

class DestroyStudentView(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)
    
'''
class LCStudentView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)


class glStudentView(ListAPIView,CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class glrudStudentView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class gl_StudentView(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class gl_rudStudentView(RetrieveUpdateAPIView,RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class gl_rud_StudentView(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer