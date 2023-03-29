import numpy as np
import math
import random
from matplotlib import pyplot as plt
from spicy import stats
#--------------------------------------------------------------------------------------------------------------------------------------------
#Obtención de las variables estadisticas de la altura

Alturas =np.loadtxt("datos_altura.txt",dtype=float);
x=0;
media_altura=np.mean(Alturas);
for i in Alturas:
    x+=(i-media_altura)**2;
des_est_alt=(x/len(Alturas))**(1/2);
print("\nAlturas: media = "+str(media_altura)+", desviación estandar = "+str(des_est_alt));
xi=[];
p=[];
probabilidad_alt=0;

#Obtención de la curva gaussiana con distribución normal con tamaño de paso de 0.001 con rango de 70 cm a 210 cm

for i in range (70000,210000):
    p.append(i/1000);
    xi.append((1/(des_est_alt*(2*math.pi)**(1/2)))*math.e**((-1*(((i/1000)-media_altura)**2)/(2*des_est_alt**2))));
    if ((media_altura-des_est_alt)<(i/1000)<media_altura+des_est_alt):
        probabilidad_alt+=((1/(des_est_alt*(2*math.pi)**(1/2)))*math.e**((-1*(((i/1000)-media_altura)**2)/(2*des_est_alt**2))))/10;


#Grágica del histograma de altura con 15 clases
        
plt.figure(1)
plt.subplot(121)
clases= 15
Alt= np.array(Alturas[:])
rango= (min(Alturas),max(Alturas))
plt.title("Histograma Alturas")
plt.xlabel("Clases")
plt.ylabel("Frecuencia")
plt.hist(Alt, range=rango, bins = clases, density=False)


#Gráfica de la primera distribución normal con histograma

plt.subplot(122)
plt.grid();
plt.plot(p,xi)
plt.title("Distribución normal para alturas")
plt.xlabel("Alturas (cm)")
plt.ylabel("Probabilidad")
xi=[];
p=[];

#Obtención de la curva gaussiana con distribución normal con tamaño de paso de 0.001 con rango de 120 cm a 210 cm

for i in range (120000,210000):
    p.append(i/1000);
    xi.append((1/(des_est_alt*(2*math.pi)**(1/2)))*math.e**((-1*(((i/1000)-media_altura)**2)/(2*des_est_alt**2))));
    
#Gráfica de la segunda distribución normal

plt.figure(2)
plt.grid();
plt.plot(p,xi)
plt.title("Distribución normal para alturas")
plt.xlabel("Alturas (cm)")
plt.ylabel("Probabilidad")

#--------------------------------------------------------------------------------------------------------------------------------------------
#Obtención de las variables estadisticas del calzado

Calzado=np.loadtxt("datos_calzado.txt",dtype=float);
x=0;
media_calzado=np.mean(Calzado);
for i in Calzado:
    x+=(i-media_calzado)**2;
des_est_calz=(x/len(Alturas))**(1/2);
print("\nCalzado: media = "+str(media_calzado)+", desviación estandar = "+str(des_est_calz));

#Obtención de la curva gaussiana con distribución normalcon tamaño de paso de 0.001 con rnago de 18 cm a 34 cm

xi=[];
p=[];
probabilidad_calz=0;
probabilidad_total=0;
for i in range (18000,34000):
    p.append(i/1000);
    xi.append((1/(des_est_calz*(2*math.pi)**(1/2)))*math.e**((-1*(((i/1000)-media_calzado)**2)/(2*des_est_calz**2))));
    probabilidad_total+=(1/(des_est_calz*(2*math.pi)**(1/2)))*math.e**((-1*(((i/1000)-media_calzado)**2)/(2*des_est_calz**2)));
    if (media_calzado-des_est_calz<=(i/1000)<=media_calzado+des_est_calz):
        probabilidad_calz+=((1/(des_est_calz*(2*math.pi)**(1/2)))*math.e**((-1*(((i/1000)-media_calzado)**2)/(2*des_est_calz**2))))/10

#Gráfica de la distribución normal
        
plt.figure(3)
plt.subplot(122)
plt.grid();
plt.plot(p,xi)
plt.title("Distribución normal para calzado")
plt.xlabel("Calzado (cm)")
plt.ylabel("Probabilidad")

#Gráfica del histograma con 8 clases

clases= 8
Clz= np.array(Calzado[:])
rango= (min(Calzado),max(Calzado))
plt.subplot(121)
plt.title("Histograma Calzado")
plt.xlabel("Clases")
plt.ylabel("Frecuencia")
plt.hist(Clz, range=rango, bins = clases, density=False)
graf=[[],[]];

#Despliegue de los valores estadísticos

print("\n La probabilidad de la altura en la primera desviación estandar es de "+str(round(probabilidad_alt,3))+" %");
print("\n La probabilidad del calzado en la primera desviación estandar es de "+str(round(probabilidad_calz,3))+" %");

#--------------------------------------------------------------------------------------------------------------------------------------------
#Eliminación de outliers (ambos sexos)

Alt_n=[];
Clz_n=[];
for i in range (0,len(Alt)):
    if (Alt[i]>=140):
        Alt_n.append(Alt[i]);
        Clz_n.append(Clz[i]);
        
#Obtención de la linea de tendencia (ambos sexos con outliers)

a=0;
b=0;
x_i=0;
x_iy_i=0;
y_i=0;
x_i2=0;
n=len(Alt)
for i in range (0,len(Alt)):
    x_i+=Alt[i];
    x_iy_i+=Alt[i]*Clz[i];
    y_i+=Clz[i];
    x_i2+=Alt[i]**2;
R= np.corrcoef(Alt,Clz);
a=((x_i*x_iy_i)-(y_i*x_i2))/((x_i)**2-(n*x_i2))
b=(((n*x_iy_i)-(x_i*y_i))/(n*x_i2-x_i**2))

#Despliegue de la linea de tendencia (ambos sexos con outliers)

print("\nLa linea de tendencia con outliers es: y = "+str(a)+" + x "+str(b)+ " con una R="+str(R[0][1]))

#Obtención de los valores de y de la linea de tendencia (ambos sexo con outliers)

valores=[];
for i in Alt:
    valores.append(a+b*i);

#Gráfica de disperción con outliers (ambos sexos)

plt.figure(4)
plt.subplot(121)
plt.grid();
plt.scatter(Alt,Clz);
plt.plot(Alt,valores,"red")
plt.title("Clazado vs Altura con outliers")
plt.xlabel("Altura")
plt.ylabel("Clazado")

#Obtención de la linea de tendencia (ambos sexos sin outliers)

a=0;
b=0;
x_i=0;
x_iy_i=0;
y_i=0;
x_i2=0;
n=len(Alt_n)
for i in range (0,len(Alt_n)):
    x_i+=Alt_n[i];
    x_iy_i+=Alt_n[i]*Clz_n[i];
    y_i+=Clz_n[i];
    x_i2+=Alt_n[i]**2;
R= np.corrcoef(Alt_n,Clz_n);
a=((x_i*x_iy_i)-(y_i*x_i2))/((x_i)**2-(n*x_i2))
b=(((n*x_iy_i)-(x_i*y_i))/(n*x_i2-x_i**2))

#Despliegue de la linea de tendencia (ambos sexos sin outliers)

print("\nLa linea de tendencia sin outliers es: y = "+str(a)+" + x "+str(b)+ " con una R="+str(R[0][1]))

#Obtención de los valores de y de la linea de tendencia (ambos sexo sin outliers)

valores=[];
for i in Alt_n:
    valores.append(a+b*i);

#Gráfica de disperción sin outliers (ambos sexos)
        
plt.subplot(122)
plt.grid();
plt.scatter(Alt_n,Clz_n);
plt.plot(Alt_n,valores,"red")
plt.title("Clazado vs Altura sin outliers")
plt.xlabel("Altura")
plt.ylabel("Calzado")

#-----------------------------------------------------------------------------------------------------------------------------------------
#Separación de datos por sexo y quitando outliers
#1=masculino; 0=femenino

sexo=np.loadtxt("datos1.txt",dtype=int);
Alt_h=[];
Clz_h=[];
Alt_m=[];
Clz_m=[];
for i in range (0,len(sexo)):
    if (Alt[i]>=130):
        if sexo[i]==1:
            Alt_h.append(Alt[i]);
            Clz_h.append(Clz[i]);
        if sexo[i]==0:
            Alt_m.append(Alt[i]);
            Clz_m.append(Clz[i]);

#Obtención de la linea de tendencia para hombres sin outliers
        
a=0;
b=0;
x_i=0;
x_iy_i=0;
y_i=0;
x_i2=0;
n=len(Alt_h)
for i in range (0,len(Alt_h)):
    x_i+=Alt_h[i];
    x_iy_i+=Alt_h[i]*Clz_h[i];
    y_i+=Clz_h[i];
    x_i2+=Alt_h[i]**2;
R= np.corrcoef(Alt_h,Clz_h);
a=((x_i*x_iy_i)-(y_i*x_i2))/((x_i)**2-(n*x_i2))
b=(((n*x_iy_i)-(x_i*y_i))/(n*x_i2-x_i**2))

#Despliegue de la linea de tendencia (Hombres sin outliers)

print("\nLa linea de tendencia para hombres es: y = "+str(a)+" + x "+str(b)+ " con una R="+str(R[0][1]))

#Obtención de los valores en y de la linea de tendencia (Hombres sin outliers)

valores=[];
for i in Alt_h:
    valores.append(a+b*i);
    
#Gráfica de disperción de los valores (hombres sin outliers)
    
plt.figure(5)
plt.subplot(121)
plt.grid();
plt.scatter(Alt_h,Clz_h);
plt.plot(Alt_h,valores,"red")
plt.title("Clazado vs Altura (Hombres)")
plt.xlabel("Altura")
plt.ylabel("Clazado")

#Obtención de la linea de tendencia para mujeres sin outliers

a=0;
b=0;
x_i=0;
x_iy_i=0;
y_i=0;
x_i2=0;
n=len(Alt_m)
for i in range (0,len(Alt_m)):
    x_i+=Alt_m[i];
    x_iy_i+=Alt_m[i]*Clz_m[i];
    y_i+=Clz_m[i];
    x_i2+=Alt_m[i]**2;
R= np.corrcoef(Alt_m,Clz_m);
a=((x_i*x_iy_i)-(y_i*x_i2))/((x_i)**2-(n*x_i2))
b=(((n*x_iy_i)-(x_i*y_i))/(n*x_i2-x_i**2))

#Despliegue de la linea de tendencia oara Mujeres sin outliers

print("\nLa linea de tendencia para mujeres es: y = "+str(a)+" + x "+str(b)+ " con una R="+str(R[0][1]))

#Obtención de los datos en y de la linea de tendencia sin outliers

valores=[];
for i in Alt_n:
    valores.append(a+b*i);

#Gráfica de dispersión de los valores de mujers sin outliers
    
plt.subplot(122)
plt.grid();
plt.scatter(Alt_m,Clz_m);
plt.plot(Alt_n,valores,"red")
plt.title("Clazado vs Altura (Mujeres)")
plt.xlabel("Altura")
plt.ylabel("Calzado")
plt.show();
    