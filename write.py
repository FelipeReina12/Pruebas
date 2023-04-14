with open('./text.txt', 'w+') as file:      #r+ nos permite ler y escribir
    for line in file:                       #w+ sobre escribe el texto
        print(line)
    file.write('Nuevas cosas en el archivo de texto\n')
    file.write('Otra linea\n')
    file.write('Zeta mago de oz\n')

