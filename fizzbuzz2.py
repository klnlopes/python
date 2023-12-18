def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    else:
        return numero

numero = int(input("Digite um número inteiro: "))

resultado = fizz_buzz(numero)
print(resultado)