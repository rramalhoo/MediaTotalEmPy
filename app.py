while True:
    ac = float(input("Digite a sua média de AC:"))
    at = float(input("Digite a nota de AT:"))
    agh = float(input("Digite a nota de AGH:"))

    media = (ac*3 + at*5 + agh*2 ) /10

    print (f"Sua média final é {media}")

    continuar = input("Quer calcular outra média?")
    if continuar == 'n':
        print("Codigo encerrado")
        break