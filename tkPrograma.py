from tkinter import Tk, Label, Entry, Button, messagebox, Radiobutton, Checkbutton
from tkinter import IntVar, StringVar
from openpyxl import Workbook
import csv

root = Tk()
root.title("Campeonato de tiro con arco y flecha")
root.config(width=400, height=500)

db = []

def mejorDisparo(dis1, dis2, dis3):
    mejor = dis1
    if dis2 < mejor:
       mejor = dis2
    if dis3 < mejor:
       mejor = dis3
    return mejor

def guardar():

    iD = entry_iD.get()
    nom = entry_nom.get()
    ape = entry_ape.get()
    edad = entry_edad.get()
    sexo = opcion.get()
    dis1 = entry_d1.get()
    dis2 = entry_d2.get()
    dis3 = entry_d3.get()
    
    mejor = mejorDisparo(dis1, dis2, dis3)
    datosParticipante = [iD, nom, ape, edad, sexo, mejor]
    
    db.append(datosParticipante)
    
    with open('db.csv', 'a', newline='') as archivo:
        registro = csv.writer(archivo)
        headers = ['Id', 'Nombre', 'Apellido', 'Edad', 'Sexo', 'Mejor disparo']
        
        registro.writerow(headers)
         
        registro.writerow(datosParticipante)
    
    borrar()
    ordenaDisparos(db)
    
    print(db)

def borrar():
    entry_nom.delete(0, 'end')
    entry_ape.delete(0, 'end')
    entry_edad.delete(0, 'end')
    entry_d1.delete(0, 'end')
    entry_d2.delete(0, 'end')
    entry_d3.delete(0, 'end')
    entry_iD.delete(0, 'end')


def ordenaDisparos(db):
    intercambios = True
    numPasada = len(db)-1
    
    while numPasada > 0 and intercambios:
        intercambios = False
        for datosParticipante in range(numPasada):
            if db[datosParticipante][-1] > db[datosParticipante+1][-1]:
                intercambios = True
                db[datosParticipante],db[datosParticipante+1] = db[datosParticipante+1],db[datosParticipante]
        numPasada = numPasada-1
    return ordenaDisparos
    
def exportar():
    
    workbook = Workbook()
    sheet = workbook.active
    
    headers = ['Id', 'Nombre', 'Apellido', 'Edad', 'Sexo', 'Mejor disparo']
    sheet.append(headers)

    ordenaDisparos(db)

    for datosParticipante in db:
        sheet.append(datosParticipante)
    
    workbook.save(filename='Campeonato de tiro con arco y flecha.xlsx')
    
    borrar()    

def seleccionar():
    opcion.get()
    

def ganador():
    ganador = db[0]
    messagebox.showinfo('El ganador es', ganador)
    print(f'ganador {ganador}')



label_iD = Label(root, text='Id')
label_iD.place(x=5, y=10)
entry_iD = Entry(root, width=35)
entry_iD.place(x=100, y=10)

label_nom = Label(root, text='Nombre')
label_nom.place(x=5, y=50)
entry_nom = Entry(root, width=35)
entry_nom.place(x=100, y=50)

label_ape = Label(root, text='Apellido')
label_ape.place(x=5, y=100)
entry_ape = Entry(root, width=35)
entry_ape.place(x=100, y=100)

label_edad = Label(root, text='Edad')
label_edad.place(x=5, y=150)
entry_edad = Entry(root, width=35)
entry_edad.place(x=100, y=150)

  
opcion = IntVar()
rb1 = Radiobutton(root, text='Femenino', value='1', command=seleccionar, variable=opcion)
rb1.place(x=5,y=200)
rb2 = Radiobutton(root, text='Masculino', value='2', command=seleccionar, variable=opcion)
rb2.place(x=100,y=200)

label_d1 = Label(root, text='Disparo 1')
label_d1.place(x=5, y=250)
entry_d1 = Entry(root, width=35)
entry_d1.place(x=100, y=250)

label_d2 = Label(root, text='Disparo 2')
label_d2.place(x=5, y=300)
entry_d2 = Entry(root, width=35)
entry_d2.place(x=100, y=300)

label_d3 = Label(root, text='Disparo 3')
label_d3.place(x=5, y=350)
entry_d3 = Entry(root, width=35)
entry_d3.place(x=100, y=350)


btn_guardar = Button(root, text='Guardar', command=guardar)
btn_guardar.place(x=80, y=400)

btn_guardar = Button(root, text='Ganador', command=ganador)
btn_guardar.place(x=160, y=400)

btn_export = Button(root, text='Exportar xls', command=exportar)
btn_export.place(x=240, y=400)



root.mainloop()