import os, sys
class Hex(object):
	"""This module is responsible for string hex operations."""
	def __init__(self, string):
		self.string = string
		self.hex = self.turnToHex(string)
		self.t = self.turnToText(self.hex)
		self.t2 = self.turnToText(self.t)
	def turnToHex(self, string):
		if(type(string) == str):
			hexString = ''
			for char in string:
				hexadecimal = hex(ord(char))
				hexString = hexString + '\\' + str(hexadecimal)[1:]
			return hexString
	def turnToText(self, hexa):
		if(type(hexa) == str):
			textString=''
			hexList = hexa.split('\\')
			for hexxor in hexList:
				hexxor = str('0') + str(hexxor)
				textString+= chr(int(hexxor,0))
			return textString[1:]
def main():
	if(len(sys.argv) < 2):
		print 'Not enought arguments.'
	else:
		if(len(sys.argv) == 3):
			mode = str(sys.argv[1])
			fileName = str(sys.argv[2])
			if(mode == '--hex'):
				print ' [+] File: Looking for ' + str(fileName) + '...' 
				if(os.path.isfile(fileName)):
					print ' [+] File: ' + str(fileName) + ' found.'
					infile = open(fileName, 'r')
					print ' [+] File: Reading contents...'
					data = infile.read()
					h = Hex(data)
					print ' [+] Transform: Text to Hex...'
					outfile_name = fileName + '.hex'
					outfile = open(outfile_name,'w')
					outfile.write(h.hex)
					print ' [+] Text file encoded to hex.'
			if(mode == '--text'):
				if(os.path.isfile(fileName)):
					if(fileName[len(fileName) -3:] == 'hex'):
						infile = open(fileName, 'r')
						data = infile.read()
						h = Hex(data)
						outfile_name = fileName[:-3]
						if(os.path.isfile(outfile_name)):
							print ' [*] File: ' + str(outfile_name) + ' already exists. Overwrite? (y/n)'
							opt = raw_input('Y/N: ')
							if(opt == 'Y' or 'y'):
								outfile = open(outfile_name,'w')
								outfile.write(str(h.t2))
								print ' [+] Hex file decoded to text.'
							else:
								print ' [!] Aborting...'
								sys.exit(0)
						else:
							outfile = open(outfile_name,'w')
							outfile.write(str(h.t2))
							print ' [+] Hex file decoded to text.'
					else:
						print ' [!] File not in hex format.'
if __name__ == '__main__':
	main()