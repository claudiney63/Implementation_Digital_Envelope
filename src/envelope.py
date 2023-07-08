if __name__ == '__main__':
    import aes
    import des
    import rc4
    import rsa
    import utils
else:
    import src.aes as aes
    import src.des as des
    import src.rc4 as rc4
    import src.rsa as rsa
    import src.utils as utils

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey

def create_envelope(plain_file_path, public_key_path, algorithm):
    public_key = rsa.load_public_key(public_key_path)
    plain_file = utils.open_file(plain_file_path)
    if not isinstance(public_key, RSAPublicKey):
        raise Exception("A chave pública não é válida")
        
    if(algorithm == 'AES'):
        simetric_key = aes.generate_key(32)
        encrypted_file = aes.encrypt(simetric_key, plain_file)
    
    elif(algorithm == 'DES'):
        simetric_key = des.generate_key(32)
        encrypted_file = des.encrypt(simetric_key, plain_file)
    
    elif(algorithm == 'RC4'):
        simetric_key = rc4.generate_rc4_key()
        encrypted_file = rc4.encrypt_decrypt(simetric_key, plain_file)
    
    else:
        raise Exception("Algoritmo simétrico não econtrado")

    encrypted_key = rsa.encrypt(public_key, simetric_key)

    utils.save_file("encrypted_simetric_key.key", encrypted_key)
    utils.save_file("encrypted_" + plain_file_path, encrypted_file)

def open_envelope(encrypted_file_path,encrypted_key_path, private_key_path, algorithm):
    private_key = rsa.load_private_key(private_key_path)
    encrypted_key = utils.open_file(encrypted_key_path)
    encrypted_file = utils.open_file(encrypted_file_path)

    simetric_key = rsa.decrypt(private_key, encrypted_key)
    
    if(algorithm == 'AES'):
        decrypted_file = aes.decrypt(simetric_key, encrypted_file)

    elif(algorithm == 'DES'):
        decrypted_file = des.decrypt(simetric_key, encrypted_file)
    
    elif(algorithm == 'RC4'):
        decrypted_file = des.decrypt(simetric_key, encrypted_file) #MODIFICAR

    else:
        raise Exception("Algoritmo simétrico não econtrado")

    utils.save_file("decrypted_" + encrypted_file_path, decrypted_file)

if __name__ == '__main__':
    #cifrar
    # try:
    #     create_envelope("image.png", "ellem_public_key.pem", "AES")
    # except Exception as e:
    #     print(e)

    
    #decifrar
    try:
        open_envelope("encrypted_image.png", "encrypted_simetric_key.key", "ellem_private_key.pem","AES")
    except Exception as e:
        print(e)


    print("fim")


