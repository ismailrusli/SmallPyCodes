import numpy as np
import matplotlib.pyplot as plt

angka1 = angka2 = angka3 = angka4 = angka5 = angka6 = 0.0
repeat = 10000

for num in range(1,repeat):
	rand = np.random.random_integers(1,6)
	if rand == 1:
		angka1 += 1
	elif rand == 2:
		angka2 += 1
	elif rand == 3:
		angka3 += 1
	elif rand == 4:
		angka4 += 1
	elif rand == 5:
		angka5 += 1
	elif rand == 6:
		angka6 += 1

figure1 = plt.figure()
plt.plot([1,2,3,4,5,6],[angka1,angka2,angka3,angka4,angka5,angka6],'b-')
plt.xlim(1,6)
plt.ylim(0,5000)
plt.xlabel("angka dadu")
plt.ylabel("kemunculan")
plt.title("Simulasi Pelemparan Dadu")

plt.show()
	
