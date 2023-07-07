import aes
import des
import rc4
import rsa
import utils

def create_envelope(plain_file, public_key, algorithm):

    if(algorithm == 'AES'):
        key = aes.generate_key(32)
        cipher_file = aes.encrypt(key, plain_file)
    
    if(algorithm == 'DES'):
        des.generate_key(32)
        cipher_file = des.encrypt(key, plain_file)
    
    if(algorithm == 'RC4'):
        rc4.generate_rc4_key()
        cipher_file = rc4.encrypt_decrypt(key, plain_file)
    
    cipher_key = rsa.encrypt(public_key, key)

    utils.save_file("cipher_key", cipher_key)
    utils.save_file("cipher_file", cipher_file)

def open_envelope(cipher_file, cipher_key, algorithm, private_key):
    key = rsa.decrypt(private_key, cipher_key)
    
    if(algorithm == 'AES'):
        plain_file = aes.decrypt(key, cipher_file)

    if(algorithm == 'DES'):
        plain_file = des.decrypt(key, cipher_file)
    
    if(algorithm == 'RC4'):
        plain_file = des.decrypt(key, cipher_file) #MODIFICAR

    utils.save_file("plain_file.txt", plain_file)

if __name__ == '__main__':
    #cifrar
    #public_key = rsa.load_public_key("public_key.pem")
    #create_envelope(b"Chocolate da Ellem", public_key, "AES")

    #decifrar
    cipher_file = utils.open_file("cipher_file")
    cipher_key = utils.open_file("cipher_key")

    private_key = rsa.load_private_key("private_key.pem")
    open_envelope(cipher_file, cipher_key, "AES", private_key)


