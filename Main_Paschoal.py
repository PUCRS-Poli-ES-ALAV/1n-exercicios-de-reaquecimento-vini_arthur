def somas_sucessivas(num1: int, num2: int):
    if num1 == 1:
        return num2
    else:
        return num2 + somas_sucessivas(num1-1, num2)


# print(somas_sucessivas(5, 5))


def soma_nat(num1: int, num2: int):
    if num1 == -(num2):
        return 0
    else:
        return 1 + soma_nat(num1-1, num2)


# print(soma_nat(5, 6))


def serie_dMattos(num1: int):
    if num1 == 1:
        return 1
    else:
        return 1/num1 + serie_dMattos(num1-1)

# print(serie_dMattos(2))


def inverte_string(string: str):
    if len(string) == 1:
        return string
    else:
        return string[-1] + inverte_string(string[:-1])


def gerador_sequencia(n: int):
    if n < 3:
        return n
    else:
        return 2 * gerador_sequencia(n - 1) + 3 * gerador_sequencia(n-2)

# print(gerador_sequencia(1))


def gerador_ackerman(m: int, n: int):
    if m == 0:
        return n + 1
    elif m != 0 and n == 0:
        return gerador_ackerman(m-1, 1)
    else:
        return gerador_ackerman(m-1, gerador_ackerman(m, n-1))

# print(gerador_ackerman(1, 1))


def soma_produto_vetor(vetor: list):
    if len(vetor) == 0:
        return 0, 1
    else:
        resto_soma, resto_produto = soma_produto_vetor(vetor[1:])
        return vetor[0] + resto_soma, vetor[0] * resto_produto

# print(soma_produto_vetor([1, 2, 3, 4, 5]))


def palavra_pelindromo(palavra: str):
    palavra_invertida = inverte_string(palavra)
    if palavra == palavra_invertida:
        return "É palindromo"
    else:
        return "Não é palindromo"


# print(palavra_pelindromo("anão"))
# print(palavra_pelindromo("aba"))


def palavra_palindromo2(palavra: str):
    if len(palavra) == 1:
        return "É palindromo"
    else:
        if (palavra[0] == palavra[-1]):
            return palavra_palindromo2(palavra[1:-1])
        else:
            return "Não é palindromo"

# print(palavra_palindromo2("anão"))
# print(palavra_palindromo2("aba"))


def fibonacci(f0: int, f1: int, n: int):
    if n == 0:
        return [f0]
    elif n == 1:
        return [f0, f1]
    else:
        return sequencia([f0,f1],2, 10)


def sequencia(seq: list, i:int, n:int):
    if i > n:
        return seq

    seq.append(seq[-1] + seq[-2])
    
    return sequencia(seq, i+1, n)


# print(fibonacci(2, 3, 10))

