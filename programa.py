from funciones import *

contParticipantes = 0
contDisparos = 0
disparos = 0
contMasculino = 0
contFemenino = 0
contEdadFem = 0
db = []
promedioMayor = []
numeroParticipante = int(input('Ingrese el numero de participante: '))

while numeroParticipante < 999:
    nombreParticipante = (input('Ingrese nombre del participante: '))
    apellidoParticipante = (input('Ingrese apellido del participante: '))
    edadParticipante = int(input('Ingrese edad del participante: '))
    sexoParticipante = (input('Ingrese el sexo del participante: '))

    x = float(input('Ingrese posición en eje x: '))
    y = float(input('Ingrese posición en eje y: '))
    disparo1 = distanciaDisparo(x, y)

    x = float(input('Ingrese posición en eje x: '))
    y = float(input('Ingrese posición en eje y: '))
    disparo2 = distanciaDisparo(x, y)

    x = float(input('Ingrese posición en eje x: '))
    y = float(input('Ingrese posición en eje y: '))
    disparo3 = distanciaDisparo(x, y)

    totalDisparos = (disparo1+disparo2+disparo3)


    datosParticipante = {
        'numeroParticipante': '',
        'nombreParticipante': '',
        'apellidoParticipante': '',
        'edadParticipante': '',
        'sexoParticipante': '',
        'disparo1': '',
        'disparo2': '',
        'disparo3': '',
        'mejorDisparo': '',
        'promedioDisparo': ''
    }

    datosParticipante['numeroParticipante'] = numeroParticipante
    datosParticipante['nombreParticipante'] = nombreParticipante
    datosParticipante['apellidoParticipante'] = apellidoParticipante
    datosParticipante['edadParticipante'] = edadParticipante
    datosParticipante['sexoParticipante'] = sexoParticipante
    datosParticipante['disparo1'] = disparo1
    datosParticipante['disparo2'] = disparo2
    datosParticipante['disparo3'] = disparo3
    datosParticipante['mejorDisparo'] = mejorDisparo(disparo1, disparo2, disparo3)
    datosParticipante['promedioDisparo'] = promedioDisparo(disparo1, disparo2, disparo3)
    
    db.append(datosParticipante)

    contParticipantes += 1
    disparos += 3
    contDisparos = contDisparos + totalDisparos

    for key, value in datosParticipante.items():
        if value == 'm':
            contMasculino += 1
        else:
            if value == 'f':
                contFemenino += 1
                contEdadFem = contEdadFem + edadParticipante

    numeroParticipante = int(input('Ingrese el numero de participante: '))

promedioEdadMujer = contEdadFem // contFemenino    
mejorDisparoOrdenado = ordenaDisparos(db)
ganadores = podioGanadores(db)
participanteUltimo = ultimoParticipante(db)
edadOrdenado = ordenaEdad(db)
promedioTotalDisparos = promedioDisparosGeneral(contDisparos, disparos)

for dato in db:
    if dato['promedioDisparo'] > promedioTotalDisparos:
        promedioMayor.append(dato)

db_file = open('db.txt', 'w')
db_file.write(f'Podio de los ganadores: {ganadores}\n')
db_file.write(f'El ultimo participante: {participanteUltimo}\n')
db_file.write(f'Cantidad total de participantes: {contParticipantes}\n')
db_file.write(f'Cantidad de hombres que fueron parte del concurso: {contMasculino}\n')
db_file.write(f'Edad promedio de las mujeres: {promedioEdadMujer}\n')
db_file.write(f'Participantes ordenados por edad: {edadOrdenado}\n')
db_file.write(f'Promedio de disparos general: {promedioTotalDisparos}\n')
db_file.write(f'Participantes cuyo promedio de disparos es mayor al promedio general: {promedioMayor}')
db_file.close()

print(f'Podio de los ganadores: {ganadores}\n')
print(f'El último participante: {participanteUltimo}\n')
print(f'Cantidad total de participantes: {contParticipantes}\n')
print(f'Cantidad de hombres que fueron parte del concurso: {contMasculino}\n')
print(f'Edad promedio de las mujeres: {promedioEdadMujer}\n')
print(f'Participantes ordenados por edad: {edadOrdenado}\n')
print(f'Promedio de disparos general: {promedioTotalDisparos}\n')
print(f'Participantes cuyo promedio de disparos es mayor al promedio general: {promedioMayor}')