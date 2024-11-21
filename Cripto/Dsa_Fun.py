
from math import gcd
def modular_inverse(a, m):
    # GCD'yi kontrol et, eğer 1 değilse tersini almanın mümkün olmadığını bildir
    if gcd(a, m) != 1:
        raise ValueError(f"Modüler ters bulunamaz çünkü gcd({a}, {m}) = 1 değil.")

    # Extended Euclidean Algorithm
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0

    return x1 + m0 if x1 < 0 else x1

