print("Bem Vindo a Loja")
valor = float(input("Diga o valor do produto: ")) #Variavel valor pede o valor do produto
quantidade = int(input("Diga a quantidade de produtos: ")) #Variavel quantidade pede quantos produtos serão comprados
valortotal = float #Cria variável para armazenar o valor total pós desconto
valortotalsd = float(valor*quantidade) #Cria variável para armazenar o valor total sem desconto
desconto = int(0)
if quantidade >= 1000: #Caso a quantidade de produtos seja maior ou igual a mil, faz o calculo do desconto de 15%
    valortotal = valor*0.85*quantidade
    desconto = 15
elif quantidade >= 100 and quantidade <= 999: #Caso a quantidade de produtos seja maior ou igual a cem e menor ou igual a 999, faz o calculo do desconto de 10%
    valortotal = valor*0.9*quantidade
    desconto = 10
elif quantidade >= 10 and quantidade <= 99: #Caso a quantidade de produtos seja maior ou igual a 10 e menor ou igual a 99, faz o calculo do desconto de 5%
    valortotal = valor*0.95*quantidade
    desconto = 5
else: #Caso não se aplique em nenhuma das alternativas anteriores, calcula apenas o valor total
    valortotal = valor*quantidade
if quantidade >= 10: #Caso a quantidade de produtos seja maior que 10, mostra o valor com e sem desconto
    print("O valor sem desconto foi: R$ {:.2f}" .format(valortotalsd))
    print("O valor com desconto foi: R$ {:.2f}, desconto de: {}%".format(valortotal, desconto))
else: #Caso contrário, mostra apenas o valor sem desconto, já que não teremos desconto aplicado
    print("O valor total foi: R$ {:.2f}" .format(valortotalsd))
