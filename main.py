import matplotlib.pyplot as plt

actividades = ['jugar','trabajar','comer','dormir']
horas = [5,8,3,8]
colores = ['r','g','b','m']

plt.pie(horas,labels=actividades,colors=colores,startangle=90,shadow=True,
        explode=(0,0,0.2,0),autopct="%1.2f%%")

plt.legend()
plt.show()