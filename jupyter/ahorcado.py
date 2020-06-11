import random

lista = ['ajo', 'abanico', 'bateria']
objetivo = random.choice(lista)
run = 1
intentos = 10

letrasValidas = 'abcdefghijklmnñopqrstuvwxyz'

banco = ''


def banner():

    print('Te quedan ', intentos, ' intentos.')
    if intentos == 10:
        inicio()
    elif intentos == 9:
        menosNueve()
    elif intentos == 8:
        menosOcho()
    elif intentos == 7:
        menosSiete()
    elif intentos == 6:
        menosSeis()
    elif intentos == 5:
        menosCinco()
    elif intentos == 4:
        menosCuatro()
    elif intentos == 3:
        menosTres()
    elif intentos == 2:
        menosDos()
    elif intentos == 1:
        menosUno()
    else:
        muerto()


p5 = '________'
p4 = '|/  |'
p42 = '|/'
p3 = '|   0'
p32 = '|'
p2 = '|  /|\\'
p23 = '|  /'
p1 = '|  / \\'
base = '|_______'


def muerto():
    print(p5)
    print(p4)
    print(p3)
    print(p2)
    print(p1)
    print(base)


def menosUno():
    print(p5)
    print(p42)
    print(p3)
    print(p2)
    print(p1)
    print(base)


def menosDos():
    print(p5)
    print(p42)
    print(p32)
    print(p2)
    print(p1)
    print(base)


def menosTres():
    print(p5)
    print(p42)
    print(p32)
    print(p1)
    print(p1)
    print(base)


def menosCuatro():
    print(p5)
    print(p42)
    print(p32)
    print(p23)
    print(p1)
    print(base)


def menosCinco():
    print(p5)
    print(p42)
    print(p32)
    print(p32)
    print(p1)
    print(base)


def menosSeis():
    print(p5)
    print(p42)
    print(p32)
    print(p32)
    print(p23)
    print(base)


def menosSiete():
    print(p5)
    print(p42)
    print(p32)
    print(p32)
    print(p32)
    print(base)


def menosOcho():
    print(' ')
    print(p42)
    print(p32)
    print(p32)
    print(p32)
    print(base)


def menosNueve():
    print(' ')
    print(p32)
    print(p32)
    print(p32)
    print(p32)
    print(base)


def inicio():
    print('\n\n\n\n\n', '_'+base[1:])


while run == 1:
    incognita = ""
    letraValida = 0
    intentos = 10
    for letra in objetivo:
        if letra in banco:
            incognita = incognita + letra
        else:
            incognita = incognita + "_ "

    if incognita == objetivo:
        print(incognita)
        print("HAS GANADO")
        again = input('¿Quieres jugar de nuevo? s/n :')

        if again != 's':
            print('\nGracias por jugar.\n... ... ... Saliendo.')
            run = 0

        else:
            print('\n### INICIANDO UNA NUEVA PARTIDA ###')
            objetivo = random.choice(lista)
            intentos = 10
            banco = ''
            incognita = ""
            letraValida = 0

        while letraValida == 0:
            print("Adivina la palabra:", incognita)
            banner()
            prueba = input('\nescoge una letra: ').lower()

            if len(prueba) > 1:
                print('Eso son varias letras... Por favor introduce UNA letra')
            elif len(prueba) < 1:
                print('Introduce por lo menos UNA letra')
            elif prueba in letrasValidas:
                letraValida = 1
                banco = banco + prueba
            elif prueba not in objetivo:
                intentos -= 1
                letraValida = 1
