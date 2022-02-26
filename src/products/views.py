from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Product,Purchase
import pandas as pd 
from .utils import get_simple_plot,get_salesman_from_id,get_image
from .forms import PurchaseForm
import csv 
from django.http import HttpResponse 
import matplotlib.pyplot as plt
import seaborn as sns 
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def sales_dist_view(request):
    df = pd.DataFrame(Purchase.objects.all().values())
    df['salesman_id'] = df['salesman_id'].apply(get_salesman_from_id)
    df.rename({'salesman_id':'salesman'},axis= 1,inplace =True)
    df['date'] =df['date'].apply(lambda x:x.strftime('%Y-%m-%d'))
    plt.switch_backend('Agg')
    plt.xticks(rotation= 45)
    sns.barplot(x='date',y='total_price',hue='salesman',data = df)
    plt.tight_layout()
    graph = get_image()

    return render(request,'products/sales.html',{'graph':graph})

@login_required
def chart_select_view(request):
    graph = None
    error_message = None
    df = None
    price = None

    try: 
        product_df = pd.DataFrame(Product.objects.all().values())
        product_df['product_id'] = product_df['id']
        purchase_df = pd.DataFrame(Purchase.objects.all().values())
        
        if purchase_df.shape[0]>0: 
            df = pd.merge(purchase_df,product_df,on= 'product_id').drop(['id_y','date_y'],axis= 1).rename({'id_x':'id','date_x':'date'},axis =1)
            price = df['price']
            # print(df['date'][0])
            # print(type(df['date'][0]))
        
            # qs2 = Product.objects.all.values_list()
            if request.method == 'POST':
                
                chart_type = request.POST['sales']
                date_from = request.POST['date_from']
                date_to = request.POST['date_to']
                df['date'] = df['date'].apply(lambda x: x.strftime('%y-%m-%d'))
                print(df['date'])
                df2 = df.groupby('date',as_index = False)['total_price'].agg('sum')
                print(df2)

                if chart_type : 
                    if date_from  and date_to : 
                        df = df[df['date']> date_from ]&(df['date']<date_to)
                        df2 = df.groupby('date',as_index = False)['total_price'].agg('sum')
                    #function to get a graph
                    graph = get_simple_plot(chart_type,x = df2['date'], y =df2['total_price'] ,data = df ) 
                else: 
                    error_message = "please select a chart type to continue"

            else: 
                error_message = "no purchase records in the database"

    except: 
        sucess_message = None
        error_message = None
        

    context = {
        'graph':graph,
        'error_message':error_message,
        'price':price
        # 'products':product_df.to_html(),
        # 'purchase':purchase_df.to_html(),
        # "df" : df

    }
    return render(request, 'products/main.html',context)


@login_required
def add_purchase_view(request):
    form = PurchaseForm(request.POST or None)
    added_message = None
    if form.is_valid(): 
        obj = form.save(commit = False)
        obj.salesman = request.user
        obj.save()

        form = PurchaseForm()
        added_message = "The sale has been added"

    context ={
        'form': form,
        'added_message' : added_message
    }
    return render(request,'products/add.html',context)

def export_csv_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="purchase.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['product','quantity','price','total_price','salesman','date'])
    for purchase in Purchase.objects.all().values_list('product','quantity','price','total_price','salesman','date'):
        writer.writerow(purchase)
    return response