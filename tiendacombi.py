from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                     f'$ {int(postres.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'Lo esperamos pronto')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1200x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo de la ventana
aplicacion.title("Mi Restaurante - Sistema de Facturacion")

# color de fondo de la ventana
aplicacion.config(bg='#DCE6F1')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Restaurante ANEL LEONEL MORALES ARZATE', fg='azure4',
                        font=('Dosis', 30), bg='#DCE6F1', width=45)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='#DCE6F1')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='#DCE6F1')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='#DCE6F1')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'coredero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2', 'pizza3']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino1', 'vino2', 'cerveza1', 'cerveza2']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'pastel1', 'pastel2', 'pastel3']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)

    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    # crear checkbutton
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                         command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # crear los cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador += 1


# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

etiqueta_costo_postres = Label(panel_costos,
                              text='Costo Postres',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuestos = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                       '1', '2', '3', 'x', 'R', 'B', '0', '/']
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))



# evitar que la pantalla se cierre
aplicacion.mainloop()


import sqlite3

def crear_bd():
	conexion = sqlite3.connect("restaurante_final.db")
	cursor = conexion.cursor()

	try:
		cursor.execute('''CREATE TABLE categoria(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL)''')
	except sqlite3.OperationalError:
		print("La tabla de Categorías ya existe.")
	else:
		print("La tabla de Categorías se ha creado correctamente.")


	try:
		cursor.execute('''CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
	except sqlite3.OperationalError:
		print("La tabla de Platos ya existe.")
	else:
		print("La tabla de Platos se ha creado correctamente.")


	conexion.close()


def agregar_categoria():
	categoria = input("¿Nombre de la nueva categoría?\n> ")

	conexion = sqlite3.connect("restaurante_final.db")
	cursor = conexion.cursor()

	try:
		cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria) )
	except sqlite3.IntegrityError:
		print("La categoría '{}' ya existe.".format(categoria))
	else:
		print("Categoría '{}' creada correctamente.".format(categoria))

	conexion.commit()
	conexion.close()


def agregar_plato():

	conexion = sqlite3.connect("restaurante_final.db")
	cursor = conexion.cursor()

	categorias = cursor.execute("SELECT * FROM categoria").fetchall()
	print("Selecciona una categoría para añadir el plato:")
	for categoria in categorias:
		print("[{}] {}".format(categoria[0], categoria[1]))

	categoria_usuario = int(input("> "))

	plato = input("¿Nombre del nuevo plato?\n> ")

	try:
		cursor.execute("INSERT INTO plato VALUES (null, '{}', {})".format(plato, categoria_usuario) )
	except sqlite3.IntegrityError:
		print("El plato '{}' ya existe.".format(plato))
	else:
		print("Plato '{}' creado correctamente.".format(plato))


	conexion.commit()
	conexion.close()


def mostrar_menu():

	conexion = sqlite3.connect("restaurante_final.db")
	cursor = conexion.cursor()	

	categorias = cursor.execute("SELECT * FROM categoria").fetchall()	
	for categoria in categorias:
		print(categoria[1])
		platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
		for plato in platos:
			print("\t{}".format(plato[1]))

	conexion.close()


# Crear la base de datos
crear_bd()

# Menú de opciones del programa
while True:
	print("\nBienvenido al gestor del restaurante!")
	opcion = input("\nIntroduce una opción:\n[1] Agregar una categoría\n[2] Agregar un plato\n[3] Mostrar el menú\n[4] Salir del programa\n\n> ")

	if opcion == "1":
		agregar_categoria()

	elif opcion == "2":
		agregar_plato()

	elif opcion == "3":
		mostrar_menu()

	elif opcion == "4":
		print("Nos vemos!")
		break

	else:
		print("Opción incorrecta")

"""
SISTEMA DE GESTION - MI RESTAURANTE
----------------------------------
Aplicacion de escritorio desarrollada con Python, Tkinter y SQLite.

Funciones:
- Registrar ventas y generar recibos.
- Guardar ventas y detalles en una base de datos SQLite.
- Consultar el historial de ventas.
- Administrar el catalogo de productos y sus precios.
- Mostrar reportes graficos: ventas por dia, ventas por mes,
  productos mas vendidos e ingresos por categoria.
- Consultar los ingresos totales.

Instalacion:
    pip install matplotlib

Ejecucion:
    python mi_restaurante_mejorado.py

La base de datos restaurante.db se crea automaticamente junto al programa.
"""

import sqlite3
from pathlib import Path
from datetime import datetime, date, timedelta
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

# Matplotlib se utiliza para dibujar las graficas dentro de Tkinter.
try:
    from matplotlib.figure import Figure
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    MATPLOTLIB_DISPONIBLE = True
except ImportError:
    MATPLOTLIB_DISPONIBLE = False


# ---------------------------------------------------------------------
# CONFIGURACION GENERAL
# ---------------------------------------------------------------------

NOMBRE_RESTAURANTE = "Restaurante ANEL LEONEL MORALES ARZATE"
IMPUESTO = 0.07  # Se conserva el 7 % de impuesto del programa original.
SIMBOLO_MONEDA = "$"

# La base de datos se guarda en la misma carpeta que este archivo.
RUTA_BASE_DATOS = Path(__file__).resolve().with_name("restaurante.db")

# Productos iniciales tomados del programa original.
PRODUCTOS_INICIALES = [
    ("Pollo", "Comida", 1.32),
    ("Cordero", "Comida", 1.65),
    ("Salmon", "Comida", 2.31),
    ("Merluza", "Comida", 3.22),
    ("Kebab", "Comida", 1.22),
    ("Pizza 1", "Comida", 1.99),
    ("Pizza 2", "Comida", 2.05),
    ("Pizza 3", "Comida", 2.65),
    ("Agua", "Bebida", 0.25),
    ("Soda", "Bebida", 0.99),
    ("Jugo", "Bebida", 1.21),
    ("Cola", "Bebida", 1.54),
    ("Vino 1", "Bebida", 1.08),
    ("Vino 2", "Bebida", 1.10),
    ("Cerveza 1", "Bebida", 2.00),
    ("Cerveza 2", "Bebida", 1.58),
    ("Helado", "Postre", 1.54),
    ("Fruta", "Postre", 1.68),
    ("Brownies", "Postre", 1.32),
    ("Flan", "Postre", 1.97),
    ("Mousse", "Postre", 2.55),
    ("Pastel 1", "Postre", 2.14),
    ("Pastel 2", "Postre", 1.94),
    ("Pastel 3", "Postre", 1.74),
]


def dinero(valor):
    """Convierte un importe numerico a una cadena con dos decimales."""
    return f"{SIMBOLO_MONEDA} {valor:,.2f}"


# ---------------------------------------------------------------------
# BASE DE DATOS SQLITE
# ---------------------------------------------------------------------

class BaseDatos:
    """Administra la conexion y las operaciones de la base de datos."""

    def __init__(self, ruta):
        self.ruta = ruta
        self.crear_tablas()
        self.cargar_productos_iniciales()

    def conectar(self):
        """Abre una conexion nueva con SQLite."""
        conexion = sqlite3.connect(self.ruta)
        conexion.row_factory = sqlite3.Row
        return conexion

    def crear_tablas(self):
        """Crea las tablas necesarias si todavia no existen."""
        with self.conectar() as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL UNIQUE,
                    categoria TEXT NOT NULL,
                    precio REAL NOT NULL CHECK(precio >= 0),
                    activo INTEGER NOT NULL DEFAULT 1
                )
            """)
            con.execute("""
                CREATE TABLE IF NOT EXISTS ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fecha TEXT NOT NULL,
                    subtotal REAL NOT NULL,
                    impuesto REAL NOT NULL,
                    total REAL NOT NULL
                )
            """)
            con.execute("""
                CREATE TABLE IF NOT EXISTS detalle_ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    venta_id INTEGER NOT NULL,
                    producto_id INTEGER,
                    producto_nombre TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    cantidad INTEGER NOT NULL,
                    precio_unitario REAL NOT NULL,
                    importe REAL NOT NULL,
                    FOREIGN KEY (venta_id) REFERENCES ventas(id)
                )
            """)
            con.execute("CREATE INDEX IF NOT EXISTS idx_ventas_fecha ON ventas(fecha)")
            con.execute("CREATE INDEX IF NOT EXISTS idx_detalle_venta ON detalle_ventas(venta_id)")

    def cargar_productos_iniciales(self):
        """Registra el catalogo original solo cuando la tabla esta vacia."""
        with self.conectar() as con:
            cantidad = con.execute("SELECT COUNT(*) FROM productos").fetchone()[0]
            if cantidad == 0:
                con.executemany(
                    "INSERT INTO productos(nombre, categoria, precio) VALUES (?, ?, ?)",
                    PRODUCTOS_INICIALES
                )

    def obtener_productos(self, incluir_inactivos=False):
        """Devuelve los productos ordenados por categoria y nombre."""
        with self.conectar() as con:
            if incluir_inactivos:
                return con.execute(
                    "SELECT * FROM productos ORDER BY categoria, nombre"
                ).fetchall()
            return con.execute(
                "SELECT * FROM productos WHERE activo=1 ORDER BY categoria, nombre"
            ).fetchall()

    def guardar_producto(self, producto_id, nombre, categoria, precio):
        """Inserta un producto nuevo o actualiza uno existente."""
        with self.conectar() as con:
            if producto_id:
                con.execute("""
                    UPDATE productos
                    SET nombre=?, categoria=?, precio=?
                    WHERE id=?
                """, (nombre, categoria, precio, producto_id))
            else:
                con.execute("""
                    INSERT INTO productos(nombre, categoria, precio)
                    VALUES (?, ?, ?)
                """, (nombre, categoria, precio))

    def desactivar_producto(self, producto_id):
        """Oculta un producto del catalogo sin borrar ventas anteriores."""
        with self.conectar() as con:
            con.execute("UPDATE productos SET activo=0 WHERE id=?", (producto_id,))

    def registrar_venta(self, carrito):
        """Guarda la venta y sus productos en una sola transaccion."""
        subtotal = sum(item["cantidad"] * item["precio"] for item in carrito.values())
        impuesto = round(subtotal * IMPUESTO, 2)
        total = round(subtotal + impuesto, 2)
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with self.conectar() as con:
            cursor = con.execute("""
                INSERT INTO ventas(fecha, subtotal, impuesto, total)
                VALUES (?, ?, ?, ?)
            """, (fecha, subtotal, impuesto, total))
            venta_id = cursor.lastrowid

            for producto_id, item in carrito.items():
                importe = item["cantidad"] * item["precio"]
                con.execute("""
                    INSERT INTO detalle_ventas(
                        venta_id, producto_id, producto_nombre, categoria,
                        cantidad, precio_unitario, importe
                    ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    venta_id, producto_id, item["nombre"], item["categoria"],
                    item["cantidad"], item["precio"], importe
                ))

        return venta_id, fecha, subtotal, impuesto, total

    def obtener_ventas(self, limite=500):
        """Consulta las ventas mas recientes."""
        with self.conectar() as con:
            return con.execute("""
                SELECT id, fecha, subtotal, impuesto, total
                FROM ventas
                ORDER BY id DESC
                LIMIT ?
            """, (limite,)).fetchall()

    def obtener_detalle_venta(self, venta_id):
        """Consulta los productos que pertenecen a una venta."""
        with self.conectar() as con:
            return con.execute("""
                SELECT producto_nombre, categoria, cantidad,
                       precio_unitario, importe
                FROM detalle_ventas
                WHERE venta_id=?
                ORDER BY id
            """, (venta_id,)).fetchall()

    def ingresos_totales(self):
        """Suma los importes de todas las ventas registradas."""
        with self.conectar() as con:
            return con.execute(
                "SELECT COALESCE(SUM(total), 0) FROM ventas"
            ).fetchone()[0]

    def datos_ventas_por_dia(self):
        with self.conectar() as con:
            return con.execute("""
                SELECT date(fecha) AS periodo, SUM(total) AS importe
                FROM ventas
                GROUP BY date(fecha)
                ORDER BY periodo
            """).fetchall()

    def datos_ventas_por_mes(self):
        with self.conectar() as con:
            return con.execute("""
                SELECT strftime('%Y-%m', fecha) AS periodo, SUM(total) AS importe
                FROM ventas
                GROUP BY strftime('%Y-%m', fecha)
                ORDER BY periodo
            """).fetchall()

    def datos_productos_mas_vendidos(self):
        with self.conectar() as con:
            return con.execute("""
                SELECT producto_nombre AS nombre, SUM(cantidad) AS cantidad
                FROM detalle_ventas
                GROUP BY producto_nombre
                ORDER BY cantidad DESC
                LIMIT 10
            """).fetchall()

    def datos_ingresos_categoria(self):
        with self.conectar() as con:
            return con.execute("""
                SELECT categoria, SUM(importe) AS importe
                FROM detalle_ventas
                GROUP BY categoria
                ORDER BY importe DESC
            """).fetchall()


# ---------------------------------------------------------------------
# APLICACION E INTERFAZ GRAFICA
# ---------------------------------------------------------------------

class RestauranteApp:
    """Ventana principal y funciones de la aplicacion."""

    def __init__(self, ventana):
        self.ventana = ventana
        self.db = BaseDatos(RUTA_BASE_DATOS)
        self.carrito = {}
        self.venta_actual_id = None
        self.producto_seleccionado_id = None

        self.configurar_ventana()
        self.crear_estilos()
        self.crear_interfaz()
        self.actualizar_productos()
        self.actualizar_historial()
        self.actualizar_reportes()

    def configurar_ventana(self):
        self.ventana.title(f"{NOMBRE_RESTAURANTE} - Sistema de gestion")
        self.ventana.geometry("1280x780")
        self.ventana.minsize(1050, 680)
        self.ventana.configure(bg="#DCE6F1")

    def crear_estilos(self):
        estilo = ttk.Style()
        try:
            estilo.theme_use("clam")
        except tk.TclError:
            pass
        estilo.configure("TNotebook", background="#DCE6F1", borderwidth=0)
        estilo.configure("TNotebook.Tab", padding=(16, 9), font=("Arial", 10, "bold"))
        estilo.configure("Treeview", rowheight=27, font=("Arial", 10))
        estilo.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        estilo.configure("TButton", padding=7, font=("Arial", 10, "bold"))
        estilo.configure("Titulo.TLabel", font=("Arial", 22, "bold"),
                         foreground="#40545A", background="#DCE6F1")
        estilo.configure("Subtitulo.TLabel", font=("Arial", 12, "bold"),
                         foreground="#40545A", background="#DCE6F1")

    def crear_interfaz(self):
        encabezado = tk.Frame(self.ventana, bg="#DCE6F1")
        encabezado.pack(fill="x", padx=18, pady=(12, 5))

        tk.Label(
            encabezado, text=NOMBRE_RESTAURANTE,
            font=("Arial", 21, "bold"), fg="#40545A", bg="#DCE6F1", wraplength=760, justify="left"
        ).pack(side="left")

        tk.Label(
            encabezado, text="Sistema de ventas y administracion",
            font=("Arial", 10), fg="#5D5144", bg="#DCE6F1"
        ).pack(side="right", pady=12)

        self.pestanas = ttk.Notebook(self.ventana)
        self.pestanas.pack(fill="both", expand=True, padx=15, pady=10)

        self.tab_venta = tk.Frame(self.pestanas, bg="#F2F6FC")
        self.tab_productos = tk.Frame(self.pestanas, bg="#F2F6FC")
        self.tab_historial = tk.Frame(self.pestanas, bg="#F2F6FC")
        self.tab_reportes = tk.Frame(self.pestanas, bg="#F2F6FC")

        self.pestanas.add(self.tab_venta, text="  Ventas  ")
        self.pestanas.add(self.tab_productos, text="  Productos  ")
        self.pestanas.add(self.tab_historial, text="  Historial  ")
        self.pestanas.add(self.tab_reportes, text="  Reportes graficos  ")

        self.crear_pestana_ventas()
        self.crear_pestana_productos()
        self.crear_pestana_historial()
        self.crear_pestana_reportes()

    # ---------------------------- VENTAS ----------------------------

    def crear_pestana_ventas(self):
        marco = self.tab_venta
        tk.Label(marco, text="Registro de venta", font=("Arial", 17, "bold"),
                 bg="#F2F6FC", fg="#40545A").pack(anchor="w", padx=15, pady=12)

        controles = tk.Frame(marco, bg="#F2F6FC")
        controles.pack(fill="x", padx=15)

        tk.Label(controles, text="Producto:", bg="#F2F6FC").grid(row=0, column=0, padx=5)
        self.combo_producto = ttk.Combobox(controles, state="readonly", width=38)
        self.combo_producto.grid(row=0, column=1, padx=5, pady=8)

        tk.Label(controles, text="Cantidad:", bg="#F2F6FC").grid(row=0, column=2, padx=5)
        self.spin_cantidad = tk.Spinbox(controles, from_=1, to=999, width=7)
        self.spin_cantidad.grid(row=0, column=3, padx=5)

        ttk.Button(controles, text="Agregar al pedido",
                   command=self.agregar_al_carrito).grid(row=0, column=4, padx=10)

        zona = tk.Frame(marco, bg="#F2F6FC")
        zona.pack(fill="both", expand=True, padx=15, pady=8)

        marco_tabla = tk.LabelFrame(zona, text="Productos de la cuenta",
                                    bg="#F2F6FC", padx=8, pady=8)
        marco_tabla.pack(side="left", fill="both", expand=True, padx=(0, 8))

        columnas = ("producto", "categoria", "cantidad", "precio", "importe")
        self.tabla_carrito = ttk.Treeview(
            marco_tabla, columns=columnas, show="headings", height=14
        )
        encabezados = {
            "producto": "Producto", "categoria": "Categoria",
            "cantidad": "Cantidad", "precio": "Precio unitario", "importe": "Importe"
        }
        anchos = {"producto": 190, "categoria": 100, "cantidad": 75,
                  "precio": 110, "importe": 110}
        for col in columnas:
            self.tabla_carrito.heading(col, text=encabezados[col])
            self.tabla_carrito.column(col, width=anchos[col], anchor="center")
        self.tabla_carrito.pack(fill="both", expand=True)

        panel_derecho = tk.Frame(zona, bg="#D2DEEC", padx=15, pady=12)
        panel_derecho.pack(side="right", fill="y")

        tk.Label(panel_derecho, text="Resumen de cuenta",
                 font=("Arial", 14, "bold"), bg="#D2DEEC",
                 fg="#40545A").pack(pady=(4, 18))

        self.lbl_subtotal = tk.Label(panel_derecho, text="Subtotal: $ 0.00",
                                     font=("Arial", 11), bg="#D2DEEC")
        self.lbl_subtotal.pack(anchor="w", pady=6)
        self.lbl_impuesto = tk.Label(panel_derecho, text="Impuesto (7 %): $ 0.00",
                                     font=("Arial", 11), bg="#D2DEEC")
        self.lbl_impuesto.pack(anchor="w", pady=6)
        self.lbl_total = tk.Label(panel_derecho, text="TOTAL: $ 0.00",
                                  font=("Arial", 15, "bold"), bg="#D2DEEC",
                                  fg="#8A4B25")
        self.lbl_total.pack(anchor="w", pady=12)

        ttk.Button(panel_derecho, text="Quitar producto",
                   command=self.quitar_del_carrito).pack(fill="x", pady=5)
        ttk.Button(panel_derecho, text="Vaciar cuenta",
                   command=self.vaciar_carrito).pack(fill="x", pady=5)
        ttk.Button(panel_derecho, text="FINALIZAR Y GUARDAR VENTA",
                   command=self.finalizar_venta).pack(fill="x", pady=(18, 5))

        self.texto_recibo = tk.Text(marco, height=8, font=("Courier New", 9),
                                    wrap="none", bg="white")
        self.texto_recibo.pack(fill="x", padx=15, pady=(3, 12))
        self.texto_recibo.insert("1.0", "El recibo de la venta aparecera aqui.")

    def actualizar_productos_combo(self):
        self.productos_combo = self.db.obtener_productos()
        self.mapa_combo = {}
        opciones = []
        for p in self.productos_combo:
            etiqueta = f'{p["nombre"]} | {p["categoria"]} | {dinero(p["precio"])}'
            opciones.append(etiqueta)
            self.mapa_combo[etiqueta] = p
        self.combo_producto["values"] = opciones
        if opciones:
            self.combo_producto.current(0)
        else:
            self.combo_producto.set("")

    def agregar_al_carrito(self):
        seleccion = self.combo_producto.get()
        if not seleccion or seleccion not in self.mapa_combo:
            messagebox.showwarning("Producto", "Selecciona un producto.")
            return
        try:
            cantidad = int(self.spin_cantidad.get())
            if cantidad <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Cantidad", "Escribe una cantidad entera mayor que cero.")
            return

        producto = self.mapa_combo[seleccion]
        pid = producto["id"]
        if pid not in self.carrito:
            self.carrito[pid] = {
                "nombre": producto["nombre"],
                "categoria": producto["categoria"],
                "precio": float(producto["precio"]),
                "cantidad": 0
            }
        self.carrito[pid]["cantidad"] += cantidad
        self.refrescar_carrito()

    def refrescar_carrito(self):
        for fila in self.tabla_carrito.get_children():
            self.tabla_carrito.delete(fila)

        subtotal = 0
        for pid, item in self.carrito.items():
            importe = item["cantidad"] * item["precio"]
            subtotal += importe
            self.tabla_carrito.insert("", "end", iid=str(pid), values=(
                item["nombre"], item["categoria"], item["cantidad"],
                dinero(item["precio"]), dinero(importe)
            ))

        impuesto = round(subtotal * IMPUESTO, 2)
        total = round(subtotal + impuesto, 2)
        self.lbl_subtotal.config(text=f"Subtotal: {dinero(subtotal)}")
        self.lbl_impuesto.config(text=f"Impuesto ({IMPUESTO:.0%}): {dinero(impuesto)}")
        self.lbl_total.config(text=f"TOTAL: {dinero(total)}")

    def quitar_del_carrito(self):
        seleccion = self.tabla_carrito.selection()
        if not seleccion:
            messagebox.showinfo("Pedido", "Selecciona un producto de la cuenta.")
            return
        pid = int(seleccion[0])
        self.carrito.pop(pid, None)
        self.refrescar_carrito()

    def vaciar_carrito(self):
        if self.carrito and not messagebox.askyesno(
            "Confirmar", "¿Deseas vaciar todos los productos de la cuenta?"
        ):
            return
        self.carrito.clear()
        self.refrescar_carrito()

    def finalizar_venta(self):
        if not self.carrito:
            messagebox.showwarning("Venta", "Agrega al menos un producto.")
            return
        if not messagebox.askyesno("Confirmar venta", "¿Deseas guardar esta venta?"):
            return

        try:
            venta_id, fecha, subtotal, impuesto, total = self.db.registrar_venta(self.carrito)
        except sqlite3.Error as error:
            messagebox.showerror("Base de datos", f"No se pudo guardar la venta:\n{error}")
            return

        lineas = [
            f"{NOMBRE_RESTAURANTE}",
            f"Recibo de venta No. {venta_id}",
            f"Fecha: {fecha}",
            "-" * 48,
            f"{'Producto':20} {'Cant.':>5} {'Importe':>12}",
            "-" * 48
        ]
        for item in self.carrito.values():
            importe = item["cantidad"] * item["precio"]
            lineas.append(
                f"{item['nombre'][:20]:20} {item['cantidad']:>5} {dinero(importe):>12}"
            )
        lineas.extend([
            "-" * 48,
            f"Subtotal: {dinero(subtotal)}",
            f"Impuesto ({IMPUESTO:.0%}): {dinero(impuesto)}",
            f"TOTAL: {dinero(total)}",
            "",
            "Gracias por su visita."
        ])
        recibo = "\n".join(lineas)
        self.texto_recibo.delete("1.0", "end")
        self.texto_recibo.insert("1.0", recibo)

        self.venta_actual_id = venta_id
        self.carrito.clear()
        self.refrescar_carrito()
        self.actualizar_historial()
        self.actualizar_reportes()
        messagebox.showinfo(
            "Venta guardada",
            f"La venta #{venta_id} se guardo correctamente.\nTotal: {dinero(total)}"
        )

    # -------------------------- PRODUCTOS ---------------------------

    def crear_pestana_productos(self):
        marco = self.tab_productos
        tk.Label(marco, text="Administracion de productos",
                 font=("Arial", 17, "bold"), bg="#F2F6FC",
                 fg="#40545A").pack(anchor="w", padx=15, pady=12)

        formulario = tk.LabelFrame(marco, text="Datos del producto",
                                   bg="#F2F6FC", padx=12, pady=12)
        formulario.pack(fill="x", padx=15, pady=5)

        tk.Label(formulario, text="Nombre:", bg="#F2F6FC").grid(row=0, column=0, padx=5)
        self.entry_nombre = ttk.Entry(formulario, width=25)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(formulario, text="Categoria:", bg="#F2F6FC").grid(row=0, column=2, padx=5)
        self.combo_categoria = ttk.Combobox(
            formulario, values=["Comida", "Bebida", "Postre"], state="readonly", width=17
        )
        self.combo_categoria.grid(row=0, column=3, padx=5)
        self.combo_categoria.current(0)

        tk.Label(formulario, text="Precio:", bg="#F2F6FC").grid(row=0, column=4, padx=5)
        self.entry_precio = ttk.Entry(formulario, width=12)
        self.entry_precio.grid(row=0, column=5, padx=5)

        ttk.Button(formulario, text="Guardar producto",
                   command=self.guardar_producto).grid(row=0, column=6, padx=8)
        ttk.Button(formulario, text="Limpiar",
                   command=self.limpiar_formulario_producto).grid(row=0, column=7, padx=4)

        columnas = ("id", "nombre", "categoria", "precio", "estado")
        self.tabla_productos = ttk.Treeview(
            marco, columns=columnas, show="headings", height=17
        )
        for col, titulo, ancho in [
            ("id", "ID", 60), ("nombre", "Nombre", 260),
            ("categoria", "Categoria", 160), ("precio", "Precio", 130),
            ("estado", "Estado", 100)
        ]:
            self.tabla_productos.heading(col, text=titulo)
            self.tabla_productos.column(col, width=ancho, anchor="center")
        self.tabla_productos.pack(fill="both", expand=True, padx=15, pady=10)
        self.tabla_productos.bind("<<TreeviewSelect>>", self.seleccionar_producto)

        acciones = tk.Frame(marco, bg="#F2F6FC")
        acciones.pack(fill="x", padx=15, pady=(0, 12))
        ttk.Button(acciones, text="Actualizar lista",
                   command=self.actualizar_productos).pack(side="left", padx=4)
        ttk.Button(acciones, text="Desactivar producto seleccionado",
                   command=self.eliminar_producto).pack(side="left", padx=4)

    def actualizar_productos(self):
        if not hasattr(self, "tabla_productos"):
            return
        for fila in self.tabla_productos.get_children():
            self.tabla_productos.delete(fila)
        for p in self.db.obtener_productos(incluir_inactivos=True):
            estado = "Activo" if p["activo"] else "Inactivo"
            self.tabla_productos.insert("", "end", iid=str(p["id"]), values=(
                p["id"], p["nombre"], p["categoria"], dinero(p["precio"]), estado
            ))
        if hasattr(self, "combo_producto"):
            self.actualizar_productos_combo()

    def seleccionar_producto(self, _evento=None):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            return
        pid = int(seleccion[0])
        producto = next(
            (p for p in self.db.obtener_productos(incluir_inactivos=True) if p["id"] == pid),
            None
        )
        if producto is None:
            return
        self.producto_seleccionado_id = pid
        self.entry_nombre.delete(0, "end")
        self.entry_nombre.insert(0, producto["nombre"])
        self.combo_categoria.set(producto["categoria"])
        self.entry_precio.delete(0, "end")
        self.entry_precio.insert(0, str(producto["precio"]))

    def limpiar_formulario_producto(self):
        self.producto_seleccionado_id = None
        self.entry_nombre.delete(0, "end")
        self.entry_precio.delete(0, "end")
        self.combo_categoria.current(0)
        self.tabla_productos.selection_remove(self.tabla_productos.selection())

    def guardar_producto(self):
        nombre = self.entry_nombre.get().strip()
        categoria = self.combo_categoria.get().strip()
        try:
            precio = float(self.entry_precio.get().replace(",", "."))
            if precio < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Precio", "Escribe un precio numerico igual o mayor que cero.")
            return
        if not nombre:
            messagebox.showwarning("Producto", "Escribe el nombre del producto.")
            return
        if categoria not in ("Comida", "Bebida", "Postre"):
            messagebox.showwarning("Categoria", "Selecciona una categoria valida.")
            return

        try:
            self.db.guardar_producto(self.producto_seleccionado_id, nombre, categoria, precio)
        except sqlite3.IntegrityError:
            messagebox.showerror("Producto", "Ya existe un producto con ese nombre.")
            return
        except sqlite3.Error as error:
            messagebox.showerror("Base de datos", str(error))
            return

        self.limpiar_formulario_producto()
        self.actualizar_productos()
        messagebox.showinfo("Productos", "El producto se guardo correctamente.")

    def eliminar_producto(self):
        seleccion = self.tabla_productos.selection()
        if not seleccion:
            messagebox.showwarning("Productos", "Selecciona un producto.")
            return
        pid = int(seleccion[0])
        if not messagebox.askyesno(
            "Confirmar", "El producto se desactivara y ya no aparecera en nuevas ventas."
        ):
            return
        self.db.desactivar_producto(pid)
        self.limpiar_formulario_producto()
        self.actualizar_productos()
        messagebox.showinfo("Productos", "Producto desactivado.")

    # --------------------------- HISTORIAL --------------------------

    def crear_pestana_historial(self):
        marco = self.tab_historial
        tk.Label(marco, text="Historial de ventas",
                 font=("Arial", 17, "bold"), bg="#F2F6FC",
                 fg="#40545A").pack(anchor="w", padx=15, pady=12)

        columnas = ("id", "fecha", "subtotal", "impuesto", "total")
        self.tabla_historial = ttk.Treeview(
            marco, columns=columnas, show="headings", height=15
        )
        for col, titulo, ancho in [
            ("id", "Folio", 80), ("fecha", "Fecha y hora", 220),
            ("subtotal", "Subtotal", 150), ("impuesto", "Impuesto", 150),
            ("total", "Total", 150)
        ]:
            self.tabla_historial.heading(col, text=titulo)
            self.tabla_historial.column(col, width=ancho, anchor="center")
        self.tabla_historial.pack(fill="both", expand=True, padx=15, pady=8)
        self.tabla_historial.bind("<<TreeviewSelect>>", self.mostrar_detalle_historial)

        ttk.Button(marco, text="Actualizar historial",
                   command=self.actualizar_historial).pack(anchor="w", padx=15, pady=5)

        self.detalle_historial = tk.Text(marco, height=9, font=("Courier New", 9))
        self.detalle_historial.pack(fill="x", padx=15, pady=8)

    def actualizar_historial(self):
        if not hasattr(self, "tabla_historial"):
            return
        for fila in self.tabla_historial.get_children():
            self.tabla_historial.delete(fila)
        for venta in self.db.obtener_ventas():
            self.tabla_historial.insert("", "end", iid=str(venta["id"]), values=(
                venta["id"], venta["fecha"], dinero(venta["subtotal"]),
                dinero(venta["impuesto"]), dinero(venta["total"])
            ))

    def mostrar_detalle_historial(self, _evento=None):
        seleccion = self.tabla_historial.selection()
        if not seleccion:
            return
        venta_id = int(seleccion[0])
        detalles = self.db.obtener_detalle_venta(venta_id)
        self.detalle_historial.delete("1.0", "end")
        self.detalle_historial.insert("end", f"DETALLE DE LA VENTA #{venta_id}\n")
        self.detalle_historial.insert("end", "-" * 65 + "\n")
        for item in detalles:
            self.detalle_historial.insert(
                "end",
                f'{item["producto_nombre"]} | {item["categoria"]} | '
                f'{item["cantidad"]} x {dinero(item["precio_unitario"])} = '
                f'{dinero(item["importe"])}\n'
            )

    # ---------------------------- REPORTES --------------------------

    def crear_pestana_reportes(self):
        marco = self.tab_reportes
        tk.Label(marco, text="Reportes y estadisticas",
                 font=("Arial", 17, "bold"), bg="#F2F6FC",
                 fg="#40545A").pack(anchor="w", padx=15, pady=12)

        resumen = tk.Frame(marco, bg="#D2DEEC", padx=15, pady=12)
        resumen.pack(fill="x", padx=15, pady=5)

        self.lbl_ingresos_totales = tk.Label(
            resumen, text="Ingresos totales: $ 0.00",
            font=("Arial", 17, "bold"), fg="#40545A", bg="#D2DEEC"
        )
        self.lbl_ingresos_totales.pack(side="left", padx=10)

        self.lbl_num_ventas = tk.Label(
            resumen, text="Ventas registradas: 0",
            font=("Arial", 12, "bold"), bg="#D2DEEC"
        )
        self.lbl_num_ventas.pack(side="right", padx=10)

        barra = tk.Frame(marco, bg="#F2F6FC")
        barra.pack(fill="x", padx=15, pady=8)
        tk.Label(barra, text="Tipo de reporte:", bg="#F2F6FC").pack(side="left")
        self.combo_reporte = ttk.Combobox(
            barra, state="readonly", width=32,
            values=[
                "Ventas por dia",
                "Productos mas vendidos",
                "Ingresos por categoria",
                "Ventas por mes"
            ]
        )
        self.combo_reporte.pack(side="left", padx=8)
        self.combo_reporte.current(0)
        ttk.Button(barra, text="Mostrar grafica",
                   command=self.dibujar_grafica).pack(side="left", padx=5)
        ttk.Button(barra, text="Actualizar reportes",
                   command=self.actualizar_reportes).pack(side="left", padx=5)

        self.marco_grafica = tk.Frame(marco, bg="white")
        self.marco_grafica.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        if not MATPLOTLIB_DISPONIBLE:
            tk.Label(
                self.marco_grafica,
                text="Para mostrar las graficas instala Matplotlib:\n"
                     "python -m pip install matplotlib",
                font=("Arial", 13), bg="white", fg="#8A4B25"
            ).pack(expand=True)
        else:
            self.figura = Figure(figsize=(9, 4.5), dpi=100)
            self.ejes = self.figura.add_subplot(111)
            self.canvas = FigureCanvasTkAgg(self.figura, master=self.marco_grafica)
            self.canvas.get_tk_widget().pack(fill="both", expand=True)
            self.dibujar_grafica()

    def actualizar_reportes(self):
        total = self.db.ingresos_totales()
        ventas = self.db.obtener_ventas(limite=100000)
        if hasattr(self, "lbl_ingresos_totales"):
            self.lbl_ingresos_totales.config(
                text=f"Ingresos totales: {dinero(total)}"
            )
            self.lbl_num_ventas.config(text=f"Ventas registradas: {len(ventas)}")
        if MATPLOTLIB_DISPONIBLE and hasattr(self, "canvas"):
            self.dibujar_grafica()

    def dibujar_grafica(self):
        if not MATPLOTLIB_DISPONIBLE or not hasattr(self, "ejes"):
            return

        tipo = self.combo_reporte.get()
        self.ejes.clear()
        self.figura.patch.set_facecolor("white")
        self.ejes.set_facecolor("#FAFAFA")

        if tipo == "Ventas por dia":
            datos = self.db.datos_ventas_por_dia()
            etiquetas = [fila["periodo"] for fila in datos]
            valores = [fila["importe"] for fila in datos]
            self.ejes.bar(etiquetas, valores)
            self.ejes.set_title("Ingresos por dia")
            self.ejes.set_ylabel("Importe")
            self.ejes.set_xlabel("Fecha")
            self.ejes.tick_params(axis="x", rotation=40)

        elif tipo == "Productos mas vendidos":
            datos = self.db.datos_productos_mas_vendidos()
            etiquetas = [fila["nombre"] for fila in datos]
            valores = [fila["cantidad"] for fila in datos]
            self.ejes.barh(etiquetas[::-1], valores[::-1])
            self.ejes.set_title("Los 10 productos mas vendidos")
            self.ejes.set_xlabel("Unidades vendidas")

        elif tipo == "Ingresos por categoria":
            datos = self.db.datos_ingresos_categoria()
            etiquetas = [fila["categoria"] for fila in datos]
            valores = [fila["importe"] for fila in datos]
            if valores:
                self.ejes.pie(
                    valores, labels=etiquetas, autopct="%1.1f%%",
                    startangle=90
                )
                self.ejes.set_title("Distribucion de ingresos por categoria")
                self.ejes.axis("equal")
            else:
                self.ejes.text(0.5, 0.5, "Todavia no hay ventas registradas",
                               ha="center", va="center", transform=self.ejes.transAxes)

        elif tipo == "Ventas por mes":
            datos = self.db.datos_ventas_por_mes()
            etiquetas = [fila["periodo"] for fila in datos]
            valores = [fila["importe"] for fila in datos]
            self.ejes.bar(etiquetas, valores)
            self.ejes.set_title("Ingresos por mes")
            self.ejes.set_ylabel("Importe")
            self.ejes.set_xlabel("Mes")
            self.ejes.tick_params(axis="x", rotation=35)

        if tipo != "Ingresos por categoria" and not (
            self.db.datos_ventas_por_dia() if tipo == "Ventas por dia"
            else self.db.datos_productos_mas_vendidos() if tipo == "Productos mas vendidos"
            else self.db.datos_ventas_por_mes()
        ):
            self.ejes.text(0.5, 0.5, "Todavia no hay ventas registradas",
                           ha="center", va="center", transform=self.ejes.transAxes)

        self.figura.tight_layout()
        self.canvas.draw()


# ---------------------------------------------------------------------
# INICIO DEL PROGRAMA
# ---------------------------------------------------------------------

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    aplicacion = RestauranteApp(ventana_principal)
    ventana_principal.mainloop()




