import os

def generate_rc4_key(key_length=16):
    """
    Gera uma chave aleatória para o algoritmo RC4.

    Args:
        key_length (int): O tamanho da chave em bytes. O padrão é 16.

    Returns:
        bytes: A chave gerada.
    """
    key = os.urandom(key_length)  # Gera uma sequência de bytes aleatórios como chave
    return key

def rc4(key, plaintext):
    """
    Criptografa ou descriptografa um texto usando o algoritmo RC4.

    Args:
        key (bytes): A chave para o algoritmo RC4.
        plaintext (bytes): O texto a ser criptografado ou descriptografado.

    Returns:
        bytes: O texto criptografado ou descriptografado.
    """
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

if __name__ == '__main__':
    rc4_key = generate_rc4_key()
    mensagem_original = "Essa é uma mensagem de teste para criptografia com RC4."
    plaintext = mensagem_original.encode()
    ciphertext = rc4(rc4_key, plaintext)
    decrypted_text = rc4(rc4_key, ciphertext)

    # Converter a mensagem descriptografada de bytes para string
    mensagem_decifrada = decrypted_text.decode()

    print("Mensagem Original:", mensagem_original)
    print("Chave RC4:", rc4_key.hex())
    print("Mensagem Criptografada:", ciphertext.hex())
    print("Mensagem Decifrada:", mensagem_decifrada)
