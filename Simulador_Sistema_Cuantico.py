#Simulador de un sistema cuantico en una linea
#MICHAEL BALLESTEROS
#2019-2

from Library.Calculadora import *

def detectarParticula(ket,X):
    """ Recibo  vector ket de estado
                posicion a determinar la probabilidad de la particula
        y calculo la probabilidad de que la particula este en la posicion -> entero
    """
    cal=Calculadora()
    normaKet=cal.normaMatriz([ket])
    normaComplejo=cal.normaMatriz([[ket[X]]])
    return (normaComplejo**2)/(normaKet**2)
def transitarVector(ket,ket2):
    """ Recibo  vector ket de estado
                vector ket de estado
        y determino la probabilidad de transitar del primer vector al segundo
    """
    cal=Calculadora()
    ket1=cal.transpuesta([ket])
    bra=cal.matrizConjugada([ket2])
    car=cal.multiplicacionMatrizMatriz(bra,ket1)[0][0]
    normaBra=cal.normaMatriz(bra)
    normaket=cal.normaMatriz(ket1)
    car2=(normaBra*normaket,0)
    return cal.division(car,car2)

def interfaz():
    """ En caso de necesitarlo el simulador genera una interfaz con el usuario
    """
    print("Bienvenido")
    print("Este es el Simulador de un Sistema Cuantico en una Linea")
    print("Ingrese el numero de posiciones")
    nPosiciones = int(input("Posiciones "))
    print("Ingrese las amplitudes para el ket de estado")
    ket=[tuple(map(float, x.split(","))) for x in (input("ket ").split(" "))]
    opt = int(input("Opcion"))
    while opt!=0:
        print("Opciones")
        print("1. Calcular la probabilidad de encontrar la particula en una posicion")
        print("2. Buscar probabilidad de transitar de vector a vector")
        print("0. Salir")
        if (opt==1):
            print("Ingrese posicion")
            X= int(input("X: "))
            print(detectarParticula(ket,X))
        elif (opt==2):
            print("Ingrese vector ket")
            ket2=[tuple(map(float, x.split(","))) for x in (input("ket ").split(" "))]
            print(transitarVector(ket,ket2))
        else:
            print("Opcion Invalida")
        opt = int(input("Opcion "))

"""
Ejemplo de entrada para los ket usando
ket=[tuple(map(float, x.split(","))) for x in (input("ket ").split(" "))]
In:
2,-1 0,2 1,-1 1,0 0,-2 2,0
Out:
[(2.0,-1.0), (0.0,2.0), (1.0,-1.0), (1.0,0.0), (0.0,-2.0), (2.0,0.0)]

"""

