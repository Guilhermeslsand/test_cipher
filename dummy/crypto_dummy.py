import random


class CryptoDummy:
    """ "
    classe para fazer a criptografia de forma burra
    """

    def __init__(self) -> None:
        self.textoCifrado = None
        self.textoDecifrado = None

    def gerarChave(self, file: str):
        """Gerar a chave de criptografia"""
        dk = random.randint(1, 100)
        try:
            with open(file, "w") as f:
                f.write(str(dk))
        except Exception as e:
            print(f"Erro ao gerar chave:{e}")

    def carregarChave(self, file: str) -> int:
        """Carregar a chave de criptografia"""
        try:
            with open(file, "r") as f:
                return f.read()
        except Exception as e:
            print(f"Erro ao carregar_chave:{e}")
            return 0

    def gerarCifra(self, texto: str, file: str):
        """Gerar a cifra a partir do texto e da chave"""
        try:
            texto = texto.encode("utf-8")
            chave = int(self.carregarChave(file))
            if chave == 0:
                print("Não existe uma chave para criptografar")
                return 0
            self.textoCifrado = bytes([(b + chave) % 256 for b in texto])
        except Exception as e:
            print(f"Erro decifrar texto:{e}")

    def gerarDecifra(self, cifrado: bytes, file: str):
        """Gerar a decifra a partir do texto e da chave"""
        try:
            chave = int(self.carregarChave(file))
            if chave == 0:
                print("Não existe uma chave para descifrar")
                return 0
            self.textoDecifrado = bytes([(b - chave) % 256 for b in cifrado])
            return self.textoDecifrado
        except Exception as e:
            print(f"Erro ao decifrar texto:{e}")
            return 0

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
