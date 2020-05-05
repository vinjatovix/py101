# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# 33.- Expresiones regulares, regex, regexp.
# secuencias de caracteres que buscan por patrón

# (search, findall, split, sub)


# %%
# Para emplearlas tenemos que importar el módulo

import re


# %%
# search()

# Si lo la cadena nos devuelve un objeto del tipo Match
# El span nos indica en que posición de la cadena se encuentra

txt = 'Python 101 me sirve de repaso'

busqueda = re.search('101',txt)

busqueda


# %%
# Si no, no devuelve nada
# ten en cuenta que es Case Sensitive

txt = 'Python 101 me sirve de repaso'

busqueda = re.search('python',txt)

if (busqueda):
    print('Tienes un nuevo Match!')
else:
    print('Sigue buscando campeón')


# %%
# de esta busqueda podemos sacar bastante información

txt = 'Python 101 me sirve de repaso'

busqueda = re.search('101',txt)

print(busqueda.start())
print(busqueda.end())
print(busqueda.span())
print(busqueda.string) 


# %%
# $ busca si coincide el final

txt = 'Python 101 me sirve de repaso'

re.search('repaso$',txt)


# %%
# ^ busca si coincide el principio

txt = 'Python 101 me sirve de repaso'
re.search('^Python',txt)


# %%
# .match() se restringe al inicio del primer string

txt = '''Verde
Verde que te quiero verde.
Verde viento, verdes ramas.
El barco sobre la mar,
el caballo en la montaña.
'''

print(re.match('Verde',txt))


# %%
# en modo MULTILINE .match() solo mirará la primera línea

busqueda = re.match('El',txt,re.MULTILINE)
if (not busqueda):
    print('No hay match')


# %%
# .search() in embargo toma el principio de cada línea

re.search('El',txt,re.MULTILINE)


# %%
# Podemos hacer consultas inclusivas.

# Queremos ver si la cadena tiene me y de sin importar 
# lo que haya entre ellos. Para eso el . nos sirve de comodín
# y el * que puede aparecer 0 o mas veces en el medio

txt = 'Python 101 me sirve de repaso'

re.search('me.*de',txt)


# %%
# .search() tiene un montón de posibilidades
# aquí vemos las principales pero deberías de
# profundizar en https://docs.python.org/


# %%
# split
# divide una cadena a partir de un patrón
# en este caso la referencia es \s que quiere decir espacio
# nos devuelve una lista []

txt = 'Dábale arroz a la zorra el abad'

re.split('\s',txt)


# %%
# sub sustituye todas las coincidencias
# Capital Sensitive

txt = '''Verde
Verde que te quiero verde.
Verde viento, verdes ramas.
El barco sobre la mar,
el caballo en la montaña.
'''

print(re.sub('verde','roja',txt))


# %%
# findall
# busca todas las ocurrencias en la cadena
# nos devuelve una lista []

txt = '''
Python 101 me sirve de repaso.
Los puntos clave de mi estudio los convierto en tarjetas.
Siempre las tengo a mano en el IG de @Vinjadevix.
'''

busqueda = re.findall('de.*',txt)
busqueda


# %%
# Patrones con varios valores, el pipe funciona como OR

txt = 'hola adiós hello bye'

re.findall('hola|hello',txt)


# %%
# Patrones con sintaxis repetida

txt = "addddddios adios aaaaadios aaadio"



def buscar(bp, txt):
    for item in bp:
        print( re.findall(item, txt) )

bp = ['dios', 'aaadios', 'aaaa']
buscar(bp, txt)


# %%
# con meta * definimos ninguna o mas repeticiones 
# a la izd del caracter
 

txt = "addddddios adios aaaaadios aaadio"

bp = ['ad*ios','a*dios']
buscar(bp,txt)


# %%
# con meta + definimos UNA o mas repeticiones 
# a la izd del caracter

txt = "addddddios aios aaaaadios aaadio"

bp = ['ad+ios','a+dios']
buscar(bp,txt)


# %%
# con meta ? UNA o NINGUNA

txt = "addddddios adios aaaaadios aaadio"

bp = ['ad?ios','a?dios']
buscar(bp,txt)


# %%
# si sabemos en mumero concreto de repeticiones
# podemos acotarlo con {n}

txt = "addddddios adios aaaaadios aaadio"

bp = ['ad{6}ios','a{5}dios']
buscar(bp,txt)


# %%
# o un numero de repeticiones en un rango
# {n,m}

txt = "addddddios adios aaaaadios aaadio"

bp = ['ad{1,6}ios','a{1,3}dios']
buscar(bp,txt)


# %%
# podemos crear un patron con un conjunto

txt = "parra perra pirra porra purra parre perre pirre porre purre parri perri pirri porri purri "

bp = ['p[ao]rr[ei]', 'p[eu]rra']
buscar(bp,txt)


# %%
# Exclusion en grupos
# [^] indicamos la busqueda contraria

txt = "parra perra pirra porra purra parre perre pirre porre purre parri perri pirri porri purri "

bp = ['p[^ao]rr[^ei]', 'p[^eu]rra']
buscar(bp,txt)


# %%
# rangos
# [-]
'''
[A-Z]: caracter alfabético en mayúscula
[a-z]: caracter alfabético en minúscula
[A-Za-z]: Cualquier carácter alfabético
[A-z]: Cualquier carácter alfabético
[0-9]: Cualquier carácter numérico 
[a-zA-Z0-9]: Cualquier carácter alfanumérico 

cualquier rango puede ser excluido para conseguir el patrón contrario
'''

txt = "parra p3rr4 pirr4 p0rra purr4 parre p3rr3 pirre porre purre parri perri pirri porri purri "

bp = ['p[0-9]rr[0-9]']
buscar(bp,txt)


# %%
# Códigos escapados \
# tienen un significado único
# por ejemplo

'''
\d	numérico
\D	no numérico
\s	espacio en blanco
\S	no espacio en blanco
\w	alfanumérico
\W	no alfanumérico
'''

# hay que predecirlos con una r

txt = "Python 101 son mis resúmenes de estudio"

bp = [r'\d+', r'\D+', r'\s', r'\S+', r'\w+', r'\W+'] 
print(buscar(bp, txt))


# %%
# https://docs.python.org/3.8/library/re.html

