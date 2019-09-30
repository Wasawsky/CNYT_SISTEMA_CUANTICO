# SIMULADOR 
# Sistema cuántico de partícula en una línea

El sistema consiste en una partícula confinada a un conjunto discreto de posiciones en una línea. 
El simulador permite especificar el número de posiciones y un vector ket de estado asignando las amplitudes.

- El sistema calcula la probabilidad de encontrarlo en una posición en particular.
- El sistema si se le da otro vector Ket busca la probabilidad de transitar del primer vector al segundo.

# Generalidades

El estado actual de la partícula ndimensional puede representarse en un vector de columna compleja [c0, c1,. . . , cn − 1] T.
Sera nombrado como *ket* y cada estado de nuestro sistema sera representado por un elemento de Cn como


## Como usar

Esta libreria esta programada en la version de Python 3.7.4 y funciona para las versiones 3.7.* 
Debe tener instalado un entorno de desarrollo o un editor de texto donde se pueda compilar el archivo.

Si no posee uno puede ingresar a https://www.python.org/ para descargar la ultima version.


Despues de tenerlo, puede crear un archivo .py en el mismo directorio del archivo Simulador_Sistema_Cuantico.py

Importe la libreria en el nuevo archivo y use las operaciones de manera directa
Por ejemplo el siguiente codigo le indicara cual es la probabilidad de encontrar una particula dandole el ket y la posicion:

`import Simulador_Sistema_Cuantico`

`a=Simulador_Sistema_Cuantico.detectarParticula([(-3.0, -1.0), (0.0, -2.0), (0.0, 1.0), (2.0, 0.0)],2)`

`print(a)`

Producira un resultado:

`0.05263157894736841`

En caso de que tenga problemas puede ejecutar el archivo Pruebas_Simulador_Sistema_Cuantico.py para ejecutar las pruebas establecidas.
En el repositorio existe un archivo Entradas_Manuales en las que puede ver codigo que le puede ayudar a hacer lectura de datos para el simulador por teclado; tambien esta el archivo Casos_Prueba si desea usar el archivo de Entradas_Manuales para probar casos de prueba.

### Como usarlo por consola?

Si desea usarlo por consola, ubique la consola en la carpeta donde esta el archivo Simulador_Sistema_Cuantico.py y escriba en la consola

        $ py Simulador_Sistema_Cuantico.py

Para ejecutar las pruebas escriba en la consola

        $ py Pruebas_Simulador_Sistema_Cuantico.py
        
Puede ejecutar el idle de python si escribe

        $ py

Estando en el directorio puede ejecutar 

        import Simulador_Sistema_Cuantico
        Simulador_Sistema_Cuantico.detectarParticula([(-3.0, -1.0), (0.0, -2.0), (0.0, 1.0), (2.0, 0.0)],2)
 
Y el resultado sera:

        0.05263157894736841

## FUNCIONALIDADES:

- Detectar cual es la probabilidad de encontrar una particula en una posicion
- Transitar desde un vector a otro


## BIBLIOGRAFIA:


        > Quantum Computing For Computer Scientists 
        Noson S. Yanofsky 
        Mirco A. Mannucci
    
    
    
*Por: Michael Ballesteros*
