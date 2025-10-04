from test_crypto.crypto_test import CryptoTest
import os


def main():
    # Limpando o terminal sempre que rodar o código

    os.system("clear")
    # Classe para teste dos algoritmos de criptografia
    test = CryptoTest("Testando vários algoritmos de criptografia")

    print("--------------------------------------------------------")
    print("Testando algoritmos de criptografia\n")

    # Testando Dummy
    chave_dummy = "dummy/dummy.txt"
    test.testar_dummy(chave_dummy)
    # Testando AES
    chave_aes = "simetrica/aes.txt"
    test.testar_aes(chave_aes)
    # Testando RSA
    chave_publica_rsa = "assimetrica/rsa_publica.txt"
    chave_privada_rsa = "assimetrica/rsa_privada.txt"
    test.testar_rsa(chave_privada_rsa, chave_publica_rsa)

    nova_chave_dummy = "dummy/dummy1.txt"
    nova_chave_aes = "simetrica/aes1.txt"
    nova_chave_publica_rsa = "assimetrica/rsa_publica1.txt"
    nova_chave_privada_rsa = "assimetrica/rsa_privada1.txt"

    # Renomear o arquivo
    os.rename(chave_dummy, nova_chave_dummy)
    print(f"Arquivo renomeado de '{chave_dummy}' para '{nova_chave_dummy}'")
    os.rename(chave_aes, nova_chave_aes)
    print(f"Arquivo renomeado de '{chave_aes}' para '{nova_chave_aes}'")
    os.rename(chave_publica_rsa, nova_chave_publica_rsa)
    print(f"Arquivo renomeado de '{chave_publica_rsa}' para '{nova_chave_publica_rsa}'")
    os.rename(chave_privada_rsa, nova_chave_privada_rsa)
    print(f"Arquivo renomeado de '{chave_privada_rsa}' para '{nova_chave_privada_rsa}'")

    # Testando Dummy
    test.testar_dummy(chave_dummy)
    # Testando AES
    test.testar_aes(chave_aes)
    # Testando RSA
    test.testar_rsa(chave_privada_rsa, chave_publica_rsa)

    # test.testar_aes_outra_chave(chave_aes,nova_chave_aes)


if __name__ == "__main__":
    main()
