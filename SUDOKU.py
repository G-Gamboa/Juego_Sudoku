import pygame
import random
pygame.init()
class DISEÑO():
    def __init__(self):
        pass

    def variables_fijas(self):
        pygame.font.init()
        self.rojo=(255,0,0)
        self.blanco=(255,255,255)
        self.negro=(0,0,0)
        self.celeste=(92,222,220)
        self.tamaño_pantalla=(550,650)
        self.fuente_numeros=pygame.font.SysFont("Cooper",40)
        self.fuentes_textos=pygame.font.SysFont("Arial",60)
        self.tamaño=9
        self.x=0
        self.y=0
        self.valores=0
        self.espacios=self.tamaño_pantalla[0]/self.tamaño
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

    def coordenadas(self,pos):
        global x
        x = pos[0]//self.espacios
        self.x=x
        global y
        y = pos[1]//self.espacios
        self.y=y

    def fondo_pantalla(self):
        self.pantalla=pygame.display.set_mode(self.tamaño_pantalla)
        pygame.display.set_caption("JUEGO SUDOKU")
        
    def casillas(self):
        for i in range(2):
            
            limites=self.tamaño_pantalla[0]-40
            separacion=(limites)/9
        
            pygame.draw.line(self.pantalla, self.rojo, (self.x * separacion+20-3, (self.y + i)*separacion+20), (self.x * separacion+20+ separacion + 3, (self.y + i)*separacion+20), 7)
            pygame.draw.line(self.pantalla, self.rojo, ( (self.x + i)* separacion+20, self.y * separacion+20), ((self.x + i) * separacion+20	, self.y * separacion+20 + separacion), 7)
    def marco(self):
        grosor=8
        limites=self.tamaño_pantalla[0]-40
        separacion=(limites)/9

        for i in range(10):
            if i % 3 == 0 :
                grosor = 8
            else:
                grosor = 2

            #FALTA HACER QUE EL CUADRO QUEDE EXACTO EN AMBOS BORDES
            pygame.draw.line(self.pantalla, self.negro, (20, i * separacion+20), (limites+20, i * separacion+20), grosor)
            pygame.draw.line(self.pantalla, self.negro, (i * separacion+20, 20), (i * separacion+20, limites+20), grosor)	


class GENERAR_SUDOKU_PYGAME(DISEÑO):
    def __init__(self):
        pass

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

    def ingresar_sudoku(self):
        self.base=[]
        for x in range(9):
            datos=input("Ingresa los datos de la fila "+str(x+1)+": ")
            filas=datos.split(",")
            cambio_filas=[]
            for a in range(9):
                y=filas[a]
                cambio=int(y)
                cambio_filas.append(cambio)
            self.base.append(cambio_filas)

    def  asignacion (self, fila , columna ): 
        asignacion_numeros  =  0 
        for  i  in range ( 0 , self.tamaño ): 
            for j  in range  ( 0 , self.tamaño ): 
                
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
        for  i  in range ( 0 , self.tamaño ): 
            #Si hay una celda con el mismo valor retorna Falso 
            if self.base [ f ] [ i ]  ==  n : 
                return  False 
        #Comprueba las columnas
        for  i  in range ( 0 , self.tamaño ): 
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

class JUEGO(GENERAR_SUDOKU_PYGAME):
    def Juego_Sudoku(self):
        seleccion1=0
        avance=True
        while avance:
            self.pantalla.fill((self.blanco))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    avance = False

                if event.type==pygame.MOUSEBUTTONDOWN:
                    seleccion1=1
                    pos=pygame.mouse.get_pos()
                    self.coordenadas(pos)
            
            self.marco()
            if seleccion1 == 1:
                self.casillas()

            # Update window
            pygame.display.flip()

pruebas=JUEGO()
pruebas.variables_fijas()
pruebas.fondo_pantalla()
pruebas.Juego_Sudoku()