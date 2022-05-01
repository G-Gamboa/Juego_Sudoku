import random

class GENERAR_SUDOKU():
    def __init__(self):
        pass

    def crear(self):
        self.TAMAÑO=9
        self.base=[ 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ], 
            [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]]
        
#Funciona por el momento, aunque sería bueno buscar alguna mejor manera, pero cumple con el propósito de
#Generar Sudokus aleatorios

    def datos_random(self):
        numeros=[1,2,3,4,5,6,7,8,9]
        for x in range(9):
            random_fila=random.randrange(9)
            random_columna=random.randrange(9)

            aleatorio=random.choice(numeros)

            if self.comprobacion(aleatorio,x,random_columna):
                if self.comprobacion(aleatorio,random_fila,x):
                    self.base[x][random_columna]=aleatorio

            if self.comprobacion(aleatorio,random_fila,x):
                if self.comprobacion(aleatorio,x,random_columna):
                    self.base[random_fila][x]=aleatorio

            numeros.remove(aleatorio)
        
        numeros=[1,2,3,4,5,6,7,8,9]
        for x in range(9):
            random_fila=random.randrange(9)
            random_columna=random.randrange(9)

            aleatorio=random.choice(numeros)

            if self.comprobacion(aleatorio,x,random_columna):
                if self.comprobacion(aleatorio,random_fila,x):
                    self.base[x][random_columna]=aleatorio

            if self.comprobacion(aleatorio,random_fila,x):
                if self.comprobacion(aleatorio,x,random_columna):
                    self.base[random_fila][x]=aleatorio

            numeros.remove(aleatorio)


    def  impresion_sudoku (self): 
        for  i  in  self.base : 
            print  ( i )

    def  asignacion (self, fila , columna ): 
        asignacion_numeros  =  0 
        for  i  in range ( 0 , self.TAMAÑO ): 
            for j  in range  ( 0 , self.TAMAÑO ): 
                
                #Si hay un espacio en blanco acá lo detecta
                if self.base [ i ] [ j ]  ==  0 : 
                    fila =  i 
                    columna  =  j 
                    asignacion_numeros  =  1 
                    a  =  [ fila ,  columna ,  asignacion_numeros ] 
                    return  a 
        a  =  [ - 1 ,  - 1 ,  asignacion_numeros ] 
        return  a 


    def  comprobacion (self, n ,  f ,  c ): 
        #Comprueba la fila
        for  i  in range ( 0 , self.TAMAÑO ): 
            #Si hay una celda con el mismo valor retorna Falso 
            if self.base [ f ] [ i ]  ==  n : 
                return  False 
        #Comprueba las columnas
        for  i  in range ( 0 , self.TAMAÑO ): 
            #Si hay una celda con el mismo valor retorna Falso 
            if  self.base [ i ] [ c ]  ==  n : 
                return  False 

        sub_fila  =  ( f // 3 ) * 3 
        sub_columna  =  ( c// 3 ) * 3 ; 
        #Comprueba que los valores no se repitan en los espacios 3x3
        for  i  in range ( sub_fila , sub_fila + 3 ): 
            for  j  in range ( sub_columna , sub_columna + 3 ): 
                if  self.base [ i ] [ j ] == n : 
                    return  False 
        return  True

    def  solucion_sudoku (self): 
        fil  =  0 
        col  =  0 
        #SI en este punto cada punto tiene un valor asignado significa que pasó todas las comprobaciones
        a  =  self.asignacion ( fil ,  col ) 
        if  a [ 2 ]  ==  0 : 
            return  True 
        #Ubica la fila y columa en la que se encuentra un número cero
        fil  =  a [ 0 ] 
        col  =  a [ 1 ]
    
        for  i  in range ( 1 , 10 ): 
            if self.comprobacion ( i ,  fil ,  col ): 
                self.base [ fil ] [ col ]  =  i 
                #regreso 
                if  self.solucion_sudoku(): 
                    return  True 
                self.base [ fil ] [ col ] = 0
        return  False

#-----------------------------PARTE CENTRAL---------------------------

solucion=GENERAR_SUDOKU()
solucion.crear()
solucion.datos_random()
solucion.impresion_sudoku()
print("---------------------SOLUCIÓN---------------------------------")
if  solucion.solucion_sudoku (): 
    solucion.impresion_sudoku () 
else : 
    print("Sin solución")