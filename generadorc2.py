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

archivo=open("datosgeneradosc2.txt","w")

for entry in usuarios:
    #identificador
    usuario=entry[0]
    avatar=entry[1]
    archivo.write(avatar+";")
    #cantloves,comments,wallpost,snapshot
#     cursor.execute("SELECT type FROM feed WHERE feed.source='"+str(avatar)+"'")
#     matches=cursor.fetchall()
#     cantlove=0
#     cantcom=0
#     cantwall=0
#     cantsnap=0
#     for match in matches:
#         tipo=match[0]
#         if tipo=="LOVE":
#             cantlove+=1            
#         elif tipo=="COMMENT":
#             cantcom+=1
#         elif tipo=="WALLPOST":
#             cantwall+=1
#         elif tipo=="SNAPSHOT":
#             cantsnap+=1
#     archivo.write(str(cantlove)+";"+str(cantcom)+";"+str(cantwall)+";"+str(cantsnap)+";")
    
# ##    #avgsubjectivity status
# ##    cursor.execute("SELECT data FROM feed WHERE feed.source='"+str(avatar)+"' AND feed.destination='"+str(avatar)+"'")
# ##    data=cursor.fetchall()
##    cant_estados=0
##    contadorsubj=0
##    contadorpol=0
##
##    datossub1=[]
##    datospol1=[]
##    
##    for estado in data:
##        if len(estado[0])!=0:   #necesario pq aparecen muchas tuplas de la forma ('',)
##            cant_estados+=1
##            subjectivity=calcsubj(estado[0])
##            contadorsubj+=subjectivity
##            polarity=calcpol(estado[0])       
##            contadorpol+=polarity
##
##            datossub1.append(subjectivity)
##            datospol1.append(polarity)
##            
##    if cant_estados>0:
##        avg_subjectivity=contadorsubj/cant_estados
##        avg_polarity_STATUS=contadorpol/cant_estados      
##
##        
##    else:
##        avg_subjectivity=0
##        avg_polarity_STATUS=0 #guardamos este valor para escribirlo despues y mantener el orden pedido
##        
##    archivo.write(str(avg_subjectivity)+";")
##
##    #avgsubject de comentariossoc
##
##    cursor.execute("SELECT data FROM feed WHERE feed.source='"+str(avatar)+"' AND type='COMMENT'")
##    matches=cursor.fetchall()
##    cant_com=0
##    contadorsubj=0
##    contadorpol=0
##
##    datossub2=[]
##    datospol2=[]
##    
##    for comentario in matches:
##        if len(comentario[0])!=0:
##            cant_com+=1
##            subjectivity=calcsubj(comentario[0])
##            contadorsubj+=subjectivity
##            polarity=calcpol(comentario[0])
##            contadorpol+=polarity
##
##            datossub2.append(subjectivity)
##            datospol2.append(polarity)
##            
##    if cant_com>0:
##        avg_subjectivity=contadorsubj/cant_com
##        avg_polarity_COMMENTSOC=contadorpol/cant_com #guardamos valor pa dps
##    else:
##        avg_subjectivity=0
##        avg_polarity_COMMENTSOC=0  #guardamos valor para dps
##    archivo.write(str(avg_subjectivity)+";")


    #avgsubject de reviews 

    cursor.execute("SELECT review FROM reviews WHERE id='"+str(usuario)+"'")
    data=cursor.fetchall()
    cant_rev=0
    contadorsubj=0
    contadorpol=0

    datossub3=[]
    datospol3=[]
    
    for review in data:
        if len(review[0])!=0:
            cant_rev+=1
            subjectivity=calcsubj(review[0])
            contadorsubj+=subjectivity
            polarity=calcpol(review[0])
            contadorpol+=polarity

            datossub3.append(subjectivity)
            datospol3.append(polarity)
            
    if cant_rev>0:
        avg_subjectivity=contadorsubj/cant_rev
        avg_polarity_REVIEWS=contadorpol/cant_rev
    else:
        avg_subjectivity=0
        avg_polarity_REVIEWS=0  #guardamos valor para dps
    archivo.write(str(avg_subjectivity)+";")
        
    #avgsubject de commentsmarket
    
    cursor.execute("SELECT comment FROM comments WHERE id='"+str(usuario)+"'")
    data=cursor.fetchall()
    cant_comm=0
    contadorsubj=0
    contadorpol=0

    datossub4=[]
    datospol4=[]
    
    for comentario in data:
        if len(comentario[0])!=0:
            cant_comm+=1
            subjectivity=calcsubj(comentario[0])
            contadorsubj+=subjectivity
            polarity=calcpol(comentario[0])
            contadorpol+=polarity

            
            datossub4.append(subjectivity)
            datospol4.append(polarity)

    
    if cant_comm>0:
        avg_subjectivity=contadorsubj/cant_comm
        avg_polarity_COMENTSMARK=contadorpol/cant_comm
    else:
        avg_subjectivity=0
        avg_polarity_COMENTSMARK=0 #guardamos este valor para escribirlo dps
    archivo.write(str(avg_subjectivity)+";")

    #desviacion estandar subject
    
##    stdev_stat_sub=stand_dev(datossub1)
##    archivo.write(str(stdev_stat_sub)+";")
##    
##    stdev_comsoc_sub=stand_dev(datossub2)
##    archivo.write(str(stdev_comsoc_sub)+";")
    
    stdev_rev_sub=stand_dev(datossub3)
    archivo.write(str(stdev_rev_sub)+";")
    
    stdev_commark_sub=stand_dev(datossub4)
    archivo.write(str(stdev_commark_sub)+";") 
    
    #avgpolarity 

##    archivo.write(str(avg_polarity_STATUS)+";")
##    archivo.write(str(avg_polarity_COMMENTSOC)+";")    
    archivo.write(str(avg_polarity_REVIEWS)+";")
    archivo.write(str(avg_polarity_COMENTSMARK)+";")

    #desviacion estandar polarity

##    stdev_stat_pol=stand_dev(datospol1)
##    archivo.write(str(stdev_stat_pol)+";")
##    
##    stdev_comsoc_pol=stand_dev(datospol2)
##    archivo.write(str(stdev_comsoc_pol)+";")
    
    stdev_rev_pol=stand_dev(datospol3)
    archivo.write(str(stdev_rev_pol)+";")
    
    stdev_commark_pol=stand_dev(datospol4)
    archivo.write(str(stdev_commark_pol)+"\n") 

    
archivo.close()


cursor.close()


connection.close ()


