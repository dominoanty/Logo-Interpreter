class Scanner:

	def __init__(self, filename):

		print "Scanner class initialized"
		self.filename = filename
		try:
			self.file = open(filename, 'r')
		except Exception, e:
			raise e
		self.analyze()

	def analyze(self):
		for line in self.file:
			for char in line:
				if char == '\n' or char == '\r':
					print 'newline'
				elif char == ' ':
					print 'whitespace'
				else:
					print char

print "Hello world"
print "Enter a file : "
filename = raw_input()
S = Scanner(filename)