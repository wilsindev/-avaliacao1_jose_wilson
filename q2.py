total = 0
abaixocinq = 0
acimacinq = 0
produtos_v = int(input("Quantos produtos foram vendidos?: "))
for i in range(1, produtos_v +1):
    vlr = float(input(f"Digite o preço do produto {i}: "))
    total += vlr
    if vlr > 50:
        acimacinq += 1
    else:
        abaixocinq +=1
print(f'o valor total foi de {total}R$ e {abaixocinq} produto(s) ficaram abaixo de 50R$ e {acimacinq} produto(s) ficaram acima de 50R$. ')