class Combustivel:
	def __init__(self, capacidade, preco):

		self.capacidade = capacidade
		self.preco = preco

	def abastecer_por_valor(self, valor):

		self.capacidade = self.capacidade - valor
		
