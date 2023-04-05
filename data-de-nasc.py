ano = 2023

ano_nasc = int(input("Digite o ano que você nasceu:\n"))

idade = ano - ano_nasc

if(idade <= 16):
    print("Você tem:\n",idade, "anos")
elif(idade >= 18):
    print("Você tem:\n",idade, "anos e já pode fazer TG")
else:
    print("Você tem:\n",idade, "anos e já pode votar e dirigir")