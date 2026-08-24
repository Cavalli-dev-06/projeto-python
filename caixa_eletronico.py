nome = str(input ("digite seu nome:"))
saldo = float(input ("digite seu saldo:"))

print ("1. consultar saldo")
print ("2. sacar dinheiro")
print ("3. depositar dinheiro")
print ("4. sair")

while True:
    opcao = int(input ("digite a opção desejada:"))
    if opcao == 1:
        print ("seu saldo é:", saldo)
    elif opcao == 2:
        valor_saque = float(input ("digite o valor que deseja sacar:"))
        if valor_saque > saldo:
            print ("saldo insuficiente")
        else:
            saldo = saldo - valor_saque
            print ("saque realizado com sucesso, seu novo saldo é:", saldo)
    elif opcao == 3:
        valor_deposito = float(input ("digite o valor que deseja depositar:"))
        saldo = saldo + valor_deposito
        print ("depósito realizado com sucesso, seu novo saldo é:", saldo)
    elif opcao == 4:
        print ("saindo...")
        break
    else:
        print ("opção inválida")        