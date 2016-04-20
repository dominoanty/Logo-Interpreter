from turtle import Turtle
import sys, pygame
import math
import time

keywords = """
fd
bk
lt
rt
arc
st
ht
pu
pd
penerase
setcolor
fill
repeat
"""

#KEYWORDS
keywords= keywords.split()

#TOKENIZER KEYS
alphabetical = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

numerical    = "1234567890"

whitespace_key = "\t \n"

operators = ["[", "]"]

eof_key = '\0'

#TOKENS
IDENTIFIER = "Indentifier"
KEYWORD = "Keyword"
WHITESPACE = "Whitespace"
NUMERIC = "Numeric"
OPERATOR = "Operator"
COMMENT = "Comment"
EOF = 'Eof'

WINDOWX    = 500
WINDOWY    = 500

#TURTLE PROPERTIES
TURTLE_WIDTH = 25
TURTLE_HEIGHT = 25
HYPOTENUSE = int(math.sqrt(15**2 + 20**2))
NOSEANGLE  = 15


class Token:

	def __init__(self, startChar):
		self.value = startChar
		self.type = None

	def display(self):
		#print self.value + " " + self.type
		a = " "


class Tokenizer:

	def __init__(self,source):
		self.scanner = Scanner(source)

	def getToken(self):
		char = self.getChar()
		#print char

		if char in " \t \n":
			#print "WHITESPACE"
			char = self.getChar()

			while char in " \t \n":
				char = self.getChar()
			self.scanner.rewind()
			return None

		token = Token(char)
		#print "TOKEN CREATED"

		if char in eof_key:
			#print "EOF TOKEN"
			token.type = EOF
			return token

		if char in alphabetical:
			#print "IDENTIFIER TOKEN"
			token.type = IDENTIFIER
			char = self.getChar()

			while char in alphabetical + numerical:
				token.value += char
				char = self.getChar()

			self.scanner.rewind()

			if token.value in keywords:
				token.type = KEYWORD
			return token

		if char in numerical:
			#print "NUMERIC TOKEN"
			token.type = NUMERIC
			char = self.getChar()

			while char in numerical:
				token.value += char
				char = self.getChar()
			self.scanner.rewind()
			return token

		if char in operators:
			#print "OPERATOR TOKEN"
			token.type = char
			return token

	def getChar(self):

		char   = self.scanner.scan()
		self.charAhead  = char + self.scanner.lookAhead()
		return char

	def close(self):
		self.scanner.close()


class Scanner:

	def __init__(self, source):

		#print "Scanner class initialized"
		
		self.source = source
		
		try:
			self.file  = self.source
			self.eof   = len(self.file) - 1
			self.index = 0

		except Exception, e:
			raise e

	def scan(self):
		
		if	self.index < self.eof:

			char = self.file[self.index]
			self.index = self.index +  1

			return char

		return '\0'

	def rewind(self):
		if self.index == self.eof:
			return
		self.index-=1

	def lookAhead(self):
		if self.index + 1 < self.eof :
			return self.file[self.index+1] 
		else:
			return '\0'

	
class Parser:

	def __init__(self, source):
		self.T = Tokenizer(source)
		self.tokenList = []
		self.createTokenList()
		self.dispTokenList()
		self.index = -1
		self.history = []

	def reInit(self, source):
		self.T = Tokenizer(source)
		self.tokenList = []
		self.createTokenList()
		self.dispTokenList()
		self.index = -1
		self.history = []

	def createTokenList(self):

		#print "TOKENIZER STEP"
		while True:
			token = self.T.getToken()
			if token is  not None:
				token.display()
				self.tokenList.append(token)
				if token.type == EOF:
					break
				
			#raw_input()

	def dispTokenList(self):
		for token in self.tokenList:
			token.display()


	def lookNextToken(self):
		try:
			return self.tokenList[self.index + 1]
		except IndexError as e:
			return None

	def currToken(self):
		return self.tokenList[self.index]

	def getNextToken(self):
		self.index += 1
		return self.tokenList[self.index]

	def graphInit(self):
				#graphics part

		pygame.init()
		self.white = 255, 255 , 255

		self.screen = pygame.display.set_mode((WINDOWX,WINDOWY))

		self.Turtle = Turtle(WINDOWX,WINDOWY)
		self.Turtle.setImage(pygame.image.load("logo2.png"))

		self.screen.fill(self.white)
		self.Turtle.draw(self.screen)
		pygame.display.flip()	
		pygame.display.set_icon(pygame.image.load("logo2.png"))
		pygame.display.set_caption(" Turtle")

	def parse(self):
			
		self.parseSentence()
		while True:
			tokenAhead = self.lookNextToken()
			if tokenAhead == None:
				break
			elif tokenAhead.type == EOF:
				break
			elif tokenAhead.type == KEYWORD:
				self.parseSentence()
			else:
				break



	def parseSentence(self):
		
		

		#parsing 
		nextToken = self.lookNextToken()
		if nextToken.value not in keywords:
			print "Invalid input"
			return
		if nextToken.value in ['fd', 'bk', 'rt', 'lt']:
			self.Match()
			if(self.Match(NUMERIC) == -1):
				return

			# graphics
			if nextToken.value == 'fd':
				self.Turtle.mvForward(int(self.currToken().value), self.screen)
			if nextToken.value == 'bk':
				self.Turtle.mvBackward(int(self.currToken().value), self.screen)
			if nextToken.value == 'lt':
				self.Turtle.rotate(int(self.currToken().value))
			if nextToken.value == 'rt':
				self.Turtle.rotate(int(-1 * int(self.currToken().value)))

			self.history.append((nextToken.value,self.currToken().value))


		if nextToken.value in ['pu', 'pd', 'ht', 'st', 'penerase']:
			self.Match()
			if nextToken.value == 'pu':
				self.Turtle.penUp()
			if nextToken.value == 'pd':
				self.Turtle.penDown()
			if nextToken.value == 'st':
				self.Turtle.showTurtle()
			if nextToken.value == 'ht':
				self.Turtle.hideTurtle()
			self.history.append(nextToken.value)

		if nextToken.value in ['setcolor']:
			self.Match()
			try:
				self.Match(NUMERIC)
				red = int(self.currToken().value)
				self.Match(NUMERIC)
				green = int(self.currToken().value)
				self.Match(NUMERIC)
				blue = int(self.currToken().value)
				self.Turtle.setPenColor(red, green, blue)
				self.history.append((nextToken.value, red, green, blue))
			except ValueError as e:
				print e
		if nextToken.value in ['repeat']:
			self.Match()
			self.Match(NUMERIC)

			timesToLoop = int(self.currToken().value)

			self.Match('[')
			savedIndex = self.index
			for i in range(0, timesToLoop):
				self.parse()
				if i != timesToLoop -1:
					self.index = savedIndex
			self.Match(']')
			


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		self.screen.fill(self.white)
		self.Turtle.draw(self.screen)
		pygame.display.flip()	
		#raw_input()


	def Match(self, expectedTokenType = None):
		token = self.getNextToken()
		if(expectedTokenType == None):
			return
		if(token.type != expectedTokenType):
			print "Expected token type " + expectedTokenType + " but got " + token.type
			return -1




print "Enter commands : "
#source = raw_input()
source = " "
P = Parser(source)
P.graphInit()
#P.parse()
while True:
	source = raw_input()
	if source == "exit" :
		break
	source = source + "  "
	P.reInit(source)
	P.parse()


print P.history



