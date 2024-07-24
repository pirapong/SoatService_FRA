from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .models import Student
import os


def upload_file(request):
    if(request.method == 'POST'):
        form = UploadFileForm(request.POST,request.FILES)
        file = request.FILES['file']
        print(file)
        # MyModel.objects.delete(file
        # dd = MyModel.objects.delete('img/boy.jpg')
        # dd.save()
        _delete_file('imgDb/' +str(file))
        student = Student.objects.create(diploma=file)
        print(student)
        student.save()
        return HttpResponse('name of UploadFile ==> ' + str(file.name) + ' sut ' + str(student.pk) + ' dip ' + str(student.diploma) )
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def _delete_file(path):
    # Deletes file from filesystem.
    if os.path.isfile(path):
        os.remove(path)
