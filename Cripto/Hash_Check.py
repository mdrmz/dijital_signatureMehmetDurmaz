import hashlib

# Dosyanın hash'ini hesaplama
def calculate_file_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):  # Dosyayı parça parça oku
            sha256.update(chunk)
    return sha256.digest()


def calculate_text_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode("utf-8"))
    return sha256.digest()
