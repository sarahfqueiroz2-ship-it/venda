from item_venda import ItemVenda


class Venda:

    def __init__(self, data_venda):
        self._data_venda = data_venda
        self._valor_total = 0.0
        self._itens = []

    @property
    def data_venda(self):
        return self._data_venda

    @property
    def valor_total(self):
        return self._valor_total

    @property
    def itens(self):
        return self._itens

    def adicionar_item(self, produto, quantidade):
        if quantidade <= 0:
            return False
        item = ItemVenda(produto, quantidade)
        self._itens.append(item)
        return True

    def remover_item(self, item):
        if item in self._itens:
            self._itens.remove(item)
            return True
        return False

    def calcular_valor_total(self):
        total = 0.0
        for item in self._itens:
            total += item.subtotal()
        self._valor_total = total
        return total