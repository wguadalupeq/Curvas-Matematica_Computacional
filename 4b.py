#Pregunta 4b-Curva Cúbica Bézier
#***********************************
import matplotlib.pyplot as plt
import numpy as np

#Definiendo listas
Bezier_x = []
Bezier_y = []

#Parametros del rango
limite=1
secuencia=0.001

#Definimos los puntos P0,P1,P2,P3
xn=np.array([-3,-1,2,4])
yn=np.array([0,4,3,1])

#Definimos el intervalo de iteracion
def range(inicio, fin=None, secuencia=None):
    while True:
        if 0 < secuencia and inicio >= fin: break
        elif secuencia < 0 and inicio <= fin: break
        yield inicio
        inicio = inicio + secuencia
    if fin == None:
        fin = inicio + 0.0
        inicio = 0.0
    if secuencia == None:
        secuencia = 1

#Insertando data en la lista
for i in range(0,limite,secuencia):
    #Ecuaciones Parámetricas de Bezier
    Bezier_x.append(-2*pow(i,3)+3*pow(i,2)+6*i-3)
    Bezier_y.append(4*pow(i,3)-15*pow(i,2)+12*i)

#Gráfica Curva Cúbica de Bézier
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.suptitle('Curva Cúbica Bézier',fontsize=20)
plt.grid()
plt.axis([min(xn)-1,max(xn)+1,min(yn)-1,max(yn)+1])
plt.plot(xn,yn,'ro')
plt.plot(Bezier_x,Bezier_y)
plt.show()
