# =================== PRIMEIRA PARTE ===================

# Leitura dos dados de entrada
peso = float(input("Insira o peso em toneladas: "))
preco_por_tonelada = float(input("Insira o preço por tonelada: "))
tipo_cliente = input("Insira se a tipo do cliente: ").title()

# Calcula o valor total sem desconto
valor_total = peso * preco_por_tonelada

if tipo_cliente == "Novo Cliente":
    desconto = 0
elif tipo_cliente == "Cliente Fidelizado":
    desconto = 0.05
elif tipo_cliente == "Cliente Premium":
    desconto = 0.10

valor_final = valor_total * (1 - desconto)

# Exibe o resultado formatado com duas casas decimais
print(f"{valor_final:.2f}")

# =================== SEGUNDA PARTE ===================
import math

# Leitura das entradas como strings
total_caixas = input().strip()
capacidade_palete = input().strip()

# Conversão para inteiros
total_caixas = int(total_caixas)
capacidade_palete = int(capacidade_palete)

# TODO: Calcule o número de paletes necessários (arredondando para cima)
paletes_necessarios = round(total_caixas / capacidade_palete)

# Impressão como string (sem espaços ou caracteres especiais)
print(str(paletes_necessarios))