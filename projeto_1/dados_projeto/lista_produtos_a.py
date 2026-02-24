# Lista de 100 produtos comuns em mercados brasileiros
produtos_mercado = [
    # Mercearia Salgada (Curva A e B)
    "Arroz Agulhinha T1 5kg", "Feijão Carioca 1kg", "Açúcar Refinado 1kg", 
    "Sal Refinado 1kg", "Óleo de Soja 900ml", "Azeite de Oliva Extra Virgem", 
    "Macarrão Espaguete 500g", "Macarrão Parafuso 500g", "Molho de Tomate Sachê", 
    "Milho de Pipoca", "Farinha de Trigo 1kg", "Farinha de Mandioca", 
    "Café Torrado e Moído 500g", "Leite Condensado 395g", "Creme de Leite 200g",
    "Maionese 500g", "Ketchup 400g", "Mostarda 190g", "Sardinha em Lata", 
    "Atum em Pedaços", "Biscoito Cream Cracker", "Biscoito Recheado Chocolate",

    # Matinal e Padaria
    "Pão de Forma Tradicional", "Pão de Queijo Congelado", "Achocolatado em Pó 400g", 
    "Cereal Matinal", "Geléia de Morango", "Mel Natural", "Torrada Tradicional",
    "Aveia em Flocos", "Chá de Camomila Caixa", "Mistura para Bolo Chocolate",

    # Laticínios e Frios (Perecíveis - PVPS)
    "Leite UHT Integral 1L", "Leite UHT Desnatado 1L", "Manteiga com Sal 200g", 
    "Margarina 500g", "Iogurte Natural 170g", "Petit Suisse Morango", 
    "Queijo Muçarela Fatiado", "Queijo Prato Fatiado", "Requeijão Cremoso", 
    "Presunto Cozido Fatiado", "Salame Italiano 100g", "Ovos Brancos 12un",

    # Bebidas (Alto Giro)
    "Refrigerante Cola 2L", "Refrigerante Guaraná 2L", "Suco de Uva Integral 1L", 
    "Água Mineral sem Gás 500ml", "Água Mineral com Gás 500ml", "Cerveja Pilsen Lata 350ml", 
    "Cerveja Puro Malte Long Neck", "Vinho Tinto Seco", "Energético 250ml", 
    "Água de Coco 1L", "Néctar de Laranja 1L",

    # Hortifrúti (FLV - Alta Perda)
    "Batata Inglesa kg", "Cebola Nacional kg", "Alho Granel 100g", 
    "Tomate Italiano kg", "Banana Nanica un", "Maçã Gala kg", 
    "Laranja Pêra kg", "Limão Taiti kg", "Mamão Papaia un", "Cenoura kg",

    # Açougue e Congelados
    "Peito de Frango kg", "Coxa e Sobrecoxa de Frango", "Carne Moída de Patinho", 
    "Acém Bovino kg", "Picanha Bovina kg", "Linguiça Calabresa kg", 
    "Salsicha Hot Dog kg", "Nuggets de Frango", "Pizza Congelada Calabresa", 
    "Hambúrguer de Carne 120g", "Lasanha Congelada",

    # Higiene Pessoal
    "Papel Higiênico Folha Dupla 12un", "Creme Dental 90g", "Escova de Dentes Média", 
    "Sabonete em Barra 90g", "Shampoo para Cabelos Normais", "Condicionador", 
    "Desodorante Aerosol", "Fio Dental 50m", "Absorvente com Abas", "Carga de Barbear",

    # Limpeza (Cuidado com Contaminação)
    "Detergente Líquido 500ml", "Sabão em Pó 1kg", "Amaciante de Roupas 2L", 
    "Água Sanitária 1L", "Desinfetante Lavanda 500ml", "Esponja de Aço 3un", 
    "Esponja Multiuso", "Limpador Multiuso", "Saco de Lixo 50L", "Inseticida Spray",

    # Bazar e Pet
    "Ração para Cães Adultos 1kg", "Ração para Gatos 1kg", "Areia Sanitária Gatos",
    "Carvão Vegetal 3kg", "Lâmpada LED 9W", "Pilha Alcalina AA 4un"
]

# Exibindo o total para conferência
# print(f"Total de itens na lista: {len(produtos_mercado)}")


cargos_mercado = {
    "Estratégico": ["Gerente de Loja", "Comprador"],
    "Controle": ["Encarregado de Prevenção de Perdas", "Conferente"],
    "Operacional": ["Encarregado de Setor", "Repositor", "Açougueiro"],
    "Atendimento": ["Operador de Caixa", "Fiscal de Caixa", "Auxiliar de Limpeza"]
}