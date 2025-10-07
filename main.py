from test_crypto.crypto_test import CryptoTest
import os


def main():
    try:
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
        print("\n✅ Todos os testes concluídos com sucesso!")

    except KeyboardInterrupt:
        print("\n\nExecução interrompida pelo usuário")
    except Exception as e:
        print(f"\nErro fatal durante execução: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
