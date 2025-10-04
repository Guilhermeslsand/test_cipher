import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class CryptoAes:
    def __init__(self):
        """
        Classe para fazer a criptografia com o algoritmo AES de chave simétrica

        params:
            - textoCifrado: Armazena o texto após a cifragem
            - textoDecifrado: Armazena o texto descifrado
        """
        self.textoCifrado = None
        self.textoDecifrado = None

    def gerarChave(self, file: str):
        # Gerarando a chave simétrica do AES
        key = AESGCM.generate_key(bit_length=256)  # 256 bits
        try:
            with open(file, "wb") as f:
                f.write(key)
        except Exception as e:
            print(f"Erro ao gerar chave:{e}")

    def carregarChave(self, file: str) -> int:
        try:
            with open(file, "rb") as f:
                return f.read()
        except Exception as e:
            print(f"Erro ao carregar a chave:{e}")

    def gerarCifra(self, texto: str, file: str):
        """Gerar a cifra a partir do texto e da chave"""
        try:
            texto = texto.encode("utf-8")
            key = self.carregarChave(file)
            aesgcm = AESGCM(key)

            # 2) Nonce
            # Usado para gerar valores diferentes para para cada cifragem
            nonce = os.urandom(12)  # 96 bits

            # # 4) Cifrar
            textoCifrado = aesgcm.encrypt(nonce, texto, None)
            self.textoCifrado = nonce + textoCifrado
        except Exception as e:
            print(f"Erro ao cifrar o texto:{e}")

    def gerarDecifra(self, cifrado: bytes, file: str):
        """Decifrando o texto cifrado"""
        try:
            key = self.carregarChave(file)
            if not key:
                print("Não existe uma chave para decifrar")
                return 0
            aesgcm = AESGCM(key)
            nonce = cifrado[:12]
            textoCifrado = cifrado[12:]
            self.textoDecifrado = aesgcm.decrypt(nonce, textoCifrado, None)
        except Exception as e:
            print(f"Erro ao decifrar o texto:{e}")

    def get_texto_cifrado(self):
        """
        Retorna o texto cifrado em formato string
        """
        return self.textoCifrado

    def get_texto_decifrado(self):
        """
        Retorna o texto decifrado em formato string
        """
        return self.textoDecifrado.decode("utf-8")
