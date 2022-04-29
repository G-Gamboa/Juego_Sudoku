
TAMAÑO  =  9 

#Creamos una matriz de ejemplo para resolver.
base  =  [ 
    [ 6 , 5 , 0 , 8 , 7 , 3 , 0 , 9 , 0 ], 
    [ 0 , 0 , 3 , 2 , 5 , 0 , 0 , 0 , 8 ], 
    [ 9 , 8 , 0 , 1 , 0 ,4 , 3 , 5 , 7 ], 
    [ 1 , 0 , 5 , 0 , 0 , 0 , 0 , 0 , 0 ], 
    [ 4 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 2 ], 
    [ 0 , 0 , 0 , 0 , 0 , 0 , 5 ,0 , 3 ], 
    [ 5 , 7 , 8 , 3 , 0 , 1 , 0 , 2 , 6 ], 
    [ 2 , 0 , 0 , 0 , 4 , 8 , 9 , 0 , 0 ], 
    [ 0 , 9 , 0 , 6 , 2 , 5 , 0 , 8 , 1 ]]

#Coloca el sudoku de línea en línea
def  impresion_sudoku (): 
    for  i  in  base : 
        print  ( i )

#Asigna valores a los espacios que se encuentran en blanco
def  asignacion ( fila ,  columna ): 
    asignacion_numeros  =  0 
    for  i  in range ( 0 , TAMAÑO ): 
        for j  in range  ( 0 , TAMAÑO ): 
            
            #Si hay un espacio en blanco acá lo detecta
            if base [ i ] [ j ]  ==  0 : 
                fila =  i 
                columna  =  j 
                asignacion_numeros  =  1 
                a  =  [ fila ,  columna ,  asignacion_numeros ] 
                return  a 
    a  =  [ - 1 ,  - 1 ,  asignacion_numeros ] 
    return  a 
  
#Comprueba que el valor n no se repita
def  comprobacion ( n ,  r ,  c ): 
    #Comprueba la fila
    for  i  in range ( 0 ,TAMAÑO ): 
        #Si hay una celda con el mismo valor retorna Falso 
        if base [ r ] [ i ]  ==  n : 
            return  False 
    #Comprueba las columnas
    for  i  in range ( 0 , TAMAÑO ): 
        #Si hay una celda con el mismo valor retorna Falso 
        if  base [ i ] [ c ]  ==  n : 
            return  False 
    
    sub_fila  =  ( r // 3 ) * 3 
    sub_columna  =  ( c// 3 ) * 3 ; 
    #Comprueba que los valores no se repitan en los espacios 3x3
    for  i  in range ( sub_fila , sub_fila + 3 ): 
        for  j  in range ( sub_columna , sub_columna + 3 ): 
            if  base [ i ] [ j ] == n : 
                return  False 
    return  True

#Resolución del sudokus
def  solucion_sudoku (): 
    fil  =  0 
    col  =  0 
    #SI en este punto cada punto tiene un valor asignado significa que pasó todas las comprobaciones
    a  =  asignacion ( fil ,  col ) 
    if  a [ 2 ]  ==  0 : 
        return  True 
    fil  =  a [ 0 ] 
    col  =  a [ 1 ]
  
    for  i  in range ( 1 , 10 ): 
        if comprobacion ( i ,  fil ,  col ): 
            base [ fil ] [ col ]  =  i 
            #regreso 
            if  solucion_sudoku (): 
                return  True 
            base [ fil ] [ col ] = 0
    return  False
if  solucion_sudoku (): 
    impresion_sudoku () 
else : 
    print ( "Sin solución" )


