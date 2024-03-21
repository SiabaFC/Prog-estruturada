def piramide():
    print("Coloque os lados do triangulo para identificar qual é o tipo do triangulo")
    l1 = input("Lado 1: ")
    print(l1)
    l2 = input("Lado 2: ")
    print(l1, l2)
    l3 = input("Lado 3: ")
    print(l1, l2, l3)
    
    if l1 == l2 == l3:
        print("triangulo") 
    elif l1 + l2 == l3:
        print("burro")        
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("k")
    elif l1 != l2 != l3:
        print("peitos")
    else:
        print("Houve um erro, tente novamente")
        piramide()
        
    
piramide()

print("-" * 30)

def semana():
    d = input("Coloque o dia que equivale o dia da semana: ")
    
    if d == "1":
        print("Domingo")
    elif d == "2":
        print("Segunda-feira")
    elif d == "3":
        print("Terça-feira")   
    elif d == "4":
        print("Quarta-feira")   
    elif d == "5":
        print("Quinta-feira")   
    elif d == "6":
        print("Sexta-feira")   
    elif d == "7":
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
    x = int(input())
    print("coloque qual sinal haverá na conta: ")
    print("(+ = soma | - = subtração | * = multiplicação | / = divisão)")
    print(x)
    y = input()
    print("coloque o último número para realizar sua conta: ")
    print(x, y)
    z = int(input( ))
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
        print("Ocorreu um erro na aplicação, voce quer tentar novamente", "S/N")
        Q = input()
        if Q == "S":
            print("-" * 30)
            calculadora()
        elif Q == "N":
            print("Até logo")
        else:
            print("????")
        
    
calculadora() 


    
    
    
