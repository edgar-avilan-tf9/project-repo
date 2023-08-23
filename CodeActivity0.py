# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:09:42 2023

"""

import requests
import json
import numpy as np

link='https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'

# Conectarse a los datos del link
f = requests.get(link)
mtext=f.text

# Convertir a formato diccionario usando JSON
res = json.loads(mtext)

# Explorar los valores en el apartado 'items'
res['items'][0].keys()

#Obtener el número de respuestas contestadas y no contestadas
count_answered=0
count_notanswered=0

# Iterar a lo largo de todo el apartado items buscando los que hayan sido respondidos o no
for i in res['items']:
    #print(i['is_answered'])
    if i['is_answered']==True:
        count_answered+=1
    else:
        count_notanswered+=1
print(f'Número de contestadas: {count_answered} Número de no contestadas: {count_notanswered}')


# Buscar la respuesta con menor número de vistas
bottom_answer= {'title':'', 'question_id':0,'position':0, 'views_count':np.inf}
count=0
for i in res['items']:
    #print(i['view_count'])
    if i['view_count']<bottom_answer['views_count']:
        bottom_answer['views_count'] =i['view_count']
        bottom_answer['title']= i['title']
        bottom_answer['question_id']= i['question_id']
        bottom_answer['position']= count
    else:
        pass
    count+=1
print(f'Respuesta con menos vistas: {bottom_answer["title"]} , Número de vistas {bottom_answer["views_count"]}')

# Buscar la respuesta mas vieja
old_answer= {'title':'', 'question_id':0,'position':0, 'views_count':0, 'date':np.inf}
count=0
for i in res['items']:
    #print(i['view_count'])
    if i['creation_date']<old_answer['date']:
        old_answer['views_count'] =i['view_count']
        old_answer['title']= i['title']
        old_answer['question_id']= i['question_id']
        old_answer['position']= count
        old_answer['date']=i['creation_date']
    else:
        pass
    count+=1
print(f"Respuesta mas vieja: {old_answer['title']}, {old_answer['date']}")


# Buscar la mas actual
newest_answer= {'title':'', 'question_id':0,'position':0, 'views_count':0, 'date':0}
count=0
for i in res['items']:
    #print(i['view_count'])
    if i['creation_date']>newest_answer['date']:
        newest_answer['views_count'] =i['view_count']
        newest_answer['title']= i['title']
        newest_answer['question_id']= i['question_id']
        newest_answer['position']= count
        newest_answer['date']=i['creation_date']
    else:
        pass
    count+=1
print(f"Respuesta mas actual: {newest_answer['title']}, {newest_answer['date']}")

#Owner con mayor reputación
toprep_answer= {'title':'', 'question_id':0,'position':0, 'user_id':0, 'reputation':0}
count=0
for i in res['items']:
    if 'reputation' in i['owner'].keys():
        #print(i['owner'].keys())
        if i['owner']['reputation']>toprep_answer['reputation']:
            toprep_answer['user_id'] =i['owner']['user_id']
            toprep_answer['title']= i['title']
            toprep_answer['question_id']= i['question_id']
            toprep_answer['position']= count
            toprep_answer['reputation']=i['owner']['reputation']
        else:
            pass
    count+=1

print(f"Respuesta del owner con mayor reputación: {toprep_answer['title']}, {toprep_answer['reputation']}")

