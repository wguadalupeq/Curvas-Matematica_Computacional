#Pregunta 4c-Curva Cúbica Uniforme B-Spline
#**********************************************
import matplotlib.pyplot as plt
import numpy as np

#Definiendo listas
B_Spline_x = []
B_Spline_y = []

#Parametros del rango
limite=5
arranque=2.9
secuencia=0.001

#Definimos los puntos P0,P1,P2,P3,P4
xn=np.array([-1,1,3,4,6])
yn=np.array([0,4,-2,3,1])

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
        secuencia = 1.0

#Insertando data en la lista
for i in range(arranque,limite,secuencia):
    #Ecuaciones Parámetricas de B-Spline
    if i>4 and i<5 :
        B_Spline_x.append((pow(i,3)/3)-9*(pow(i,2)/2)+43*(i/2)-(65/2))
        B_Spline_y.append(-3*pow(i,3)+83*(pow(i,2)/2)-377*(i/2)+(1691/6))
    else:    
        B_Spline_x.append((-pow(i,3)/6)+3*(pow(i,2)/2)-5*(i/2)-(1/2))
        B_Spline_y.append((7*pow(i,3)/2)-73*(pow(i,2)/2)+247*(i/2)-(805/6))    

#Gráfica Curva Cúbica de B-Spline
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.suptitle('Curva Cúbica uniforme B-Spline',fontsize=16)
plt.grid()
plt.axis([min(xn)-1,max(xn)+1,min(yn)-1,max(yn)+1])
plt.plot(xn,yn,'ro')
plt.plot(B_Spline_x,B_Spline_y)
plt.show()
