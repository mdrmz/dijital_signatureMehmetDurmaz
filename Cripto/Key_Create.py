import random


# Anahtar üretimi
def generate_keys():
    # Büyük asal sayılar (örnek değerler, pratikte güvenli asal değerler seçilmelidir)
    p = 0xFCA682CE8E12CABA26EFCCF7110E526DB078B05EDE3EF815984D386B5C899FFEFFFFF
    q = 0x123456789ABCDEF123456789ABCDEF123456789ABCDEF123456789ABCDEF12345  # p - 1 böleni

    # g değerini hesapla
    h = random.randint(2, p - 1)
    g = pow(h, (p - 1) // q, p)

    # Özel anahtar (x) ve genel anahtar (y)
    x = random.randint(1, q - 1)  # Özel anahtar
    y = pow(g, x, p)  # Genel anahtar
    return p, q, g, x, y

def Practical_outline_production():
    # 1. Asal sayılar (örnek olarak alınmış değerler, pratikte çok daha büyük olmalı)
    p = 23  # Büyük asal (örnek)
    q = 11  # p - 1’in bir böleni (örnek)

    # 2. g hesaplama
    h = random.randint(2, p - 1)  # Rastgele bir sayı seç
    g = pow(h, (p - 1) // q, p)  # g = h^((p-1)/q) mod p

    # 3. Özel ve genel anahtarlar
    x = random.randint(1, q - 1)  # Özel anahtar
    y = pow(g, x, p)  # Genel anahtar

    return p, q, g, x, y