import time
import random

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
    \_____\___\____\CA15
'''

print(art)
print('\033[0;34m--=\033[m'*20)
print("\033[1;33mbem-vindo ao PyAssist, o assistente virtual!\033[m")
print('\033[0;34m--=\033[m'*20)

while True:
    try:
        command = int(input("digite o número do comando:\n1. ver hora atual\n2. Ver a data de hoje\n3. dado RPG(20 lados)\n4. sair\n-> "))
    except ValueError:
        print("Erro! Digite somente número!")
        continue

#criar a nossa lógica
    if command == 1:
        hora_atual = time.localtime()
        hora = hora_atual.tm_hour
        minuto = hora_atual.tm_min

        print(f"São \033[0;34m{hora:02d}:{minuto:02d}\033[m")
    elif command == 2:
        dia_atual = time.localtime()
        dia = dia_atual.tm_mday
        mes = dia_atual.tm_mon
        ano = dia_atual.tm_year
        print(f"hoje é \033[0;34m{dia:02d}/{mes:02d}/{ano:04d}\033[m")
    elif command == 3:
        print("Rolando o dado...")
        time.sleep(3)
        print(f"O número sorteado foi \033[0;34m{random.randint(1, 20)}\033[m!")
    elif command == 4:
        print("Obrigado por usar o PyAssist. Volte sempre!")
        time.sleep(3)
        break
    else:
        print('Opção inválida!')