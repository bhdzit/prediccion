from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
from django.http import HttpResponse
import json
import string

from requests import NullHandler
def index(request):
    df = pd.read_csv("empleos.csv",encoding = "utf-8",dtype = str)
    #print(df['salario'].describe())
  
    df['salario'].hist(bins=20 , figsize=(100,20), color="r")
    df_dropped = df.drop(labels = ["url"], axis = 1)
    df_dropped.head()
    df_dropped.rename(columns={"descripcio":"descripcion", "Fecha De Publicacion": "fecha"}, inplace=True)

    for feature in df_dropped:
        if df_dropped[feature].dtype == "object":
         df_dropped[feature] = df_dropped[feature].fillna("None")
        else: 
         df_dropped[feature] = df_dropped[feature].fillna(-1)
    df_dropped["salario_m"] = df_dropped['salario'].apply(remove_punctuations)
    df_sal = df_dropped['salario'].str.split('[ ]' , expand=True)
    print(df_dropped)
#    dump = json.dumps(df_dropped)
    df_dropped= df_dropped.groupby("busqueda")["empresa"].count().sort_values(ascending= False)
    return HttpResponse(df_dropped.to_json(), content_type='application/json')

def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

def numeroDeVacantes():
    df = pd.read_csv("empleos.csv",encoding = "utf-8",dtype = str)
    #print(df['salario'].describe())
  
    df['salario'].hist(bins=20 , figsize=(100,20), color="r")
    df_dropped = df.drop(labels = ["url"], axis = 1)
    df_dropped.head()
    df_dropped.rename(columns={"descripcio":"descripcion", "Fecha De Publicacion": "fecha"}, inplace=True)

    for feature in df_dropped:
        if df_dropped[feature].dtype == "object":
         df_dropped[feature] = df_dropped[feature].fillna("None")
        else: 
         df_dropped[feature] = df_dropped[feature].fillna(-1)
    df_dropped["salario_m"] = df_dropped['salario'].apply(remove_punctuations)
    df_sal = df_dropped['salario'].str.split('[ ]' , expand=True)
 
#    dump = json.dumps(df_dropped)
    df_dropped= df_dropped.groupby("busqueda")["empresa"].count().sort_values(ascending= False)
    return df_dropped.to_json()

def agruparPorFecha():
    df = pd.read_csv("empleos.csv",encoding = "utf-8",dtype = str)
    #print(df['salario'].describe())
  
    df['salario'].hist(bins=20 , figsize=(100,20), color="r")
    df_dropped = df.drop(labels = ["url"], axis = 1)
    df_dropped.head()
    df_dropped.rename(columns={"descripcio":"descripcion", "Fecha De Publicacion": "fecha"}, inplace=True)

    for feature in df_dropped:
        if df_dropped[feature].dtype == "object":
         df_dropped[feature] = df_dropped[feature].fillna("None")
        else: 
         df_dropped[feature] = df_dropped[feature].fillna(-1)
    df_dropped["salario_m"] = df_dropped['salario'].apply(remove_punctuations)
    df_sal = df_dropped['salario'].str.split('[ ]' , expand=True)
    df_dropped= df_dropped.groupby("fecha")["busqueda"].count().sort_values(ascending= False)
    return df_dropped.to_json()

def obtnenerEmpresas():
    df = pd.read_csv("empleos.csv",encoding = "utf-8",dtype = str)
    #print(df['salario'].describe())
  
    df['salario'].hist(bins=20 , figsize=(100,20), color="r")
    df_dropped = df.drop(labels = ["url"], axis = 1)
    df_dropped.head()
    df_dropped.rename(columns={"descripcio":"descripcion", "Fecha De Publicacion": "fecha"}, inplace=True)

    for feature in df_dropped:
        if df_dropped[feature].dtype == "object":
         df_dropped[feature] = df_dropped[feature].fillna("None")
        else: 
         df_dropped[feature] = df_dropped[feature].fillna(-1)
    df_dropped["salario_m"] = df_dropped['salario'].apply(remove_punctuations)
    df_sal = df_dropped['salario'].str.split('[ ]' , expand=True)
    df_dropped= df_dropped.groupby("empresa")["busqueda"].count().sort_values(ascending= False)
    return df_dropped[1:11].to_json()
df_dropped2=""

def remove(text,df_dropped):
    for punctuation in df_dropped2['ubicacion'] :
        text = text.replace('\r', ' ')
    return text


def obtnenerCiudades():
    df = pd.read_csv("empleos.csv",encoding = "utf-8",dtype = str)
    #print(df['salario'].describe())
  
    df['salario'].hist(bins=20 , figsize=(100,20), color="r")
    df_dropped = df.drop(labels = ["url"], axis = 1)
    df_dropped.head()
    df_dropped.rename(columns={"descripcio":"descripcion", "Fecha De Publicacion": "fecha"}, inplace=True)

    for feature in df_dropped:
        if df_dropped[feature].dtype == "object":
         df_dropped[feature] = df_dropped[feature].fillna("None")
        else: 
         df_dropped[feature] = df_dropped[feature].fillna(-1)
    df_dropped["salario_m"] = df_dropped['salario'].apply(remove_punctuations)
    df_sal = df_dropped['salario'].str.split('[ ]' , expand=True)

    df_dropped['ubicacion']=df_dropped['ubicacion'].replace([".\r"]," ")
    df_dropped2=df_dropped
    df_dropped["ubicacion_m"] = df_dropped['ubicacion']

    df_dropped= df_dropped.groupby("ubicacion_m")["busqueda"].count().sort_values(ascending= False)
    return df_dropped[1:11].to_json()

def obtenerLenguajes():
    df = pd.read_csv("empleos.csv",encoding = "utf-8",dtype = str)
    #print(df['salario'].describe())
  
    df['salario'].hist(bins=20 , figsize=(100,20), color="r")
    df_dropped = df.drop(labels = ["url"], axis = 1)
    df_dropped.head()
    df_dropped.rename(columns={"descripcio":"descripcion", "Fecha De Publicacion": "fecha"}, inplace=True)

    for feature in df_dropped:
        if df_dropped[feature].dtype == "object":
         df_dropped[feature] = df_dropped[feature].fillna("None")
        else: 
         df_dropped[feature] = df_dropped[feature].fillna(-1)
    df_dropped["salario_m"] = df_dropped['salario'].apply(remove_punctuations)
    df_sal = df_dropped['salario'].str.split('[ ]' , expand=True)

    df_dropped['ubicacion']=df_dropped['ubicacion'].replace([".\r"]," ")
    df_dropped2=df_dropped
    df_dropped["ubicacion_m"] = df_dropped['ubicacion']

    df_dropped= df_dropped.groupby("descripcion")["busqueda"].count().sort_values(ascending= False)
    return df_dropped.to_json()
def prueba():
    df = pd.read_csv("empleos.csv",encoding = "utf-8",dtype = str)
    
    print("Fin")
#prueba()