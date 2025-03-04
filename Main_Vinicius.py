def soma_suce(num1: int, num2: int):
    if num1 == 1:
        return num2
    return num2 + soma_suce(num1 -1, num2)

#print(soma_suce(5,2))

def soma_inc (num1: int, num2: int):
    if num1 == 0:
        return num2
    return 1 + soma_inc(num1-1, num2)

#print(soma_inc(4,5))

def serie_dMattos (num1: int):
    if num1 == 1:
        return 1
    return 1/num1 + serie_dMattos(num1-1)

#print(serie_dMattos(3))


def inverter(text: str):
    if len(text) <= 1: 
        return text
    return inverter(text[1:]) + text[0]  

#print(inverter("texto"))

def F(num: int):
    if num == 1:
        return 1
    if num == 2:
        return 2
    return 2 * F(num -1) + 3 * F(num -2)

#print(sequencia(4))

def A(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, 1)
    else:
        return A(m - 1, A(m, n - 1))

#print(A(2, 4))


def vetor_soma(vetor, index=0):
    if index == len(vetor):
        return 0
    return vetor[index] + vetor_soma(vetor, index +1)

#print(vetor_soma([1,2,3,4]))

def vetor_multi(vetor, index=0):
    if index == len(vetor):
        return 1
    return vetor[index] * vetor_multi(vetor, index + 1)

#print(vetor_multi([1,2,3,4]))


def palindromo(text: str):
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return  False
    else:
        return palindromo(text[1:-1])

#print(palindromo("ovo"))


def combina(n: int):
    alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if n == len(alfabeto) - 1:
        return [alfabeto[0]]
    if n >= 1:
        return 

#print(combina(2))


def fibg(f0, f1, n: int):
    if n == 0:
        return f0
    elif n == 1:
        return f1
    elif n > 1:
        return fibg(f0, f1, n-1) + fibg(f0,f1, n-2)

print(fibg(2,2,2))