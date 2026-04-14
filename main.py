import time
import random
import webbrowser
import urllib.parse
import math

#funções para que o programa funcione e deixar mais organizado
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

    if dia == 12 and mes == 4:
        idade = ano - 2015
        print('\033[1;34mHOJE É O ANIVER\033[1;33mSÁRIO DO CRIADOR!\033[m')
        print(f"ELE ESTÁ COM \033[1;32m{idade}\033[m ANOS!")
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
    numero_secreto = random.randint(0, 10)
    while True:
        try:
            numero = int(input("em que número eu pensei? "))
            break
        except ValueError:
            print("DIGITE SOMENTE NÚMERO!")
    if numero == numero_secreto:
        print("\033[1;32mVOCÊ ACERTOU!\033[m")
    else:
        print(f"Que pena! eu pensei no numero {numero_secreto}")

def abrir_um_site_inutil():
    sites = ['https://theuselessweb.com/', 'https://pointerpointer.com/', 'https://www.boredbutton.com/', 'https://cat-bounce.com/',
             'https://heeeeeeeey.com/', 'https://zoomquilt.org/', 'http://www.staggeringbeauty.com/', 'http://www.fallingfalling.com/',
             'http://eelslap.com/', 'http://endless.horse/', 'https://trumpet.dance/', 'https://screamintothevoid.com/',
             'https://isitchristmas.com/', 'https://randomcolour.com/', 'https://longdogechallenge.com/',
             'https://checkboxrace.com/', 'https://clickclickclick.click/']
    print("Abrindo um site inutil...")
    time.sleep(2)
    site_escolhido = random.choice(sites)
    print(f"O site {site_escolhido} foi o escolhido!")
    time.sleep(1)
    webbrowser.open(site_escolhido)

def calculadora():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("DIGITE SOMENTE NÚMERO!")
            continue
    operacao = input("digite a operação: (+ - * /) ")
    if operacao == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operacao == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operacao == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operacao == '/':
        try:
            print(f"{num1} / {num2} = {num1 / num2}")
        except ZeroDivisionError:
            print("NÃO É POSSIVEL DIVIDIR POR 0!")

def pesquisar():
    tema = input('O que deseja pesquisar? ')
    tema_formatado = urllib.parse.quote(tema.replace(' ', '_'))
    webbrowser.open(f'https://pt.wikipedia.org/wiki/{tema_formatado}')

def hipotenusa():
    while True:
        try:
            cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
            cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
            break
        except ValueError:
            print("digite somente numero!")
            continue
    print("Calculando hipotenusa...")
    time.sleep(3)
    hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
    print(f"A hipotenusa é de {hipotenusa:.2f}")
def pedrapapeltesoura():
    pontos_computador = 0
    pontos_jogador = 0

    print('\033[0;33m--=\033[m'*20)
    print("\033[1;34mBEM-VINDO AO PEDRA PAPEL E TESOURA\033[m")
    print('\033[0;33m--=\033[m'*20)

    opcoes = ['pedra', 'papel', 'tesoura']
    while True:
        print(f"Placar: \033[0;31m{pontos_jogador}x{pontos_computador}\033[m")
        escolha = input("digite pedra ,papel, tesoura ou sair: ").lower().strip()
        if escolha == 'sair':
            print(f"O jogo ficou com o placar de \033[0;31m{pontos_jogador}x{pontos_computador}\033[m")
            print('\033[0;32mVOLTE LOGO :)')
            break

        elif escolha in opcoes:
            print("PEDRA")
            time.sleep(1)
            print("PAPEL")
            time.sleep(1)
            print("TESOURA!")
            time.sleep(1)
            escolha_computador = random.choice(opcoes)
            print(f"Eu escolhi \033[1;32m{escolha_computador}\033[m\nVocê escolheu \033[1;32m{escolha}\033[m")
            if escolha_computador == escolha:
                print("\033[0;33mEMPATE!\033[m")
            elif (escolha == 'pedra' and escolha_computador == 'tesoura') or (escolha == 'papel' and escolha_computador == 'pedra') or (escolha == 'tesoura' and escolha_computador == 'papel'):
                print('\033[1;32mVOCÊ ME VENCEU!\033[m')
                pontos_jogador += 1
            else:
                print("\033[1;31mEU VENCI\033[m")
                pontos_computador += 1
        else:
            print("Não entendi :~")

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
print("Version 12.0")
print('\033[0;34m--=\033[m'*15)
print("\033[1;33mBem-vindo ao PyAssist, o assistente virtual!\033[m")
print('\033[0;34m--=\033[m'*15)

while True:
    try:
        command = int(input("""\033[0;36mDigite o número do comando:\033[m
[1] Ver a hora atual
[2] Ver a data atual
[3] Dado de 20 lados(RPG)
[4] Ver Tabuada
[5] Piadas
[6] Adivinhe o número
[7] Abrir um site inútil
[8] Calculadora
[9] Pesquisar na wikipédia
[10] Calcular hipotenusa
[11] Pedra, papel e tesoura
[12] Sair
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
        abrir_um_site_inutil()
    elif command == 8:
        calculadora()
    elif command == 9:
        pesquisar()
    elif command == 10:
        hipotenusa()
    elif command == 11:
        pedrapapeltesoura()
    elif command == 12:
        sair()
        break
    else:
        print('Opção inválida!')