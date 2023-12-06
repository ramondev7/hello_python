name = 'Ramón Gómez'
words = name.split(' ') 
character = ''

for word in words:
   character += word[0]

print(character)