"""Algoritmo de criptografia com chave simétrica"""
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag


class CryptoAes:
    def __init__(self):
        """
        Classe para fazer a criptografia com o algoritmo AES de chave simétrica

        params:
            - textoCifrado: Armazena o texto após a cifragem
            - textoDecifrado: Armazena o texto decifrado
        """
        self.textoCifrado = None
        self.textoDecifrado = None

    @staticmethod
    def create_key(file_key: str):
        """
        Função para gerar a chave para o alogirmos AES e salvar em um arquivo

        params:
            - file_key: Caminho do arquivo onde está a chave de decifragem
        """
        key = AESGCM.generate_key(bit_length=256)  # 256 bits
        try:
            with open(file_key, "wb") as f:
                f.write(key)
        except OSError as e:
            print(f"Erro ao salvar a chave no arquivo: {e}")

    @staticmethod
    def read_key(file_key: str) -> bytes:
        """
        Função para ler a chave usada para decifrar

        params:
            - file_key: Caminho do arquivo onde está a chave de decifragem
        """
        try:
            with open(file_key, "rb") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Arquivo de chave não encontrado: {file_key}")
        except OSError as e:
            print(f"Erro ao ler arquivo de chave: {e}")
        return None

    def cipher(self, texto: str, file_key: str):
        """
        Gerar a cifra a partir do texto e da chave

        params:
            - texto (str): Mensagem que vai ser decifrada
            - file_key (str): Caminho do arquivo onde está a chave de decifragem
        """
        try:
            # Convertento texto em bytes
            texto = texto.encode("utf-8")

            key = self.read_key(file_key)
            aesgcm = AESGCM(key)
            if not key:
                print("Erro ao ler a cave")
                raise ValueError

            # Nonce
            # Usado para gerar valores diferentes para para cada cifragem
            nonce = os.urandom(12)  # 96 bits

            # Cifrar
            textoCifrado = aesgcm.encrypt(nonce, texto, None)
            self.textoCifrado = nonce + textoCifrado
        except (ValueError, TypeError) as e:
            print(f"Erro ao cifrar o texto: {e}")

    def decipher(self, cifrado: bytes, file_key: str):
        """
        Decifrando o texto cifrado

        params:
            - cifrado (bytes): Texto cifrado pelo algoritimo AES
            - file_key (str): Caminho do arquivo onde está a chave de decifragem
        """
        try:
            key = self.read_key(file_key)
            if not key:
                print("Não existe uma chave para decifrar")
                raise ValueError

            aesgcm = AESGCM(key)
            nonce = cifrado[:12]
            textoCifrado = cifrado[12:]
            self.textoDecifrado = aesgcm.decrypt(nonce, textoCifrado, None)

        except InvalidTag:
            print(
                "Falha na autenticação do AES-GCM: dados alterados ou chave incorreta"
            )
        except (ValueError, TypeError) as e:
            print(f"Erro ao decifrar o texto: {e}")

    def get_texto_cifrado(self) -> bytes:
        """
        Retorna o texto cifrado em formato string
        """
        return self.textoCifrado

    def get_texto_decifrado(self) -> bytes:
        """Retorna o texto decifrado em string UTF-8"""
        return self.textoDecifrado
