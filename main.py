import tkinter as tk
import tkinter.font as tkFont
import funciones

# Main donde nos moveremos por las pantallas de la aplicacion

root = tk.Tk()
root.title("Mi primera aplicación gráfica")
root.geometry("800x500")

root.imagen1 = tk.PhotoImage()
root.imagen1.configure(file="presupuesto.png")
root.imagen1.subsample(1)
root.img = tk.Label()
root.img.configure(image = root.imagen1)
root.img.place(x=330,y=100)

root.etiqueta1 = tk.Label()
root.etiqueta1.configure(text="Nominator")
root.etiqueta1.grid(padx=(0, 0))
root.etiqueta1.config(font=('Helvetica bold', 30))
root.etiqueta1.place(x=300,y=30)

root.boton = tk.Button()
root.boton.configure(text="ALTAS")
root.boton.configure(width=40, height=5)
root.boton.place(x=100,y=250)
root.boton.configure(command=funciones.altas)

root.boton1 = tk.Button()
root.boton1.configure(text="BAJAS",width=40,height=5)
root.boton1.place(x=400,y=250)
root.boton1.configure(command=funciones.bajas)

root.boton2 = tk.Button()
root.boton2.configure(text="INFORMES",width=40,height=5)
root.boton2.place(x=100,y=350)
root.boton2.configure(command=funciones.informes)

root.boton3 = tk.Button()
root.boton3.configure(text="NOMINAS",width=40,height=5)
root.boton3.place(x=400,y=350)
root.boton3.configure(command= funciones.nominas)
"""
boton2 = Button(vp, text="BAJAS", width=40, height=5)
boton2.grid(column=1, row=4)

boton3 = Button(vp, text="INFORMES", width=40, height=5)
boton3.grid(column=2, row=3)

boton4 = Button(vp, text="NÓMINAS", width=40, height=5, command=nominas)
boton4.grid(column=2, row=4)

#entradatxt = Entry(vp,width=10)
# entradatxt.grid(column=2,row=3)

imagen = PhotoImage(file="contabilidad.png").subsample(4)
imagenMenu = Label(vp, image=imagen).grid(
column=1, row=2, padx=(250, 0), pady=(40, 40))
"""
root.mainloop()
