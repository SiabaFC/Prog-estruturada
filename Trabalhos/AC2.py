def calcula_salario():
   valor_hora = float(input("Valor do salário por hora: "))
   num_horas = float(input("Número de horas trabalhadas no mês: "))
   irpf = 0.275
   
   salario = valor_hora * num_horas 
   salario_liq = salario * (1 - irpf)
   
   if salario_liq < 0:
       print("Valor informado negativo")
   else:
        print( "Seu salário líquido é: R$",salario_liq)
   

calcula_salario()
   
   
 
