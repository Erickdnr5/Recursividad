from math import factorial


class funcionFactorial:

    def calcularFactorial(n):
        if n == 0 or n == 1:
            rs = 1
        elif n > 1:
            rs = n * factorial(n - 1)
        return rs

    factorial = calcularFactorial(10)
    print(factorial)
