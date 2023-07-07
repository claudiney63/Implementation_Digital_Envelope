from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
# from Crypto.Cipher import PKCS1_OAEP
# from Crypto.PublicKey import RSA
import os


def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return private_pem, public_pem


def create_envelope(plain_file, recipient_public_key, symmetric_algorithm):
    # Generate temporary symmetric key
    symmetric_key = os.urandom(32)
    
    # Read recipient's public key
    recipient_public_key = serialization.load_pem_public_key(
        recipient_public_key,
        backend=default_backend()
    )
    
    # Encrypt the symmetric key with recipient's public key
    ciphertext_key = recipient_public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Encrypt the plain file with the symmetric key
    cipher = Cipher(symmetric_algorithm(symmetric_key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext_file = encryptor.update(plain_file) + encryptor.finalize()
    
    return ciphertext_key, ciphertext_file


def open_envelope(ciphertext_file, ciphertext_key, recipient_private_key, symmetric_algorithm):
    # Read recipient's private key
    recipient_private_key = serialization.load_pem_private_key(
        recipient_private_key,
        password=None,
        backend=default_backend()
    )
    
    # Decrypt the symmetric key with recipient's private key
    decrypted_key = recipient_private_key.decrypt(
        ciphertext_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    # Decrypt the ciphertext file with the symmetric key
    cipher = Cipher(symmetric_algorithm(decrypted_key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext_file = decryptor.update(ciphertext_file) + decryptor.finalize()
    
    return plaintext_file


# Exemplo de uso:

# Geração das chaves RSA
private_key, public_key = generate_key_pair()

# Dados de exemplo
plain_file = b'This is a sample plain file.'
symmetric_algorithm = algorithms.AES

# Criação do envelope
ciphertext_key, ciphertext_file = create_envelope(plain_file, public_key, symmetric_algorithm)

# Abertura do envelope
plaintext_file = open_envelope(ciphertext_file, ciphertext_key, private_key, symmetric_algorithm)

# Exibição dos resultados
print("Plaintext file:")
print(plaintext_file.decode())
print()
print("Ciphertext key:")
print(ciphertext_key)
print()
print("Ciphertext file:")
print(ciphertext_file)
