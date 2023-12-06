# Escribiendo código con ❤️
# Strings

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea" # Salto de línea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación" # Tabulacion
print(my_tab_string)

# Formateo
name, surname, country, age = "Ramón", "Gómez", "España", 40
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s, soy de %s y mi edad es %d" % (name, surname, country, age)) # %s para String, %d para int
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

'''
La forma mas simplificada la siguiente, añadiendo una 'f' delante de la cadena
y añadiendo las variables {}
'''
print(f"Mi nombre es {name} {surname}, soy de {country} y tengo {age} años")

# Desempaqueado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje
print(language.capitalize()) # Python
print(language.upper()) # PYTHON
print(language.count("t")) # 1
print(language.isnumeric()) # False
print("1".isnumeric()) # True
print(language.lower()) # python
print(language.lower().isupper()) # False
print(language.startswith("Py")) # False
print("Py" == "py")  # False