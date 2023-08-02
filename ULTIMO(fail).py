import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se deberan cargar tantos vehiculos como el usuario desee. 
    Los datos a cargar de cada vehiculo son: tipo de vehiculo (auto, camioneta, moto) y kilometros*.

* Todos los autos son usados.

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al presionar el boton mostrar se deberan listar todos los vehiculos ingresados con su correspondiente kilometraje y su posicion en la lista.
Ejemplo: 1 - Auto - 1000 km
         2 - Camioneta - 2000 km
         etc..

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al presionar el boton Informar 
    0- El mayor kilometraje y su tipo de vehiculo.
    1- El menor kilometraje y su tipo de vehiculo.
    2- Kilometraje promedio de los autos.
    3- Precio promedios de todos los servicios.
    4- Informar los kilometrajes que superan el promedio (total).
    5- Informar los kilometrajes que NO superan el promedio (total).
    6- Informar la cantidad de vehiculos de cada tipo.
    7- Informar el precio promedio de los servicios cuyo kilometraje es mayor a 10000 kms.
    8- Indicar el mayor de los promedios de kilometros por tipo de vehiculo.
    9- Informar el monto promedio de cada servicio realizado.


Los montos de los servicios son:
    - Auto: $15000
    - Camioneta: $25000
    - Moto: $10000
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("EXAMEN INGRESO")
        
        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_tipo_vehiculo = []
        self.lista_marca_vehiculo = []

    def btn_agregar_on_click(self):
        tipo_auto = prompt("ingrese tipo de vehiculo", "moto, camioneta o auto?")
        kilometro = prompt("ingrese kilmetros", "ingrese kilometros")
        tipo_valido = ["auto", "camioneta", "moto"]
        lista_vehiculos = self.lista_tipo_vehiculo
        lista_kilometros = self.lista_marca_vehiculo
        contador = 0
        if tipo_auto:
            for tipo in tipo_auto:
                if not tipo.isalpha:
                    break
                else:
                    if tipo_auto != tipo_valido:
                        break
                    else:
                        question ("ingresar mas", "ingresar mas?")
                        if question == True:
                            lista_vehiculos.append(tipo_auto)
                            lista_kilometros.append(kilometro)
                            contador += 1
                            continue
                        else: 
                            lista_vehiculos.append(tipo_auto)
                            lista_kilometros.append(kilometro)
                            break


    
    def btn_mostrar_on_click(self):
        lista_vehiculos = self.lista_tipo_vehiculo
        lista_kilometro = self.lista_marca_vehiculo

        i = 0
        for auto in lista_vehiculos:
            print(f"indice {i}")
            i += 1
        for i in range(len(lista_vehiculos)):
            print(f"indice{i} - tipo {lista_vehiculos[i]}")

        i2 = 0
        for kilometro in lista_kilometro:
            print(f"indice{i}")
            i2 += 1
        for i in range(len(lista_kilometro)):
            print (f"indice{i} - kilometros {lista_kilometro}")

        listafinal = []
        for i, auto in enumerate(lista_vehiculos):
            print(f"indice{i} - tipo {lista_vehiculos}")

        for i, kilometro in enumerate(lista_kilometro):
            print(f"indice{i} - kilometro {lista_kilometro}")

        listafinal.append(auto + kilometro)

        alert("resultado", listafinal)

        


    def btn_informar_on_click(self):
       pass

       
if __name__ == "__main__":
    app = App()
    app.geometry("200x400")
    app.mainloop()
