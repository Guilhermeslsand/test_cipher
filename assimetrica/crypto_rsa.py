from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from crypto_exceptions import (
    KeyGenerationError,
    KeyLoadError,
    EncryptionError,
    DecryptionError,
)


class CryptoRSA:
    def __init__(self):
        """
        Classe para fazer a criptografia com o algoritmo AES de chave simétrica

        params:
            - textoCifrado: Armazena o texto após a cifragem
            - textoDecifrado: Armazena o texto descifrado
        """
        self.textoCifrado = None
        self.textoDecifrado = None

    @staticmethod
    def crete_key(file_private_key: str, file_public_key: str):
        """
        Função para gerar as chaves privada e pública e salvar em um arquivo

        params:
            - file_private_key: Caminho do arquivo onde está a chave privada
            - file_public_key: Caminho do arquivo onde está a chave pública

        raises:
            - KeyGenerationError: Se houver erro ao gerar ou salvar as chaves
        """
        try:
            # Gerando a chave privada
            private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

            with open(file_private_key, "wb") as f:
                f.write(
                    private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                )
        except OSError as e:
            raise KeyGenerationError(
                f"Erro ao salvar chave particular no arquivo: {e}"
            ) from e

        except Exception as e:
            raise KeyGenerationError(
                f"Erro inesperado ao gerar chave particular: {e}"
            ) from e

        try:
            public_key = private_key.public_key()
            with open(file_public_key, "wb") as f:
                f.write(
                    public_key.public_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PublicFormat.SubjectPublicKeyInfo,
                    )
                )
        except OSError as e:
            raise KeyGenerationError(
                f"Erro ao salvar chave particular no arquivo: {e}"
            ) from e

        except Exception as e:
            raise KeyGenerationError(
                f"Erro inesperado ao gerar chave particular: {e}"
            ) from e

    @staticmethod
    def read_private_key(file_private_key: str):
        """
        Função para ler a chave privada

        params:
            - file_private_key: Caminho do arquivo onde está a chave privada

        raises:
            - KeyLoadError: Se houver erro ao carregar a chave
        """
        try:
            with open(file_private_key, "rb") as f:
                priv_pem = f.read()
            return serialization.load_pem_private_key(priv_pem, password=None)

        except FileNotFoundError as e:
            raise KeyLoadError(
                f"Arquivo de chave privada não encontrado: {file_private_key}"
            ) from e
        except (ValueError, TypeError) as e:
            raise KeyLoadError(
                f"Arquivo de chave privada inválido ou corrompido: {e}"
            ) from e
        except Exception as e:
            raise KeyLoadError(f"Erro inesperado ao carregar chave privada: {e}") from e

    @staticmethod
    def read_public_key(file_public_key: str):
        """
        Função para ler a chave pública

        params:
            - file_public_key: Caminho do arquivo onde está a chave pública

        raises:
            - KeyLoadError: Se houver erro ao carregar a chave
        """
        try:
            with open(file_public_key, "rb") as f:
                pub_pem = f.read()
                return serialization.load_pem_public_key(pub_pem)

        except FileNotFoundError as e:
            raise KeyLoadError(
                f"Arquivo de chave pública não encontrado: {file_public_key}"
            ) from e
        except ValueError as e:
            raise KeyLoadError(
                f"Arquivo de chave pública inválido ou corrompido: {e}"
            ) from e
        except Exception as e:
            raise KeyLoadError(f"Erro inesperado ao carregar chave pública: {e}") from e

    def cipher(self, texto: str, file_public_key: str):
        """
        Gerar a cifra a partir do texto e da chave

        params:
            - texto (str): Mensagem que vai ser decifrada
            - file_public_key (str): Caminho do arquivo onde está a chave pública

        raises:
            - EncryptionError: Se houver erro ao cifrar
        """
        try:
            texto = texto.encode("utf-8")
            key = self.read_public_key(file_public_key)
            self.textoCifrado = key.encrypt(
                texto,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )

        except KeyLoadError:
            raise
        except (ValueError, TypeError) as e:
            raise EncryptionError(f"Erro ao cifrar texto: {e}") from e
        except UnicodeEncodeError as e:
            raise EncryptionError(f"Erro ao codificar texto em UTF-8: {e}") from e
        except Exception as e:
            raise EncryptionError(f"Erro inesperado durante cifragem: {e}") from e

    def decipher(self, cifrado: bytes, file_private_key: str):
        """
        Decifrando o texto cifrado

        params:
            - cifrado (bytes): Texto cifrado pelo algoritimo RSA
            - file_private_key (str): Caminho do arquivo onde está a chave privada

        raises:
            - DecryptionError: Se houver erro ao decifrar
        """
        if cifrado is None:
            raise DecryptionError("Nenhum texto cifrado fornecido")

        try:
            key = self.read_private_key(file_private_key)
            self.textoDecifrado = key.decrypt(
                cifrado,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
        except KeyLoadError:
            raise
        except (ValueError, TypeError) as e:
            raise DecryptionError(
                f"Erro ao decifrar texto (chave incorreta ou texto corrompido): {e}"
            ) from e
        except Exception as e:
            raise DecryptionError(f"Erro inesperado durante decifragem: {e}") from e

    def get_texto_cifrado(self) -> bytes:
        """Retorna o texto cifrado"""
        return self.textoCifrado

    def get_texto_decifrado(self) -> bytes:
        """Retorna o texto decifrado"""
        return self.textoDecifrado
