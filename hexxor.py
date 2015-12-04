import os, sys
def update_progress(progress):
	    barLength = 50 # Modify this to change the length of the progress bar
	    status = ""
	    if isinstance(progress, int):
	        progress = float(progress)
	    if not isinstance(progress, float):
	        progress = 0
	        status = "Erro: Variavel precisa ser float\r\n"
	    if progress < 0:
	        progress = 0
	        status = "Pausa.\r\n"
	    if progress >= 1:
	        progress = 1
	        status = " Completo.\r\n"
	    block = int(round(barLength*progress))
	    text = "\r [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), str(progress*100)[:4], status)
	    sys.stdout.write(text)
	    sys.stdout.flush()
class Hex(object):
	"""This module is responsible for string hex operations."""
	def __init__(self, string, mode):
		self.string = string
		if(mode == 'hex'):
			self.hex = self.turnToHex(string)
		if(mode == 'text'):
			self.t = self.turnToText(self.string)
	def turnToHex(self, string):
		if(type(string) == str):
			hexString = ''
			string_len = len(string)
			max_steps = float(len(string))
			one_step = float(1)
			calc = (one_step/max_steps)
			progress = calc
			print ' [+] Converting file into hex code... (This might take a while)'
			for char in string:
				hexadecimal = hex(ord(char))
				hexString = hexString + '\\' + str(hexadecimal)[1:]
				update_progress(progress)
				progress+=calc
			return hexString
	def turnToText(self, hexa):
		if(type(hexa) == str):
			textString=''
			hexList = hexa.split('\\')
			max_steps = float(len(hexList))
			one_step = float(1)
			calc = (one_step/max_steps)
			progress =calc
			print ' [+] Converting hex file into original code... (This might take a while)'
			for hexxor in hexList:
				hexxor = str('0') + str(hexxor)
				#print hexxor
				textString+= chr(int(hexxor,0))
				update_progress(progress)
				progress+=calc
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
					infile = open(fileName, 'rb')
					print ' [+] File: Reading contents...'
					data = infile.read()
					h = Hex(data,'hex')
					print ' [+] Transform: Text to Hex...'
					outfile_name = fileName + '.hex'
					outfile = open(outfile_name,'wb')
					outfile.write(h.hex)
					print ' [+] Text file encoded to hex.'
				else:
					if(os.path.isdir(fileName)):
						print ' [+] Directory: ' + str(fileName) + ' is a directory. Looking for files...'
						os.chdir(fileName)
						for n_file in os.listdir(fileName):
							if(n_file.endswith(".hex")):
								continue
							if(os.path.isdir(n_file)):
								continue
							if(fileName[len(fileName)-1:] <> '\\'):
								fileName = fileName + '\\'
							n_file = fileName + str(n_file)
							print ' [+] File: ' + str(n_file) + ' found.'
							infile = open(n_file, 'rb')
							print ' [+] File: Reading contents...'
							data = infile.read()
							h = Hex(data,'hex')
							print ' [+] Transform: Text to Hex...'
							outfile_name = n_file + '.hex'
							outfile = open(outfile_name,'wb')
							outfile.write(h.hex)
							print ' [+] Text file encoded to hex.'
							print '\n'
			if(mode == '--text'):
				if(os.path.isfile(fileName)):
					if(fileName[len(fileName) -3:] == 'hex'):
						infile = open(fileName, 'rb')
						data = infile.read()
						h = Hex(data,'text')
						outfile_name = fileName[:-3]
						if(os.path.isfile(outfile_name)):
							print ' [*] File: ' + str(outfile_name) + ' already exists. Overwrite? (y/n)'
							opt = raw_input('Y/N: ')
							if(opt == 'Y' or 'y'):
								outfile = open(outfile_name,'wb')
								outfile.write(str(h.t))
								print ' [+] Hex file decoded to text.'
							else:
								print ' [!] Aborting...'
								sys.exit(0)
						else:
							outfile = open(outfile_name,'wb')
							outfile.write(str(h.t))
							print ' [+] Hex file decoded to text.'
					else:
						print ' [!] File not in hex format.'
				else:
					if(os.path.isdir(fileName)):
						print ' [+] Directory: ' + str(fileName) + ' is a directory. Looking for hexxed files...'
						for n_file in os.listdir(fileName):
							if(os.path.isdir(n_file)):
								pass
							if(n_file.endswith(".hex")):
								if(fileName[len(fileName)-1:] <> '\\'):
									fileName = fileName + '\\'
								n_file = fileName + str(n_file)
								print ' [+] File: ' + str(n_file) + ' found.'
								infile = open(n_file, 'rb')
								print ' [+] File: Reading contents...'
								data = infile.read()
								h = Hex(data,'text')
								print ' [+] Transform: Hex to text...'
								outfile_name = n_file[:-3]
								outfile = open(outfile_name,'wb')
								outfile.write(str(h.t))
								print ' [+] Hex file decoded to text.'
								print '\n'
if __name__ == '__main__':
	main()