import telebot
from dotenv import load_dotenv
import pandas as pd
import os
from time import sleep
from datetime import datetime


class SolanaBot:
    def __init__(self):
        # Carregar credenciais do .env
        load_dotenv()
        self.token = os.getenv("TELEGRAM_TOKEN")
        self.bot = telebot.TeleBot(self.token)
        self.arquivo_ids = 'solana_ids.xlsx'

        # Configurar handlers
        self.bot.message_handler(commands=['id'])(self.enviar_id)
        self.bot.message_handler(commands=['start'])(self.enviar_boas_vindas)

    def ler_ids_no_bot(self):
        """Lê os IDs armazenados na planilha."""
        if not os.path.exists(self.arquivo_ids):
            # Criar arquivo caso não exista
            df = pd.DataFrame(columns=['ids', 'alias', 'datetime'])
            df.to_excel(self.arquivo_ids, index=False)

        df = pd.read_excel(self.arquivo_ids, dtype="str")
        return df.to_dict(orient='index')

    def salvar_ids_no_bot(self, nome, chat_id):
        """Salva o ID, alias e data de inclusão no arquivo Excel."""
        data_inclusao = datetime.now().isoformat()

        data = pd.read_excel(self.arquivo_ids, dtype="str")
        nova_linha = pd.DataFrame([{'ids': chat_id, 'alias': nome, 'datetime': data_inclusao}])
        if not str(chat_id) in data['ids'].values:
            data = pd.concat([data, nova_linha], ignore_index=True)
            data.to_excel(self.arquivo_ids, index=False)
            print(f"ID '{chat_id}', alias '{nome}' e data de inclusão '{data_inclusao}' foram salvos com sucesso!")

    def enviar_mensagem(self, mensagem, chat_id):
        """Envia uma mensagem para o chat especificado."""
        try:
            self.bot.send_message(chat_id, mensagem, parse_mode="Markdown")
        except Exception as e:
            print(f"Erro ao enviar mensagem: {e}")

    def enviar_msg_todos_contatos(self, mensagem):
        """ Itera sobre os contatos e envia mensagem a todos. """
        ctts = self.ler_ids_no_bot()
        for ctt in ctts.keys():
            ident = ctts[ctt]['ids']
            self.enviar_mensagem(mensagem, ident)

    def boas_vindas(self, chat_id):
        """Envia uma mensagem de boas-vindas ao chat."""
        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        mensagem = (
            f"⏰ Atualização: {agora}\n"
            "🤖 Seu bot está funcionando!\n"
        )
        self.enviar_mensagem(mensagem, chat_id)

    def enviar_id(self, mensagem):
        """Responde ao comando '/id' com o ID do chat."""
        self.bot.reply_to(mensagem, f"O ID deste chat é: {mensagem.chat.id}")

    def enviar_boas_vindas(self, mensagem):
        """Responde ao comando '/start' com uma mensagem de boas-vindas."""
        self.boas_vindas(mensagem.chat.id)
        sleep(5)
        self.bot.reply_to(
            mensagem,
            f"Olá, {mensagem.chat.first_name}! 👋\n\n"
            "Bem-vindo ao bot de monitoramento de carteiras de Altcoins em Solana! 🚀\n\n"
            "Este bot permite acompanhar as transações e o saldo das carteiras de Solana com altcoins.\n\n"
            "Aqui estão alguns comandos que você pode usar:\n"
            "/id - Para obter o ID deste chat.\n"
        )
        self.salvar_ids_no_bot(mensagem.chat.first_name, mensagem.chat.id)

    def iniciar(self):
        """Inicia o bot e mantém a escuta infinita."""
        print("Bot ATSolanaCoin iniciado!")
        self.bot.infinity_polling()

