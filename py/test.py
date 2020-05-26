class Node(object):
    ''' esta clase define como son los nodos'''
    
    def __init__( self, d, n=None ):
        ''' cada nodo tiene dos partes, una parte con los datos y otra que indica cual es el siguiente nodo'''
        self.data = d
        self.next_node = n
        
    def get_next( self ):
        ''' retorna el siguiente nodo'''
        return self.next_node
    
    def set_next( self, n ):
        ''' fijamos el siguiente nodo'''
        self.next_node = n
        
    def set_data( self, d ):
        ''' asignamos datos al nodo'''
        self.data = d
     
        
        
        
        
class LinkedList(object):
    ''' esta clase linkeara las listas con los objetos'''
    
    def __init__(self, r = None):
        ''' r es el primer nodo, size indica la cantidad de nodos que tenemos linkados'''
        self.root = r
        self.size = 0
        
    def get_size(self):
        ''' retorna la cantidad total de nodos'''
        return self.size
    
    def add(self,d):
        ''' con esto creamos un nuevo nodo, el argumento d son los datos que queremos añadir '''
        new_node = Node (d, self.root)
        self.root = new_node
        self.size +=1
    
    def remove(self,d):
        ''' con esto borramos un nodo, el argumento d son los datos que queremos borrar '''
        this_node = self.root
        prev_node = None
        
        while this_node:                                                # mientras que este modo:
            if this_node.get_data() == d:                               # Sea el que tiene los datos
                
                if prev_node:                                               # si no es el primer nodo
                    prev_node.set_next(this_node.get_next())                # tenemos que relinkar el anterior y el siguiente
                
                else:                                                       # en el caso de que sea el primer nodo,       
                    self.root = this_node.get_next()                        # tenemos que asignar el siguiente como nodo raiz
                    
                self.size -= 1                                          # restamos uno a la cantidad de nodos
                return True                                             
            
            else:                                                       # En caso de que no sean los datos que buscamos
                prev_node = this_node                                   # marcamos este modo como que es el anterior
                this_node = this_node.get_next()                        # y el siguiente modulo como el actual
        return False 

            
    
lista = LinkedList()    

lista.add(5)
print(lista)