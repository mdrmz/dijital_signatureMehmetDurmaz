import Key_Create as mdkey
import  Hash_Check as mdhash
import Dsa_Fun as mdfun
import Dsa_Signature as mdsign

# DSA anahtarlarını üret
p, q, g, x, y = mdkey.Practical_outline_production()

# Görüntü dosyasını imzalama
image_path = "data.png"
image_hash = mdhash.calculate_file_hash(image_path)
r, s = mdsign.sign_data(image_hash, p, q, g, x)
print(f"Görüntü imzası: r = {r}, s = {s}")

# Görüntü doğrulama
is_valid = mdsign.verify_data(image_hash, r, s, p, q, g, y)
print(f"Görüntü imzası geçerli mi? {is_valid}")

# Metni imzalama
text = "Mehmet Durmaz."
text_hash = mdhash.calculate_text_hash(text)
r, s = mdsign.sign_data(text_hash, p, q, g, x)
print(f"Metin imzası: r = {r}, s = {s}")

# Metni doğrulama
is_valid = mdsign.verify_data(text_hash, r, s, p, q, g, y)
print(f"Metin imzası geçerli mi? {is_valid}")


