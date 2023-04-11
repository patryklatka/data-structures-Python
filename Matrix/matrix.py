class Matrix:
    def __init__(self, dim, value=0):
        if isinstance(dim, tuple):
            self.matrix = list()
            self.rows = dim[0]
            self.cols = dim[1]
            for i in range(self.rows):
                self.matrix.append([])
                for j in range(self.cols):
                    self.matrix[i].insert(j, value)
            
        else:
            self.matrix = dim
            self.rows = len(dim)
            self.cols = len(dim[0])

    def __add__(self, other):
        if self.size() != other.size():
            return None
        else:
            self.SumMatrix = Matrix((self.size()))
            for i in range(self.rows):
                for j in range(self.cols):
                    self.SumMatrix[i][j] += self.matrix[i][j] + other[i][j]
            return self.SumMatrix
        

    def __mul__(self, other):
        if self.rows != other.cols:
            return None

        else:
            self.MulMatrix = Matrix((self.rows, other.cols))
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        self.MulMatrix[i][j] += self.matrix[i][k] * other[k][j]
            return self.MulMatrix

    def __getitem__(self, item):
        return self.matrix[item]


    def __str__(self):
        word = ''
        for row in range(self.rows):
            word += str(self.matrix[row])
            if row < self.rows - 1:
                word += '\n'
        return word
    

    def size(self):
        return (self.rows, self.cols)


def transpose_matrix(matrix):
    TransMatrix = Matrix((matrix.cols, matrix.rows))

    for i in range(matrix.rows):
        for j in range(matrix.cols):
            TransMatrix[j][i] = matrix[i][j]
    return TransMatrix



def main():
    m1 = Matrix([[1, 0, 2],
                [-1, 3, 1]])

    m2 = Matrix((2, 3), value=1)
    
    m3 = Matrix([[3, 1],
                [2, 1],
                [1, 0]])
    
    print(f'transpozycja macierzy \n{transpose_matrix(m1)}')
    print(f'suma macierzy \n{m1+m2}')
    print(f'iloczyn macierzy \n{m1*m3}')


if __name__ == '__main__':
    main()