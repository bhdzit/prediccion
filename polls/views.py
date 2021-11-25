from os import replace
from django.http import HttpResponse
from django.shortcuts import render
from bs4 import BeautifulSoup
import json
from django.http import HttpResponse
import requests
import pandas as pd
import csv
import re
import datetime
from . import plots
listaEmpleos=list()
listaEmpleosACsv=list()
listaEmpleosACsv.append(["busqueda","titulo","empresa","ubicacion","url","salario","plataforma","descripcio","Fecha De Publicacion"])
listaDeEmpleos=['c#','c++','oracle','mysql','jsp',' c','python','uml','swift','sql server','mysql','asp.net','pearl','prolog','lisp','jquery','visual basic','arduino','microcontroladores','assembler','unity','laravel','fortran','dart','haskell','cobol','delph','go','ajax','maria db',' r','ruby','kotlin','pascal','perl','rust','power bi','tableau','qlik','google analytics','google tag managerte','hootsuite','google adwords','power query','power pivot','bigquery','fortinet','checkpoint',
'html','html5','scala','scrum','ccsa','ccse','linux','.net','sql','waf','dbf','cctv','mdm','revit ','autocad2d','nodejs','nextjs','graphql','sequelize','redis','react','unix','matlab','cisco','veeam','prtg','css','mongodb','angular','ux','react','redux','flux','npm','routing-json','typescript','js','boostrap','unix','aws','mvc.net','azure','googlecloud','core','batch','fullstack','ngfp','juniper','klout']
def obtenerReferneciaDeFecha(fecha):
    try:
        if(fecha.find("Ayer")>= 0 ):
            fecha=datetime.datetime.today()+datetime.timedelta(days=-1)
            return fecha.strftime('%d/%m/%Y')

        if(fecha.find("días")>= 1 or fecha.find("día")>=1 or fecha.find("days")>=1):
            dias=int(re.sub('[^\d]','',fecha))
            fecha=datetime.datetime.today()+datetime.timedelta(days=-dias)
            return fecha.strftime('%d/%m/%Y')
        if(fecha.find("semana")>= 1 or fecha.find("semanas")>=1):
            semanas=int(re.sub('[^\d]','',fecha))
            fecha=datetime.datetime.today()+datetime.timedelta(weeks=-semanas)
            return fecha.strftime('%d/%m/%Y')
        if(fecha.find("hora")>= 1 or fecha.find("horas")>=1 or fecha.find("hours")>=1 ):
            horas=int(re.sub('[^\d]','',fecha))
            fecha=datetime.datetime.today()+datetime.timedelta(hours=-horas)
            return fecha.strftime('%d/%m/%Y')
        if(fecha.find("meses")>= 1 or fecha.find("mese")>=1):
            dias=int(re.sub('[^\d]','',fecha))*30
            fecha=datetime.datetime.today()+datetime.timedelta(days=-dias)
            return fecha.strftime('%d/%m/%Y')
    except:
            return "N/A"
    return "N/A"

def limpiarTexto(texto):
    texto=texto.replace("\n","")
    texto=re.sub('(\ \ )+', '', texto)
    return texto 


def obtenerDatosDeEmpleo(url,elementos,plataforma):
    
        
        page =requests.get(url)
        soup =BeautifulSoup(page.content,"html.parser")
        empresa=soup.select(elementos["empresa"])
        
        titulo=soup.select(elementos["titulo"])
       
        ubicacion=soup.select(elementos['ubicacion'])
        salario=soup.select(elementos["salario"])
        
        descripcion=soup.select(elementos["descripcion"])
        fecha=soup.select(elementos["fechaDePublicacion"])
        
        if(len(titulo)>=1):
            titulo=limpiarTexto(titulo[0].text)
            print(titulo)
        else:
            titulo="N/A"
        if(len(descripcion)>=1):
            descripcion=limpiarTexto(descripcion[0].text)
            matches = [x for x in listaDeEmpleos if x.lower() in descripcion.lower()]
            descripcion=matches
            
        else:
            descripcion="N/A"
        if(len(ubicacion)>=1):
            ubicacion=limpiarTexto(ubicacion[0].text)
        else:
            ubicacion="N/A"
        if(len(empresa)>=1):
            empresa=limpiarTexto(empresa[0].text)
        else:
            empresa="N/A"
        if(len(fecha)>=1):
           
            fecha=limpiarTexto(fecha[0].text)
            if(plataforma=="CompuTrabajo"):
                fecha= fecha.split("\r")
                fecha=fecha[-2]
            fecha=obtenerReferneciaDeFecha(fecha)
        else:
            fecha="N/A"

        if(len(salario)>=1):
            salario=limpiarTexto(salario[0].text)
            if(salario.find("yr")>0):
               salario=re.sub('[^\d^-]','',salario)
            
        else:
            salario="N/A"
        
        listaEmpleosACsv.append([elementos["busqueda"],titulo,empresa,ubicacion,url,salario,plataforma,descripcion,fecha])
        return {"titulo":titulo,"empresa":empresa,"ubicacion":ubicacion,"url":url,"salario":salario,"plataforma":plataforma,"descripcion":descripcion,"fecha":fecha}
    

def obtenerEmpleosDisponibles(url,contenido,palataforma):
    print("obteneniendo Empleo")
    page =requests.get(url)
    soup =BeautifulSoup(page.content,"html.parser")
    empleos=soup.find_all('a',class_=contenido["url"])
    i=0
    for empleo in empleos:
        url=empleo.get('href')
        if(contenido[ "url"]=='js-o-link'):
            url="https://www.computrabajo.com.mx"+url
        if(contenido[ "url"]=='sponTapItem'):
            url="https://mx.indeed.com"+url
         

        listaEmpleos.append(obtenerDatosDeEmpleo(url,contenido,palataforma))
        i=i+1
        if(i>=2):
            break

# Create your views here.
def index(request):
   
    return render(request, 'polls/index.html')
def buscar(request):

     
        listaDeInforme=list()
        puesto=request.POST["puesto"]
        url ="https://www.linkedin.com/jobs/search/?keywords="+puesto+"&location=México"
        print("url:"+url)
        obtenerEmpleosDisponibles(url,{
                "busqueda":puesto,
                "titulo":"h1.top-card-layout__title",
                "empresa":"span.topcard__flavor",
                "ubicacion":"span.topcard__flavor--bullet",
                "salario":"div.salary.compensation__salary",
                "url":'base-card__full-link',
                "descripcion":"div.show-more-less-html__markup",
                "fechaDePublicacion":"span.posted-time-ago__text"},"Linkedin")
        url ="https://mx.indeed.com/jobs?q="+puesto
        print("url:"+url)
        obtenerEmpleosDisponibles(url,{
                "busqueda":puesto,
                "empresa":"div.jobsearch-InlineCompanyRating",
                "titulo":"h1.jobsearch-JobInfoHeader-title",
                "ubicacion":"div.jobsearch-JobInfoHeader-subtitle div:nth-of-type(2)",
                "salario":"div.jobsearch-JobMetadataHeader-item",
                "url":"sponTapItem",
                "descripcion":"div.jobsearch-jobDescriptionText",
                "fechaDePublicacion":"div.jobsearch-JobMetadataFooter div"},"Indeed")
        url ="https://www.computrabajo.com.mx/trabajo-de-"+puesto
        print("url:"+url)
        obtenerEmpleosDisponibles(url,{
                "busqueda":puesto,
                "empresa":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(3) a",
                "titulo":"article.boxWhite.info_offer h1",
                "ubicacion":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(2)",
                "salario":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(6) p:nth-of-type(2)",
                "url":'js-o-link',
                "descripcion":"section.boxWhite.fl.w_100.detail_of.mb20.bWord",
                "fechaDePublicacion":"article.boxWhite p"},"CompuTrabajo")
        
        with open('empleos.csv', 'w', newline='',  encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(listaEmpleosACsv)
        listaDeInforme.append({"numeroDeEmpleos":plots.numeroDeVacantes()})
        listaDeInforme.append({"empleos":listaEmpleos})
        listaDeInforme.append({"fechasDeVacantes":plots.agruparPorFecha()})
        

        dump = json.dumps(listaDeInforme)
        return HttpResponse(dump, content_type='application/json')

def busquedaManual():
    languages = ['frontend','backend', 'desarollador-de-base-de-datos',
    'analista-de-base-datos','dba-trainee','dba-jr','dba-ssr','dba-sr','ingeniero-en-redes-jr','administrador-de-servidores',
    'analista-en-seguridad','arquitecto-de-ciberseguridad','programador-de-microcontroladores','ingeniero-en-software','dearollador-movil']  
    
    for index in range(len(languages)):
        print("Obteniendo empleos")
        puesto=languages[index]

        url ="https://www.linkedin.com/jobs/search/?keywords="+puesto+"&location=México"
        print("url:"+url)
        obtenerEmpleosDisponibles(url,{
                "busqueda":puesto,
                "titulo":"h1.top-card-layout__title",
                "empresa":"span.topcard__flavor",
                "ubicacion":"span.topcard__flavor--bullet",
                "salario":"div.salary.compensation__salary",
                "url":'base-card__full-link',
                "descripcion":"div.show-more-less-html__markup",
                "fechaDePublicacion":"span.posted-time-ago__text"},"Linkedin")
        url ="https://mx.indeed.com/jobs?q="+puesto
        print("url:"+url)

        obtenerEmpleosDisponibles(url,{
                "busqueda":puesto,
                "empresa":"div.jobsearch-InlineCompanyRating",
                "titulo":"h1.jobsearch-JobInfoHeader-title",
                "ubicacion":"div.jobsearch-JobInfoHeader-subtitle div:nth-of-type(2)",
                "salario":"div.jobsearch-JobMetadataHeader-item",
                "url":"sponTapItem",
                "descripcion":"div.jobsearch-jobDescriptionText",
                "fechaDePublicacion":"div.jobsearch-JobMetadataFooter div"},"Indeed")

        for i in range(1,3):
            url ="https://mx.indeed.com/jobs?q="+puesto+"&start="+str(i)+"0"
            print(url)

            obtenerEmpleosDisponibles(url,{
                "busqueda":puesto,
                "empresa":"div.jobsearch-InlineCompanyRating",
                "titulo":"h1.jobsearch-JobInfoHeader-title",
                "ubicacion":"div.jobsearch-JobInfoHeader-subtitle div:nth-of-type(2)",
                "salario":"div.jobsearch-JobMetadataHeader-item",
                "url":"sponTapItem",
                "descripcion":"div.jobsearch-jobDescriptionText",
                "fechaDePublicacion":"div.jobsearch-JobMetadataFooter div"},"Indeed")


        url ="https://www.computrabajo.com.mx/trabajo-de-"+puesto
        obtenerEmpleosDisponibles(url,{
                "busqueda":puesto,
                "empresa":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(3) a",
                "titulo":"article.boxWhite.info_offer h1",
                "ubicacion":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(2)",
                "salario":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(6) p:nth-of-type(2)",
                "url":'js-o-link',
                "descripcion":"section.boxWhite.fl.w_100.detail_of.mb20.bWord",
                "fechaDePublicacion":"article.boxWhite p"},"CompuTrabajo")

        for i in range(1,3):
            url ="https://www.computrabajo.com.mx/trabajo-de-"+puesto+"?q="+puesto+"&p="+str(i)
            print(url)
            obtenerEmpleosDisponibles(url,{
                "busqueda":puesto,
                "empresa":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(3) a",
                "titulo":"article.boxWhite.info_offer h1",
                "ubicacion":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(2)",
                "salario":"section.boxWhite.fl.w_100.ocultar_mvl.p30 ul li:nth-of-type(6) p:nth-of-type(2)",
                "url":'js-o-link',
                "descripcion":"section.boxWhite.fl.w_100.detail_of.mb20.bWord",
                "fechaDePublicacion":"article.boxWhite p"},"CompuTrabajo")

        with open('empleos.csv', 'w', newline='',  encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows(listaEmpleosACsv)

#busquedaManual()