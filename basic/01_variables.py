# Variables

my_string_variable = "Mi variable de tipo String"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

"""
¿Se puede cambiar el tipo de una variable? Sí
Por ejemplo, 'my_int_variable' es de tipo 'int'
y la vamos a convertir en 'string' sin función,
simplemente añadiendo comillas
"""
print("Mi variable", my_int_variable, "es de tipo:", type(my_int_variable))

my_int_variable = "5" #Cambio de int a str
print("Ahora mi variable de tipo int se ha convertido en:", type(my_int_variable))

my_bool_variable = False
print("Mi variable booleana es:", my_bool_variable)

# Concatenacion de variables en un print
print(my_string_variable, my_int_variable, my_bool_variable)

# Para contar caracteres en el caso de las variables se utiliza len()
print(my_string_variable, "tiene" ,len(my_string_variable), "caracteres")

"""
Aunque no es recomendable abusar de este tipo de sintaxis, 
se pueden definir varias variables en una sola línea
"""
name, surname, alias, age = "Ramón", "Gómez", 'Keler', 40
print("Mi nombre es", name, surname, "tengo",
      age, "años y mi nick siempre ha sido", alias)

# Inputs por consola, poco habituales, pero existen
input_name = input('¿Como te llamas? ')
input_nick = input('¿Cual es tu nick? ')
print("Hola", input_name, "AKA", input_nick)

'''
Aunque declaremos una variable de un tipo específico,
no quiere decir que sea inmutable. En este caso, declaramos
adress como "str", y al final pasa por varios tipos
convirtiéndose sin problema'''
adress: str = "Dirección"
address = True
address = 5
address = 1.2
print("La variable adress comenzó como un 'str' y ahora es", type(address))