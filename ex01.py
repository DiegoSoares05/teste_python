def fibonacci(n):
    # Iniciando a sequência com 0 e 1
    sequencia_fibo = [0, 1]

    # Gerando a sequência de Fibonacci até o maior valor menor ou igual a n
    while sequencia_fibo[-1] < n:
        proximo_valor = sequencia_fibo[-1] + sequencia_fibo[-2]
        sequencia_fibo.append(proximo_valor) #adicionando elemento a uma lista existente

    # Verificando se o número pertence à sequência
    if n in sequencia_fibo:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."


# Teste
numero = int(input("Digite um número: "))
resultado = fibonacci(numero)
print(resultado)
