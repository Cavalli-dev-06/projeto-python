numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))

if operacao == "+":
	resultado = numero1 + numero2
elif operacao == "-":
	resultado = numero1 - numero2
elif operacao == "*":
	resultado = numero1 * numero2
elif operacao == "/":
	if numero2 == 0:
		print("Não é possível dividir por zero.")
		raise SystemExit
	resultado = numero1 / numero2
else:
	print("Operação inválida.")
	raise SystemExit

print(f"Resultado: {resultado}")
