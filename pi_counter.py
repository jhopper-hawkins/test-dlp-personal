from decimal import Decimal, getcontext

def compute_pi(n_digits: int) -> Decimal:
    # Set precision a bit higher to avoid rounding errors
    getcontext().prec = n_digits + 5

    pi = Decimal(0)
    k = 0

    while k < n_digits:
        numerator = Decimal((-1)**k) * factorial(6*k) * (545140134*k + 13591409)
        denominator = Decimal(factorial(3*k)) * (factorial(k)**3) * (640320**(3*k))
        pi += numerator / denominator
        k += 1

    pi = pi * Decimal(12) / Decimal(640320**1.5)
    return 1 / pi

def factorial(n: int) -> int:
    if n == 0: return 1
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

if __name__ == "__main__":
    digits = int(input("How many digits of pi do you want? "))
    print(compute_pi(digits))
