from datetime import datetime
import time
import sys

def i64_datetime(block_time):
    data_humana = datetime.fromtimestamp(block_time)
    return data_humana


def brasil_date_format(date):
    _day = str(date.day).zfill(2)
    _month = str(date.month).zfill(2)
    _year = str(date.year)
    _hour = str(date.hour).zfill(2) if date.hour else str('00')
    _minute = str(date.minute).zfill(2) if date.minute else str("00")
    _seconds = str(date.second).zfill(2) if date.second else str('00')   

    return _day, _month, _year, _hour, _minute, _seconds


def timer_with_loading(duration):
    loading_states = ["Buscando.", "Buscando..", "Buscando..."]
    start_time = time.time()

    while time.time() - start_time < duration:
        for state in loading_states:
            sys.stdout.write(f"\r{state}")
            sys.stdout.flush()
            time.sleep(0.5)
    
    # Apagar o texto após o tempo
    sys.stdout.write("\r" + " " * len(max(loading_states, key=len)) + "\r")
    sys.stdout.flush()


def timer(numero):
    contador = int(numero)
    while contador >= 0:
        time.sleep(1)
        sys.stdout.write(f'\rNova Requisição em {contador} Segundos.')
        sys.stdout.flush()
        contador -= 1

def timer_encerramento(numero):
    contador = int(numero)
    while contador >= 0:
        time.sleep(1)
        sys.stdout.write(f'\rEncerrando em {contador} Segundos.')
        sys.stdout.flush()
        contador -= 1
    sys.exit()


def timer_with_time(duration):
    # Adiciona uma linha antes do timer para separar
    sys.stdout.write("\n")  # Nova linha para separar o timer
    sys.stdout.flush()

    start_time = time.time()

    while time.time() - start_time < duration:
        # Obter o horário atual
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # Mostrar 'buscando' seguido do horário, sobrescrevendo a linha a cada segundo
        sys.stdout.write(f'\r\033[34m\033[40mBuscando... {current_time}\033[0m')
        sys.stdout.flush()
        time.sleep(1)  # Atualiza a cada segundo

    # Apagar o texto após o tempo, movendo o cursor para a linha anterior
    sys.stdout.write("\r" + " " * 40 + "\r")  # Limpa a linha do timer
    sys.stdout.flush()
