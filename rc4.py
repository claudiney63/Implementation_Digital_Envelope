import os

def generate_rc4_key(key_length):
    #key_length = 16  # Define o tamanho da chave em bytes
    key = os.urandom(key_length)  # Gera uma sequência de bytes aleatórios como chave
    return key

def encrypt_decrypt(key, plaintext):
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

# def generate_key(size):
#     return os.urandom(size)

if __name__ == '__main__':

    rc4_key = generate_rc4_key()
    mensagem_original = "Essa é uma mensagem de teste para criptografia com RC4."
    plaintext = mensagem_original.encode()
    ciphertext = rc4(rc4_key, plaintext)
    #ciphertext = bytes.fromhex('1ebd618d8ebdf84e8037de076f9e3eed3d8d9405d6abcaddf9de9eb5881f3993334e56e08338693a7065da0b3a6b228b4fb5088d5d5672ce')
    decrypted_text = rc4(rc4_key, ciphertext)

    # Converter a mensagem descriptografada de bytes para string
    mensagem_decifrada = decrypted_text.decode()

    print("Mensagem Original:", mensagem_original)
    print("Chave RC4:", rc4_key.hex())
    print("Mensagem Criptografada:", ciphertext.hex())
    print("Mensagem Decifrada:", mensagem_decifrada)