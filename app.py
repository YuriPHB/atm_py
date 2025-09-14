import datetime

# Variáveis de controle
saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def mostrar_data():
    data = datetime.date.today().strftime("%d/%m/%Y")
    print(f"📅 Data: {data}\n")

def menu():
    print("""
=== Banco Python ===

[1] Depositar
[2] Sacar
[3] Ver Extrato
[0] Sair
""")

def depositar():
    global saldo, extrato
    try:
        valor = float(input("💰 Valor para depósito: R$ "))
        if valor <= 0:
            print("⚠️ Valor inválido.\n")
        else:
            saldo += valor
            extrato += f"Depósito: +R$ {valor:.2f}\n"
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!\n")
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número.\n")

def sacar():
    global saldo, extrato, numero_saques
    try:
        valor = float(input("💸 Valor para saque: R$ "))
        if valor <= 0:
            print("⚠️ Valor inválido.\n")
        elif valor > saldo:
            print("❌ Saldo insuficiente.\n")
        elif valor > limite:
            print(f"❌ Limite de saque é R$ {limite:.2f} por operação.\n")
        elif numero_saques >= LIMITE_SAQUES:
            print("❌ Limite diário de saques atingido.\n")
        else:
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!\n")
    except ValueError:
