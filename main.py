keywords = """
fd
bk
lt
rt
arc
arc2
st
ht
pu
pd
penerase
setfloodcolor
fill"""

#KEYWORDS
keywords= keywords.split()

#TOKENIZER KEYS
alphabetical = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

numerical    = "1234567890"

whitespace_key = "\t \n"

operator_key = "[]"

eof_key = '\0'

#TOKENS
IDENTIFIER = "Indentifier"
KEYWORD = "Keyword"
WHITESPACE = "Whitespace"
NUMERIC = "Numeric"
OPERATOR = "Operator"
COMMENT = "Comment"
EOF = 'Eof'

class Token:

	def __init__(self, startChar):
		self.value = startChar
		self.type = None

	def display(self):
		print self.value + " " + self.type



class Tokenizer:

	def __init__(self,filename):
		self.scanner = Scanner(filename)

	def getToken(self):
		char = self.getChar()
		
		if char in " \t \n":
			print "WHITESPACE"
			char = self.getChar()

			while char in " \t \n":
				char = self.getChar()
			self.scanner.rewind()
			return None

		token = Token(char)
		print "TOKEN CREATED"

		if char in eof_key:
			print "EOF TOKEN"
			token.type = EOF
			return token

		if char in alphabetical:
			print "IDENTIFIER TOKEN"
			token.type = IDENTIFIER
			char = self.getChar()

			while char in alphabetical + numerical:
				token.value += char
				char = self.getChar()

			self.scanner.rewind()

			if token.value in keywords:
				print "KEYWORD TOKEN"
				token.type = KEYWORD
			return token

		if char in numerical:
			print "NUMERIC TOKEN"
			token.type = NUMERIC
			char = self.getChar()

			while char in numerical:
				token.value += char
				char = self.getChar()
			self.scanner.rewind()
			return token

		if char in operator_key:
			print "OPERATOR TOKEN"
			token.type = char
			return token

	def getChar(self):

		char   = self.scanner.scan()
		self.charAhead  = char + self.scanner.lookAhead()
		return char

	def close(self):
		self.scanner.close()


class Scanner:

	def __init__(self, filename):

		print "Scanner class initialized"
		
		self.filename = filename
		
		try:
			self.file  = open(filename, 'r').read()
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

	def close(self):
		self.file.close()


print "Enter a file : "
filename = raw_input()
T = Tokenizer(filename)
while True:
	print "TOKENIZER STEP"
	token = T.getToken()
	if token is  not None:
		token.display()
		if token.type == EOF:
			break
	raw_input()