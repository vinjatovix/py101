# Docstrings - cadenas para documentacion
class Galleta:
    '''La clase galleta tiene dos métodos.
    El primero sirve para inicializar el objeto.
    Con el segundo comeríamos la galleta'''

    def __init__(self, sabor, efecto):
        '''Este método nos sirve para inicializar el objeto cuando lo creamos.
        Necesitamos enviar dos argumentos para ello. (sabor,efecto)'''
        self.sabor = sabor
        self.efecto = efecto

    def comer(self):
        '''Con este método comemos la galleta'''
        print('Comiste una galleta de {} y recuperaste {} puntos'.format(
            self.sabor, self.efecto))
