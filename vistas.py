import sys
import tkinter as tk
import os.path
from tkinter import *
from tkinter import ttk
from tkinter.constants import *
import funciones
from datetime import date

_script = sys.argv[0]
_location = os.path.dirname(_script)

# Clases de las vistas con todos los elementos gráficos
class Altas:
    def __init__(self, top=None):
        #altas = Tk()
        top.geometry("800x500")
        top.title("ALTAS")
        top.config(bd=20,width=400)
        self.top = top
        Label(top,text ="CODIGO").place(x = 20, y = 5)
        Label(top,text ="APELLIDOS Y NOMBRE").place(x = 400, y = 5)
        Label(top,text ="FECHA INICIO").place(x = 20, y = 80)
        Label(top,text ="FECHA DE NACIMIENTO").place(x = 250, y = 80)
        Label(top,text ="DIRECCION").place(x = 500, y = 80)
        Label(top,text ="NIF").place(x = 20, y = 150)
        Label(top,text ="DATOS BANCARIOS").place(x = 250, y = 150)
        Label(top,text ="NUMERO DE AFILIACION SS").place(x = 500, y = 150)
        Label(top,text ="GENERO").place(x = 20, y = 220)
        Label(top,text ="DEPARTAMENTO").place(x = 250, y = 220)
        Label(top,text ="PUESTO").place(x = 550, y = 220)
        Label(top,text ="TELEFONO").place(x = 1, y = 320)
        Label(top,text ="EMAIL").place(x = 1, y = 350)
        Label(top,text ="SALARIO MENSUAL").place(x = 250, y = 320)
        Label(top,text ="PAGAS EXTRA").place(x = 250, y = 350)
        Label(top,text ="IRPF").place(x = 530, y = 320)
        Label(top,text ="SEG. SOCIAL").place(x = 530, y = 350)
        #mensaje1 = Label(top,text ="MENSAJE VALIDACION",foreground="red",font=20).place(x = 200, y = 420)
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%Y-%m-%d")
        print("d1 =", d1)

        self.msj = Label(top)
        self.msj.config(text="Introduzca los datos de usuarios",font=("Times14",20))
        self.msj.place(x=150, y=420)

        self.cod = Entry(top)
        self.cod.place(x = 5, y = 30)
        self.cod.config(state="disabled")

        self.apelNom = Entry(top)
        self.apelNom.place(x = 300, y = 30)
        self.apelNom.configure(width=70)

        self.fechaini = Entry(top)
        self.fechaini.place(x = 1, y = 100)
        self.fechaini.insert(0,str(d1))
        self.fechaini.config(state="disabled")

        self.fechafin = Entry(top)
        self.fechafin.place(x = 230, y = 100)
        self.fechafin.configure(width=30)
        

        self.direccion = Entry(top)
        self.direccion.place(x = 500, y = 100)
        self.direccion.configure(width=30)

        self.nif = Entry(top)
        self.nif.place(x = 1, y = 170)

        self.datosbanc = Entry(top)
        self.datosbanc.place(x = 230, y = 170)
        self.datosbanc.configure(width=30)

        self.numafss = Entry(top)
        self.numafss.place(x = 500, y = 170)
        self.numafss.configure(width=30)

        self.genero = ttk.Combobox(top,width=17)
        self.genero.place(x=1, y=240)
        opciones =["Masculino","Femenino"]
        self.genero['values']=opciones

        #self.genero = Entry(top)
        #self.genero.place(x = 1, y = 240)
        self.departamento = ttk.Combobox(top)
        self.departamento.place(x=230, y=240)
        self.departamento.configure(width=28)
        opciones1 = ["Marketing","Finanzas","Logistica"]
        self.departamento['values'] = opciones1

        self.puesto = Entry(top)
        self.puesto.place(x = 500, y = 240)
        self.puesto.configure(width=30)

        self.tlf = Entry(top)
        self.tlf.place(x = 70, y = 320)

        self.email = Entry(top)
        self.email.place(x = 70, y = 350)

        self.salariomens = Entry(top)
        self.salariomens.place(x = 370, y = 320)

        self.pagasextra = Entry(top)
        self.pagasextra.place(x = 370, y = 350)

        self.irpf = Entry(top)
        self.irpf.place(x = 620, y = 320)

        self.segsocial = Entry(top)
        self.segsocial.insert(0, 4.70)
        self.segsocial.place(x = 620, y = 350)


        Button(top,text ="INSERTAR",width=15, height=2,background="#ffe599", command=funciones.imprimir).place(x =630 , y =400)

class Nominas:    
    def __init__(self, top=None):
        top.geometry("1000x500")
        top.title("NOMINAS")
        top.config(bd=20,width=400)
        self.top = top
        Label(top, text="CODIGO").place(x=50, y=10)
        Label(top, text="NOMBRE Y APELLIDOS").place(x=500, y=10)
        Label(top, text="FECHA INICIO").place(x=40, y=65)
        Label(top, text="FECHA NACIMIENTO").place(x=250, y=65)
        Label(top, text="DIRECCION").place(x=600, y=65)
        Label(top, text="NIF").place(x=70, y=115)
        Label(top, text="DATOS BANCARIOS").place(x=360, y=115)
        Label(top, text="NUMERO DE ALICIACION A LA SS").place(x=670, y=115)
        Label(top, text="SALARIO BRUTO", width=20).place(x=16, y=175)
        Label(top, text="NUMERO DE PAGAS").place(x=350, y=175)
        Label(top, text="_____________________________________________________________________________________________________________________________________________________________________________________").place(x=20, y=190)
        Label(top, text="SALARIO MES", width=19).place(x=16, y=220)
        Label(top, text="%IRPF", width=19).place(x=350, y=220)
        Label(top, text="Retencion IRPF").place(x=650, y=220)
        Label(top, text="PRORRATA PAGAS", width=19).place(x=16, y=255)
        Label(top, text="SEG.SOCIAL", width=19).place(x=350, y=255)
        Label(top, text="DEDUCCION SS").place(x=650, y=255)
        Label(top, text="A PERCIBIR").place(x=650, y=350)
        Label(top, text="MENSAJE VALIDACION",font=('Times 14', 20),foreground='red').place(x=40, y=350)

        self.cod = Entry(top)
        self.cod.place(x=20,y=40)

        self.apell = Entry(top)
        self.apell.place(x=200,y=40)
        self.apell.config(width=120)
        self.apell.config(state="disabled")

        self.fini = Entry(top)
        self.fini.place(x=20,y=90)
        self.fini.insert(0, str())
        self.fini.config(state="disabled")


        self.fnaci = Entry(top)
        self.fnaci.place(x=200,y=90)
        self.fnaci.configure(width=40)
        self.fnaci.config(state="disabled")

        self.dir = Entry(top)
        self.dir.place(x=500,y=90)
        self.dir.configure(width=70)
        self.dir.config(state="disabled")

        self.nif = Entry(top)
        self.nif.place(x=20,y=140)
        self.nif.configure(width=20)
        self.nif.config(state="disabled")

        self.dban = Entry(top)
        self.dban.place(x=200,y=140)
        self.dban.configure(width=65)
        self.dban.config(state="disabled")

        self.nss = Entry(top)
        self.nss.place(x=600,y=140)
        self.nss.configure(width=53)
        self.nss.config(state="disabled")

        self.sb = Entry(top)
        self.sb.place(x=200,y=175)
        self.sb.config(state="disabled")

        self.numpagas = Entry(top)
        self.numpagas.place(x=500,y=175)
        self.numpagas.config(state="disabled")

        self.smes = Entry(top)
        self.smes.place(x=200,y=220)

        self.irpf = Entry(top)
        self.irpf.place(x=450,y=220)
        self.irpf.config(state="disabled")
       
        self.rirpf = Entry(top)
        self.rirpf.place(x=750,y=220)

        self.prpagas = Entry(top)
        self.prpagas.place(x=200,y=255)

        self.ssocial = Entry(top)
        self.ssocial.place(x=450,y=255)
        self.ssocial.config(state="disabled")

        self.deducss = Entry(top)
        self.deducss.place(x=750,y=255)

        self.percibir = Entry(top)
        self.percibir.place(x=750,y=350)
        
        Button(top, text="CARGAR EMPLEADO", width=35, height=3,
                    background='#ffe599', font=('Times 14'),command=funciones.crear_nominas).place(x=40, y=400)
        Button(top, text="CALCULAR", width=20, height=3,
                      background='#ffe599', font=('Times 14')).place(x=500, y=400)
        Button(top, text="IMPRIMIR", width=20, height=3,
                      background='#ffe599', font=('Times 14')).place(x=750, y=400)


class Bajas:
    def __init__(self, top=None):
    #altas = Tk()
        top.geometry("800x500")
        top.title("BAJAS")
        top.config(bd=20,width=400)
        self.top = top

        Label(top,text ="CODIGO EMPLEADO",font=20).place(x = 100, y = 100)
        Label(top,text ="FECHA DE BAJA",font= 20).place(x = 400, y = 100)

        self.msj = Label(top)
        self.msj.configure(text="Introduce codigo de cliente y fecha de baja",foreground='Black',font=20)
        self.msj.place(x=200,y=300)

        self.cod = Entry(top)
        self.cod.place(x = 100, y = 150)
        self.cod.configure(width=45)
          
        today = date.today()
        # dd/mm/YY
        d1 = today.strftime("%Y-%m-%d")
        print("d1 =", d1)

        self.fbaja = Entry(top)
        self.fbaja.place(x = 400, y = 150 )
        self.fbaja.insert(0, str(d1))
        self.fbaja.configure(width=45)
        Button(top,text ="Dar Baja",width=15, height=2,background="#ffe599",command=funciones.dar_baja).place(x =330 , y =200)         
class Informes:
    def __init__(self, top=None):
        top.geometry("800x500")
        top.title("INFORMES")
        top.config(bd=20,width=400)
        self.top = top
        Label(top,text ="EMPLEADOS ALTA").place(x = 25, y = 100)
        self.alta = Label(top)
        self.alta.configure(text="",borderwidth=1,relief="solid",width=15, height=3)
        self.alta.place(x = 25, y = 125)
        Label(top,text ="EMPLEADOS BAJA").place(x = 250, y = 100)
        self.baja = Label(top)
        self.baja.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.baja.place(x=250, y=125 )
        Label(top,text ="MEDIA EDADES").place(x = 450, y = 100)
        self.mediaEdades = Label(top)
        self.mediaEdades.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.mediaEdades.place(x=450, y=125 )
        Label(top,text ="RETRIBUCION MEDIA",foreground="blue").place(x = 650, y = 100)
        self.salariom = Label(top)
        self.salariom.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.salariom.place(x=650, y=125 )
        Label(top,text ="% MUJERES").place(x = 25, y = 200)
        self.mujer_alta = Label(top)
        self.mujer_alta.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.mujer_alta.place(x=25, y=225 )
        Label(top,text ="% MUJERES").place(x = 250, y = 200)
        self.mujer_baja = Label(top)
        self.mujer_baja.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.mujer_baja.place(x=250, y=225 )
        Label(top,text ="MUJERES").place(x = 450, y = 200)
        self.edad_media_muj = Label(top)
        self.edad_media_muj.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.edad_media_muj.place(x=450, y=225 )
        Label(top,text ="MUJERES",foreground="blue").place(x = 650, y = 200)
        self.salariomuj = Label(top)
        self.salariomuj.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.salariomuj.place(x=650, y=225 )

        Label(top,text ="% HOMBRES").place(x = 25, y = 300)
        self.hombre_alta = Label(top)
        self.hombre_alta.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.hombre_alta.place(x=25, y=325 )
        Label(top,text ="% HOMBRES").place(x = 250, y = 300)
        self.hombre_baja = Label(top)
        self.hombre_baja.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.hombre_baja.place(x=250, y=325 )
        Label(top,text ="HOMBRES").place(x = 450, y = 300)
        self.edadHombre = Label(top)
        self.edadHombre.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.edadHombre.place(x=450, y=325 )
        Label(top,text ="HOMBRES",foreground="blue").place(x = 650, y = 300)
        self.salarioh = Label(top)
        self.salarioh.configure(text="",borderwidth=1, relief="solid",width=15,height=3)
        self.salarioh.place(x=650, y=325 )  
        Button(top,text="Cargar Informes",background="#ffe599",command=funciones.informes_alta).place(x=350,y=400)
    
from time import time, localtime, strftime
class ToolTip(tk.Toplevel):
    """ Provides a ToolTip widget for Tkinter. """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')
    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)
    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()
    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)
    def hide(self, event=None):
        self.visible = 0
        self.withdraw()
    def update(self, msg):
        self.msgVar.set(msg)
#                   End of Class ToolTip
