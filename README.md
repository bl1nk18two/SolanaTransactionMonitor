# Solana Transaction Monitor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Em Desenvolvimento](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange)]()

## Descrição

O Solana Transaction Monitor é um projeto em Python que monitora transações de carteiras Solana e envia notificações via Telegram quando uma nova transação é detectada. Ele é projetado para rastrear atividades específicas, como transferências de altcoins, e fornece informações detalhadas sobre as transações.



![Sol](https://github.com/user-attachments/assets/d8314f0f-68b3-4532-95c3-40a4bbda509b)
<img src="https://github.com/user-attachments/assets/ddb0771b-0a51-484c-a614-ec13b671b84c" width="400">
<img src="https://github.com/user-attachments/assets/a27d4f12-398b-4709-8da9-f42e00134f39" width="400">



## Funcionalidades Principais

*   **Monitoramento de Transações:** Rastreia as transações em tempo real de uma lista de carteiras Solana fornecidas.
*   **Notificações via Telegram:** Envia notificações instantâneas para um grupo ou canal do Telegram sobre novas transações detectadas.
*   **Filtro de Programa:**  Identifica e notifica transações baseadas em programas específicos (ex: transferências de altcoins).
*   **Informações Detalhadas:** Fornece informações detalhadas sobre a transação, incluindo o endereço da carteira, assinatura da transação, programa envolvido e um link para o Solscan.
*   **Configuração Simples:** Fácil de configurar e usar com um arquivo `.env` para gerenciar o token do Telegram.
*   **Log de Atividade:** Exibe as transações detectadas no console com informações relevantes.
*   **Persistência de ID:** Guarda os IDs dos usuários do bot em uma planilha Excel, para que as mensagens sejam enviadas corretamente.
*   **Boas Vindas:** Envia mensagem de boas vindas ao usuário que usa o comando `/start`.

## Como Usar

### Pré-requisitos

*   Python 3.6 ou superior
*   Pip (gerenciador de pacotes do Python)
*   Uma conta no Telegram e um bot criado via BotFather
*   [Opcional] Conta no Solscan.io para consultar as transações.

### Instalação

1.  Clone o repositório:

    ```bash
    git clone <URL do seu repositório>
    cd seu-repositorio
    ```

2.  Crie um ambiente virtual (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Linux/macOS
    .\venv\Scripts\activate  # No Windows
    ```

3.  Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

    *   `telebot`: Para a integração com o Telegram.
    *   `python-dotenv`: Para carregar variáveis de ambiente do arquivo `.env`.
    *   `pandas`: Para manipulação de dados em formato de tabela (Excel).
    *   `requests`: Para fazer requisições HTTP à API da Solana.

4.  Configure o arquivo `.env`:

    Crie um arquivo `.env` na raiz do projeto e adicione o token do seu bot do Telegram:

    ```
    TELEGRAM_TOKEN=SEU_TOKEN_DO_TELEGRAM
    ```

    Substitua `SEU_TOKEN_DO_TELEGRAM` pelo token que você recebeu do BotFather.

5.  Adicione as carteiras Solana que você deseja monitorar no script principal:

    Abra o arquivo principal do projeto (ex: `main.py`) e modifique a lista `addresses` para incluir as carteiras que você deseja monitorar:

    ```python
    addresses = [
        {'SOL_WALLET_ADDRESS_1': 'Nome da Carteira 1'},
        {'SOL_WALLET_ADDRESS_2': 'Nome da Carteira 2'}
    ]
    ```

    Substitua `SOL_WALLET_ADDRESS_1` e `SOL_WALLET_ADDRESS_2` pelos endereços das carteiras Solana que você deseja monitorar e `Nome da Carteira 1` e `Nome da Carteira 2` por nomes descritivos para cada carteira.

### Execução

1.  Execute o script principal:

    ```bash
    python main.py
    ```

    O script irá iniciar o bot do Telegram e começar a monitorar as transações das carteiras Solana especificadas.  Você verá mensagens no console indicando o status do monitoramento e as transações detectadas.

### Interagindo com o Bot do Telegram

1. Inicie uma conversa com o seu bot no Telegram.
2. Utilize os seguintes comandos:
   * `/start`: Inicia o bot e envia uma mensagem de boas vindas
   * `/id`: Retorna o ID do chat.

## Detalhes do Código

### Arquivos Principais

*   `main.py`: Script principal que inicia o bot do Telegram e o monitoramento de transações.
*   `models/`: Contém os módulos com as classes principais:
    *   `ATSolanaCoin_bot.py` (ou `SolanaBot.py`): Define a classe `SolanaBot` para a interação com o Telegram.
    *   `SolanaTransactionMonitor.py` (ou similar): Define a classe `SolanaTransactionMonitor` para monitorar as transações na blockchain Solana.
    *   `funcoes.py`: Funções auxiliares para formatação de datas e timers.

### Configuração

O projeto utiliza as seguintes variáveis de ambiente:

*   `TELEGRAM_TOKEN`: Token do bot do Telegram.  (Definido no arquivo `.env`)

### Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.

*   `telebot`
*   `python-dotenv`
*   `pandas`
*   `requests`

## Contribuição

Contribuições são bem-vindas! Se você deseja contribuir para o projeto, siga estas etapas:

1.  Faça um fork do repositório.
2.  Crie uma branch para sua feature (`git checkout -b feature/minha-feature`).
3.  Faça commit das suas mudanças (`git commit -m 'Adiciona nova feature'`).
4.  Faça push para a branch (`git push origin feature/minha-feature`).
5.  Crie um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Autores

*   [Henrique Reis]([Link para seu GitHub](https://github.com/bl1nk18two))

## Agradecimentos

*   Agradecimentos à comunidade Solana e aos desenvolvedores das bibliotecas utilizadas.

## Status do Projeto

Este projeto está em desenvolvimento ativo.  Novas funcionalidades e melhorias estão sendo implementadas.

## Próximos passos
* Adicionar mais funcionalidades ao bot do telegram (ex: consultar saldo da carteira)
* Adicionar suporte a outras blockchains
* Implementar testes unitários
