
class Queue:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.size = len(self.tab)
        self.safeIndex = 0
        self.readIndex = 0


    def realloc(self, tab, size):
        oldSize = len(tab)
        return [tab[i] if i<oldSize else None  for i in range(size)]


    def is_empty(self):
        if self.safeIndex == self.readIndex:
            return True


    def peek(self):
        if self.safeIndex == self.readIndex:
            return None
        return self.tab[self.readIndex]


    def dequeue(self):
        if self.safeIndex == self.readIndex:
            return None

        else:
            element = self.tab[self.readIndex]
            self.tab[self.readIndex] = None
            self.readIndex += 1
            if self.readIndex > self.size:
                self.readIndex = 0
        return element


    def enqueue(self, data):
        self.tab[self.safeIndex] = data
        self.safeIndex += 1
        

        if self.safeIndex >= self.size:
            old_readIndex = self.readIndex
            self.size = 2 * self.size
            self.tab = self.realloc(self.tab, self.size)
            self.readIndex = old_readIndex


    def __str__(self):
        word = '['
        for i in range(self.readIndex, self.safeIndex + 1):
            if self.tab[i] is not None:
                word += str(self.tab[i]) 
        
        word += ']'
        return word


    def pomoc(self):
        return print(f"{self.tab}")


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]


def main():

    queue = Queue()

    for i in range(1, 5):
        queue.enqueue(i)

    print(queue.dequeue())

    print(queue.peek())
    
    print(queue)

    for i in range(5, 9):
        queue.enqueue(i)

    queue.pomoc()
    
    while queue.readIndex != queue.safeIndex:
        print(queue.dequeue())
    
    print(queue)



if __name__ == '__main__':
    main()