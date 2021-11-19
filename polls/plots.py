from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
def index(request):
    df = pd.read_csv("empleos.csv",encoding = "utf-8",dtype = str)
    df['salario'].hist(bins=20 , figsize=(100,20), color="r")
    mydict = {
        "df": df.to_html()
    }
    return render(request, 'polls/plots.html', context=mydict)
    
