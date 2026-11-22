cardapio = {
    "pizza de calabresa": 45.00,
    "pizza de frango com catupiry": 48.00,
    "coca-cola 2L": 12.00,
}

def consultar_cardapio(item: str):
    """
    Consulta o cardápio e retorna o preço de um produto.
    """
    if item in cardapio:
        return cardapio[item]
    else:
        return "Item não encontrado no cardápio."