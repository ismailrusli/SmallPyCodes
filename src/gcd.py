"""Greatest Common Divisor
Euclid's algorithm

by ISM
November 12th, 2012
"""


def gcd(number1,number2):
	if number1 == number2: return number1	
	
	big,small = 0,0
			
	if number1 > number2:
		big=number1		
		small=number2
	else:
		big=number2
		small=number1
	
	sisa = big
	
	while sisa != 0:
		sisa = big%small
		big = small
		small = sisa
		#print(big,small)
	
	return(big)
	
print(gcd(640,15))
#gcd(100,16)
