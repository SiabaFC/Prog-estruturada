""" 
def media():
    ap1 = float(input("Informe a nota da AP1: "))
    ap2 = float(input("Informe a nota da AP2: "))
    ac = float(input("Informe a nota da AC: "))

    media = (ap1 + ap2) * 0.4 + ac * 0.2

    print("A média é", round(media, 2))

media()
"""



def vroom():
    X2 = float(input("Informe valor de A: "))
    x1 = float(input("Informe o valor de B: "))
    x =  float(input("Informe o valor de C: "))

    vroom1 = x1 * x1 
    vroom2 = 4 * X2 * x
    vromm3 = vroom1 - vroom2

    import math
    vroom = math.sqrt(vromm3)
    vroom4 =  ((x1 * -1) / 2 * X2) + vroom / 2 * X2
    vroom5 =  ((x1 * -1) / 2 * X2) - vroom / 2 * X2 

    print("Resultados", vroom4, vroom5) 

vroom()


def Ano():
    num = float(input("Digite um ano para verificar se é bissexto: "))
    print(num % 4 == 0)
   
     


Ano()