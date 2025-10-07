import os
from crypto_exceptions import (
    DecryptionError,
    EncryptionError,
    KeyGenerationError,
    KeyLoadError,
)
from dummy.crypto_dummy import CryptoDummy


class FileCryptoTest:
    def __init__(self, arquivo: str):
        """
        Classe para realizar criptografia de arquivos txt

        paramans:
            - texto (str): Texto para criptografar.
        """
        self.caminho = "/test_crypto/test_file/"
        self.arquivo = arquivo
        self.caminho_completo = os.path.join(self.caminho, self.arquivo)

        print("--------------------------------------------------------")
        print(">>> Arquivo para criptografar...")
        print("Caminho do arquivo:")
        print(self.caminho_completo)

    def cifrar_with_dummy(self, file_key: str):
        try:
            dummy = CryptoDummy()
            print(">>>> Cifrando com o algoritmo Dummy...\n")
            dummy.create_key(file_key)
            cipher_path = os.path.join(self.caminho, "cipher_dummy.txt")
            dummy.cipher_file(self.caminho_completo, cipher_path, file_key)

            print(">>>> Decifrando com algoritmo Dummy...\n")
            dummy.decipher_file(cipher_path)
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
