from test_crypto.crypto_test import CryptoTest

def __main__():
    test = CryptoTest()
    # Testando a dummy
    texto = "Cifrando com algoritmo dummy"
    test.testar_dummy("dummy\chave_dummy.txt", texto)

__main__()