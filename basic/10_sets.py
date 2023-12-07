# Escribiendo código con ❤️
# Sets

# Definición
my_set = set()
my_other_set = {}

# print(type(my_set)) => <class 'set'>
# print(type(my_other_set))  => <class 'dict'> Inicialmente es un diccionario

my_other_set = {"Ramón", "Gómez", 41}
# print(type(my_other_set)) => <class 'set'> Ahora es un set

print(len(my_other_set))

# Inserción
my_other_set.add("ramongmz_")

print(my_other_set)  # No es una estructura ordenada
my_other_set.add("ramongmz_")  # No admite repetidos

print(my_other_set)

# Búsqueda
print("Ramón" in my_other_set)
print("Ray" in my_other_set)

# Eliminación
my_other_set.remove("Ramón")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined

# Transformación
my_set = {"Ramón", "Gómez", 41}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Java", "HTML", "Python"}

# Otras operaciones
my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))
print(my_new_set.difference(my_set))