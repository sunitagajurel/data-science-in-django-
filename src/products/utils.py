import base64
import dataclasses
import matplotlib.pyplot as plt 
import seaborn as sns 
from io import BytesIO

def get_image(): 
    #cretaes a byte buffer for the image to save 
    buffer = BytesIO()
    #create the plot with the use of ByteIO object as its file 
    plt.savefig(buffer,format = 'png')
    #set the cursor to the begining of the stream 
    buffer.seek(0)
    #retrieve the entire content of the 'file'
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode()
     #free the memory of the buffer 
    buffer.close() 
    return graph


def get_simple_plot(chart_type,*args,**kwargs):
    plt .switch_backend('Agg')
    plt.figure(figsize = (10,4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    print(x,y)
    data = kwargs.get('data')
 

    if chart_type == "bar plot": 
        title = chart_type
        plt.title(title)
        plt.bar(x,y)
        
    elif chart_type == "line plot": 
        title = chart_type
        plt.title(title)
        plt.plot(x,y)

    else: 
        title = chart_type
        plt.title(title)
        sns.countplot('name',data= data)
    plt.xticks(rotation = 45)    
    plt.tight_layout
    graph = get_image() 
    return graph


