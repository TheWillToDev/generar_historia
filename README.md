# Generador de historias locas

Este proyecto consiste en un programa que genera historias locas combinando personajes, lugares y eventos de manera aleatoria. Las historias resultantes son divertidas y variadas, lo que las hace ideales para entretener a los niños.

## Cómo funciona

El programa utiliza el módulo `random` para seleccionar elementos aleatorios de listas que contienen personajes, lugares y eventos. A continuación, combina los elementos seleccionados y crea una historia única utilizando cadenas de formato. El número de historias generadas se puede ajustar mediante una variable.

Aquí tienes una explicación paso a paso del código:

1. Importamos el módulo `random` para utilizar la función `choice`, que nos permite seleccionar elementos aleatorios de una lista.

2. Definimos la función `generar_historia()` que no requiere argumentos. En esta función, tenemos tres listas: personajes, lugares y eventos, que contienen diferentes elementos para cada categoría.

3. Utilizamos `random.choice()` para seleccionar aleatoriamente un elemento de cada lista y asignarlo a las variables `personaje`, `lugar` y `evento`.

4. Creamos la historia combinando los elementos anteriores utilizando una cadena de formato (f-string) y la guardamos en la variable `historia`.

5. La función `generar_historia()` retorna la historia generada.

6. Creamos una lista llamada `historias_locas` para almacenar las historias generadas.

7. Definimos la variable `cantidad_historias` para establecer cuántas historias queremos generar.

8. Utilizamos un bucle `for` para generar la cantidad de historias especificada. En cada iteración, llamamos a la función `generar_historia()` y añadimos la historia generada a la lista `historias_locas`.

9. Por último, utilizamos otro bucle `for` para imprimir cada historia generada en la lista `historias_locas`.

## Ejecución

Para ejecutar el programa, simplemente ejecuta el archivo principal, con cualquiera de las siguientes formas puedes correr el codigo:
- `main.py`
- `py main.py`
- `python3 main.py`

Puedes ajustar la variable `cantidad_historias` para generar más o menos historias según tu preferencia.

## Personalización

Si deseas agregar más opciones y variedad a las historias, puedes modificar las listas `personajes`, `lugares` y `eventos`.

Agrega nuevos elementos a las listas para ampliar las opciones de generación de historias.

¡Diviértete generando historias locas!

