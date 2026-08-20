produto = float(input("Preço das compras: R$ "))
opcao= int(input("Escolha uma FORMA DE PAGAENTO:\n[1] à vista dinheiro/cheque\n[2] à vista cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão "))

if opcao == 1:
    valor = produto - (produto *0.10)
    print(f"Sua compra de R${produto} vai custar R${valor} no final")

elif opcao == 2:
    valor = produto - (produto *0.05)
    print(f"Sua compra de R${produto} vai custar R${valor} no final")

elif opcao == 3:
    print(f"Sua compra de R${produto} vai continuar o mesmo preço")


else:
    parcelas = int(input("Quantas parcelas? "))
    valor = produto + (produto * 0.20)
    q_parcela = valor / parcelas
    print(f"Sua compra será parcelada em {parcelas}x de {q_parcela} com JUROS")
    print(f"Sua compra de R${produto} vai custar R${valor} no final")
