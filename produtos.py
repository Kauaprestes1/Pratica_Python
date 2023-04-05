produtos = []
precos = []
quant = []

while True: 
    print("1 - Adicione um produto em seu carrinho")
    print("2 - Remova um produto de seu carrinho")
    print("3 - Exiba os produtos de seu carrinho")
    print("4 - Sair do programa")

    opc = input("Digite sua escolha (1/2/3/4):\n")

    if opc == "1":
        nome_produto = input("Digite o nome do produto:\n")
        produtos.append(nome_produto)
        preco_produto = float(input("Digite o valor do produto:\n"))
        precos.append(preco_produto)
        quant_produto = int(input("Digite a quantodade de produtos: \n"))
        quant.append(quant_produto)
        print("Adicionado com sucesso!") 
    if opc == "2":
        nome_produto = input("Qual produto você pretende remover:\n")
        if nome_produto in produtos:
            index = produtos.index(nome_produto)
            produtos.pop(index)
            precos.pop(index)
            print("Produto removido com sucesso!!!")
        else:
            print("Produto não encontrado no carrinho!!!")
    if opc == "3":
        print("Carrinho de compras:\n")
        for i in range(len(produtos)):
            print(f"{produtos[i]} - R${precos[i]} - quantidade:{quant[i]:d}")
    if opc == "4":
        print("Programa finalizado com sucesso!!!")
        break
