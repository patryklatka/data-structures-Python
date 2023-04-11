class NoPlaceError(Exception):
    pass


class NoDataError(Exception):
    pass


class Elem:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2
        self.size = size


    def collision(self, AddData):
        if isinstance(AddData.key, str):
            suma = sum([ord(i) for i in AddData.key])
            key = suma      

        i = 1

        while self.tab[(self.hash(AddData.key) + self.c1 * i + self.c2 * i**2) % self.size] is not None:
            i += 1
            if i > self.size:
                raise NoPlaceError('Brak Miejsca')
        else:
            self.tab[(self.hash(AddData.key) + self.c1 * i + self.c2 * i**2) % self.size] = AddData
            return

            
    def hash(self, key):
        if isinstance(key, str):
            suma = sum([ord(i) for i in key])
            key = suma

        modulo = key % self.size
        return modulo



    def search(self, key):
        index = self.hash(key)
        if self.tab[index] is not None: 
            if self.tab[index].key == key:
                return self.tab[index].data
            else:
                for index in range(self.size):
                    if self.tab[index] is not None: 
                        if self.tab[index].key == key:
                            return self.tab[index].data 

        elif self.tab[index] is None: 
            for index in range(self.size):
                if self.tab[index] is not None: 
                    if self.tab[index].key == key:
                        return self.tab[index].data 



    def insert(self, AddData): 
        index = self.hash(AddData.key)
        if self.tab[index] is None or AddData.key == self.tab[index].key:
            self.tab[index] = AddData
            return

        self.collision(AddData)


    def remove(self, key):  
        index = self.hash(key)
        if self.tab[index] is None:
            raise NoDataError("Brak Danej")
            return None
        else:
            self.tab[index] = None
        pass


    def __str__(self):
        word = '{'
        for elem in self.tab:
            if elem is None:
                word += 'None, '
            else:
                word += f'{elem.key}: {elem.data}, '
        word = word[0:-2]
        word += '}'
        return word


def main():

    def first_function(size, c1=1 , c2=0):
        hashtable = HashTable(size, c1, c2)

        ValueList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 'N']
        KeyList = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14]

        try:
            for index, value in enumerate(ValueList):
                hashtable.insert(Elem(KeyList[index], value))
        except NoPlaceError:
            print('Brak Miejsca')
            pass


        print(hashtable)
        
        print(hashtable.search(5))  
        
        print(hashtable.search(14))

        hashtable.insert(Elem(5, 'Z'))

        print(hashtable.search(5))

        hashtable.remove(5)

        print(hashtable)

        print(hashtable.search(31))
        
        hashtable.insert(Elem('test', 'W'))

        print(hashtable)

    first_function(13)

if __name__ == '__main__':
    main()
