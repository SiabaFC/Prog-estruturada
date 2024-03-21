def piramide():
    print("Coloque os lados do triangulo para identificar qual é o tipo do triangulo")
    l1 = (input("Lado 1: "))
    try:
        l1 = int(l1)
    except ValueError:
        print("Número invalido")
        quit()
    
    print(l1)
    l2 = (input("Lado 2: "))
    try:
        l2 = int(l2)
    except ValueError:
        print("Número invalido")
        quit()
        
        
    print(l1, l2)
    l3 = (input("Lado 3: "))
    try:
        l3 = int(l3)
    except ValueError:
        print("Número invalido")
        quit()
        
        
    print(l1, l2, l3)
    
    if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1):
        print("Não é um triângulo")
    elif l1 == l2 == l3:
        print("Equilátero")     
    elif (l1 == l2) or (l1 == l3) or (l2 == l3):
        print("Isósceles")
    elif l1 != l2 != l3:
        print("Escaleno")
    else:
        print("Houve um erro, tente novamente")
        piramide()

        
    
piramide()

print("-" * 30)

def semana():
    d = input("Coloque o numero que equivale o dia da semana: ")
    try:
        d = int(d)
    except ValueError:
        print("Número invalido")
        quit()
        
        
    if d == 1:
        print("Domingo")
    elif d == 2:
        print("Segunda-feira")
    elif d == 3:
        print("Terça-feira")   
    elif d == 4:
        print("Quarta-feira")   
    elif d == 5:
        print("Quinta-feira")   
    elif d == 6:
        print("Sexta-feira")   
    elif d == 7:
        print("Sabado")           
    else:
        print("Numero invalido, tente novamente!")
        print("-" * 30)
        semana()

semana()    

print("-" * 30)

def calculadora():
    print("Olá, bem vindo a calculadora!")
    print("Para iniciar, coloque seu primeiro número que desejar para começar os calculos: ")
    x = float(input())
    print("Coloque a operação a ser realizada: ")
    print("(+ = soma | - = subtração | * = multiplicação | / = divisão)")
    print(x)
    y = input()
    print("Coloque o último número para realizar sua conta: ")
    print(x, y)
    z = float(input( ))
    print(x, y, z)
    
    print("Esse foi o seu resultado")
    
    if y == "+":
        print("{} + {} = ".format(x, z))
        print(x + z)

    elif y == "-":
        print("{} - {} = ".format(x, z))
        print(x - z)

    elif y == "*":
        print("{} * {} = ".format(x, z))
        print(x * z)

    elif y == "/":
        print("{} / {} = ".format(x, z))
        print(x / z)

    else:
        print("Ocorreu um erro na aplicação, tente novamente")
        print("-" * 30)
        calculadora()
        
    
calculadora() 


    
    
    
