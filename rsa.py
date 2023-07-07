from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

def rsa_generate_key_pair():
    # Gera um par de chaves RSA
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Serializa a chave privada no formato PEM
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

    return pem_private_key, pem_public_key

def rsa_load_public_key(public_key_path):
    # Carrega a chave pública RSA a partir do arquivo PEM
    print("teste")
    with open(public_key_path, "rb") as f:
        return serialization.load_pem_public_key(f.read())

def rsa_load_private_key(private_key_path, password=None):
    # Carrega a chave privada RSA a partir do arquivo PEM
    with open(private_key_path, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=password
        )
    return private_key

def rsa_encrypt(public_key, plaintext):
    # Carrega a chave pública RSA
    #public_key = serialization.load_pem_public_key(public_key)

    # Criptografa os dados usando a chave pública RSA
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return ciphertext

def rsa_decrypt(private_key, ciphertext):
    # Carrega a chave privada RSA
    #private_key = serialization.load_pem_private_key(private_key, password=None)

    # Descriptografa os dados usando a chave privada RSA
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext

# Exemplo de uso
plaintext = b'Dados a serem criptografados'

# Gera um par de chaves RSA
#private_key, public_key = rsa_generate_key_pair()

public_key_path = "public_key.pem"
private_key_path = "private_key.pem"
public_key = rsa_load_public_key(public_key_path)
private_key = rsa_load_private_key(private_key_path)

# Criptografa os dados usando a chave pública
ciphertext = rsa_encrypt(public_key, plaintext)
print("Texto cifrado:", ciphertext)

# Descriptografa os dados usando a chave privada
decrypted_text = rsa_decrypt(private_key, ciphertext)
print("Texto descriptografado:", decrypted_text)