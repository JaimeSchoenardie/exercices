# # Faça um Programa que mostre a mensagem "Olá mundo" na tela.

print('Olá mundo!')

# # Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

num = int(input('Digite um número: '))
print('O número digitado foi: {}.'.format(num))

# # Faça um Programa que peça dois números e imprima a soma.

num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

resultado = num_1 + num_2

print('O resultado da soma dos dois números digitados é: {}'.format(resultado))

# # Faça um Programa que peça as 4 notas bimestrais e mostre a média.


from statistics import median
num_1 = int(input('Digite a nota do 1° bimestre: '))
num_2 = int(input('Digite a nota do 2° bimestre: '))
num_3 = int(input('Digite a nota do 3° bimestre: '))
num_4 = int(input('Digite a nota do 4° bimestre: '))

média = median([num_1, num_2, num_3, num_4])

print('A nota média do aluno foi: {}'.format(média))

# Faça um Programa que converta metros para centímetros.


print('----------------------')
print('-- CONVERSOR m x cm --')
print('----------------------')

med_m = int(input('Digite a medida em metros: '))

med_cent = med_m * 100

print('A medida em centímetros é: {} cm.'.format(med_cent))

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

print('---------------------------')
print('-- CONVERSOR raio x área --')
print('---------------------------')

raio = int(input('Digite o raio de uma circunferência (em cm): '))

area = 3.14 * (raio ** 2)

print('A área é: {} cm.'.format(area))

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print('-------------------------')
print('-- Calculadora de área --')
print('-------------------------')

num_1 = float(input('Digite o tamanho do 1° lado (em metros): '))
num_2 = float(input('Digite o tamanho do 2° lado (em metros): '))

resultado = num_1 * num_2
dobro = resultado * 2

print('A área total é: {:2} metros, e seu dobro é: {:2} metros.'.format(resultado, dobro))

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print('----------------------------')
print('-- Calculadora de salário --')
print('----------------------------')

valor_hora = float(input('Quanto voçê ganha por hora? R$ '))
horas_trabalhadas = int(input('Quantas horas voçê trabalha por mês? '))

calc = float(valor_hora * horas_trabalhadas)

print('Voçê recebe R$ {:2} de salário por mês.'.format(calc))

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

print('-------------------------------')
print('-- Calculadora de peso ideal --')
print('-------------------------------')

print('Digite M para masculino ou F para feminino.')
sexo = str(input('Sexo: ')).capitalize()

while True:

    if 'M' in sexo:
        altura = float(input('Digite sua altura em metros: '))
        peso = float((72.7 * altura) - 58)
        print("Seu peso ideal é: {:2} Kg.".format(peso))
        break
    elif 'F' in sexo:
        altura = float(input('Digite sua altura em metros: '))
        peso = float((62.1 * altura) - 44.7)
        print("Seu peso ideal é: {:2} Kg.".format(peso))
        break
    else:
        print('digite apenas as letras M ou F.')
        break

    