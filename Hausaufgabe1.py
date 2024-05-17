import matplotlib.pyplot as plt

def spar_funktion(AK, SR, r, lz):
    kapital = AK
    gesamt_kapital = []

for k in range(0, lz+1):
    kapital = SR + kapital * (1+r)
    gesamt_kapital.append(kapital)
    
return gesamt_kapital

print(spar_funktion (AK =10000, SR = 1000, r = 0.01, lz = 10))


plt.bar(range(1,11), end_kapital)