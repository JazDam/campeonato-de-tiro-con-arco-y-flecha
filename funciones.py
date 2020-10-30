from math import sqrt

def distanciaDisparo(x, y):
    distancia =  round(sqrt(x**2 + y**2))
    return distancia

def mejorDisparo(dis1, dis2, dis3):
    mejor = dis1
    if dis2 < mejor:
       mejor = dis2
    if dis3 < mejor:
       mejor = dis3
    return mejor

def promedioDisparo(disparo1, disparo2, disparo3):
    promedio = (disparo1+disparo2+disparo3)//3
    return promedio

def ordenaDisparos(db):
    intercambios = True
    numPasada = len(db)-1
    cont = 0
    while numPasada > 0 and intercambios:
        intercambios = False
        for k in range(numPasada):
            cont += 1
            if db[k]['mejorDisparo'] > db[k+1]['mejorDisparo']:
                intercambios = True
                db[k],db[k+1] = db[k+1],db[k]
        numPasada = numPasada-1
    return ordenaDisparos

def podioGanadores(db):
    podioGanadores = db[:3]
    return podioGanadores

def ultimoParticipante(db):
    ultimoParticipante = db[-1]
    return ultimoParticipante

def ordenaEdad(db):
    intercambios = True
    numPasada = len(db)-1
    cont = 0
    while numPasada > 0 and intercambios:
        intercambios = False
        for k in range(numPasada):
            cont += 1
            if db[k]['edadParticipante'] > db[k+1]['edadParticipante']:
                intercambios = True
                db[k],db[k+1] = db[k+1],db[k]
        numPasada = numPasada-1
    return db

def promedioDisparosGeneral(contDisparos, disparos):
    promedioDisparosGeneral = contDisparos // disparos
    return promedioDisparosGeneral