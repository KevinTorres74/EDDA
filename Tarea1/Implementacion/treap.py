import random

# Representa un nodo en el Treap.
class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None
        self.size = 1
        
class Treap:
    def __init__(self):
        self.root = None
        
    # Función auxiliar para obtener el tamaño de un nodo
    def get_size(self, node):
        if node is None:
            return 0
        return node.size
    
    # Función auxiliar para actualizar el tamaño de un nodo
    def update_size(self, node):
        if node is None:
            return
        node.size = self.get_size(node.left) + self.get_size(node.right) + 1
        
    # Función auxiliar para rotar a la izquierda
    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_size(node)
        self.update_size(new_root)
        return new_root
    
    # Función auxiliar para rotar a la derecha
    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_size(node)
        self.update_size(new_root)
        return new_root
    
    # Función auxiliar para insertar un nodo en el Treap
    def insert_node(self, node, key):
        if node is None:
            return TreapNode(key)
        
        if key < node.key:
            node.left = self.insert_node(node.left, key)
            if node.left.priority > node.priority:
                node = self.rotate_right(node)
        else:
            node.right = self.insert_node(node.right, key)
            if node.right.priority > node.priority:
                node = self.rotate_left(node)
        
        self.update_size(node)
        return node
    
    # Función para insertar una llave en el Treap
    def insert(self, key):
        self.root = self.insert_node(self.root, key)
    
    # Función auxiliar para obtener la llave con rank i
    def get_rank_node(self, node, i):
        if node is None:
            return None
        
        left_size = self.get_size(node.left)
        
        if i == left_size:
            return node.key
        elif i < left_size:
            return self.get_rank_node(node.left, i)
        else:
            return self.get_rank_node(node.right, i - left_size - 1)
    
    # Función para obtener la llave con rank i en el Treap
    def get(self, i):
        return self.get_rank_node(self.root, i)


# Ejemplo de uso
treap = Treap()
treap.insert(5)
treap.insert(3)
treap.insert(7)
treap.insert(1)
treap.insert(4)
treap.insert(6)
treap.insert(9)

print(treap.get(0))  # Salida: 1
print(treap.get(3))  # Salida: 5
print(treap.get(6))  # Salida: 9
