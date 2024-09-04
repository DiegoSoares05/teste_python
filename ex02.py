def verificar_letra_a(string):
    # Convertendo o texto para minúsculas para contar 'a' e 'A' como a mesma letra
    texto_lower = string.lower()
    
    # Contando o número de vezes que 'a' aparece na string
    contagem_a = texto_lower.count('a')
    
    # Verificando se a letra 'a' aparece na string
    if (contagem_a > 0):
        return f"A letra 'a' aparece {contagem_a} vez(es) na string."
    else:
        return "A letra 'a' não aparece na string."

# Exemplo de como testar
string = input("digite um texto: ")
verificacao = verificar_letra_a(string)
print(verificacao)
    
