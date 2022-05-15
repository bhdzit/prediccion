from os import replace
from django.http import HttpResponse
from django.shortcuts import render
import yfinance as yahoofin
import pandas_datareader.data as pdatareader
import datetime
import json 

from . import plots

# Create your views here.
def index(request):
    return render(request, 'polls/index.html')

def buscar(request):
        
        startDate=request.GET["startDate"].split("-")
        empresa=request.GET["empresa"]
        ahora = datetime.datetime.utcnow()
        yahoofin.pdr_override() 
        start1 = datetime.datetime(int(startDate[0]), int(startDate[1]), int(startDate[2]))
        end1 = ahora - datetime.timedelta(days=1)
        dataframe = pdatareader.get_data_yahoo(empresa, start1, end1)
        lista1=list()
        for i in dataframe.index:
           
            lista1.append({"fecha":""+i.strftime("%m/%d/%Y"),
                          "open":dataframe["Open"][i],
                          "close":dataframe["Close"][i],
                          "high":dataframe["High"][i],
                          "low":dataframe["Low"][i]}) 
            #print("Total income in "+ df["Date"][i]+ " is:"+str(df["Income_1"][i]+df["Income_2"][i]))
        dump = json.dumps(lista1)

        return HttpResponse(dump, content_type='application/json')

def ggplot(request):
    dump = json.dumps([])
    return HttpResponse(dump, content_type='application/json')