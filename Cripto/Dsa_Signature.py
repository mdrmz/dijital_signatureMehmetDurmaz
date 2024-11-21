import Dsa_Fun as md
import random

def sign_data(data, p, q, g, x):
    h = int.from_bytes(data, "big") % q  # Hash'i tam sayıya çevir
    k = random.randint(1, q - 1)  # Rastgele k seç
    r = pow(g, k, p) % q
    k_inv = md.modular_inverse(k, q)
    s = (k_inv * (h + x * r)) % q
    return r, s

# Doğrulama
def verify_data(data, r, s, p, q, g, y):
    h = int.from_bytes(data, "big") % q  # Hash'i tam sayıya çevir
    w = md.modular_inverse(s, q)
    u1 = (h * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q
    return v == r
