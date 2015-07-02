import random

angka1 = angka2 = 0
repeat = 100000

for num in range(1,repeat):
	rand = random.randrange(1,3)
	if(rand == 1):
		angka1 += 1
	elif(rand == 2):
		angka2 += 1

prob1 = angka1/repeat
prob2 = angka2/repeat

print("H: ", prob1*100)
print("T: ", prob2*100)
