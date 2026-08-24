"""
EXERCICIO: resultado final de um aluno

Complete o programa abaixo usando operadores e logica de Python.

Regras:
1. Leia duas notas entre 0 e 10 e a quantidade de faltas.
2. Calcule a media das duas notas.
3. O aluno sera aprovado se:
   - a media for maior ou igual a 7 e as faltas forem menores ou iguais a 10; ou
   - a media for maior ou igual a 5, as faltas forem menores ou iguais a 10
	 e ele fizer a prova de recuperacao.
4. Caso contrario, ele sera reprovado.
5. Mostre tambem se o aluno tem media par ou impar, usando o operador %.

Exemplos:
- Notas 8 e 6, 5 faltas, sem recuperacao -> aprovado
- Notas 5 e 4, 2 faltas, com recuperacao -> aprovado
- Notas 6 e 5, 12 faltas, com recuperacao -> reprovado
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite a quantidade de faltas: "))
recuperacao = input("Fez a prova de recuperacao? (s/n): ").lower()

# TODO: calcule a media das notas.
media = (nota1 + nota2) / 2

# TODO: rejeite notas invalidas e quantidade de faltas negativa.
if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10 or faltas < 0:
	print("Dados invalidos.")
else:
	# TODO: crie uma expressao booleana para decidir a aprovacao.
	aprovado = (
		(media >= 7 and faltas <= 10)
		or (media >= 5 and faltas <= 10 and recuperacao == "s")
	)

	print(f"Media: {media:.1f}")

	if aprovado:
		print("Resultado: aprovado")
	else:
		print("Resultado: reprovado")

	# A media pode ter casas decimais; compare o resto da parte inteira.
	if int(media) % 2 == 0:
		print("A parte inteira da media e par.")
	else:
		print("A parte inteira da media e impar.")
