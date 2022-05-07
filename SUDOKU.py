#--------------------ARCHIVO PRINCIPAL PARA RESOLVER SUDOKU---------------------------
import pygame
import random
import copy

pygame.init()

class DISEÑO():
    def __init__(self):
        pass

    def variables_fijas(self):
        pygame.font.init()

        #-------------------COLORES
        self.rojo=(255,0,0)
        self.blanco=(255,255,255)
        self.negro=(0,0,0)
        self.celeste=(92,222,220)

        #-----------------PANTALLA
        self.tamaño_pantalla=(550,650)
        self.tamaño=9
        self.pantalla=pygame.display.set_mode(self.tamaño_pantalla)
        self.separacion=(self.tamaño_pantalla[0]-40)/9
        self.espacios=self.tamaño_pantalla[0]/self.tamaño

        #-----------------IMÁGENES
        self.fondo=pygame.image.load("fondo.png")
        self.icono=pygame.image.load("icono.png")
        self.image_Marca=pygame.image.load("G.png")
        self.image_resolver=pygame.image.load("ResolverSudoku.png")
        self.image_jugar=pygame.image.load("JugarSudoku.png")
        self.image_menu=pygame.image.load("MenuSudoku.png")
        self.image_enter=pygame.image.load("EnterSudoku.png")
        self.image_reset=pygame.image.load("ResetSudoku.png")
        self.image_volver=pygame.image.load("VolverSudoku.png")
        self.image_SI=pygame.image.load("SiSudoku.png")
        self.image_NO=pygame.image.load("NoSudoku.png")


        #-----------------FUENTES
        self.fuente_numeros=pygame.font.SysFont("Cooper",40)
        self.fuente_titulos=pygame.font.SysFont("Snap ITC",80)
        self.fuente_textos=pygame.font.SysFont("Arial",20)
        
        #----------------VARIABLES VARIAS
        self.x=0
        self.y=0
        self.inicio=True
        self.seleccion1=0
        self.seleccion2=0
        self.instruccion=0
        self.valores=0
        self.pos=0
        self.modo=""
        
        #----------------BASES SUDOKU
        #CONTIENE NÚMEROS SOLAMENTE PARA PRUEBAS, AL TERMINAR EL PROGRAMA DEBE ESTABLECERSE VACÍA
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
        self.pantalla.blit(self.fondo,(0,0))
        pygame.display.set_caption("JUEGO SUDOKU")
        pygame.display.set_icon(self.icono)
              
    def casillas(self):
        if self.y<9:
            for i in range(2):
                pygame.draw.line(self.pantalla, self.rojo, (self.x * self.separacion+20-3, (self.y + i)*self.separacion+20), (self.x * self.separacion+20+ self.separacion + 3, (self.y + i)*self.separacion+20), 7)
                pygame.draw.line(self.pantalla, self.rojo, ( (self.x + i)* self.separacion+20, self.y * self.separacion+20), ((self.x + i) * self.separacion+20	, self.y * self.separacion+20 + self.separacion), 7)
 
    def instrucciones_marco(self):
        if self.instruccion==2:
            self.pantalla.blit(self.image_volver,(115,535))
            self.pantalla.blit(self.image_SI,(100,590))
            self.pantalla.blit(self.image_NO,(350,590))
        else:
            self.pantalla.blit(self.image_menu,(10,535))
            self.pantalla.blit(self.image_enter,(230,535))
            self.pantalla.blit(self.image_reset,(130,590))

    def marco(self):
        limites=self.tamaño_pantalla[0]-40
        for i in range(10):
            if i % 3 == 0 :
                grosor = 8
            else:
                grosor = 2

            pygame.draw.line(self.pantalla, self.negro, (20, i * self.separacion+20), (limites+20, i * self.separacion+20), grosor)
            pygame.draw.line(self.pantalla, self.negro, (i * self.separacion+20, 20), (i * self.separacion+20, limites+20), grosor)	
        self.instrucciones_marco()
 
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
        self.solucion_sudoku()
        #Sudoku aleatorio creado satisfactoriamente, solamente resta crear espacios en blanco
        cero=0
        while cero<60:
            cero=0
            for i in range (9):
                for j in range (9):
                    if self.base[j][i]== 0:
                        cero+=1
            random_fila=random.randrange(9)
            random_columna=random.randrange(9)
            self.base[random_fila][random_columna]=0

        self.copia=copy.deepcopy(self.base)            

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
    
    def valores_en_pantalla(self,impresion):
        for i in range (9):
            for j in range (9):
                if impresion[j][i]!= 0:
                    pygame.draw.rect(self.pantalla, (self.celeste),(i * self.separacion+20, j * self.separacion+20, self.separacion+3, self.separacion+3))
                    numeros = self.fuente_numeros.render(str(impresion[j][i]), 1,self.negro)
                    self.pantalla.blit(numeros, (i * self.separacion + 42, j * self.separacion + 37))
        self.marco()

    def valores_ingresados(self, valores):
        val = self.fuente_numeros.render(str(valores), 1, (0, 0, 0))
        self.pantalla.blit(val, (self.x * self.separacion + 15, self.y * self.separacion + 15))

    def solucion_en_pantalla(self,modo):
        for i in range (9):
            for j in range (9):
                if modo[j][i]!= 0:
                    pygame.draw.rect(self.pantalla, (self.celeste),(i * self.separacion+20, j * self.separacion+20, self.separacion+3, self.separacion+3))
                    if modo[j][i]==self.base[j][i]:
                        numeros = self.fuente_numeros.render(str(modo[j][i]), 1,self.negro)
                    else:
                        numeros = self.fuente_numeros.render(str(modo[j][i]), 1,self.rojo)
                    self.pantalla.blit(numeros, (i * self.separacion + 42, j * self.separacion + 37))
        self.marco()

    def instrucciones_principal(self):
        titulo=self.fuente_titulos.render("SUDOKU",1,self.negro)
        self.pantalla.blit(titulo,(self.tamaño_pantalla[0]/6.2,10))

        self.pantalla.blit(self.image_resolver,(30,150))
        self.pantalla.blit(self.image_jugar,(30,250))
        self.pantalla.blit(self.image_Marca,(20,370))

    def reinicio(self):
        if self.instruccion==3 or self.instruccion==0:
            for i in range (9):
                for j in range (9):
                    self.base[i][j]=0
        elif self.instruccion==1:
            for i in range (9):
                for j in range (9):
                    self.copia[i][j]=0

class JUEGO(GENERAR_SUDOKU_PYGAME):

    def Eventos_Pygame_Instrucciones(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inicio = False

            if event.type==pygame.MOUSEBUTTONDOWN:
                    self.seleccion1=1
                    self.pos=pygame.mouse.get_pos()
                    self.coordenadas(self.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    self.datos_random()
                    self.instruccion=1   
                    self.modo=1
                if event.key == pygame.K_r:
                    self.instruccion=3   
                    self.modo=2                                              

    def Eventos_Pygame_Sudoku(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inicio = False
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                    self.seleccion1=1
                    self.pos=pygame.mouse.get_pos()
                    self.coordenadas(self.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.x<1:
                        self.x=0
                        self.seleccion1=1
                    else:
                        self.x-=1
                        self.seleccion1=1
                if event.key == pygame.K_RIGHT:
                    if self.x>7:
                        self.x=8
                        self.seleccion1=1
                    else:
                        self.x+=1
                        self.seleccion1=1
                if event.key == pygame.K_UP:
                    if self.y<1:
                        self.y=0
                        self.seleccion1=1
                    else:
                        self.y-=1
                        self.seleccion1=1
                if event.key == pygame.K_DOWN:
                    if self.y>7:
                        self.y=8
                        self.seleccion1=1
                    else:
                        self.y+=1
                        self.seleccion1=1
                
                #Ingreso de los números        
                if event.key == pygame.K_1:
                    self.valores = 1
                if event.key == pygame.K_2:
                    self.valores = 2
                if event.key == pygame.K_3:
                    self.valores = 3
                if event.key == pygame.K_4:
                    self.valores = 4
                if event.key == pygame.K_5:
                    self.valores = 5
                if event.key == pygame.K_6:
                    self.valores = 6
                if event.key == pygame.K_7:
                    self.valores = 7
                if event.key == pygame.K_8:
                    self.valores = 8
                if event.key == pygame.K_9:
                    self.valores = 9
                
                if event.key == pygame.K_RETURN:
                    self.instruccion=2
                    self.seleccion2=1
                
                if event.key==pygame.K_BACKSPACE:
                    self.base[int(self.y)][int(self.x)]= self.valores

                if event.key == pygame.K_m:
                    self.instruccion=0
                    self.modo=0
                    self.reinicio()                    

                if event.key == pygame.K_x:
                    self.reinicio()

    def Eventos_Pygame_Final(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inicio = False

            if event.type==pygame.MOUSEBUTTONDOWN:
                    self.seleccion1=1
                    self.pos=pygame.mouse.get_pos()
                    self.coordenadas(self.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.seleccion2=0
                    self.instruccion=0
                    self.modo=0
                    self.reinicio()  
                        
                if event.key == pygame.K_n:
                    self.inicio=False
    
    def Juego_Sudoku(self):
        self.variables_fijas()
        self.fondo_pantalla()
        while self.inicio:
            self.pantalla.blit(self.fondo,(0,0))

            if self.instruccion==0:
                self.Eventos_Pygame_Instrucciones()                
                self.instrucciones_principal()

            if self.modo==1 or self.modo==2:
                self.Eventos_Pygame_Sudoku()

            if self.instruccion==1:
                if self.valores !=0:		
                    self.valores_ingresados(self.valores)
                    self.copia[int(self.y)][int(self.x)]= self.valores
                    self.valores=0
                self.valores_en_pantalla(self.base)
                self.valores_en_pantalla(self.copia)

                if self.seleccion1 == 1:
                    self.casillas()

            if self.instruccion==2:
                if self.modo==2:
                    self.solucion_sudoku()
                    self.valores_en_pantalla(self.base)
                    self.solucion_en_pantalla(self.base)


                if self.modo==1:             
                    self.solucion_sudoku()
                    self.valores_en_pantalla(self.base)
                    self.solucion_en_pantalla(self.copia)

            if self.instruccion==3:
                if self.valores !=0:		
                    self.valores_ingresados(self.valores)
                    self.base[int(self.y)][int(self.x)]= self.valores
                    self.valores=0
                self.valores_en_pantalla(self.base)

                if self.seleccion1 == 1:
                    self.casillas()


            if self.seleccion2==1:
                self.Eventos_Pygame_Final()
            #Actualizar pantalla
            pygame.display.flip()

SUDOKU_OFICIAL=JUEGO()
SUDOKU_OFICIAL.Juego_Sudoku()