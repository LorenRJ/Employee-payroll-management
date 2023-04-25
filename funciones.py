#Clase de funciones
import vistas
import tkinter as tk
import sqlite3
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

#Metodos que inician altas nominas, bajas e informes dentro de la vista funciones
def altas():
    root = tk.Tk()
    root.protocol('VM_DELETE_WINDOW', root.destroy)
    global vAltas, top2
    top2 = root
    vAltas = vistas.Altas(top2)
    root.mainloop()

def nominas():
    root = tk.Tk()
    root.protocol('VM_DELETE_WINDOW', root.destroy)
    global n1, top2
    top2 = root
    n1 = vistas.Nominas(top2)
    root.mainloop()

def bajas():
    root = tk.Tk()
    root.protocol('VM_DELETE_WINDOW', root.destroy)
    global b1, top2
    top2 = root
    b1 = vistas.Bajas(top2)
    root.mainloop()

def informes():
    root = tk.Tk()
    root.protocol('VM_DELETE_WINDOW',root.destroy)
    global in1, top2
    top2 = root
    in1 = vistas.Informes(top2)
    root.mainloop()


#Método que crea la fecha a dia de hoy en formato Y-M-D
def fecha_baja():
    today = date.today()
    # dd/mm/YY
    d1 = today.strftime("%Y-%m-%d")
    print("d1 =", d1)
    return d1

#Método que valida el telefono
def tlf(numero):
    if(numero.isdigit() and len(numero) == 9):
        print("Numero de telefono completo")
        return True
    else:
        vAltas.msj.configure(text="Telefono introducido es incorrecto")
        vAltas.msj.configure(foreground='Red')
        print("Telefono incorrecto")
#Método que valida el nif
def nif(numero):
    letras = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",21:"K",22:"E"}
    if (len(numero) == 9) & (numero[:8].isdigit()):
            num1 = numero.upper()
            letra = num1[8]
            print("Letra posicion 9",letra)
            for i,c in letras.items():
                if letra == c:
                    print("Formato correcto")
                    nume = num1.rstrip(num1[-1])
                    por = int(nume)%23
                    print(por)
                    print(letra)
                    for h,j in letras.items():
                        if  (por== h) & (letra == j):
                            print("DNI CORRECTO")
                            return True
                else: 
                    print("Dni introducido es incorrecto")
                    vAltas.msj.configure(text="DNI INCORRECTO")
                    vAltas.msj.configure(foreground="Red")
    else: 
        print("Formato no valido")
        vAltas.msj.configure(text=" DNI INCORRECTO")
        vAltas.msj.configure(foreground="Red")
def porcentajes_alta():
    print("Porcentajes alta")
    conexion = sqlite3.connect('nominas1.db')
    cursor = conexion.cursor()
    #Porcentajes de hombres
    consulta =""" SELECT COUNT(*) FROM USUARIOS WHERE FBAJA IS NULL AND GENERO = "Masculino" """
    cursor.execute(consulta)
    conexion.commit()
    linea = cursor.fetchone()
    registro = str(linea)
    registro = int(registro[1:2])
    resultadoh = str(int((registro * 100)/contador1)),"%"
    print("Contador de hombres",registro,"Registro global de altas",contador1,"Resultado final",resultadoh)
    in1.hombre_alta.configure(text=resultadoh)
    #Porcentajes Mujeres
    consulta =""" SELECT COUNT(*) FROM USUARIOS WHERE FBAJA IS NULL AND GENERO = "Femenino" """
    cursor.execute(consulta)
    conexion.commit()
    linea = cursor.fetchone()
    registro = str(linea)
    registro = int(registro[1:2])
    resultadoh = str(int((registro * 100)/contador1)),"%"
    print("Contador de hombres",registro,"Registro global de altas",contador1,"Resultado final",resultadoh)
    in1.mujer_alta.configure(text=resultadoh)
    conexion.close()
def baja_mujeres():
    print("Este es el apartado de baja de mujeres")
    conexion = sqlite3.connect('nominas1.db')
    cursor = conexion.cursor()
    #Porcentaje de hombres
    consulta = """ SELECT COUNT(*) FROM USUARIOS WHERE FBAJA IS NOT NULL and genero = "Femenino" """
    cursor.execute(consulta)
    conexion.commit()
    linea = cursor.fetchall()
    registro = str(linea)
    registro = int(registro[2:3])
    resultadof = str(round((registro* 100)/contador2,2)),"%"
    print("Regfistros de las mujeres",resultadof)
    in1.mujer_baja.configure(text=resultadof)
    #Porcentaje de hombres
    consulta = """ SELECT COUNT(*) FROM USUARIOS WHERE FBAJA IS NOT NULL AND GENERO = "Masculino" """
    cursor.execute(consulta)
    conexion.commit()
    linea = cursor.fetchone()
    registro = str(linea)
    registro = int(registro[1:2])
    resultadoh = str(round((registro * 100)/contador2,2)),"%"
    print("Registro de hombres",resultadoh)
    in1.hombre_baja.configure(text=resultadof)
    conexion.close()
    
#Método que realiza el el relleno de informes
def informes_alta():
    conexion = sqlite3.connect('nominas1.db')
    cursor = conexion.cursor()
    consulta = """ SELECT COUNT(*) FROM USUARIOS where FBAJA is NULL """
    cursor.execute(consulta)
    conexion.commit()
    row = cursor.fetchone()
    result = str(row)
    result = result.replace("(","").replace(",","").replace(")","")
    global contador1 
    contador1 = int(result)
    in1.alta.configure(text=result)
    cursor1 = conexion.cursor()
    consulta = """SELECT COUNT(*) FROM USUARIOS where FBAJA is NOT NULL"""
    cursor1.execute(consulta)
    conexion.commit()
    row = cursor1.fetchone()
    result = str(row)
    result = result.replace("(","").replace(",","").replace(")","")
    global contador2
    contador2 = int(result)
    in1.baja.configure(text=result)
    conexion.close()
    porcentajes_alta()
    baja_mujeres()
    salario1()
    edades1()
    #Metdoso 
#Metodo que calcula los salarios mensuales / incompleto
def calcular_edades():
    print("")
    conexion = sqlite3.connect('nominas1.db')
    cursor = conexion.cursor()
    consulta = """ SELECT SMENSUAL from USUARIOS """
    cursor.execute(consulta)
    conexion.commit()
    row1 = cursor.fetchall()
    suma = 0
    a = 0
    for i in row1:
        a1 = str(i)
        a += 1
        suma += float(a1)
    print(suma,"Esto es la suma de los sueldos",a,"Esto es el contador")
    conexion.close()
#Método que da de baja a los usuarios de la database
def dar_baja():
    try:
        print("Entrando en el metodo dar baja")
        conexion = sqlite3.connect('nominas1.db')
        cursor = conexion.cursor()
        consulta  = """Update USUARIOS set FBAJA = ? where CODCLI = ?"""
        values = (str(b1.fbaja.get()),b1.cod.get())
        print(fecha_baja())
        cursor.execute(consulta,values)
        conexion.commit()
        conexion.close()
        b1.msj.configure(text="Empleado dado de baja con exito",foreground="Green")
        b1.msj.place(x=250,y=300)
    except:
        b1.msj.configure(text="Codigo de empleado no existe")
        b1.msj.configure(background="Red")

#Método que rellena los campos de nominas
def crear_nominas():
        print("NOMINAS CREADAS")
        conexion = sqlite3.connect('nominas1.db')
        cursor = conexion.cursor()
        consulta = """ Select * from USUARIOS where CODCLI = ?"""
        print("COD CLIENTE",n1.cod.get())
        values = (n1.cod.get(),)
        cursor.execute(consulta,values)
        conexion.commit()
        row = cursor.fetchone()
        print("Registro cod",row[0])
        n1.apell.config(state="normal")
        n1.apell.insert(0,row[1])
        n1.apell.config(state="disabled")

        n1.fini.config(state="normal")
        n1.fini.insert(0,row[2])
        n1.fini.config(state="disabled")

        n1.fnaci.config(state="normal")
        n1.fnaci.insert(0,row[3])
        n1.fnaci.config(state="disabled")

        n1.dir.config(state="normal")
        n1.dir.insert(0,row[4])
        n1.dir.config(state="disabled")

        n1.nif.config(state="normal")
        n1.nif.insert(0,row[5])
        n1.nif.config(state="disabled")

        n1.dban.config(state="normal")
        n1.dban.insert(0,row[6])
        n1.dban.config(state="disabled")

        n1.nss.config(state="normal")
        n1.nss.insert(0,row[7])
        n1.nss.config(state="disabled")

        n1.sb.config(state="normal")
        n1.sb.insert(0,row[12])
        n1.sb.config(state="disabled")

        n1.numpagas.config(state="normal")
        n1.numpagas.insert(0,2)
        n1.numpagas.config(state="disabled")

        n1.irpf.config(state="normal")
        n1.irpf.insert(0,row[13])
        n1.irpf.config(state="disabled")

        n1.ssocial.config(state="normal")
        n1.ssocial.insert(0,row[16])
        n1.ssocial.config(state="disabled")
        conexion.close()
        print(row,"Registros de las nominas")
#Método que valida el naf
def validacion_naf(naf):
    naf = naf.replace(" ","")
    if len(naf)== 12:
        if naf.isdigit():
            a = int(naf[:2])
            b = int(naf[2:-2])
            c = int(naf[-2:])
            if b < 10000000:
                print("Mayor que 1M")
                codc = ((b+(a*10000000))%97)
                print(codc)
                if codc == c:
                    print("NAF VALIDO")
                    return True
                else:
                    print("NAF NO VALIDO")
            elif b > 10000000:
                print("Menor que 1M")
                codc1 = str(a)+str(b)
                codc = int(codc1)%97
                print(codc)
                if codc == c:
                    print("NAF VALIDADO CORRECTAMENTE")
                else:
                    print("NAF INCORRECTO")
        else:
            print("Numero mal introducido")
    else:
        print("Numero NAF mal introducido")
#Método que crear los empleados
def imprimir():
    fecha_baja()
    if (nif(vAltas.nif.get()) & tlf(vAltas.tlf.get()) ):
        print("NIF correcto")
        vAltas.msj.configure(foreground='Green')
        vAltas.msj.configure(text="Valores Introducidos Correctos")
        conexion = sqlite3.connect('nominas1.db')
        cursor = conexion.cursor()
        #consulta = "Insert into USUARIOS(NOMAPELL,FINI,FNACI,DIR,NIF,DBANCA,NASS,GENERO,DEPARTAMENTO,PUESTO,TLF,SMENSUAL,IRPF,EMAIL,PEXTRA,SEGSOCIAL) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",str(vAltas.apelNom.get()),str(vAltas.fechaini.get()),vAltas.fechafin.get(),vAltas.direccion.get(),vAltas.nif.get(),vAltas.datosbanc.get(),vAltas.numafss.get(),vAltas.genero.get(),vAltas.departamento.get(),vAltas.puesto.get(),vAltas.tlf.get(),vAltas.salariomens.get(),vAltas.irpf.get(),vAltas.email.get(),vAltas.pagasextra.get(),vAltas.segsocial.get()
        datos = (vAltas.apelNom.get(),vAltas.fechaini.get(),vAltas.fechafin.get(),vAltas.direccion.get(),vAltas.nif.get(),vAltas.datosbanc.get(),vAltas.numafss.get(),vAltas.genero.get(),vAltas.departamento.get(),vAltas.puesto.get(),vAltas.tlf.get(),vAltas.salariomens.get(),vAltas.irpf.get(),vAltas.email.get(),vAltas.pagasextra.get(),vAltas.segsocial.get())
        consulta2 = "INSERT INTO USUARIOS VALUES(null,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,null)"
        cursor.execute(consulta2, datos)
        #cursor.execute(consulta)
        #cursor.execute("INSERT INTO Usuarios VALUES ('Pedrito','2022-11-23','2002-12-12','Calle del Arbol','0599164W','000000000123456789','123456789087654321','M','MARKETING','Director','65075326',5000.0,10,'pedrto@gmail.com',NULL,123457890,1,0)")
        #consulta = "INSERT INTO USUARIOS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",vAltas.apelNom.get(),vAltas.fechaini.get(),vAltas.fechafin.get(),vAltas.direccion.get(),vAltas.nif.get(),vAltas.datosbanc.get(),vAltas.numafss.get(),vAltas.genero.get(),vAltas.departamento.get(),vAltas.puesto.get(),vAltas.tlf.get(),vAltas.salariomens.get(),vAltas.irpf.get(),vAltas.email.get(),vAltas.pagasextra.get(),vAltas.segsocial.get(),1,0
        #cursor.executemany(consulta)
        # Ahora podemos recorrer todos los usuarios
        conexion.commit()
        conexion.close()
        print(vAltas.cod.get() + " " + vAltas.apelNom.get())    
    else:
        print("Valores introducidos incorrectos")
    
 #Informes 
def edades1():
    conexion = sqlite3.connect('nominas1.db')
    cursor = conexion.cursor()
    consulta = """ SELECT FNACI from USUARIOS WHERE FBAJA is null and FNACI is not null """
    cursor.execute(consulta)
    conexion.commit()
    linea = cursor.fetchall()
    sumatorio = 0
    contador = 0
    for a in linea:
        contador = contador + 1
        registro = str(a)
        registro = registro.replace("(","").replace("'","").replace(",","").replace(")","")
        print("Estas son las fechas de los registros",registro)
        edad1 = str(datetime.now())
        y = int(registro[:4])
        m = int(registro[5:7])
        d = int(registro[8::])
        y1 = int(edad1[:4])
        m1 = int(edad1[5:7])
        d1 = int(edad1[8:10])
        #edad = relativedelta(datetime.now(), datetime(y, m, d))
        #print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
        añof = y1 - y
        print("Edad 1:",añof)
        if(m1 < m):
            añof = añof -1
        if(m1 == m):
            print("Entrando a meses igualados")
            if(d1 < d):
                añof = añof -1
                print("Entrando a dia de edad",añof)
        print("EDADES FINALES:",añof)
        sumatorio += añof
        print("Conjunto de edades:",sumatorio)
        mediaedad = int(sumatorio / contador)
        in1.mediaEdades.configure(text=mediaedad)
        conexion.close()
        mujeres_edad()
        hombres_edad()
def hombres_edad():
    #Edades medias de hombres
    conexion = sqlite3.connect('nominas1.db')
    cursor = conexion.cursor()
    consulta = """ SELECT FNACI from USUARIOS WHERE FBAJA is null and FNACI is not null and genero = "Masculino" """
    cursor.execute(consulta)
    conexion.commit()
    linea = cursor.fetchall()
    sumatorio = 0
    contador = 0
    for a in linea:
        contador = contador + 1
        registro = str(a)
        registro = registro.replace("(","").replace("'","").replace(",","").replace(")","")
        print("Estas son las fechas de los registros",registro)
        edad1 = str(datetime.now())
        y= int(registro[:4])
        m = int(registro[5:7])
        d = int(registro[8::])
        y1 = int(edad1[:4])
        m1 = int(edad1[5:7])
        d1 = int(edad1[8:10])
        #edad = relativedelta(datetime.now(), datetime(y, m, d))
        #print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
        añof = y1 - y
        print("Edad 1:",añof)
        if(m1 < m):
            añof = añof -1
        if(m1 == m):
            print("Entrando a meses igualados")
        if(d1 < d):
            añof = añof -1
            print("Entrando a dia de edad",añof)
        print("EDADES FINALES:",añof)
        sumatorio += añof
        print("Conjunto de edades:",sumatorio)
        mediaedad = int(sumatorio / contador)
        in1.edadHombre.configure(text=mediaedad)
    conexion.close()
def mujeres_edad():
    conexion = sqlite3.connect('nominas1.db')
    cursor = conexion.cursor()
    consulta = """ SELECT FNACI from USUARIOS WHERE FBAJA is null and FNACI is not null and genero = "Femenino" """
    cursor.execute(consulta)
    conexion.commit()
    linea = cursor.fetchall()
    edad1 = str(datetime.now())
    sumatorio = 0
    contador = 0
    for i in linea:
        contador = contador + 1
        registro = str(i)
        registro = registro.replace("(","").replace("'","").replace(",","").replace(")","")
        print("Fechas formateadas",registro)
        y = int(registro[:4])
        m = int(registro[5:7])
        d = int(registro[8::])
        y1 = int(edad1[:4])
        m1 = int(edad1[5:7])
        d1 = int(edad1[8:10])
        añof = y1 - y
        if(m1 < m):
            añof = añof -1
        if(m1 == m):
            print("Entrando a meses igualados")
            if(d1 < d):
                añof = añof -1
                print("Entrando a dia de edad",añof)
        print("EDADES FINALES:",añof)
        sumatorio += añof
        print("Conjunto de edades:",sumatorio)
        mediaedad = int(sumatorio / contador)
        in1.edad_media_muj.configure(text=mediaedad)
        conexion.close()
def edades():
    print("Edades")
    print(datetime.now())
    edad = datetime.year
    conexion = sqlite3.connect('nominas1.db')
    cursor = conexion.cursor()
    consulta = """ SELECT FNACI from USUARIOS WHERE FBAJA is null and FNACI is not null """
    cursor.execute(consulta)
    conexion.commit()
    linea = cursor.fetchall()
    for a in linea:
        registro = str(a)
        registro = registro.replace("(","").replace("'","").replace(",","").replace(")","")
        print("Estas son las fechas de los registros",registro)
        contador = 1
        año = ""
        mes = ""
        dia = ""
        for i in registro:
            print("Registros",i)
            if(contador<=4):
                año +=i
            elif((contador>=6) & (contador <=7)):
                mes += i
            elif(contador >=9):
                dia += i
            print("Contador",contador)
            contador = contador +1
            print("Año",año,"Mes",mes,"dia",dia)
        #edad = relativedelta(datetime.now(), datetime(registro))
    conexion.close()    
def salario1():
        print("Salario")
        conexion = sqlite3.connect('nominas1.db')
        cursor = conexion.cursor()
        #prescindible
        consulta = """SELECT SMENSUAL FROM USUARIOS WHERE SMENSUAL is NOT null and FBAJA is null"""
        cursor.execute(consulta)
        conexion.commit()
        linea = cursor.fetchall()
        suma = 1.0
        i = 0
        for a in linea:
            i = i + 1
            registro = str(a)
            registro = registro.replace("(","").replace(")","").replace(",","")
            result  = float(registro)
            suma += result
        resultadof = round(suma / i,2)
        formateo = resultadof,"€"
        in1.salariom.configure(text=formateo)
        #Retribcion media mujeres
        consulta = """ SELECT SMENSUAL FROM USUARIOS WHERE SMENSUAL is NOT null and FBAJA is null and GENERO = "Femenino" """
        cursor.execute(consulta)
        conexion.commit()
        linea = cursor.fetchall()
        for a in linea:
            i = i + 1
            registro = str(a)
            registro = registro.replace("(","").replace(")","").replace(",","")
            result  = float(registro)
            suma += result
        resultadof = round(suma / i,2)
        formateo = resultadof,"€"
        in1.salariomuj.configure(text=formateo)
        #Reribucion media de hombres
        consulta = """ SELECT SMENSUAL FROM USUARIOS WHERE SMENSUAL is NOT null and FBAJA is null and GENERO = "Masculino" """
        cursor.execute(consulta)
        conexion.commit()
        linea = cursor.fetchall()
        for a in linea:
            i = i + 1
            registro = str(a)
            registro = registro.replace("(","").replace(")","").replace(",","")
            result  = float(registro)
            suma += result
        resultadof = round(suma / i,2)
        formateo = resultadof,"€"
        in1.salarioh.configure(text=formateo)
        conexion.close()