#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@autor: David Santos
"""
from bs4 import BeautifulSoup
import requests

#Debido al uso de caracteres especiales (tildes, ñ, ¿, etc) en nuestro idioma el español se debe realizar la codificacion a utf-8
def codificar(texto):
    return texto.encode('utf-8')

def scraping(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, "lxml")
    print("Se realiza el scraping a la página %s" %URL)
    print(soup.title.string)
    print(soup.h1.string)
    for parrafo in soup.find_all('p'):
        parrafos = codificar(parrafo.text)
        print(parrafos)

#@link tuto of this: https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211
#@link tuto parent: https://www.danielprimo.io/blog/web-scrapping-con-python-primeros-pasos-desafiopython 

if __name__ == "__main__":
    scraping("https://es.wikipedia.org/wiki/Python")
