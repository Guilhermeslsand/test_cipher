from dummy.crypto_dummy import CryptoDummy
#https://portswigger.net/web-security
class CryptoTest:

    def __init__(self):
        pass
    
    @staticmethod
    def testar_dummy(caminho_chave:str, texto: str):
        dummy = CryptoDummy()
        print('#-----------Algoritmo Dummy-----------#')
        print('#--------Usando cifra de César--------#')
        dummy.gerarChave(caminho_chave)
        print(f"Texto original:{texto}")
        dummy.gerarCifra(texto, caminho_chave)
        print(f"Texto cifrado:{dummy.get_texto_cifrado().hex()}")
        dummy.gerarDecifra(dummy.get_texto_cifrado(), caminho_chave)
        print(f"Texto decifrado:{dummy.get_texto_decifrado()}")
        print('#-------------------------------------#')