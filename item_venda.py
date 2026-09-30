class ItemVenda:

    def __init__(self, produto, quantidade):
        self._produto = produto
        self._quantidade = int(quantidade)
        self._preco_unitario = produto.valor

    @property
    def produto(self):
        return self._produto

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        self._quantidade = int(nova_quantidade)

    @property
    def preco_unitario(self):
        return self._preco_unitario

    def subtotal(self):
        return self._quantidade * self._preco_unitario