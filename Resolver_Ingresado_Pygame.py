class RESOLVER_SUDOKU():
    def __init__(self):
        pass

    def crear(self):
        self.TAMAÑO=9
        self.base=[ 
            ]
        
    def ingresar_sudoku(self):
        print("             -----Ingresa los valores del sudoku que deseas resolver-----")
        print("                 -----Debes ingresarlos fila por fila-----")
        print("         -----Debes ingresarlos incluyendo ceros en los espacios vacíos-----")
        print("                 -----Cada valor debe estar separado por una coma -----")

        for x in range(9):
            datos=input("Ingresa los datos de la fila "+str(x+1)+": ")
            filas=datos.split(",")
            cambio_filas=[]
            for a in range(9):
                y=filas[a]
                cambio=int(y)
                cambio_filas.append(cambio)
            self.base.append(cambio_filas)

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

solucion=RESOLVER_SUDOKU()
solucion.crear()
solucion.ingresar_sudoku()
print("---------------------SOLUCIÓN---------------------------------")
if  solucion.solucion_sudoku (): 
    solucion.impresion_sudoku () 
else : 
    print ( "Sin solución" )