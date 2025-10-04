import base64
from simetrica.crypto_aes import CryptoAes
from dummy.crypto_dummy import CryptoDummy
from assimetrica.crypto_rsa import CryptoRSA


# https://portswigger.net/web-security
class CryptoTest:
    def __init__(self, texto: str):
        """
        Classe para realizar testes dos algoritmos de criptografia

        paramans:
            - texto (str): Texto para criptografar.
        """
        self.texto = texto

        print("--------------------------------------------------------")
        print(">>> Imprimindo mensagem original...")
        print("Mensagem (String):")
        print(self.texto)

        print("\nMensagem (Hexadecimal):")
        print(self.texto.encode("UTF-8").hex())
        print(" ")

    def testar_dummy(self, file_key: str):
        dummy = CryptoDummy()
        print(">>>> Cifrando com o algoritmo Dummy...\n")
        dummy.create_key(file_key)
        dummy.cipher(self.texto, file_key)

        cifrado = base64.b64encode(dummy.get_texto_cifrado())
        print("Mensagem cifrada (Hexadecimal):")
        print(cifrado.hex())
        print("\nMensagem cifrado (String):")
        print(cifrado.decode("utf-8"))
        print(" ")

        print(">>>> Decifrando com algoritmo Dummy...\n")
        dummy.decipher(dummy.get_texto_cifrado(), file_key)
        decifrado = dummy.get_texto_decifrado()
        print("Mensagem Decifrada (Hexadecimal):")
        print(decifrado.hex())
        print("\nMensagem Decifrada (String):")
        print(decifrado.decode("utf-8"))
        print(" ")

    def testar_aes(self, file_key: str):
        aes = CryptoAes()
        print(">>>> Cifrando com o algoritmo AES...\n")
        aes.create_key(file_key)
        aes.cipher(self.texto, file_key)

        cifrado = base64.b64encode(aes.get_texto_cifrado())
        print("Mensagem cifrada (Hexadecimal):")
        print(cifrado.hex())
        print("\nMensagem cifrado (String):")
        print(cifrado.decode("utf-8"))
        print(" ")

        print(">>>> Decifrando com algoritmo AES...\n")
        aes.decipher(aes.get_texto_cifrado(), file_key)
        decifrado = aes.get_texto_decifrado()
        print("Mensagem Decifrada (Hexadecimal):")
        print(decifrado.hex())
        print("\nMensagem Decifrada (String):")
        print(decifrado.decode("utf-8"))
        print(" ")

    def testar_rsa(self, file_private_key: str, file_public_key: str):
        rsa = CryptoRSA()
        print(">>>> Cifrando com o algoritmo RSA...\n")
        rsa.crete_key(file_private_key, file_public_key)
        rsa.cipher(self.texto, file_public_key)

        cifrado = base64.b64encode(rsa.get_texto_cifrado())
        print("Mensagem cifrada (Hexadecimal):")
        print(cifrado.hex())
        print("\nMensagem cifrado (String):")
        print(cifrado.decode("utf-8"))
        print(" ")

        print(">>>> Decifrando com algoritmo RSA...\n")
        rsa.decipher(rsa.get_texto_cifrado(), file_private_key)
        decifrado = rsa.get_texto_decifrado()
        print("Mensagem Decifrada (Hexadecimal):")
        print(decifrado.hex())
        print("\nMensagem Decifrada (String):")
        print(decifrado.decode("utf-8"))
        print(" ")

    def testar_aes_outra_chave(self, file1_key: str, file2_key: str):
        aes = CryptoAes()
        print(">>>> Cifrando com o algoritmo AES...\n")
        aes.cipher(self.texto, file1_key)

        cifrado = base64.b64encode(aes.get_texto_cifrado())
        print("Mensagem cifrada (Hexadecimal):")
        print(cifrado.hex())
        print("\nMensagem cifrado (String):")
        print(cifrado.decode("utf-8"))
        print(" ")

        print(">>>> Decifrando com algoritmo AES...\n")
        aes.decipher(aes.get_texto_cifrado(), file2_key)
        decifrado = aes.get_texto_decifrado()
        print("Mensagem Decifrada (Hexadecimal):")
        print(decifrado.hex())
        print("\nMensagem Decifrada (String):")
        print(decifrado.decode("utf-8"))
