"""Criado por Fabricio Vieira

Descrição: Programa criado em linguagem Python para validar se o ano é bissexto ou não a partir do dado informado pelo usuário.
O valor retornado deve ser true se for bissexto e false se não for bissexto.

"""

def eh_bissexto(ano): #Função que verifica se o ano é bissexto

    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        """A lógica funciona da seguinte maneira: 
        
            Como estamos lidando com 4 algarismos numéricos, 
            Sua implementação da validação deve considerar a combinação de divisão por números específicos,
            Neste caso, o ponto relevante da execução da script é que o ano bissexto ocorre a cada 4 anos. 
            Nesse tipo de estrutura, para a condição ser verdadeira,
            A divisão por 4 deve ter resto 0 ao mesmo tempo que a divisão por 100 não deve ter resto 0
            Ou unicamente a divisão por 400 tenha resto 0 """
        return True
    else:
        return False

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