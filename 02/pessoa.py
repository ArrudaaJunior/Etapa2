class Pessoa:
	def __init__(self, nome, idade, peso, altura):

		self.nome = nome
		self.idade = idade
		self.peso = peso
		self.altura = altura

	def envelhercer(self):

		self.idade = self.idade + 1

		print("Sua idade depois de um ano: ",self.idade)

	def engordar(self):
		
		self.peso = self.peso * 0.1

		print("Voce engordou em um ano: ",self.peso)

	def emagrecer(self):
		
		self.peso = self.peso - 2

		print("Voce emagreceu em um ano: ",self.peso)
		

	def crescer(self):
		
		if(self.idade < 21):
			
			self.altura = self.altura + 0.5

			print("Sua altura eh: ",self.altura)
		