cardapio = {
    "pizza de calabresa": {
        "preco": 45.00,
        "aliases": [
            "calabresa",
            "pizza calabresa",
            "calabresa pizza"
        ]
    },
    "pizza de frango com catupiry": {
        "preco": 48.00,
        "aliases": [
            "frango com catupiry",
            "pizza frango catupiry",
            "frango catupiry pizza"
        ]
    },
    "coca-cola 2l": {
        "preco": 12.00,
        "aliases": [
            "coca",
            "coca-cola",
            "coca 2 litros",
            "coca-cola 2l",
            "coca de 2 litros",
            "coca-cola 2L"
        ]
    }
}

def consultar_cardapio(item: str):
    """
    Consulta o cardápio e retorna o preço de um produto.
    """
    for produto in cardapio:
        if item.lower() == produto.lower():
            return cardapio[produto]["preco"]
        for alias in cardapio[produto]["aliases"]:
            if item.lower() == alias.lower():                
                return cardapio[produto]["preco"]
            
    return "Item não encontrado no cardápio."