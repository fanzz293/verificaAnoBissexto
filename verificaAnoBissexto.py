"""Criado por Fabricio Vieira

Descrição: Programa criado em linguagem Python para validar se o ano é bissexto ou não a partir do dado informado pelo usuário.
O valor retornado deve ser true se for bissexto e false se não for bissexto.

"""

def eh_bissexto(ano): #Função que verifica se o ano é bissexto
        return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
    
# Interface com o usuário: verificação do ano
# Como há mais de duas possibilidades de outputs a depender da entrada, é interessante utilizar o try/catch
while True: # Para evitar que o programa encerre caso a output caia em except
    try:
        ano_digitado = int(input("Digite um ano: "))
        resultado = eh_bissexto(ano_digitado)
        print(f"O ano {ano_digitado} é bissexto? {resultado}")
        break # Sem isso o programa ia entrar em loop infinito
    except ValueError:
        print("Por favor, digite um valor numérico válido para o ano.")
