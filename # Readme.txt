# Juego de Adivinar el Número


## Descripción

El juego comienza con un menú principal en el que da 4 opciones: 

1. Solitario:
El juego genera un número aleatorio dentro de un rango especificado (por ejemplo, del 1 al 1000, dependiendo de la dificultad seleccionada) y el jugador tiene que adivinarlo. Después de cada intento, el juego proporciona pistas indicando si el número ingresado es mayor o menor que el número objetivo. El juego continúa hasta que el usuario adivina correctamente el número o se le acaban los intentos (estos dependen de la dificultad seleccionada). Guarda las estadísticas del jugador. Al acabar vuelve al menú principal.

2. En pareja:
El juego comienza pidiendo al Jugador1 que introduzca un número dentro de un rango especificado (por ejemplo, del 1 al 1000, dependiendo del rango seleccionado) y el Jugador2 tiene que adivinarlo. Después de cada intento, el juego proporciona pistas indicando si el número ingresado es mayor o menor que el número objetivo. El juego continúa hasta que el usuario adivina correctamente el número. Guarda las estadísticas del jugador. Al acabar vuelve al menú principal.

3. Estadísticas:
Tienes 4 opciones:
	1. Muestra todas las estadísticas. El juego muestra los datos de la tabla de Excel, bien ordenados.
	2. Estadísticas con GRÁFICOS filtradas por jugador. 
	3. Añadir estadísticas ficticias. El juego añade 500 partidas ficticias (10 jugadores con 50 partidas cada uno).
	4. Salir del menu de estadísticas. Te devuelve al menu principal.

4. Salir del juego:
La pantalla imprime un mensaje final dándote las gracias por jugar y esperar volver a verte. Acaba el programa.

## Características
- Indicación de si el número ingresado es MAYOR O MENOR que el número objetivo.
- CONTEO DE INTENTOS realizados por el jugador.
- MENSAJE DE FELICITACIÓN al acertar el número o de 'GAME OVER' en caso contrario.
- Incluye un MODULO PROPIO getnumber.py que tiene funciones encargadas de pedir números dentro de un rango, verificar que sean números y también pedir números ocultos.
- Elección por DIVERSAS DIFICULTADES. (Tanto en los intentos como en el rango)
- VERIFICA siempre que el número introducido sea efectivamente un número entero y en el rango. (Si el jugador introduce algo que no sea un número, lo indica y vuelve a pedirlo. Si introduce un número fuera del rango o no entero (negativo o decimal), lo indica y vuelve a pedirlo.)
- Cuando un jugador introduce un NÚMERO QUE YA HA INTRODUCIDO ANTERIORMENTE, se lo indica y vuelve a pedir otro número. (No cuenta ese intento.)
- En la modalidad de 2 jugadores. El programa NO MUESTRA EL NÚMERO A ADIVINAR introducido por el jugador 1. (getpass)
- Las ESTADÍSTICAS se crean si no existe el archivo. Si existen, se van actualizando sobre el archivo.
- Al terminar la partida el programa ACTUALIZA la línea de Excel que coincide con el jugador, dificultad, modo. Si no hay coincidencia, crea una línea nueva.
- El juego tiene la opción de AÑADIR 500 PARTIDAS FICTICIAS(10 jugadores con 50 partidas cada uno). (faker)
- En la opción 2 de estadísticas se muestran GRÁFICOS FILTRANDO POR JUGADOR.


##Consejos de uso:

Recomendamos utilizar el apartado 3 de estadísticas para añadir partidas de prueba y así comprobar el resultado de los apartados 1 y 2. También, se puede probar a jugar una partida con un jugador que ya haya jugado en una misma modalidad y dificultades para así ver que el juego actualiza correctamente la línea de Excel.