class Node:
    def __init__(self, key, value, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None


    def search(self, key):
        return self.__searchRecu(key, self.root)

    
    def __searchRecu(self, key, currentNode):
        if currentNode is None:
            return None

        if key > currentNode.key:
            return self.__searchRecu(key, currentNode.right)

        if key < currentNode.key:
            return self.__searchRecu(key, currentNode.left)
        
        else:
            return currentNode.value


    def insert(self, key, value):
        self.root = self.__insert(key, value, self.root)


    def __insert(self, key, value, parentNode):
        if parentNode is None:
            return Node(key, value)

        if key < parentNode.key:
            parentNode.left = self.__insert(key, value, parentNode.left)
            return parentNode
        
        if key > parentNode.key:
            parentNode.right = self.__insert(key, value, parentNode.right)    
            return parentNode   
        
        else:
            parentNode.value = value
            return parentNode


    def delete(self, key):
        self.__delete(key, self.root)


    def __delete(self, key, node):
        if node is None:
            return None

        if node.key > key:
            node.left = self.__delete(key, node.left)
            return node

        elif node.key < key:
            node.right = self.__delete(key, node.right)
            return node

        if node.left is None and node.right is None:
            return None

        elif node.left is None and node.right is not None:
            return node.right

        elif node.right is None and node.left is not None:
            return node.left

        else:
            parents = node
            successor = node.right

            while successor.left is not None:
                parents = successor
                successor = successor.left

            if parents != node:
                parents.left = successor.right

            else:
                parents.right = successor.right
            node.key = successor.key

            return node


    def height(self, node):
        if node is None:
            return 0
        else:
            left_ = self.height(node.left)
            right_ = self.height(node.right)
            return 1 + max(left_, right_)


    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")


    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)


    def tree_list(self, node):
        if node is not None:
            self.tree_list(node.left)
            print(node.key, node.value, end=',')
            self.tree_list(node.right)






def main():
    bst = BST()
    keys = [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]
    value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    for i in range(len(keys)):
        bst.insert(keys[i], value[i])
    bst.print_tree()
    bst.tree_list(bst.root)
    print()
    print(bst.search(24))
    bst.insert(20, 'AA')
    bst.insert(6, 'M')
    bst.delete(62)
    bst.insert(59, 'N')
    bst.insert(100, 'P')
    bst.delete(8)
    bst.delete(15)
    bst.insert(55, 'R')
    bst.delete(50)
    bst.delete(5)
    bst.delete(24)
    print(bst.height(bst.root))
    bst.tree_list(bst.root)
    print()
    bst.print_tree()


if __name__ == '__main__':
    main()