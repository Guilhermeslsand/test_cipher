"""Algoritmo de criptografia utilizando cifra de César"""
import random


class CryptoDummy:
    def __init__(self) -> None:
        """
        Classe para fazer a criptografia de forma burra

        params:
            - textoCifrado: Armazena o texto após a cifragem
            - textoDecifrado: Armazena o texto decifrado
        """
        self.textoCifrado = None
        self.textoDecifrado = None

    @staticmethod
    def create_key(file_key: str):
        """
        Função para gerar a chave para o alogirmos dummy e salvar em um arquivo

        params:
            - file_key: Caminho do arquivo onde está a chave de decifragem
        """
        key = random.randint(1, 100)
        try:
            with open(file_key, "w") as f:
                f.write(str(key))
        except OSError as e:
            print(f"Erro ao gerar chave (arquivo inválido ou problema de escrita): {e}")

    @staticmethod
    def read_key(file_key: str) -> int:
        """
        Função para gerar a chave para o alogirmos dummy e salvar em um arquivo

        params:
            - file_key: Caminho do arquivo onde está a chave de decifragem
        """
        try:
            with open(file_key, "r") as f:
                return int(f.read())
        except FileNotFoundError:
            print(f"Arquivo de chave não encontrado: {file_key}")
        except ValueError:
            print(f"Chave inválida no arquivo: {file_key}")
        except OSError as e:
            print(f"Erro ao ler arquivo de chave: {e}")
        return 0

    def cipher(self, texto: str, file_key: str):
        """
        Gerar a cifra a partir do texto e da chave

        params:
            - texto (str): Mensagem que vai ser decifrada
            - file_key (str): Caminho do arquivo onde está a chave de decifragem
        """
        try:
            texto = texto.encode("utf-8")
            key = self.read_key(file_key)
            if key == 0:
                print("Não existe uma chave para criptografar")
                raise ValueError
            self.textoCifrado = bytes([(b + key) % 256 for b in texto])
        except TypeError as e:
            print(f"Erro ao criptografar: {e}")

    def decipher(self, cifrado: bytes, file_key: str):
        """
        Decifrando o texto cifrado

        params:
            - cifrado (bytes): Texto cifrado pelo algoritimo AES
            - file_key (str): Caminho do arquivo onde está a chave de decifragem
        """
        try:
            key = self.read_key(file_key)
            if key == 0:
                print("Não existe uma chave para descifrar")
                return 0
            self.textoDecifrado = bytes([(b - key) % 256 for b in cifrado])
        except TypeError as e:
            print(f"Erro ao descriptografar: {e}")

    def get_texto_cifrado(self) -> bytes:
        """Retorna o texto cifrado"""
        return self.textoCifrado

    def get_texto_decifrado(self) -> bytes:
        """Retorna o texto decifrado"""
        return self.textoDecifrado
