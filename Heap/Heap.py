class Element:
    def __init__(self, data, priorytet):
        self.data = data
        self.priorytet = priorytet

    def __lt__(self, other):
        if self.priorytet < other.priorytet:
            return True

    def __gt__(self, other):
        if self.priorytet > other.priorytet:
            return True

    def __str__(self):
        return f"{self.priorytet} : {self.data}"


class Heap:
    def __init__(self):
        self.tab = []
        self.heapSize = 0

    def is_empty(self):
        if len(self.tab) == 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            return None

        else:
            return self.tab[0]


    def dequeue(self):
        if self.is_empty():
            return None

        root = self.tab[0]

        self.tab[0], self.tab[self.heapSize - 1] = self.tab[self.heapSize - 1], self.tab[0]

        leftIndex = self.left(0)
        rightIndex = self.right(0)

        while self.tab[leftIndex] > self.tab[0] or self.tab[rightIndex] > self.tab[0]:

            if self.tab[leftIndex] > self.tab[0]:
                self.tab[0], self.tab[leftIndex] = self.tab[leftIndex], self.tab[0]
                leftIndex = self.left(0)
                rightIndex = self.right(0)

            if self.tab[rightIndex] > self.tab[0]:
                self.tab[0], self.tab[rightIndex] = self.tab[rightIndex], self.tab[0]
                leftIndex = self.left(0)
                rightIndex = self.right(0)
        self.heapSize -= 1

        return root

    def enqueue(self, element):
        if self.heapSize == len(self.tab):
            self.tab.append(element)
            self.heapSize += 1

        else:
            self.tab[self.heapSize] = element
            self.heapSize += 1
            
        elementIndex = self.heapSize - 1
        parentIndex = self.parent(elementIndex)

        if parentIndex < 0:
            parentIndex = 0
        
        
        while self.tab[parentIndex] < self.tab[elementIndex]:
            self.tab[elementIndex], self.tab[parentIndex] = self.tab[parentIndex], self.tab[elementIndex]
            elementIndex = parentIndex
            parentIndex = self.parent(parentIndex)
            if parentIndex < 0:
                parentIndex = 0


    def left(self, nodeIndex):
        return 2 * nodeIndex + 1

    def right(self, nodeIndex):
        return 2 * nodeIndex + 2

    def parent(self, nodeIndex):
        return (nodeIndex - 1) // 2







    def print_tab(self):
        print ('{', end=' ')
        print(*self.tab[:self.heapSize], sep=', ', end = ' ')
        print( '}')

    def print_tree(self, idx, lvl):
        if idx<self.heapSize:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)


def main():
    heap = Heap()

    priorityList = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    valueList = "GRYMOTYLA"

    for i in range(len(valueList)):
        heap.enqueue(Element(valueList[i], priorityList[i]))
    
    heap.print_tree(0,0)

    heap.print_tab()

    firstElement = heap.dequeue()

    print(heap.peek())

    heap.print_tab()

    print(firstElement)



if __name__ == '__main__':
    main()