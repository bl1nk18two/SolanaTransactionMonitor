""" Monitoramento de transações de carteiras solana """

import models
import threading
import sys


def iniciar_bot():
    telegram = models.SolanaBot()
    telegram.iniciar()

# Adicionar as carteiras que devem ser rastreadas
def iniciar_monitoramento():
    addresses = [
        {'ADICIONAR CARTEIRAS AQUI': 'Carteira 1'},
        {'ADICIONAR CARTEIRAS AQUI': 'Carteira 2'}
    ]

    monitor = models.SolanaTransactionMonitor(addresses)
    monitor.monitor_transactions()



if __name__ == "__main__":

    bot_thread = threading.Thread(target=iniciar_bot)
    monitor_thread = threading.Thread(target=iniciar_monitoramento)    

    try:
        bot_thread.start()
        monitor_thread.start()
        
        # Espera as threads terminarem de forma limpa
        bot_thread.join()
        monitor_thread.join()

    except KeyboardInterrupt:
        print("Interrupção do usuário. Finalizando threads...")
        bot_thread.join()
        monitor_thread.join()

    except Exception as e:
        print(f'Houve uma falha de funcionamento: {e}')
        bot_thread.join()  
        monitor_thread.join()

    finally:
        # Esse bloco sempre é executado
        models.timer_encerramento(15)
        sys.exit()
