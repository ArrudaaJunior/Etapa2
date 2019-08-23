class Conta:
	def __init__(self, numero, corretista, saldo):

		self.numero = numero
		self.corretista = corretista
		self.saldo = saldo

	def alterar_nome(self,novo_nome):

		self.corretista = novo_nome
		print("Novo nome: ",self.corretista)
	
	def deposito(self, valor):

		self.saldo = self.saldo + valor

		print("Seu saldo eh:",self.saldo)

	def saque(self, valor):

		if(self.saldo >= valor):
			self.saldo -= valor

			print("Você retirou: ",valor)
			print("Seu saldo: ",self.saldo)
			return True
		else:
			return False
		

			
				
		


