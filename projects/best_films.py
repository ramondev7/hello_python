# Escribiendo código con ❤️
# Lista con las 'mejores' películas

best_films = list()
best_films = ['Oppenheimer', 'Agente Stone', 'Gran Turismo', 'Blue Beetle', 'Barbie']

best_films.append('Warcraft')
best_films.insert(0, 'The Godfather')

best_films.remove('Barbie')

for film in range(len(best_films)):
    print (best_films[film])