import requests
from time import sleep
import sys

from . import funcoes
from .ATSolanaCoin_bot import SolanaBot

class SolanaTransactionMonitor:
    def __init__(self, addresses):
        # Recebe uma lista de dicionários {endereço: nome}
        self.addresses = addresses
        self.last_transaction_signature = {}
        self.rpc_url = "https://api.mainnet-beta.solana.com"

        # Inicializa o dicionário para armazenar a última assinatura de cada endereço
        for addr in addresses:
            for key in addr.keys():
                self.last_transaction_signature[key] = None

    def get_transaction_info(self, signature):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getTransaction",
            "params": [
                signature,
                {"maxSupportedTransactionVersion": 0, "commitment": "string", "encoding": "jsonParsed"},
            ]
        }
        response = requests.post(self.rpc_url, json=payload)
        if response.status_code == 200:
            # data = response.json()
            # pretty_json = json.dumps(data, indent=4, ensure_ascii=False)
            # print(pretty_json)
            return response.json().get('result', [])
        else:
            return None        

    def get_recent_transactions(self, address):
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getSignaturesForAddress",
            "params": [
                address,
                {"limit": 1}
            ]
        }
        response = requests.post(self.rpc_url, json=payload)
        if response.status_code == 200:
            return response.json().get('result', [])
        else:
            return None

    def monitor_transactions(self, interval=20):
        while True:
            try:
                for address_dict in self.addresses:

                    for address, name in address_dict.items():
                        # print(f"\nMonitorando transações para {name} ({address})")
                        
                        transactions = None
                        while not transactions:
                            transactions = self.get_recent_transactions(address)
                            sleep(1)
                        
                        if transactions:
                            # print(transactions)
                            for latest_transaction in transactions:
                                if latest_transaction['signature'] != self.last_transaction_signature[address]:
                                    transaction_info = None
                                    while not transaction_info:
                                        transaction_info = self.get_transaction_info(latest_transaction['signature'])
                                        sleep(1)

                                    if transaction_info and transaction_info['meta']['innerInstructions'] != []:
                                            try:
                                                if transaction_info['meta']['innerInstructions'][0]['instructions'][0]['program']:                                                
                                                    program = transaction_info['meta']['innerInstructions'][0]['instructions'][0]['program']    
                                            except:
                                                continue
                                            
                                            if 'transfer' not in program:
                                                if transaction_info.get('blockTime'):  # Usando .get() para evitar erros caso não exista
                                                    block_time = int(transaction_info['blockTime'])
                                                    formatted_date = funcoes.i64_datetime(block_time)
                                                    day, month, year, hour, minute, seconds = funcoes.brasil_date_format(formatted_date)
                                                    signature_dt = f'{day}/{month}/{year} {hour}:{minute}:{seconds}'

                                                    mensagem = f"\n\033[31m{name} - Nova Transação Detectada | {signature_dt}"
                                                else:
                                                    mensagem = f"\n\033[31m{name} - Nova Transação Detectada"
                                                mensagem += f"\n\033[32mAddress - {address}"
                                                mensagem += f"\n\033[32mAssinatura: {latest_transaction['signature']}"
                                                mensagem += f"\n\033[32mPrograma: {program}"
                                                mensagem += f"\n\033[32mAcesse: \033[34mhttps://solscan.io/tx/{latest_transaction['signature']}\033[0m"
                                                print(mensagem)

                                                telegram_mensagem = f"🚨 {name} - Nova Transação Detectada"
                                                if transaction_info.get('blockTime'):
                                                    telegram_mensagem += f" | {signature_dt}"
                                                telegram_mensagem += f"\n\n📍 Address: {address}"
                                                telegram_mensagem += f"\n📝 Assinatura: {latest_transaction['signature']}"
                                                telegram_mensagem += f"\n⚙️ Programa: {program}"
                                                telegram_mensagem += f"\n\n🔎 Ver no Solscan -> https://solscan.io/tx/{latest_transaction['signature']} "
                                                telegram = SolanaBot()
                                                telegram.enviar_msg_todos_contatos(telegram_mensagem)
                                    self.last_transaction_signature[address] = latest_transaction['signature']

                funcoes.timer_with_time(interval)
            
            except Exception as e:
                print(f"Erro ao buscar transações: {e}")
                funcoes.timer(interval)