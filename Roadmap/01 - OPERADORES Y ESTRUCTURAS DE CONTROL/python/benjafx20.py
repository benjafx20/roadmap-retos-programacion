"""
operadores
"""

#operadores arigmeticos
print(f"suma: 10 + 3 = {10 + 3}")
print(f"Resta: 10 - 3 = {10 - 3}")
print(f"Multiplicacion: 10 * 3 = {10 * 3}")
print(f"Division: 10 / 3 = {10 / 3}")
print(f"Modulo: 10 % 3 = {10 % 3}")
print(f"Exponenciales: 10 ** 3 = {10 ** 3}")
print(f"Division entera: 10 // 3 = {10 // 3}")

# operadores de comparacion
print(f"Igualdad: 10 == 3 es {10 == 3}")
print(f"Desigualdad: 10 != 3 es {10 != 3}")
print(f"Mayor que: 10 > 3 es {10 > 3}")
print(f"Menor que: 10 < 3 es {10 < 3}")
print(f"Mayor o igual que: 10 >= 3 es {10 >= 3}")
print(f"Menopr o igual que: 10 <= 3 es {10 <= 3}")

# Operadores logicos
print(f "AND && ") # los dos deben ser verdaderos
print(f "OR ||") # con uno verdadero basta
print(f "NOT") # es para decir que no o negarla

# operadores de asignacion
my_number = 11 #asignacion
print(my_number)
my_number += 1 # suma y asigna
print(my_number) 
"""
y asi con todos los operadores arigmeticos
"""

#Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_numbrt is my_new_number}") # is= es (igualdad)
print(f"my_number is bot my_new_number es {my_numbrt is not my_new_number}") # is not= no es (desigualdad)

#Operadores de pertenencia
print(f" 'u' in 'moure' = {'u' in 'moure'}") #si esque la u esta en la palabra moure
print(f" 'b' not in 'moure' = {'b' not in 'moure'}") #si esque la b no esta en la palabra moure

#operadores de bit pueden trabajar con numeros enteros y cambiarlos a binarios
a = 10 # variable a con valor 10
b = 3 # fvariable b con valor 3 
"""
binario de 3 es 11
y el de 10 es 1010
"""

print(f" AND: 10 & 3 = {10 & 3}") # si son iguales 1 diferentes 0
print(f" OR: 10 | 3 = {10 | 3}")
print(f" XOR: 10 ^ 3 = {10 ^ 3}") # si son diferentes 1 iguales 0
print(f" NOT: 10  3 = {10  3}")
print(f" Desplazamiento ala derecha: 10 >> 2 = {10 >> 2}")
print(f" Desplazamiento ala izquierda: 10 << 2 = {10 << 2}")

"""
estructuras de control
"""
#Condicionales

my_string = "Mouredev"

if my_string == "Mouredev" #if es SI
  print("my_string es 'Mouredev'")
else:
print("my_string  no es 'Mouredev'") # para cuando no se cumple el if
elif # como otra opcion es decir si no es una pude tomar el elif si correspondiese

#Interactivas
for i in range(11) #for para bucle y rango me toma todo lo que viene antes del 11 esta vez
 print(i)
  
while i <= 10: # bucle infinito si no agrego nada mas
  print(i)
  i +=1 # agrega numeros cada vez que imprima

#Manejo de excepciones
try: # intentar
print(10/0)
except:
print("se ah producido un error") # para  que no pete y siga funcionando todo lo demas
finally:
print("ha finalizado el manejo de excepciones") # cuando ya se arreglo


"""
Dificultad extra
No lo hize yo xd nose nada de python
"""

for number in range (10,56): #toma del 10 al 55
  if number % 2 == 0 and number != 16 and number % 3 != 0:
print(number)
