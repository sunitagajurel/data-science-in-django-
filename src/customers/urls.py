from django.urls import path
from .views import customer_rel_view
app_name = 'customers'
urlpatterns = [
    path('',customer_rel_view,name= 'customer-corr-view'),
    
]