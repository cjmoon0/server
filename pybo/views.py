from click import style
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import os
from config import settings



def index(request):
     return render(request, "excel/main.html")

def search1(request, pagename):
    df = pd.read_excel(settings.MEDIA_ROOT+r"\\result\\데이터.xlsx", engine = "openpyxl").astype('str')
    html = ""
    print(pagename+'jjjj\n')
    a = 0
    if (df.iloc[:,0] == pagename).any():
        html = (df[df.iloc[:,0]==pagename]).to_html(index=False, justify='center').replace('\n','')
        return render(request, "excel/main.html", context={
        'form':html
        })
    html = "<h2><b>" + pagename +"<b>을 찾을 수 없음"
    return render(request, "excel/main.html", context={
        'form':html
    })