from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Product,Purchase
import pandas as pd 
from .utils import get_simple_plot
from .forms import PurchaseForm

# Create your views here.
def chart_select_view(request):
    graph = None
    error_message = None
    df = None
    price = None

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
            print(chart_type)
            # print(chart_type)
            # print(date_from,date_to)
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
        

    context = {
        'graph':graph,
        'error_message':error_message,
        'price':price
        # 'products':product_df.to_html(),
        # 'purchase':purchase_df.to_html(),
        # "df" : df

    }
    return render(request, 'products/main.html',context)



def add_purchase_view(request):
    form = PurchaseForm(request.POST or None)
    if form.is_valid(): 
        obj = form.save(commit = False)
        obj.salesman = request.user
        obj.save()
    context ={
        'form': form,
    }
    return render(request,'products/add.html',context)