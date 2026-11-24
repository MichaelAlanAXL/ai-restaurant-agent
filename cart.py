from menu import cardapio

carrinho = []

def adicionar_item(item: str, quantidade: int):
    """
    Adiciona um produto ao carrinho, informando o nome e a quantidade.
    """
    encontrado = False

    for produto in carrinho:
        if " ".join(produto["item"].split()).lower() == " ".join(item.split()).lower():
            produto["quantidade"] += quantidade
            encontrado = True
            break

    if not encontrado:
        carrinho.append({
            "item": item,
            "quantidade": quantidade
        })

def listar_carrinho():
    """
    Retorna os itens do carrinho em formato de nota,
    incluindo quantidades, preços e valor total.
    """
    bobina_size = 32 # Try 38 42
    preco_size = 10
    descricao_size = bobina_size - preco_size

    if not carrinho:
        return "Carrinho de compras vazio"

    nota = "-----------------------------------\n"    
    total = 0

    for produto in carrinho:
        preco = cardapio[produto["item"].lower().strip()]["preco"]
        subtotal = produto["quantidade"] * preco
        total += subtotal

        nota += f'{produto["quantidade"]}x {produto["item"]:<20} R$ {subtotal:.2f}'.replace(".", ",") + "\n"
    
    nota += "-----------------------------------\n"
    nota += f"{'TOTAL':<{descricao_size}}{'R$ ' + format(total, '.2f'):>{preco_size}}"

    return nota