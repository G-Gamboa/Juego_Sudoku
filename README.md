# Juego Sudoku

Juego de Sudoku desarrollado en Python con interfaz gráfica usando **Pygame**. Permite jugar partidas generadas aleatoriamente o resolver sudokus ingresados manualmente, con un solucionador automático basado en backtracking.

## Características

- Generación aleatoria de sudokus jugables
- Resolución automática mediante el algoritmo de backtracking
- Modo juego: completa el tablero con ayuda visual
- Modo resolver: ingresa un sudoku existente y obtén la solución
- Navegación con teclado y ratón
- Interfaz gráfica con pygame

## Requisitos

- Python 3.x
- Pygame

```
pip install pygame
```

## Estructura del proyecto

```
Juego_Sudoku/
├── SUDOKU.py                    # Archivo principal — inicia el juego
├── Generar_Random_Pygame.py     # Prototipo de generación aleatoria
├── Generar_Sudoku_Random.py     # Generación aleatoria en terminal
├── Resolver_Ingresado_Pygame.py # Resolver sudoku ingresado (terminal)
├── Resolver_Sudoku_Ingresando.py# Resolver sudoku ingresado (terminal)
├── pruebas.py                   # Sudoku de prueba predefinido
└── *.png                        # Assets gráficos de la interfaz
```

## Cómo ejecutar

```
python SUDOKU.py
```

Todos los archivos `.png` deben estar en el mismo directorio que `SUDOKU.py`.

## Controles

| Tecla / Acción | Función |
|---|---|
| `J` | Generar sudoku aleatorio (modo juego) |
| `R` | Modo resolver (ingresar sudoku propio) |
| `Flechas` | Mover la selección por el tablero |
| `1` – `9` | Ingresar un número en la celda seleccionada |
| `Backspace` | Confirmar el número en la celda |
| `Enter` | Solicitar solución automática |
| `X` | Reiniciar el tablero |
| `M` | Volver al menú principal |
| `S` / `N` | Confirmar / cancelar en pantalla final |

## Scripts de terminal

Los siguientes scripts funcionan de forma independiente sin necesidad de Pygame:

- **`Generar_Sudoku_Random.py`** — genera e imprime un sudoku aleatorio resuelto
- **`Resolver_Sudoku_Ingresando.py`** — pide un sudoku fila por fila y muestra la solución
- **`pruebas.py`** — resuelve un sudoku predefinido para verificar el algoritmo

Para ingresarlos desde terminal, separa los valores de cada fila con comas e incluye `0` en las celdas vacías:

```
Ingresa los datos de la fila 1: 6,5,0,8,7,3,0,9,0
```

## Algoritmo de resolución

El solucionador usa **backtracking recursivo**:

1. Busca la primera celda vacía (valor `0`)
2. Intenta colocar números del 1 al 9 validando fila, columna y subcuadro 3×3
3. Si ningún número es válido, retrocede y prueba la siguiente opción
4. El proceso continúa hasta completar el tablero o determinar que no tiene solución

## Tecnologías

- **Python 3**
- **Pygame** — interfaz gráfica
- **random** — generación aleatoria de tableros
- **copy** — copia profunda del estado del tablero para separar puzzle de solución
