import numpy as np
import matplotlib.pyplot as plt
import aseegg as ag
import pandas as pd

dane = pd.read_csv(r"C:\Users\Admin\Desktop\kck zadanie 13\sub-007_trial-04.csv", delimiter=';', engine='python')

kolumna1=dane["1.6385697466884339"]
kolumna2=dane["0.1"]

t = np.linspace(0, 37.96, 200*37.856)

#filtracja sygnału
p1 = ag.pasmowozaporowy(kolumna1, 200, 49, 51)
p2 = ag.pasmowoprzepustowy(p1, 200, 1,50)

plt.subplot(2,1,1)
plt.title("Sygnał przefiltrowany")
plt.plot(t,p2)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [mV]')

plt.subplot(2,1,2)
plt.plot(t,kolumna2)
plt.xlabel('Czas [s]')
plt.ylabel('Wyświetlana cyfra [-]')


plt.show()

#sygnał nie przefiltrowany
'''
plt.subplot(2,1,1)
plt.title("Sygnał nieprzefiltrowany")
plt.plot(t,kolumna1)
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda [mV]')

plt.subplot(2,1,2)
plt.plot(t,kolumna2)
plt.xlabel('Czas [s]')
plt.ylabel('Wyświetlana cyfra [-]')

plt.show()
'''



print("Osoba badana wymrugała następujący kod: 1, 1, 3, 5, 2, 4, 5, 1, 2, 3, 4, 5, 5, 1, 1, 1, 3, 3, 3, 5, 1, 2, 3, 3, 4, 5")


'''
mrugniecie=[]
for i in range (len(p2)):
    if p2[i]>0.05:
        mrugniecie.append(i)
print(mrugniecie)
print(len(mrugniecie))
'''
