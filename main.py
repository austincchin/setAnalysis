import random
#User Objects
#		- search function
#		- cards awarded

class Card:
	def __init__(self,num):
		self.id = num
		self.number = int(num[0])
		self.symbol =  int(num[1])
		self.shading = int(num[2])		
		self.color =  int(num[3])		

	def getId(self):
		return self.id

	def getNum(self):
		return self.number

	def getSym(self):
		return self.symbol
	
	def getSha(self):
		return self.shading
	
	def getCol(self):
		return self.color

def createDeck(): #256 cards
	randDeck = []
	tupleDeck = []
	returnDeck = []

	#generate Deck order
	while len(randDeck) < 81:
		i = random.randint(1,81)
		if i not in randDeck:
			randDeck.append(i)

	#generate Cards
	randPoint = 0
	for num in range(1,4):
		for sym in range(1,4):
			for sha in range(1,4):
				for col in range(1,4):
					cardNum = str(num*1000 + sym*100 + sha*10 + col)
					c = Card(cardNum)
					cardTuple = (randDeck[randPoint],c)
					tupleDeck.append(cardTuple)
					randPoint += 1

	#sort Deck
	tupleDeck.sort()
	for i in tupleDeck:
		returnDeck.append(i[1])
	
	return returnDeck




if __name__ == "__main__":
	D = createDeck();
	#12 cards are placed into the table
	#players identify a set