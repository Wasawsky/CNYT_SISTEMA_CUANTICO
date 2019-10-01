#Calculadora de Numeros complejos
#Version 2.0
#MICHAEL BALLESTEROS
#2019-2

import math

#---------------------------------------------------------------------

class Calculadora:
    def __init__(self):
        return

    def suma(self,c1,c2):
        """Recibo 2 complejos y los suma -> complejo
        """
        a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
        return (a1+a2,b1+b2)
    def resta(self,c1,c2):
        """Recibo 2 complejos y los resta -> complejo
        """
        a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
        return (a1-a2,b1-b2)
    def multiplicacion(self,c1,c2):
        """Recibo 2 complejos y los multiplica -> complejo
        """
        a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
        return (a1*a2-b1*b2,a1*b2+a2*b1)
    def division(self,c1,c2):
        """Recibo 2 complejos y los divido -> complejo
        """
        a1,b1,a2,b2=c1[0],c1[1],c2[0],c2[1]
        x = (a1*a2+b1*b2)/(a2**2+b2**2)
        y = (a2*b1-a1*b2)/(a2**2+b2**2)
        return (x,y)
    def modulo(self,c1):
        """Complejo y hallo modulo -> entero
        """
        a1,b1=c1[0],c1[1]
        return (a1**2+b1**2)**(1/2)
    def conjugado(self,c1):
        """Recibo complejos y lo conjuga -> complejo
        """
        a1,b1=c1[0],c1[1]
        return (a1,b1*-1)
    def fase(self,c):
        """Recibo complejo hallo fase en grados -> entero
        """
        a,b=c[0],c[1]
        return ((math.atan2(b,a))*180)/math.pi
    def convpolaracartesiano(self,c):
        """Recibo polar (angulo en grados)y doy cartesiano -> Cartesiano
        """
        p,ang=c[0],(c[1]*math.pi)/180
        x=p*math.cos(ang)
        y=p*math.sin(ang)
        return (x,y)
    def convcartesianoapolar(self,c):
        """Recibo cartesiano y doy polar -> Polar
        """
        a,b = c[0],c[1]
        p = self.modulo(c)
        ang = self.fase(c)
        return (p,ang)

    #---------------------------------------------------------------------


    def sumaVectores(self,v1,v2):
        """Recibo 2 vectores complejos  y sumo -> vector complejo
        """
        if (len(v1)!=len(v2)):
            return "Imposible"
        else:
            for j in range(len(v1)):
                v1[j]=self.suma(v1[j],v2[j])
            return v1
    def inversa(self,v1):
        """Recibo 1 vector complejo y hallo inverso aditivo -> vector complejo
        """
        for j in range(len(v1)):
            v1[j]=self.multiplicacion((-1,0),v1[j])
        return v1
    def multiplicacionEscalarVector(self,v1,c):
        """Recibo 1 vector complejo y un escalar y hago la multiplicacion escalar de vector -> vector complejo
        """
        for j in range(len(v1)):
            v1[j]=self.multiplicacion(v1[j],c)
        return v1
    def sumaMatrices(self,m1,m2):
        """Recibo 2 matrices complejas y las sumo -> matriz compleja
        """
        if (len(m1)!=len(m2)or len(m1[0])!=len(m2[0])):
            return "Imposible"
        else:
            for j in range(len(m1)):
                m1[j]=self.sumaVectores(m1[j],m2[j])
            return m1
    def inversaMatriz(self,m1):
        """Recibo matriz compleja y hallo inverso aditivo -> matriz compleja
        """
        for j in range(len(m1)):
            m1[j]=self.inversa(m1[j])
        return m1
    def multiplicacionEscalarMatriz(self,m1,c):
        """Recibo una matriz compleja y un escalar y hago la multiplicacion escalar de matriz -> matriz compleja
        """
        for j in range(len(m1)):
            m1[j]=self.multiplicacionEscalarVector(m1[j],c)
        return m1
    def transpuesta(self,m1):
        """Recibo una matriz compleja y determino su transpuesta -> matriz compleja
        """
        m2=[[(0,0) for x in m1] for x in m1[0]]
        for j in range(len(m1[0])):
            for k in range(len(m1)):
                m2[j][k]=m1[k][j]
        return m2
    def matrizConjugada(self,m1):
        """Recibo una matriz compleja y determino la matriz conjugada -> matriz compleja
        """
        for j in range(len(m1)):
            for k in range(len(m1[0])):
                m1[j][k]=self.conjugado(m1[j][k])
        return m1
    def matrizAdjunta(self,m1):
        """Recibo una matriz compleja y determino matriz adjunta -> matriz compleja
        """
        return self.matrizConjugada(self.transpuesta(m1))
    def multiplicacionMatrizMatriz(self,m1,m2):
        """Recibo 2 matrices complejas y hallo la multiplicacion de matrices -> matriz compleja
           se debe cumplr a:m*n, b:n*p
        """
        if (len(m1[0])!=len(m2)):
            return "Imposible"
        else:
            m3=[[(0,0) for x in m2[0]] for x in m1]
            for j in range(len(m1)):
                for k in range(len(m2[0])):
                    resultado=(0,0)
                    for h in range(len(m2)):
                        resultado=self.suma(self.multiplicacion(m1[j][h],m2[h][k]),resultado)
                    m3[j][k]=resultado
            return m3
    def accion(self,m1,v1):
        """ Recibo 1 matriz compleja de n*n y 1 vector de n*1
                y hallo la accion de la matriz sobre el vector   -> vector complejo
        """
        if (len(m1[0])!=len(v1)):
            return "Imposible"
        else:
            return self.multiplicacionMatrizMatriz(m1,self.transpuesta([v1]))
    def sumaDiagonal(self,m1):
        """ Recibo una matriz de n*n y calculo la suma de los elementos diagonales -> numero complejo
        """
        sumaD=(0,0)
        for j in range(len(m1)):
            sumaD=self.suma(m1[j][j],sumaD)
        return sumaD
    def productoInternoMatriz(self,m1,m2):
        """ Recibo 2 matrices complejas y calculo el producto interno -> numero complejo
        """
        return self.sumaDiagonal(self.multiplicacionMatrizMatriz(self.matrizAdjunta(m1),m2))
    def normaMatriz(self,m1):
        """ Recibo 1 matriz de n*m y hallo su norma -> numero real
        """
        return math.sqrt(self.productoInternoMatriz(m1,m1)[0])
    def distanciaMatrizMatriz(self,m1,m2):
        """ Recibo 2 matrices y determino su distancia -> numero real
        """
        if (len(m1)!=len(m2)or len(m1[0])!=len(m2[0])):
            return "Imposible"
        else:
            return self.normaMatriz(self.sumaMatrices(m1,self.inversaMatriz(m2)))
    def matrizIdentidad(self,n):
        """ Recibo un entero y determino la matriz identidad n*n -> matriz 
        """
        ident=[[(0,0) for x in range(n)] for x in range(n)]
        for j in range(n):
            ident[j][j]=(1,0)
        return ident
    def matrizUnitaria(self,m1):
        """ Determino si una matriz es unitaria -> boolean
        """
        if (len(m1)!=len(m1[0])):
            return "Imposible"
        else:
            ident=self.matrizIdentidad(len(m1))
            m1=self.multiplicacionMatrizMatriz(self.matrizAdjunta(m1),m1)
            esUnitaria=True
            for j in range(len(m1)):
                for k in range(len(m1)):
                    if (m1[j][k]!=ident[j][k]):
                        esUnitaria=False
                        break
            return esUnitaria
    def matrizHermitian(self,m1):
        """ Determino si una matriz es hermitian -> boolean
        """
        if (len(m1)!=len(m1[0])):
            return "Imposible"
        else:
            esHermitian=True
            m2=self.matrizAdjunta(m1)
            for j in range(len(m1)):
                for k in range(len(m1)):
                    if (self.resta(m1[j][k],m2[j][k])!=(0,0)):
                        esHermitian=False
                        break
            return esHermitian
    def productoTensor(self,m1,m2):
        """ Determino el producto tensor de dos matrices complejas -> matriz compleja
        """
        m=len(m1)
        n=len(m2)
        m3=[[(0,0) for x in range(len(m1[0])*len(m2[0]))] for x in range(m*n)]
        for j in range(len(m3)):
            for k in range(len(m3[0])):
                m3[j][k]=self.multiplicacion(m1[j//n][k//m],m2[j%n][k%m])
        return m3
    #---------------------------------------------------------------------
