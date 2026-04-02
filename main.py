import time
import random


#funcoes para que o programa funcione e deixar mais organizado
def ver_hora():
    hora_atual = time.localtime()
    hora = hora_atual.tm_hour
    minuto = hora_atual.tm_min
    print(f"São \033[0;34m{hora:02d}:{minuto:02d}\033[m")

def ver_data():
    dia_atual = time.localtime()
    dia = dia_atual.tm_mday
    mes = dia_atual.tm_mon
    ano = dia_atual.tm_year
    print(f"hoje é \033[0;34m{dia:02d}/{mes:02d}/{ano:04d}\033[m")

def rolar_dado():
    print("Rolando o dado...")
    time.sleep(3)
    print(f"O número sorteado foi \033[0;34m{random.randint(1, 20)}\033[m!")

def tabuada():
    while True:
        try:
            numero = int(input("Digite o número que você quer ver a tabuada: "))
            break
        except ValueError:
            print("Erro! Digite somente numero!")
            continue
    print("--=" * 10)
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")
    print("--=" * 10)

def piadas():
    print("aqui vai uma piada:")
    lista_piadas = ['Existem 11 tipos de pessoas: as que entendem binário, as que não entendem, e as que pensam que entendem.',
                    'A mãe fala para o filho programador: "Enquanto estiver fora, compre leite". Ele nunca mais voltou',
                    'Hardware é o que você chuta, software é o que você xinga',
                    'O que o programador faz quando está com fome? Ele dá um “byte”',
                    'Por que programadores confundem Halloween com Natal? Porque OCT 31 == DEC 25']
    print(f'\033[0;34m{random.choice(lista_piadas)}\033[m')
def adivinhe_o_numero():
    print('\033[0;33mEU PENSEI EM UM NUMERO ENTRE 0 E 10, TENTE ADIVINHAR!\033[m')
    while True:
        try:
            numero = int(input("em que número eu pensei? "))
            break
        except ValueError:
            print("DIGITE SOMENTE NÚMERO!")
    numero_secreto = random.randint(0, 10)
    if numero == numero_secreto:
        print("\033[1;32mVOCÊ ACERTOU!\033[m")
    else:
        print(f"Que pena! eu pensei no numero {numero_secreto}")
def sair():
    print("Obrigado por usar o PyAssist. Volte sempre!")
    time.sleep(3)

art = '''\033[0;34m██████╗ ██╗   ██╗ █████╗ ███████╗███████╗██╗███████╗████████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝
██████╔╝ ╚████╔╝ ███████║███████╗███████╗██║███████╗   ██║   
\033[0;33m██╔═══╝   ╚██╔╝  ██╔══██║╚════██║╚════██║██║╚════██║   ██║   
██║        ██║   ██║  ██║███████║███████║██║███████║   ██║   
╚═╝        ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝
\033[m'''
#começando o programa
print(art)
print('\033[0;34m--=\033[m'*15)
print("\033[1;33mBem-vindo ao PyAssist, o assistente virtual!\033[m")
print('\033[0;34m--=\033[m'*15)

while True:
    try:
        command = int(input("""Digite o número do comando:
[1] Ver a hora atual
[2] Ver a data atual
[3] Dado de 20 lados(RPG)
[4] Ver Tabuada
[5] Piadas
[6] Adivinhe o número
[7] sair
-> """))
    except ValueError:
        print("Erro! Digite somente número!")
        continue

#criar a nossa lógica
    if command == 1:
        ver_hora()
    elif command == 2:
        ver_data()
    elif command == 3:
        rolar_dado()
    elif command == 4:
        tabuada()
    elif command == 5:
        piadas()
    elif command == 6:
        adivinhe_o_numero()
    elif command == 7:
        sair()
        break
    else:
        print('Opção inválida!')
