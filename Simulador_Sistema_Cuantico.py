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
        y determino la probabilidadad de transitar del primer vector al segundo
    """
    cal=Calculadora()
    bra=cal.matrizConjugada([ket])
    print(bra)
    
    return

def interfaz():
    print("Bienvenido")
    print("Este es el Simulador de un Sistema Cuantico en una Linea")
    print("Ingrese el numero de posiciones")
    nPosiciones = int(input("Posiciones "))
    print("Ingrese las amplitudes para el ket de estado")
    ket=[tuple(map(float, x.split(","))) for x in (input("ket ").split(" "))]
    print("Opciones")
    print("1. Calcular la probabilidad de encontrar la particula en una posicion")
    print("2. Buscar probabilidad de transitar de vector a vector")
    print("0. Salir")
    opt = int(input("Opcion"))
    while opt!=0:
        if (opt==1):
            print("Ingrese posicion")
            X= int(input("X: "))
            detectarParticula(ket,X)
        elif (opt==2):
            print("Ingrese vector ket")
            ket2=[tuple(map(float, x.split(","))) for x in (input("ket ").split(" "))]
            transitarVector(ket,ket2)
        else:
            print("Opcion Invalida")
        opt = int(input("Opcion "))

def main():
    ket=[tuple(map(float, x.split(","))) for x in (input().split(" "))]
    #X=int(input())
    #print(detectarParticula(ket,X))
    ket2=[tuple(map(float, x.split(","))) for x in (input("ket ").split(" "))]
    transitarVector(ket,ket2)
main()
