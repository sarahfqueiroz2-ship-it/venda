class Produto:

    def __init__(self, descricao, valor, estoque):
        self._descricao = descricao
        self._valor = float(valor)
        self._estoque = int(estoque)

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        self._valor = float(novo_valor)

    @property
    def estoque(self):
        return self._estoque

    @estoque.setter
    def estoque(self, novo_estoque):
        self._estoque = int(novo_estoque)

    def decrementar_estoque(self, quantidade):
        if quantidade > 0 and self._estoque >= quantidade:
            self._estoque -= quantidade
            return True
        return False

    def incrementar_estoque(self, quantidade):
        if quantidade > 0:
            self._estoque += quantidade
            return True
        return False