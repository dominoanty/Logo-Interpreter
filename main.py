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


keywords_key = keywords.split()

whitespace_key = "\t \n"

operator_key = "[ ]".split()

KEYWORD = "Keyword"
WHITESPACE = "Whitespace"
NUMERIC = "Numeric"
OPERATOR = "Operator"
COMMENT = "Comment"
EOF = '\0'
class Token

	def __init__(self, startChar):
		self.value = startChar
		self.type = None



class Tokenizer

	def __init__(self,filename):
		self.scanner = Scanner(filename)

	def getToken(self):
		char = getChar()

	    while char in whitespace_key or charAhead == "/*":

	        # process whitespace
	        while char in whitespace_key:
	            token = Token(char)
	            token.type = WHITESPACE
	            char = getChar() 

	            while char in whitespace_key:
	                token.value += c1
	                char = getChar() 
	                      

	        # process comments
	        while self.charAhead == "/*":
	            # we found comment start
	            token = Token(self.charAhead)
	            token.type = COMMENT

	            getChar() # read past the first  character of a 2-character token

	            while not (self.charAhead == "*/"):
	                if char == ENDMARK:
	                    print "Comment not ended"
	                token.value += char
	                char = getChar() 

	            token.value += charAhead  # append the */ to the token cargo

	            getChar() 

	    

	def getChar(self):

		char   = self.scanner.scan()
		self.charAhead  = char + self.scanner.lookAhead()
		return char


class Scanner:

	def __init__(self, filename):

		print "Scanner class initialized"
		
		self.filename = filename
		
		try:
			self.file  = open(filename, 'r')
			self.eof   = len(self.file) - 1
			self.index = 0

		except Exception, e:
			raise e

	def scan(self):
		
		if	self.index < self.eof:

			char = self.file[index]
			index = index +  1

			if char == '\n' or char == '\r':
				print 'newline'
				return '\n'
			elif char == ' ':
				print 'whitespace'
				return ' '
			else:
				print char
				return char
		return -1
	def lookAhead(self):
		return self.file[index+1]


print "Enter a file : "
filename = raw_input()
T = Tokenizer(filename)