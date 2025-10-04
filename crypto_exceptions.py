"""Exceções customizadas para operações criptográficas"""


class CryptoBaseException(Exception):
    """Exceção base para erros de criptografia"""

    pass


class KeyGenerationError(CryptoBaseException):
    """Erro ao gerar chaves"""

    pass


class KeyLoadError(CryptoBaseException):
    """Erro ao carregar chaves"""

    pass


class EncryptionError(CryptoBaseException):
    """Erro ao cifrar dados"""

    pass


class DecryptionError(CryptoBaseException):
    """Erro ao decifrar dados"""

    pass
