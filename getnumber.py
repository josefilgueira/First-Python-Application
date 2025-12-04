import getpass as gp #Importamos esta librería para usar en la función secret_num y así ocultar el número introducido.

#Compueba que un dato (x) es un número.
def es_num(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

#Pide un número SECRETO entero al Jugador1 entre dos valores (Este no aparece en pantalla y se asegura que ha introducido un número entero).
def secret_num(x, y, Jugador1):
    a = None 
    while True:
        a = gp.getpass(f'{Jugador1}: Introduce tu número entero secreto (entre {x} y {y}): ')
        
        if not es_num(a):# Comprueba que lo introducido es un número. Si no lo es, indica que no has introducido un número y pasa al siguiente bucle.
            print('No has introducido un número.')
            continue
        
        a = float(a)
        if a.is_integer() and x <= a <= y: #Comprueba que el número introducido es un número entero y entre los valores x e y. Si lo es, acaba el bucle (break).
            a = int(a)  
            break  

        else:
            print(f'Número no válido. Debe ser un entero entre {x} y {y}.') # Si no, devuelve un mensaje indicando que es un número NO valido.

    print()
    return a
    
#Pide un número entero entre dos valores y se asegura de ello(Al contrario que secret_num, está función no esconde los valores introducidos).
def pedir_num(x,y):
    while True:
        n=input(f'Introduce un número entero entre {x} y {y}.')
        if not es_num(n): # Comprueba que lo introducido es un número. Si no lo es, indica que no has introducido un número y pasa al siguiente bucle.
                print('No has introducido un número.')
                continue

            
        n = float(n)
        if n.is_integer() and x <= n <= y: #Comprueba que el número introducido es un número entero y entre los valores x e y. Si lo es, acaba el bucle (break).
            return int(n)  
            print()
            break  
        else:
            print(f'Número no válido. Debe ser un entero entre {x} y {y}.')


