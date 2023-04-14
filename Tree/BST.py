class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    

    def search(self, key, currentNode = None):
        if currentNode is None:
            currentNode = self.root

        if currentNode is None:
            return None

        if currentNode.key == key:
            return currentNode.value
        
        if key < currentNode.key:
            return self.search(key, currentNode.left)
        
        if key > currentNode.key:
            return self.search(key, currentNode.right)

    
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            return
        else:
            self.root = self.__insertRecu(key, value, self.root)
            return


    def __insertRecu(self, key, value, parentNode):
        if parentNode is None:
            return Node(key, value)
        
        if key < parentNode.key:
            parentNode.left = self.__insertRecu(key, value, parentNode.left)
            return parentNode
        
        elif key > parentNode.key:
            parentNode.right = self.__insertRecu(key, value, parentNode.right)
            return parentNode

        else:
            parentNode.value = value
            return parentNode


    def delete(self, key, currentNode = None):
        if currentNode is None:
            currentNode = self.root
        
        if currentNode is None:
            return None
        
        if key < currentNode.key:
            currentNode.left = self.delete(key, currentNode.left)
            return currentNode
        
        if key > currentNode.key:
            currentNode.right = self.delete(key, currentNode.right)
            return currentNode
        
        if key == currentNode.key:

            if currentNode.left is None and currentNode.right is None:
                return None

            if currentNode.left is None and currentNode.right is not None:
                return currentNode.right

            if currentNode.left is not None and currentNode.right is None:
                return currentNode.left

            else:
                deleteNode = currentNode
                succesorNode = currentNode.right

                while succesorNode.left is not None:
                    succesorNode = succesorNode.left
                
                currentNode.key = succesorNode.key
                currentNode.value = succesorNode.value

                currentNode.right = self.delete(succesorNode.key, currentNode.right)

            return currentNode


    def print(self, node):
        if node is not None:
            self.print(node.left)
            print(node.key, node.value, end=',')
            self.print(node.right)


    def height(self):
        if self.root is None:
            return 0
        else:
            return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return 0

        else:
            on_left = self.__height(node.left)
            on_right = self.__height(node.right)
            return max(on_left, on_right) + 1


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


def main():
    treeBST = BST()

    keys = [50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24]

    value = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

    for i in range(len(keys)):
        treeBST.insert(keys[i], value[i])

    treeBST.print_tree()

    treeBST.print(treeBST.root)
    print()

    print(treeBST.search(24))

    treeBST.insert(20, 'AA')
    treeBST.insert(6, 'M')

    treeBST.delete(62)

    treeBST.insert(59, 'N')
    treeBST.insert(100, 'P')

    treeBST.delete(8)
    treeBST.delete(15)

    treeBST.insert(55, 'R')

    treeBST.delete(50)
    treeBST.delete(5)
    treeBST.delete(24)

    print(treeBST.height())

    treeBST.print(treeBST.root)

    print()
    
    treeBST.print_tree()


if __name__ == '__main__':
    main()