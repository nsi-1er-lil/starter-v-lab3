c=2
p=4*c
a=c**2
b=(a>5)
print(b)
def perimetre(x):
    
    p = 4 * x  
    return p


c = 2
p = perimetre(c)
a = c**2  
b = (a > 5)  
print(f"Périmètre: {p}")
print(f"Surface supérieure à 5: {b}")

def surface(x):
   
    return x ** 2


c = 3
s = surface(c)
print(f"Surface: {s}")