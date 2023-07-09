from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Gera o par de chaves RSA
# Entrada: prefixo dos arquivos; caminho de salvamento personalizado
# Saída: nada
def generate_key_pair(prefix = "", path = ""):
    try:
        # Gera uma chave privada RSA com tamanho de chave de 2048 bits e expoente público de 65537
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        # Obtém a chave pública correspondente
        public_key = private_key.public_key()

        # Serializa a chave privada no formato PEM sem criptografia
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Serializa a chave pública no formato PEM
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # Define os nomes dos arquivos de chave a serem salvos
        if prefix == "":
            private_file_name = "private_key.pem"
            public_file_name = "public_key.pem"
        else:
            private_file_name = prefix + "_private_key.pem"
            public_file_name = prefix + "_public_key.pem"
        
        # Salva a chave privada em um arquivo
        with open(path + private_file_name, 'wb') as f:
            f.write(pem_private_key)

        # Salva a chave pública em um arquivo
        with open(path + public_file_name, 'wb') as f:
            f.write(pem_public_key)

        print(f"\n> > Par de chaves criado com sucesso!\n")
    except Exception as e:
        raise Exception("! Erro ao gerar o par de chaves RSA:", e)

# Carrega a chave pública RSA
# Entrada: caminho para o arquivo .pem
# Saída: chave pública
def load_public_key(public_key_path):
    try:
        # Carrega a chave pública a partir do arquivo PEM
        with open(public_key_path, "rb") as f:
            key = serialization.load_pem_public_key(f.read())
    except FileNotFoundError:
        raise FileNotFoundError("! Arquivo da chave pública não encontrado")
    except Exception as e:
        raise Exception("! Erro ao carregar a chave pública:", e)
    return key

# Carrega a chave privada RSA
# Entrada: caminho para o arquivo .pem
# Saída: chave privada
def load_private_key(private_key_path, password=None):
    try:
        # Carrega a chave privada a partir do arquivo PEM
        with open(private_key_path, "rb") as f:
            key = serialization.load_pem_private_key(
                f.read(),
                password=password
            )

    except FileNotFoundError:
        raise FileNotFoundError("! Arquivo da chave privada não encontrado")
    
    except Exception as e:
        raise Exception("! Erro ao carregar a chave privada:", e)
    return key

# Criptografa os dados usando a chave pública RSA
# Entrada: chave pública, arquivo em claro
# Saída: arquivo cifrado
def encrypt(public_key, plain_file):
    try:
        # Criptografa o arquivo usando o esquema de padding OAEP
        cipher_file = public_key.encrypt(
            plain_file,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return cipher_file
    except Exception as e:
        raise Exception("! Erro ao criptografar a chave simétrica:", e)

# Descriptografa os dados usando a chave privada RSA
# Entrada: chave privada, arquivo cifrado
# Saída: arquivo em claro
def decrypt(private_key, cipher_file):
    try:
        # Descriptografa o arquivo usando o esquema de padding OAEP
        plain_file = private_key.decrypt(
            cipher_file,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return plain_file
    except Exception as e:
        raise Exception("! Erro ao descriptografar a chave simétrica:", e)


if __name__ == '__main__':
    # # Exemplo de uso
    # plaintext = b'Dados a serem criptografados'

    # # Gera um par de chaves RSA
    # #private_key, public_key = rsa_generate_key_pair()

    # public_key_path = "public_key.pem"
    # private_key_path = "private_key.pem"
    # public_key = load_public_key(public_key_path)
    # private_key = load_private_key(private_key_path)

    # # Criptografa os dados usando a chave pública
    # ciphertext = encrypt(public_key, plaintext)
    # print("Texto cifrado:", ciphertext)

    # # Descriptografa os dados usando a chave privada
    # decrypted_text = decrypt(private_key, ciphertext)
    # print("Texto descriptografado:", decrypted_text)
    generate_key_pair("ellem")