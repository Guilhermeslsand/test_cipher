# Sistema de Criptografia

Um sistema completo de criptografia implementando múltiplos algoritmos para fins educacionais e de teste.

## 📋 Descrição

Este projeto implementa três algoritmos de criptografia diferentes:

- **Dummy**: Algoritmo simples para fins didáticos
- **AES**: Criptografia simétrica de alta segurança
- **RSA**: Criptografia assimétrica para chaves públicas/privadas

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **cryptography** - Biblioteca de criptografia
- **pycryptodome** - Implementações criptográficas
- **watchdog** - Monitoramento de arquivos em tempo real
- **pre-commit** - Hooks para qualidade de código
- **ruff** - Linter e formatter Python
- **black** - Formatação de código

## 📁 Estrutura do Projeto
## 📁 Estrutura do projeto
📦 com.pratica2.clientecrud<br>
 ┣ 📂 model<br>
 ┃ ┗ 📜 Cliente.java<br>
 ┃    ↳ Define a estrutura do cliente (atributos: cpf, nome, email).<br>
 ┣ 📂 repository<br>
 ┃ ┗ 📜 ClienteRepository.java<br>
 ┃    ↳ Simula o "banco de dados em memória" (lista de clientes).<br>
 ┣ 📂 usecase<br>
 ┃ ┗ 📜 ClienteUseCase.java<br>
 ┃    ↳ Camada de lógica que conecta o controller ao repositório.<br>
 ┗ 📂 controller<br>
   ┗ 📜 ClienteController.java<br>
        ↳ Recebe as requisições HTTP e chama o usecase para executar as operações.<br>

.
┣ main.py # Script principal de execução
┣ test_crypto/
┃  ┗ crypto_test.py # Classe de testes dos algoritmos
┣ dummy/
┃ ┗ crypto_dummy.py # Implementação do algoritmo Dummy
┣ simetrica/
┃ ┗ crypto_aes.py # Implementação do AES
┣ assimetrica/
┃ ┗ crypto_rsa.py # Implementação do RSA
┣ crypto_exceptions.py # Exceções customizadas
┣ requirements.txt # Dependências do projeto
┣ .pre-commit-config.yaml # Configuração do pre-commit
┣ README.md # Este arquivo

## 🚀 Como Executar

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

### Execução Principal
```bash
python3 main.py
```

### Modo Desenvolvimento (Watch Mode)
```bash
python3 watcher.py
```
O modo desenvolvimento monitora automaticamente mudanças nos arquivos e reexecuta os testes.

## 🔧 Funcionalidades
### Teste de Algoritmos
O sistema testa automaticamente três algoritmos:

Dummy: Algoritmo básico para entendimento dos conceitos

AES: Criptografia simétrica com chave única

RSA: Criptografia assimétrica com par de chaves

### Saída dos Testes
Para cada algoritmo, o sistema exibe:

Mensagem original em string e hexadecimal

Mensagem cifrada em string e hexadecimal

Mensagem decifrada em string e hexadecimal

### Gerenciamento de Chaves
Dummy/AES: Chaves armazenadas em arquivos texto

RSA: Par de chaves pública e privada em arquivos separados

## ⚙️ Configuração de Qualidade de Código
O projeto utiliza pre-commit hooks para garantir qualidade:
```bash
pre-commit install
```
### Hooks Incluídos:
ruff: Análise estática e formatação

black: Formatação automática

check-toml/yaml/json: Validação de arquivos de configuração

trailing-whitespace: Remove espaços desnecessários

end-of-file-fixer: Garante quebra de linha no final

## 🗂️ Organização de Arquivos
### Chaves de Criptografia
dummy/dummy.txt - Chave do algoritmo Dummy

simetrica/aes.txt - Chave AES

assimetrica/rsa_publica.txt - Chave pública RSA

assimetrica/rsa_privada.txt - Chave privada RSA

### Exceções Customizadas
KeyGenerationError: Erro na geração de chaves

KeyLoadError: Erro no carregamento de chaves

EncryptionError: Erro durante criptografia

DecryptionError: Erro durante descriptografia

## 🔒 Segurança
Nota: Este projeto é para fins educacionais. Para aplicações em produção, utilize bibliotecas criptográficas validadas e siga as melhores práticas de segurança.

## 🤝 Contribuição
Instale pre-commit: pre-commit install

Siga as convenções de código (ruff + black)

Teste todas as funcionalidades

Certifique-se que os hooks passam
