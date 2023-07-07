from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Gerar um par de chaves RSA
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Serializar a chave privada em formato PEM
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Serializar a chave pública em formato PEM
public_key = private_key.public_key()
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Salvar as chaves em arquivos
with open('private_key.pem', 'wb') as f:
    f.write(pem_private_key)

with open('public_key.pem', 'wb') as f:
    f.write(pem_public_key)
