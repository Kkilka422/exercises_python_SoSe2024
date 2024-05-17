
import matplotlib.pyplot as plt


s_n = [] 
r = 1.1
a = 1
n = 100

summe = 0

for k in range (0, n):
    summe += a * r**k
    s_n.append(summe)
    
print(s_n)

plt.plot(s_n)