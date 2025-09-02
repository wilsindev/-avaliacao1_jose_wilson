nm = int(input("Digite um número inteiro: "))
if nm % 2 == 0 and nm < 0:
    print("Número é par e negativo")
elif nm % 2 == 0 and nm > 0:
    print("Número é par e positivo")
elif nm % 2 != 0 and nm > 0:
    print("Número é impar e positivo")
elif nm % 2 != 0 and nm < 0:
    print("Número é impar e negativo")
if nm == 0:
    print("Número é zero")