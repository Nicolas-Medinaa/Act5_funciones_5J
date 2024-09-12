print("Ejemplo de funciones")
# Declarando Funciones
def hola():
    print("Alguien uso la funcion hola")

def chat(mensa):
    print(f"chat: {mensa}")

def ellacontesta(mensa):
    print(f"chat ella: {mensa}")

def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")

def suma(a,b):
    s=a+b
    return s

def rest(c,d):
    r=c-d
    return r

def mult(c,d):
    r=c*d
    return r

def div(c,d):
    r=c/d
    return r

# Llamadas de funciones  
hola()
chat("Ke bonia ztas")
ellacontesta("GRAZIAS uwu")
escribenombre("Medina","Nicolas")

print("Operaciones suma")
c1=int(input("Ingresa un numero: "))
c2=int(input("Ingresa un numero: "))
damesuma = suma(c1,c2)
print(f"La suma de {c1} + {c2} = {damesuma}")

print("Operaciones resta")
a1=int(input("Ingresa un numero: "))
a2=int(input("Ingresa un numero: "))
dameresta = rest(a1,a2)
print(f"La resta de {a1} - {a2} = {dameresta}")

print("Operaciones multiplicacion")
a3=int(input("Ingresa un numero: "))
a4=int(input("Ingresa un numero: "))
damemul = mult(a3,a4)
print(f"La multiplicacion de {a3} * {a4} = {damemul}")

print("Operaciones divicion")
a5=int(input("Ingresa un numero: "))
a6=int(input("Ingresa un numero: "))
damediv = div(a5,a6)
print(f"La divicion de {a5} / {a6} = {damediv}")
