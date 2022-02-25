from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv

# Create your views here.
def upload_file_view(request):
    form = CsvForm(request.POST or None,request.FILES or None)
    if form.is_valid(): 
        form.save()
        form = CsvForm()

        obj = Csv.objects.get(activated = False)
        with open(obj.file_name.path,'r') as f: 
            reader = csv.reader(f)

            for row in reader: 
                print(row)

        #to add the files as tracked
        obj.activated = True 
        obj.save()


    context = {
        'form':form
    }
    return render(request,'csvs/upload.html',context)
