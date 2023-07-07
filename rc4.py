import os

def generate_rc4_key():
    key_length = 16  # Define o tamanho da chave em bytes
    key = os.urandom(key_length)  # Gera uma sequência de bytes aleatórios como chave
    return key

def rc4(key, plaintext):
    S = list(range(256))
    j = 0
    out = []

    # Key-scheduling algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # Pseudo-random generation algorithm (PRGA)
    i = j = 0
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(char ^ S[(S[i] + S[j]) % 256])

    return bytes(out)

# Gerar a chave RC4
#rc4_key = generate_rc4_key()
rc4_key = bytes.fromhex('22f0481e9fa3d7d86e303f8d9fd6742b')

# Mensagem a ser criptografada
mensagem_original = "Essa é uma mensagem de teste para criptografia com RC4."

# Convertendo a mensagem para bytes
plaintext = mensagem_original.encode()

# Criptografar a mensagem
#ciphertext = rc4(rc4_key, plaintext)
ciphertext = bytes.fromhex('1ebd618d8ebdf84e8037de076f9e3eed3d8d9405d6abcaddf9de9eb5881f3993334e56e08338693a7065da0b3a6b228b4fb5088d5d5672ce')

# Descriptografar a mensagem
decrypted_text = rc4(rc4_key, ciphertext)

# Converter a mensagem descriptografada de bytes para string
mensagem_decifrada = decrypted_text.decode()

# Exibindo os resultados
print("Mensagem Original:", mensagem_original)
print("Chave RC4:", rc4_key.hex())
print("Mensagem Criptografada:", ciphertext.hex())
print("Mensagem Decifrada:", mensagem_decifrada)