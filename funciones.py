"""
Your module description
"""
def sumar(x, y):
    return x+y
    
def es_primo(x):
    if x == 1:
        return False
    else:
        contador=0
    for i in range(1, x+1):
        if i == 1 or i == x:
            continue
        if x % i == 0:
            contador +=1
    if contador == 0:
        return True
    else:
        return False