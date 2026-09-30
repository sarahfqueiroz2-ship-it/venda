from datetime import datetime
from produto import Produto
from venda import Venda

# Produtos
arroz = Produto("Arroz 5kg", 25.0, 100)
feijao = Produto("Feijão 1kg", 8.5, 200)
carne = Produto("Carne bovina 1kg", 45.0, 30)

# Venda
venda = Venda(datetime.now())
venda.adicionar_item(arroz, 2)
venda.adicionar_item(feijao, 3)
venda.adicionar_item(carne, 1)

# Exibir
print("===== ITENS DA VENDA =====")
for item in venda.itens:
    print(f"{item.quantidade}x {item.produto.descricao} -> R$ {item.subtotal():.2f}")

print(f"\nValor total: R$ {venda.calcular_valor_total():.2f}")