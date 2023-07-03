print("Bienvenido!")
respuesta=int(input("Ingrese un numero del 1 al 1000:"))

def comprobador():
    if respuesta > 0 and respuesta < 1000 and respuesta%2 == 0:
        print("Su numero es par")
    elif respuesta > 0 and respuesta < 1000 and respuesta%2 != 0:
        print("Su numero es impar")
    else:
        print("Ingrese un numero valido")    


comprobador()
    

    
  
       