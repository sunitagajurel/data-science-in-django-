from django.shortcuts import render
from .forms import CsvForm
from .models import Csv
import csv
from django.contrib.auth.models import User
from products.models import Product ,Purchase

# Create your views here.
def upload_file_view(request):
    error_message = None
    sucess_message = None
    form = CsvForm(request.POST or None,request.FILES or None)
    if form.is_valid(): 
        form.save()
        form = CsvForm()
        try: 
            obj = Csv.objects.get(activated = False)
            with open(obj.file_name.path,'r') as f: 
                reader = csv.reader(f)

                for row in reader:
                    user = User.objects.get(id = row[3])
                    product, _= Product.objects.get_or_create(name =row[0])
                    Purchase.objects.create(
                        product = product,
                        price =int(row[2]),
                        quantity =int(row[3]),
                        salesman = user,
                        date = row[4]
                    )
            #to add the files as tracked
            obj.activated = True 
            obj.save()
            sucess_message = "Uploaded sucessfully"
        except: 
            error_message = " Oops! Something went wrong"


    context = {
        'form':form,
        'error_message':error_message,
        'sucess_message':sucess_message

    }
    return render(request,'csvs/upload.html',context)
