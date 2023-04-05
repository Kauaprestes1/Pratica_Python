ingredientes = []
quantidades = []
receitas = []

while True:
    print("1 - Adicionar receita")
    print("2 - Exibir receita")
    print("3 - Sair do programa")

    resp = input("Qual a sua escolha? \n")

    if resp == "1":
        ingredientes_da_receita = []
        quantidades_da_receita = []

        nome_receita = input("Digite o nome de sua receita: ")
        while True:
            nome_ingrediente = input("Digite o nome do ingrediente: ")
            ingredientes_da_receita.append(nome_ingrediente)
            quantidade_ingrediente = float(input("Digite a quantidade: "))
            quantidades_da_receita.append(quantidade_ingrediente)
            opc = input("Deseja adicionar mais algum item a receita? (Sim ou Não)")

            if opc.lower() in ["sim", "s"]:
                 continue
            elif opc.lower() in ["não", "nao", "n"]:
                receitas.append((nome_receita, ingredientes_da_receita, quantidades_da_receita))
                print("Receita adicionada com sucesso!!!")
                break

    elif resp == "2":
        print("Receitas: \n")
        for receita in receitas:
            nome_receita, ingredientes_da_receita, quantidades_da_receita = receita
            print(f"Receita de {nome_receita}:")
            for i in range(len(ingredientes_da_receita)):
                print(f"{ingredientes_da_receita[i]} - {quantidades_da_receita[i]:.2f}")

    elif resp == "3":
        print("Programa finalizado")
        break
