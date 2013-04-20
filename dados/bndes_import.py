#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import urllib2
import json
import sys
import pymongo

id = sys.argv
url = id[1]
ano = id[2]
stream = urllib2.urlopen(url)
data = csv.reader(stream, delimiter=';')
conn = pymongo.MongoClient()
bndes = conn.bndes
new_data = []

if ano == '2012':

    for dados in data:
        if dados[1] != '' and dados[1] != 'CNPJ':
            
            valor_split = dados[5].split('.')
            valor_contrato = ''.join(valor_split)

            new_data.append({'empresa' : unicode(dados[0], "ISO-8859-1"),
                             'cnpj' : unicode(dados[1], "ISO-8859-1"),
                             'desc_projeto' : unicode(dados[2], "ISO-8859-1"), 
                             'uf' : unicode(dados[3], "ISO-8859-1"),
                             'data_contrato' : unicode(dados[4], "ISO-8859-1"),
                             'valor_contrato' : int(valor_contrato),
                             'porte_empresa' : unicode(dados[6], "ISO-8859-1"),
                             'ramo' : unicode(dados[7], "ISO-8859-1"),
                             'area' : unicode(dados[8], "ISO-8859-1"),
                             'modalidade' : unicode(dados[9], "ISO-8859-1")})


    for item in new_data:
        new_item = json.dumps(item)
        bndes.doismiledoze.insert(eval(new_item))


if ano == '2011':
    print ano
    for dados in data:
        if dados[5] != '' and dados[1] != 'CNPJ':
            print dados