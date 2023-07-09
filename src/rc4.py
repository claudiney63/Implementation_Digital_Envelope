import os

def generate_rc4_key(key_length=16):
    """
    Gera uma chave aleatória para o algoritmo RC4.

    Args:
        key_length (int): O tamanho da chave em bytes. O padrão é 16.

    Returns:
        bytes: A chave gerada.
    """
    try:
        key = os.urandom(key_length)  # Gera uma sequência de bytes aleatórios como chave
        return key
    except Exception as e:
        raise Exception("Erro ao gerar a chave RC4:", e)

def encrypt_decrypt(key, plain_file):
    """
    Criptografa ou descriptografa um texto usando o algoritmo RC4.

    Args:
        key (bytes): A chave para o algoritmo RC4.
        plaintext (bytes): O texto a ser criptografado ou descriptografado.

    Returns:
        bytes: O texto criptografado ou descriptografado.
    """
    try:
        S = list(range(256))  # Inicializa uma lista de 256 elementos com valores de 0 a 255
        j = 0
        out = []

        # Key-scheduling algorithm (KSA)
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256  # Gera um valor de j baseado na chave e nos valores atuais de j e S[i]
            S[i], S[j] = S[j], S[i]  # Troca os valores de S[i] e S[j] para embaralhar a lista S

        # Pseudo-random generation algorithm (PRGA)
        i = j = 0
        for char in plain_file:
            i = (i + 1) % 256  # Atualiza o valor de i
            j = (j + S[i]) % 256  # Atualiza o valor de j
            S[i], S[j] = S[j], S[i]  # Troca os valores de S[i] e S[j] para embaralhar a lista S novamente
            out.append(char ^ S[(S[i] + S[j]) % 256])  # Realiza a operação XOR entre o caractere e um valor pseudoaleatório de S

        return bytes(out)  # Retorna o texto criptografado ou descriptografado em formato de bytes
    except Exception as e:
        raise Exception("Erro ao executar o algoritmo RC4:", e)

if __name__ == '__main__':
    try:
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

    except Exception as e:
        print("Erro:", e)
