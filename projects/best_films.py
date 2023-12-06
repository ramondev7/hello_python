# Escribiendo código con ❤️
# Lista ordenada con las 'mejores' películas

best_films = list()
best_films = ['Oppenheimer', 'Agente Stone', 'Gran Turismo', 'Blue Beetle', 'Barbie']

best_films.append('Warcraft')
best_films.insert(0, 'The Godfather')

best_films.remove('Barbie')

best_films.sort()

    
for i in best_films:
    print(i)
    