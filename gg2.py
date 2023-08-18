from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

def redon(x): # Funcion para redondear o combertir en entero. Si no saldrian valores como 5.0000 em vez de un 5
    if(x-round(x) == 0):
        y=int(x)
    else:
        y=round(x,2)
    return(y)

def signo1(x): # Para colocoar el signo + a valores positivos y que aparezca en la ecuacion del resultado
    if(x<0):y= f"(x{x})"
    elif (x == 0) :y="x"
    else:  y= f"(x+{x})"
    return(y)
def signo2(x): # Para colocoar el signo + a valores positivos y que aparezca en la ecuacion del resultado
    if(x<0):y= f"{x}"
    elif (x == 0) :y="x"
    else:  y= f"+{x}"
    return(y)

def calcular(): # Hace las operaciones del metodo
    global h1
    h1=1;h2=2
    h1=x2.get() - x1.get(); h2=x3.get() - x2.get(); h3=x4.get() - x3.get(); h4=x5.get() - x4.get(); h5=x6.get() - x5.get()
    h6=x7.get() - x6.get(); h7=x8.get() - x7.get(); h8=x9.get() - x8.get(); h9=x10.get() - x9.get()

    if (punt.get()<=2): h2=h1
    if (punt.get()<=3): h3=h2
    if (punt.get()<=4): h4=h3
    if (punt.get()<=5): h5=h4
    if (punt.get()<=6): h6=h5
    if (punt.get()<=7): h7=h6
    if (punt.get()<=8): h8=h7
    if (punt.get()<=9): h9=h8

    if (h1 == h2 and h1 == h3 and h1 == h4 and h1 == h5 and h1 == h6 and h1 == h7 and h1 == h8 and h1 == h9):
        if(h1 != 0):
            t11=y2.get()-y1.get(); t12=y3.get()-y2.get(); t13=y4.get()-y3.get(); t14=y5.get()-y4.get(); t15=y6.get()-y5.get(); t16=y7.get()-y6.get(); t17=y8.get()-y7.get(); t18=y9.get()-y8.get(); t19=y10.get()-y9.get()
            t21=t12-t11; t22=t13-t12; t23=t14-t13; t24=t15-t14; t25=t16-t15; t26=t17-t16; t27=t18-t17; t28=t19-t18
            t31=t22-t21; t32=t23-t22; t33=t24-t23; t34=t25-t24; t35=t26-t25; t36=t27-t26; t37=t28-t27
            t41=t32-t31; t42=t33-t32; t43=t34-t33; t44=t35-t34; t45=t36-t35; t46=t37-t36
            t51=t42-t41; t52=t43-t42; t53=t44-t43; t54=t45-t44; t55=t46-t45
            t61=t52-t51; t62=t53-t52; t63=t54-t53; t64=t55-t54
            t71=t62-t61; t72=t63-t62; t73=t64-t63
            t81=t72-t71; t82=t73-t72
            t91=t82-t81

            global c1,c2,c3,c4,c5,c6,c7,c8,c9
            c1=redon(t11/(h1))
            c2=redon(t21/((h1**2)*2))
            c3=redon(t31/((h1**3)*6))
            c4=redon(t41/((h1**4)*24))
            c5=redon(t51/((h1**5)*120))
            c6=redon(t61/((h1**6)*760))
            c7=redon(t71/((h1**7)*5040))
            c8=redon(t81/((h1**8)*40320))
            c9=redon(t91/((h1**9)*362880))

            global x11,x21,x31,x41,x51,x61,x71,x81,x91
            y11=redon(y1.get())
            x11=redon(x1.get())*-1; x21=redon(x2.get())*-1; x31=redon(x3.get())*-1
            x41=redon(x4.get())*-1; x51=redon(x5.get())*-1; x61=redon(x6.get())*-1
            x71=redon(x7.get())*-1; x81=redon(x8.get())*-1; x91=redon(x9.get())*-1

            poli=["f(x)="]
            if(punt.get()>=1 and y11 == 0): poli.append(f"0")
            if(punt.get()>=1 and y11 != 0): poli.append(f"{y11}")
            if(punt.get()>=2 and redon(t11/(h1)) != 0): poli.append(f"{c1}{signo1(x11)}")
            if(punt.get()>=3 and redon(t21/((h1**2)*2)) != 0): poli.append(f"{signo2(c2)}{signo1(x11)}{signo1(x21)}")
            if(punt.get()>=4 and redon(t31/((h1**3)*6)) != 0): poli.append(f"{signo2(c3)}{signo1(x11)}{signo1(x21)}{signo1(x31)}")
            if(punt.get()>=5 and redon(t41/((h1**4)*24)) != 0): poli.append(f"{signo2(c4)}{signo1(x11)}{signo1(x21)}{signo1(x31)}{signo1(x41)}")
            if(punt.get()>=6 and redon(t51/((h1**5)*120)) != 0): poli.append(f"{signo2(c5)}{signo1(x11)}{signo1(x21)}{signo1(x31)}{signo1(x41)}{signo1(x51)}")
            if(punt.get()>=7 and redon(t61/((h1**6)*760)) != 0): poli.append(f"{signo2(c6)}{signo1(x11)}{signo1(x21)}{signo1(x31)}{signo1(x41)}{signo1(x51)}{signo1(x61)}")
            if(punt.get()>=8 and redon(t71/((h1**7)*5040)) != 0): poli.append(f"{signo2(c7)}{signo1(x11)}{signo1(x21)}{signo1(x31)}{signo1(x41)}{signo1(x51)}{signo1(x61)}{signo1(x71)}")
            if(punt.get()>=9 and redon(t81/((h1**8)*40320)) != 0): poli.append(f"{signo2(c8)}{signo1(x11)}{signo1(x21)}{signo1(x31)}{signo1(x41)}{signo1(x51)}{signo1(x61)}{signo1(x71)}{signo1(x81)}")
            if(punt.get()>=10 and redon(t91/((h1**9)*362880)) != 0): poli.append(f"{signo2(c9)}{signo1(x11)}{signo1(x21)}{signo1(x31)}{signo1(x41)}{signo1(x51)}{signo1(x61)}{signo1(x71)}{signo1(x81)}{signo1(x91)}")

            cal.set(poli)
            botonG.place(x=30,y=220)
        else:
            cal.set("El espacio entre los puntos no puede ser 0")
            botonG.place(x=aio,y=aio)    
    else:
        cal.set("No es igualmente espasiado")
        botonG.place(x=aio,y=aio)    
    pass

def puntos(): # Para colocar la cantidad de cuadros segun los puntos seleccionados
    global aio
    aio=9999 
    boton.place(x=30,y=120)
    tx4.place(x=30,y=90); tx2.place(x=30,y=70)
    Numx1.place(x=aio,y=aio); Numx2.place(x=aio,y=aio); Numx3.place(x=aio,y=aio); Numx4.place(x=aio,y=aio)
    Numx5.place(x=aio,y=aio); Numx6.place(x=aio,y=aio); Numx7.place(x=aio,y=aio); Numx8.place(x=aio,y=aio)
    Numx9.place(x=aio,y=aio); Numx10.place(x=aio,y=aio); Numy1.place(x=aio,y=aio); Numy2.place(x=aio,y=aio)
    Numy3.place(x=aio,y=aio); Numy4.place(x=aio,y=aio); Numy5.place(x=aio,y=aio); Numy6.place(x=aio,y=aio)
    Numy7.place(x=aio,y=aio); Numy8.place(x=aio,y=aio); Numy9.place(x=aio,y=aio); Numy10.place(x=aio,y=aio)
    if (punt.get()>=1): Numx1.place(x=50,y=70);Numy1.place(x=50,y=90)
    if (punt.get()>=2): Numx2.place(x=180,y=70);Numy2.place(x=180,y=90)
    if (punt.get()>=3): Numx3.place(x=310,y=70);Numy3.place(x=310,y=90)
    if (punt.get()>=4): Numy4.place(x=440,y=90);Numx4.place(x=440,y=70)
    if (punt.get()>=5): Numy5.place(x=570,y=90);Numx5.place(x=570,y=70);ventana.geometry("730x750")
    if (punt.get()>=6): Numy6.place(x=700,y=90);Numx6.place(x=700,y=70);ventana.geometry("860x750")
    if (punt.get()>=7): Numy7.place(x=830,y=90);Numx7.place(x=830,y=70);ventana.geometry("990x750")
    if (punt.get()>=8): Numy8.place(x=960,y=90);Numx8.place(x=960,y=70);ventana.geometry("1120x750")
    if (punt.get()>=9): Numy9.place(x=1090,y=90);Numx9.place(x=1090,y=70);ventana.geometry("1250x750")
    if (punt.get()>=10): Numy10.place(x=1220,y=90);Numx10.place(x=1220,y=70);ventana.geometry("1380x750")   
    pass 

def graficar():
    global datax,datay, fig, ax, frame,canvas

    plt.clf()
    
    fig, ax = plt.subplots(dpi=90, figsize=(7,5),facecolor=rgb)
    frame = Frame(ventana)
    frame.place(x=30,y=250)
    ax.set_facecolor(rgb)
    ax.axhline(linewidth=1, c=letra)
    ax.axvline(linewidth=1, c=letra)

    canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
    canvas.get_tk_widget().grid()

    datax=np.linspace(x1.get() , x1.get() + ((x2.get()-x1.get())*punt.get()) - h1 , 69)

    if (punt.get()>=2):datay = y1.get()+(c1*(datax+x11))
    if (punt.get()>=3):datay += c2*(datax+x11)*(datax+x21)
    if (punt.get()>=4):datay += c3*(datax+x11)*(datax+x21)*(datax+x31)
    if (punt.get()>=5):datay += c4*(datax+x11)*(datax+x21)*(datax+x31)*(datax+x41)
    if (punt.get()>=6):datay += c5*(datax+x11)*(datax+x21)*(datax+x31)*(datax+x41)*(datax+x51)
    if (punt.get()>=7):datay += c6*(datax+x11)*(datax+x21)*(datax+x31)*(datax+x41)*(datax+x51)*(datax+x61)
    if (punt.get()>=8):datay += c7*(datax+x11)*(datax+x21)*(datax+x31)*(datax+x41)*(datax+x51)*(datax+x61)*(datax+x71)
    if (punt.get()>=9):datay += c8*(datax+x11)*(datax+x21)*(datax+x31)*(datax+x41)*(datax+x51)*(datax+x61)*(datax+x71)*(datax+x81)
    if (punt.get()>=10):datay += c9*(datax+x11)*(datax+x21)*(datax+x31)*(datax+x41)*(datax+x51)*(datax+x61)*(datax+x71)*(datax+x81)*(datax+x91)

    np.delete(datax,-1)
    line, = ax.plot(datax, datay, color ='r')
    ax.grid(linestyle='dotted')
    canvas.draw()
    pass
    

from tkinter import Canvas

rgb="#F4F4F4" # Cambiar color de fondo y letra
letra="black"

ventana = Tk() # Para que se cree la ventana y lo demas son declaracion de variables, widget y posisionamiento de los widget
ventana.title("Polinomio de interpolacion de Newton con datos igualmente espaciados")
ventana.geometry("730x750") # Tamaño de la ventana
ventana.config(bg=rgb)

cal = StringVar() # Declaracion de variables y objetos
punt=IntVar()
x1 = DoubleVar(); y1 = DoubleVar()
x2 = DoubleVar(); y2 = DoubleVar()
x3 = DoubleVar(); y3 = DoubleVar()
x4 = DoubleVar(); y4 = DoubleVar()
x5 = DoubleVar(); y5 = DoubleVar()
x6 = DoubleVar(); y6 = DoubleVar()
x7 = DoubleVar(); y7 = DoubleVar()
x8 = DoubleVar(); y8 = DoubleVar()
x9 = DoubleVar(); y9 = DoubleVar()
x10 = DoubleVar(); y10 = DoubleVar()
Numx1 = Entry(ventana,textvariable=x1);Numy1 = Entry(ventana, textvariable=y1)  
Numx2 = Entry(ventana,textvariable=x2);Numy2 = Entry(ventana, textvariable=y2)
Numx3 = Entry(ventana,textvariable=x3);Numy3 = Entry(ventana, textvariable=y3)
Numx4 = Entry(ventana,textvariable=x4);Numy4 = Entry(ventana, textvariable=y4)
Numx5 = Entry(ventana,textvariable=x5);Numy5 = Entry(ventana, textvariable=y5)
Numx6 = Entry(ventana,textvariable=x6);Numy6 = Entry(ventana, textvariable=y6)
Numx7 = Entry(ventana,textvariable=x7);Numy7 = Entry(ventana, textvariable=y7)
Numx8 = Entry(ventana,textvariable=x8);Numy8 = Entry(ventana, textvariable=y8)
Numx9 = Entry(ventana,textvariable=x9); Numy9 = Entry(ventana, textvariable=y9)
Numx10 = Entry(ventana,textvariable=x10); Numy10 = Entry(ventana, textvariable=y10)

tx1 = Label(ventana,text="Colocar valores de (x,y)",bg=rgb,fg=letra,font=50) # Cajas de texto, widget y etiquetas
tx1.place(x=30,y=10)
tx3 = Label(ventana,text="Numero de puntos",bg=rgb,fg=letra) 
tx3.place(x=30,y=40)
tx2 = Label(ventana,text="x",bg=rgb,fg=letra) 
tx4 = Label(ventana,text="y",bg=rgb,fg=letra) 
NumP = Spinbox(ventana,textvariable=punt,from_=2,to=10,width = 7)
NumP.place(x=145,y=40)
botonp = Button(ventana, text="Continuar",command=puntos)
botonp.place(x=210,y=37)


txRes = Label(ventana, textvariable=cal, bg=rgb, fg=letra)
txRes.place(x=50,y=170)
boton = Button(ventana, text="Calcular", command=calcular)
botonG = Button(ventana, text='Graficar', width = 15, command= graficar)

ventana.after(1)
ventana.mainloop()