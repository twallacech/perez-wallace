#!/usr/bin/python
# -*- coding: utf-8 -*-


##
##  ESTE SCRIPT GENERA UN ARCHIVO .TXT A PARTIR DE LA BASE DE DATOS
##  
##  CADA LINEA CORRESPONDE A LA INFORMACIÓN DE UN USUARIO, SEGÚN EL FORMATO SIGUIENTE:
##
##  "avatar", N°Loves, N°Comments, N°Wallpost, N°Snapshot,                                                        (Continua abajo)
##  AvgSubj_Status, AvgSubj_Comentarios_Soc, AvgSubj_Reviews, AvgSubj_Comentarios_Market,                         (Continua abajo)
##  St_dev(Subj_Status), St_dev(Subj_Comentarios_Soc), St_dev(Subj_Reviews), St_dev(Subj_Comentarios_Market),     (Continua abajo)
##  AvgPol_Status, AvgPol_Comentarios_Soc, AvgPol_Reviews, AvgPol_Comentarios_Market,                             (Continua abajo)
##  St_dev(Pol_Status), St_dev(Pol_Comentarios_Soc), St_dev(Pol_Reviews), St_dev(Pol_Comentarios_Market)          (Continua abajo)
##


from __future__ import division
import cymysql as MySQLdb

def stand_dev(lista):
    if len(lista)>1:
        contador_prom=0
        cant_datos=0
        for numero in lista:
            cant_datos+=1
            contador_prom+=numero
        promedio=contador_prom/cant_datos
        contador_prom_dev=0
        for numero in lista:
            diferencia=abs(promedio-numero)
            dif_square=diferencia**2
            contador_prom_dev+=dif_square
        varianza=contador_prom_dev/(cant_datos-1)
        stdev=varianza**(1/2)    
        return stdev
    else:
        return 0

from textblob import TextBlob


def calcsubj(string):
    testimonial=TextBlob(string)
    return testimonial.sentiment.subjectivity

def calcpol(string):
    testimonial=TextBlob(string)
    return testimonial.sentiment.polarity

connection = MySQLdb.connect (host = "localhost", user = "", passwd = "", db = "iic1005", charset = 'utf8')


cursor = connection.cursor ()

cursor.execute("SELECT id,avatar FROM about")
data=cursor.fetchall()
usuarios=data[:]

archivo=open("datosgeneradosc3.txt","w")

for entry in usuarios:
    #identificador
    usuario=entry[0]
    avatar=entry[1]
    archivo.write(avatar+";")
    #indegree
    cursor.execute("SELECT source,destination FROM feed WHERE feed.destination='"+str(avatar)+"'")
    matches=cursor.fetchall()
    contador=0
    for match in matches:
        fuente=match[0]
        destino=match[1]
        if fuente!=destino:
            contador+=1
    indegree=str(contador)
    archivo.write(indegree +";")
    #outdegree
    cursor.execute("SELECT source,destination FROM feed WHERE feed.source='"+str(avatar)+"'")
    matches=cursor.fetchall()
    contador=0
    for match in matches:
        fuente=match[0]
        destino=match[1]
        if fuente!=destino:
            contador+=1
    outdegree=str(contador)
    archivo.write(outdegree +"\n")
        
archivo.close()


cursor.close()


connection.close ()


