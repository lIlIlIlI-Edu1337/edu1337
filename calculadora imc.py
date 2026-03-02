#######################
# Calculadora de IMC
# Edu 1°E N°8
#######################
# Recebe os valores necessarios para o calculo do IMC
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
# Usa os valores fornecidos para realizar o calculo do IMC
imc = peso / (altura * altura)
# Mostra o IMC
print(f"Seu imc é: {imc}")
# Mostra se o IMC está baixo, normal, alto
if (imc < 18.5):
    print("Abaixo do Peso")
elif (imc < 25):
    print("Peso Normal")
elif (imc < 30):
    print("Sobrepeso")
elif (imc < 35):
    print("Obesidade grau 1")
elif (imc < 40):
    print("Obesidade grau 2")
else:
    print("Obesidade grau 3")

#######################