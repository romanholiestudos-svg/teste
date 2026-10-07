limites_tarifa = (15.50, 50.0)

tarifa_min, tarifa_max = limites_tarifa

print(f"Tarifa mínima: R$ {tarifa_min:.2f}")
print(f"Tarifa máxima: R$ {tarifa_max:.2f}")

esteira = []

for i in range(1, 4):
  valor_frete = float(input(f"Digite o valor do frete para o pacote {i}: R$ "))
  esteira.append(valor_frete)

esteira.insert (0, 20.0)

pacote_retido = esteira.pop()

print(f"Pacote retido: R$ {pacote_retido:.2f}")

esteira.sort()

print()

print(f"Esteira ordenada: {[f'R$ {val:.2f}' for val in esteira]}")


quantidade_final = len(esteira)
faturamento_total = sum(esteira)
maior_tarifa = max(esteira)

print()
print("Relatório Final")
print(f"Quantidade final de pacotes: {quantidade_final}")
print(f"Faturamento total da rota: R$ {faturamento_total:.2f}")
print(f"Maior tarifa do lote: R$ {maior_tarifa:.2f}")

print()

print("Manifesto")

for id, tarifa in enumerate(esteira, start=1):
  if tarifa < tarifa_max:
    classificacao = "PADRÃO"
  else:
    classificacao = "TARIFA PREMIUM"
  print(f"Entrega #{id}: R$ {tarifa:.2f} {classificacao}")
