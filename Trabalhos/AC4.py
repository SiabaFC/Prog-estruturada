"""
Programação Estruturada
2024.1
08/03/2024

AC4
"""
"""
Programação Estruturada
2024.1
08/03/2024

AC4
"""



"""
Programação Estruturada
2024.1
08/03/2024

AC4
"""

def ler_nome():
    """Retorna o nome do aluno inserido pelo usuário."""
    return input("Informe o seu nome: ")

def ler_notas():
    """Lê as notas de AP1, AP2, AS e AC do aluno, e retorna essas notas."""
    ap1 = float(input("Informe sua AP1: "))
    ap2 = float(input("Informe suas AP2: "))
    asub = float(input("Informe suas Asub: "))
    ac = float(input("Informe suas AC: "))
    return ap1, ap2, asub, ac

def analisar_subst(ap1, ap2, asub):
    """
    Retorna as duas notas a serem usadas no cálculo.
    A AS deve substituir a AP1 ou AP2 se for maior que elas.
    """
    if ap1 <= ap2 and asub>ap1:
        return asub,ap2
    if ap2 <=ap1 and asub > ap2:
        return ap1, asub

def calcular_media(ap1, ap2, asub, ac):
    """Calcula e retorna a média final do aluno."""
    prova1, prova2 = analisar_subst(ap1, ap2, asub)
    media = (prova1 + prova2) * 0.4 + ac * 0.2
    return media

def aluno_foi_aprovado(media):
    """Retorna True se a média foi suficiente para aprovação do aluno."""
    return media >= 7

def notas_sao_validas(ap1, ap2, asub, ac):
    """Retorna True se todas as notas estão entre 0 e 10, inclusive."""
    

def main():
    nome = ler_nome()
    if nome:
        ap1, ap2, asub, ac = ler_notas()
        if notas_sao_validas(ap1, ap2, asub, ac):
            media = calcular_media(ap1, ap2, asub, ac)
            print("Média final:", media)
            if aluno_foi_aprovado(media):
                print("Aluno foi aprovado.")
            else:
                print("Aluno foi reprovado.")

main()







