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

def sair():
    print("Obrigado por usar o PyAssist. Volte sempre!")
    time.sleep(3)

art = r''' ______________
||PyAssist    ||
||            ||
||            ||
||            ||
||____________||
|______________|
 \\############\\
  \\############\\
   \      ____    \ 
    \_____\___\____\ ASCII by CA15
'''
#começando o programa
print(art)
print('\033[0;34m--=\033[m'*15)
print("\033[1;33mbem-vindo ao PyAssist, o assistente virtual!\033[m")
print('\033[0;34m--=\033[m'*15)

while True:
    try:
        command = int(input("""Digite o número do comando:
[1] Ver a hora atual
[2] Ver a data atual
[3] Dado de 20 lados(RPG)
[4] Ver Tabuada
[5] Sair
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
        sair()
        break
    else:
        print('Opção inválida!')
