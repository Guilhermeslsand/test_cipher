from test_crypto.crypto_test import CryptoTest
import os


def main():
    # Limpando o terminal sempre que rodar o código
    os.system("clear")

    # Classe para teste dos algoritmos de criptografia
    test = CryptoTest()

    print("-----------------------------")
    print("Testando algoritmos de criptografia")
    print("-----------------------------")
    # Testando a dummy
    texto = "Cifrando com algoritmo dummy"
    test.testar_dummy("dummy/chave_dummy.txt", texto)

    # Testando a aes
    texto = "Cifrando com algoritmo Aes"
    test.testar_aes("chave_simetrica/chave_aes.txt", texto)


if __name__ == "__main__":
    main()
