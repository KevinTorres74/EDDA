import random

# Representa un nodo en el Treap.
class TreapNode:
    def __init__(self, value):
        self.value = value
        self.priority = random.random()
        self.left = None
        self.right = None

class TreapList:
    def __init__(self):
        self.root = None

    # Devuelve el valor en el índice i en el Treap.
    def get(self, i):
        return self._get_node(i, self.root).value

    # Establece el valor en el índice i en x.
    def set(self, i, x):
        node = self._get_node(i, self.root)
        node.value = x

    # Inserta un nuevo nodo con el valor x en el índice i.
    def add(self, i, x):
        new_node = TreapNode(x)
        left, right = self._split(i, self.root)
        self.root = self._merge(self._merge(left, new_node), right)

    # Quita el nodo en el índice i.
    def remove(self, i):
        left, right = self._split(i, self.root)
        _, right = self._split(1, right)
        self.root = self._merge(left, right)

    # Busca recursivamente el nodo en el índice i en el Treap.
    def _get_node(self, i, node):
        if node is None:
            raise IndexError("Índice fuera de rango")
        left_size = self._size(node.left)
        if i < left_size:
            return self._get_node(i, node.left)
        elif i > left_size:
            return self._get_node(i - left_size - 1, node.right)
        else:
            return node

    # Devuelve el tamaño del Treap rooteado en el nodo.
    def _size(self, node):
        if node is None:
            return 0
        return 1 + self._size(node.left) + self._size(node.right)

    # Divide la Treap enraizada en el nodo en dos Treaps en el índice i.
    def _split(self, i, node):
        if node is None:
            return None, None
        left_size = self._size(node.left)
        if i <= left_size:
            left, right = self._split(i, node.left)
            node.left = right
            return left, node
        else:
            left, right = self._split(i - left_size - 1, node.right)
            node.right = left
            return node, right

    # Combina dos Treaps izquierda y derecha en uno solo.
    def _merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            return left
        else:
            right.left = self._merge(left, right.left)
            return right
        
# Creación de un nuevo objeto TreapList
treap_list = TreapList()

# Agrega elementos en la lista
treap_list.add(0, 10)
treap_list.add(1, 20)
treap_list.add(2, 30)

# Obtener el valor en el índice 1
value = treap_list.get(1)
print("Evalua para el elemento del indice 1:")
print(value)  # Salida: 20

# Establece el valor en el índice 2
treap_list.set(2, 40)

# Eliminar un elemento de la lista
treap_list.remove(0)

# Obtener el valor actualizado en el índice 0
value = treap_list.get(0)
print("Evalua para el elemento del indice 0:")
print(value)  # Salida: 20
