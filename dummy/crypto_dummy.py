"""Algoritmo de criptografia utilizando cifra de César"""
import base64
import random

from crypto_exceptions import (
    DecryptionError,
    EncryptionError,
    KeyGenerationError,
    KeyLoadError,
)


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
            raise KeyGenerationError(f"Erro ao salvar chave no arquivo: {e}") from e

        except Exception as e:
            raise KeyGenerationError(f"Erro inesperado ao gerar chave{e}") from e

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
        except FileNotFoundError as e:
            raise KeyLoadError(f"Arquivo de chave não encontrado: {file_key}") from e
        except (ValueError, TypeError) as e:
            raise KeyLoadError(f"Arquivo de chave inválido ou corrompido: {e}") from e
        except Exception as e:
            raise KeyLoadError(f"Erro inesperado ao carregar chave: {e}") from e

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
        except KeyLoadError:
            raise
        except (ValueError, TypeError) as e:
            raise EncryptionError(f"Erro ao cifrar texto: {e}") from e
        except UnicodeEncodeError as e:
            raise EncryptionError(f"Erro ao codificar texto em UTF-8: {e}") from e
        except Exception as e:
            raise EncryptionError(f"Erro inesperado durante cifragem: {e}") from e

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
        except KeyLoadError:
            raise
        except (ValueError, TypeError) as e:
            raise DecryptionError(
                f"Erro ao decifrar texto (chave incorreta ou texto corrompido): {e}"
            ) from e
        except Exception as e:
            raise DecryptionError(f"Erro inesperado durante decifragem: {e}") from e

    def cipher_file(self, file_path: str, cipher_path: str, file_key: str):
        """
        Gera a cifra a partir do conteúdo de um arquivo e da chave.

        Params:
            - file_path (str): Caminho do arquivo de texto a ser cifrado.
            - cipher_path (str): Caminho onde salvar arquivo cifrado
            - file_key (str): Caminho do arquivo onde está a chave de cifragem.
        """
        try:
            # Lê o conteúdo do arquivo
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    texto = f.read()
            except FileNotFoundError:
                raise EncryptionError(f"Arquivo não encontrado: {file_path}")

            texto_bytes = texto.encode("utf-8")

            key = self.read_key(file_key)
            self.textoCifrado = bytes([(b + key) % 256 for b in texto_bytes])
            base64.b64encode(self.textoCifrado)

            try:
                with open(cipher_path, "w") as f:
                    f.write(self.textoCifrado.decode("utf-8"))

            except FileNotFoundError:
                raise EncryptionError(f"Erro ao gravar no arqivo: {cipher_path}")

        except KeyLoadError:
            raise
        except (ValueError, TypeError) as e:
            raise EncryptionError(f"Erro ao cifrar texto: {e}") from e
        except UnicodeEncodeError as e:
            raise EncryptionError(f"Erro ao codificar texto em UTF-8: {e}") from e
        except Exception as e:
            raise EncryptionError(f"Erro inesperado durante cifragem: {e}") from e

    def decipher_file(self, file_path: str, decipher_path: str, file_key: str):
        """
        Gera a cifra a partir do conteúdo de um arquivo e da chave.

        Params:
            - file_path (str): Caminho do arquivo de texto cifrado.
            - decipher_path (str): Caminho onde salvar arquivo decifrado
            - file_key (str): Caminho do arquivo onde está a chave de cifragem.
        """
        try:
            # Lê o conteúdo do arquivo
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    texto = f.read()

            except FileNotFoundError:
                raise EncryptionError(f"Arquivo não encontrado: {file_path}")

            texto_bytes = texto.encode("utf-8")

            key = self.read_key(file_key)
            self.textoDecifrado = bytes([(b - key) % 256 for b in texto_bytes])
            self.textoDecifrado = self.textoDecifrado.decode("utf-8")
            try:
                with open(decipher_path, "w") as f:
                    f.write(self.textoCifrado)

            except FileNotFoundError:
                raise EncryptionError(f"Erro ao gravar no arqivo: {decipher_path}")

        except KeyLoadError:
            raise
        except (ValueError, TypeError) as e:
            raise EncryptionError(f"Erro ao cifrar texto: {e}") from e
        except UnicodeEncodeError as e:
            raise EncryptionError(f"Erro ao codificar texto em UTF-8: {e}") from e
        except Exception as e:
            raise EncryptionError(f"Erro inesperado durante cifragem: {e}") from e

    def get_texto_cifrado(self) -> bytes:
        """Retorna o texto cifrado"""
        return self.textoCifrado

    def get_texto_decifrado(self) -> bytes:
        """Retorna o texto decifrado"""
        return self.textoDecifrado
