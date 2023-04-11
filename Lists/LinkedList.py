class Elem:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, AddData):
        if self.head is None:
            self.head = AddData
            return

        AddData.next = self.head
        self.head = AddData

           

    def append(self, AddData):
        if self.head is None:
            self.head = AddData
            return

        pointer = self.head
        while pointer.next is not None:
            pointer = pointer.next

        
        pointer.next = AddData
        return
        

    def remove(self):
        if self.head is not None:
            self.head = self.head.next


    def remove_end(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return

        pointer = self.head

        while pointer.next.next is not None:
            pointer = pointer.next
        pointer.next = None

    def is_empty(self):
        if self.head is None:
            return True

    def length(self):
        len = 0
        if self.head is not None:
            pointer = self.head
            while pointer.next is not None:
                len += 1
                pointer = pointer.next
            return len+1
        else:
            return 0

    def get(self):
        return self.head.data


    def print(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next


def main():
    list_universities = [('AGH', 'Kraków', 1919),
                        ('UJ', 'Kraków', 1364),
                        ('PW', 'Warszawa', 1915),
                        ('UW', 'Warszawa', 1915),
                        ('UP', 'Poznań', 1919),
                        ('PG', 'Gdańsk', 1945)]
    
    uczelnie = LinkedList()

    uczelnie.append(Elem(list_universities[0]))
    uczelnie.append(Elem(list_universities[1]))
    uczelnie.append(Elem(list_universities[2]))

    uczelnie.add(Elem(list_universities[3]))
    uczelnie.add(Elem(list_universities[4]))
    uczelnie.add(Elem(list_universities[5]))

    uczelnie.print()

    print(uczelnie.length())

    uczelnie.remove()

    print(uczelnie.get())

    uczelnie.remove_end()

    uczelnie.print()

    uczelnie.destroy()

    print(uczelnie.is_empty())

    uczelnie.remove()

    uczelnie.append(Elem(list_universities[0]))

    uczelnie.remove_end()



if __name__ == '__main__':
    main()