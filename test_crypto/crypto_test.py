import base64
from crypto_exceptions import (
    DecryptionError,
    EncryptionError,
    KeyGenerationError,
    KeyLoadError,
)
from simetrica.crypto_aes import CryptoAes
from dummy.crypto_dummy import CryptoDummy
from assimetrica.crypto_rsa import CryptoRSA


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

        print("Mensagem (Hexadecimal):")
        print(self.texto.encode("UTF-8").hex())
        print(" ")

    def testar_dummy(self, file_key: str):
        try:
            dummy = CryptoDummy()
            print(">>>> Cifrando com o algoritmo Dummy...\n")
            dummy.create_key(file_key)
            dummy.cipher(self.texto, file_key)

            cifrado = base64.b64encode(dummy.get_texto_cifrado())
            print("Mensagem cifrada (Hexadecimal):")
            print(cifrado.hex())
            print("Mensagem cifrado (String):")
            print(cifrado.decode("utf-8"))
            print(" ")

            print(">>>> Decifrando com algoritmo Dummy...\n")
            dummy.decipher(dummy.get_texto_cifrado(), file_key)
            decifrado = dummy.get_texto_decifrado()
            print("Mensagem Decifrada (Hexadecimal):")
            print(decifrado.hex())
            print("Mensagem Decifrada (String):")
            print(decifrado.decode("utf-8"))
            print(" ")
        except KeyGenerationError as e:
            print(f"Erro ao gerar chaves: {e}")
        except KeyLoadError as e:
            print(f"Erro ao carregar chaves: {e}")
        except EncryptionError as e:
            print(f"Erro ao cifrar: {e}")
        except DecryptionError as e:
            print(f"Erro ao decifrar: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def testar_aes(self, file_key: str):
        try:
            aes = CryptoAes()
            print(">>>> Cifrando com o algoritmo AES...\n")
            aes.create_key(file_key)
            aes.cipher(self.texto, file_key)

            cifrado = base64.b64encode(aes.get_texto_cifrado())
            print("Mensagem cifrada (Hexadecimal):")
            print(cifrado.hex())
            print("Mensagem cifrado (String):")
            print(cifrado.decode("utf-8"))
            print(" ")

            print(">>>> Decifrando com algoritmo AES...\n")
            aes.decipher(aes.get_texto_cifrado(), file_key)
            decifrado = aes.get_texto_decifrado()
            print("Mensagem Decifrada (Hexadecimal):")
            print(decifrado.hex())
            print("Mensagem Decifrada (String):")
            print(decifrado.decode("utf-8"))
            print(" ")
        except KeyGenerationError as e:
            print(f"Erro ao gerar chaves: {e}")
        except KeyLoadError as e:
            print(f"Erro ao carregar chaves: {e}")
        except EncryptionError as e:
            print(f"Erro ao cifrar: {e}")
        except DecryptionError as e:
            print(f"Erro ao decifrar: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

    def testar_rsa(self, file_private_key: str, file_public_key: str):
        try:
            rsa = CryptoRSA()
            print(">>>> Cifrando com o algoritmo RSA...\n")
            rsa.crete_key(file_private_key, file_public_key)
            rsa.cipher(self.texto, file_public_key)

            cifrado = base64.b64encode(rsa.get_texto_cifrado())
            print("Mensagem cifrada (Hexadecimal):")
            print(cifrado.hex())
            print("Mensagem cifrado (String):")
            print(cifrado.decode("utf-8"))
            print(" ")

            print(">>>> Decifrando com algoritmo RSA...\n")
            rsa.decipher(rsa.get_texto_cifrado(), file_private_key)
            decifrado = rsa.get_texto_decifrado()
            print("Mensagem Decifrada (Hexadecimal):")
            print(decifrado.hex())
            print("Mensagem Decifrada (String):")
            print(decifrado.decode("utf-8"))
            print(" ")
        except KeyGenerationError as e:
            print(f"Erro ao gerar chaves: {e}")
        except KeyLoadError as e:
            print(f"Erro ao carregar chaves: {e}")
        except EncryptionError as e:
            print(f"Erro ao cifrar: {e}")
        except DecryptionError as e:
            print(f"Erro ao decifrar: {e}")
        except Exception as e:
            print(f"Erro inesperado: {e}")
