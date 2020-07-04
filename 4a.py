#Pregunta 4a-Interpolacion de Lagrange
#********************************************
import matplotlib.pyplot as plt
import numpy as np

#Definimos los puntos P0,P1,P2,P3
xn=np.array([-3,-1,2,4])
yn=np.array([0,4,3,1])

#Polinomio de Lagrange
lagrange=0
for i in range(0,len(xn)):
    den = 1
    num = np.poly1d([1.0])
    for j in range(0,len(xn)):
        if j!=i:
            num = num * np.poly1d([1.0,-xn[j]])
            den = den * (xn[i]-xn[j])
    L=num/den
    lagrange += L * yn[i]

#Gráfica Interpolación de Lagrange
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.axis([min(xn)-1,max(xn)+1,min(yn)-1,max(yn)+1])
plt.suptitle('Interpolación de Lagrange',fontsize=16)
plt.plot(xn,yn,'go')
valor=np.arange(min(xn),max(xn),0.001)
plt.plot(valor,lagrange(valor))
plt.show()
