# pydoc
class Saludos:
    """
    Esta clase tiene dos funciones, Hola y Adios.
    Ambas reciben como parámetro un nombre
    """
    def hola(self,nombre):
        ''' Esta funcion saluda '''
        print(f'Hola {nombre}')
        
    def adios(self, nombre):
        ''' Esta funcion se despide'''
        print(f'Adios {nombre}')