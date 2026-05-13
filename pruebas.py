class RESOLVER_SUDOKU():
    def __init__(self):
        pass

    def crear(self):
        self.TAMAÑO = 9
        self.base = [
            [6, 5, 0, 8, 7, 3, 0, 9, 0],
            [0, 0, 3, 2, 5, 0, 0, 0, 8],
            [9, 8, 0, 1, 0, 4, 3, 5, 7],
            [1, 0, 5, 0, 0, 0, 0, 0, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 5, 0, 3],
            [5, 7, 8, 3, 0, 1, 0, 2, 6],
            [2, 0, 0, 0, 4, 8, 9, 0, 0],
            [0, 9, 0, 6, 2, 5, 0, 8, 1]
        ]

    def impresion_sudoku(self):
        for i in self.base:
            print(i)

    def asignacion(self, fila, columna):
        asignacion_numeros = 0
        for i in range(0, self.TAMAÑO):
            for j in range(0, self.TAMAÑO):
                if self.base[i][j] == 0:
                    fila = i
                    columna = j
                    asignacion_numeros = 1
                    a = [fila, columna, asignacion_numeros]
                    return a
        a = [-1, -1, asignacion_numeros]
        return a

    def comprobacion(self, n, f, c):
        for i in range(0, self.TAMAÑO):
            if self.base[f][i] == n:
                return False
        for i in range(0, self.TAMAÑO):
            if self.base[i][c] == n:
                return False

        sub_fila = (f // 3) * 3
        sub_columna = (c // 3) * 3
        for i in range(sub_fila, sub_fila + 3):
            for j in range(sub_columna, sub_columna + 3):
                if self.base[i][j] == n:
                    return False
        return True

    def solucion_sudoku(self):
        fil = 0
        col = 0
        a = self.asignacion(fil, col)
        if a[2] == 0:
            return True
        fil = a[0]
        col = a[1]

        for i in range(1, 10):
            if self.comprobacion(i, fil, col):
                self.base[fil][col] = i
                if self.solucion_sudoku():
                    return True
                self.base[fil][col] = 0
        return False


solucion = RESOLVER_SUDOKU()
solucion.crear()
print("---------------------SOLUCIÓN---------------------------------")
if solucion.solucion_sudoku():
    solucion.impresion_sudoku()
else:
    print("Sin solución")
