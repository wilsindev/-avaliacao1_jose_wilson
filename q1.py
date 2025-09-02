nm = int(input("Digite um número inteiro: "))
if nm % 2 == 0 and nm < 0:
    print("Número é par e negativo")
elif nm % 2 == 0 and nm > 0:
    print("Número é par e positivo")
if nm == 0:
    print("Número é zero")