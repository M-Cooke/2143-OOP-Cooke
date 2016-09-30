"""
Micah Cooke
micahcooke75@gmail.com
Program 1- Easy Cipher
3 Oct @ 1p.m.
"""
"""
@ Name: ShiftCipher
@ Description: Simple class to do a shift cipher
"""
class ShiftCipher(object):
	
	"""
	@ Name: __init__
	@ Description: 
	@ Params:
	     None
	"""
	def __init__(self):
		
		self.plainText = None
		self.cipherText = None
		self.cleanText = None
		self.shift = 3
	"""
	Nice string representation of your class to help debug.
	"""
	def __str__(self):
		return "plainText: %s\ncipherText: %s\ncleanText: %s\nshift: %d\n" % (self.plainText,self.cipherText,self.cleanText,self.shift)
	
	"""
	@ Name: promptUserMessage
	@ Description: Prompts user for message from standard in
	@ Params:
	     None
	"""
	def promptUserMessage(self):
		temp = input("Message: ")
		self.setMessage(temp)

	"""
	@ Name: setMessage
	@ Description: sets plaintext and then cleans and calls encrypt.
	@ Params:
	     message {string}: String message
	     encrypted {bool}: False = plaintext True=ciphertext
	"""
	def setMessage(self,message,encrypted=False):
		if(not encrypted):
			self.plainText = message
			self.cleanData()
			self.__encrypt()
		else:
			self.cipherText = message
			self.__decrypt()
	
	"""
	@ Name: getCipherText
	@ Description: stores ciphertext in self
	@ Params:
	     None
	"""
	def getCipherText(self):
		return self.cipherText
		
	"""
	@ Name: getPlainText
	@ Description: stores plaintext in self
	@ Params:
	     None
	"""
	def getPlainText(self):
		return self.plainText

	"""
	@ Name: setShift
	@ Description: sets the shift value
	@ Params:
	     None
	"""
	def setShift(self,shift):
		self.shift = shift
	
	"""
	@ Name: getShift
	@ Description: stores shift in self
	@ Params:
	     None
	"""
	def getShift(self):
		return self.shift
		
	"""
	@ Name: cleanData
	@ Description: goes through plain text and removes
			nonAlphaNumeric values
	@ Params:
	     None
	"""	
	def cleanData(self):
		self.cleanText = ''
		AlphaNumeric = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
		for letter in self.plainText:
			if ord(letter) == 32:
				continue
			if ord(letter) > 96:
				self.cleanText += chr(ord(letter)-32)
			if not '#' in AlphaNumeric:
				continue
			else:
				self.cleanText += letter
			
	"""
	@ Name: __encrypt
	@ Description: encrypts plaintext using the shift value
	@ Params:
	     None
	"""
	def __encrypt(self):
		self.cipherText = ''
		if(not self.cleanText):
			return
		for letter in self.cleanText:
		    self.cipherText += chr((((ord(letter)-65) + self.shift) % 26)+65)
		    
		
	
	"""
	@ Name: __decrypt
	@ Description: decripts ciphertext using the shift value
	@ Params:
	     None
	"""
	def __decrypt(self):
		self.cleanText = ''
		if(not self.cipherText):
			return
		for letter in self.cipherText:
			self.cleanText += chr((((ord(letter)-65) - self.shift) %26) + 65)

"""
Only run this if we call this file directly:
"""
if __name__=='__main__':
alice = ShiftCipher()
alice.promptUserMessage()
print(alice)


bob = ShiftCipher()
bob.setMessage(alice.getCipherText(),True)
print(bob)
