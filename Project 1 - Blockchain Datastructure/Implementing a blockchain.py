import pyOpenSSL
import time

#receiver's public key + transaction hash ))))-> is signed by the sender.

#store prevthash in a global variable.
transactions = []

class User:
	def __init__(self,b):
		self.id = str(time.time())
		self.balance = 0
		self.prevtransaction = None
		self.key = None

class Transaction:
	def __init__(self,sender, receiver, amount, sph, txnHash):
		self.sender = sender
		self.receiver = receiver
		self.amount = amount
		self.id = str(time.time())
		self.signedprevhash = sph
		self.transactionHash = str(hash( self.signedprevhash + self.id + self.receiver.id ))

	def valid(self):

		if self.amount < sender.prevtransaction.amount:
			return False
		return True

	def perform(self):
		self.receiver.key = RSA.generate(2048)

		self.receiver.prevtransaction = self
		transactions.append(self.transactionHash)


user1 = User(100)
user1.key = RSA.generate(2048)
user2 = User(0)
user3 = User(0)
user4 = User(0)
user5 = User(0)
user6 = User(0)

# transaction1 and its reverse transaction
# transaction2 and its reverse transaction