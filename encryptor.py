import getopt, sys

inputFile 	= ""
outputFile 	= ""
encrypt 	= False
decrypt 	= False

def readFile(inputFile):
	message = ""
	fi = open(inputFile, "r")
	for line in fi:
		message += line
	return message

def getMessage():
	message = raw_input("Enter message    : ")
	message += "\n"
	return message

def decryptMode():
	global outputFile
	global inputFile
	original_message = ""

	if not inputFile:
		original_message = getMessage()
	elif inputFile:
		original_message = readFile(inputFile)

def encryptMode():
	global outputFile
	global inputFile
	original_message = ""

	if not inputFile:
		original_message = getMessage()
	elif inputFile:
		original_message = readFile(inputFile)


	char_array = list(original_message)	#split input into idvidual characters
	# print(char_array)	#debug output

	key_char = ord(char_array[0])	# get the first character in the message for later key obfuscation
	prev_char = 13 					# inital key = 13 (ROT-13)
	encrypted_char_array = [] 		# stores encrypted characters
	original_char_code_array = [] 	# stores original character codes

	for char in char_array:

		char_code = ord(char) 	#get ascii value of character
		new_char = char_code + prev_char #encrypted character shifts by the ascii value of the previous character

		# while new_char > 126 or 32 > new_char: 	#broken wrapping, included for no reason
		# 	# print("subtracting")
		# 	if new_char > 126:
		# 		new_char -= 126
		# 	elif new_char < 32:
		# 		new_char += 32

		while new_char > 126: 		#fixed wrapping, characters will wrap from >126 to >32
			new_char = 32 + (new_char-126)

		original_char_code_array.append(char_code)
		encrypted_char_array.append(new_char)
		# print(prev_char) 	#debug output
		# print(new_char)
		prev_char = new_char #key for next character

	key_char += ord(char_array[(len(char_array)-1)]) 	#get the final character in the message
   														# to encrypt the first character
	while key_char > 126:
		# print("wrapper key: {}").format(key_char)	#debug output
	 	key_char = 32 + (126-new_char)
	

	encrypted_char_array[0] = key_char
	# print(original_char_code_array)	#debug output
	# print(encrypted_char_array)

	final_message_array = []

	for char in encrypted_char_array:
		final_message_array.append(chr(char))

	# print(final_message_array)
	final_message_string = "".join(final_message_array)

	if outputFile:
		fo = open(outputFile,"w")
		fo.write(final_message_string)
	else:
		print("Encrypted message: {}").format(final_message_string) 	#output message

def usage():
	print
	print("Usage: rot-13.py")
	print("-h     displays this help message")
	print("-e     sets rot-13.py to encrypt mode")
	print("-d     sets rot-13.py to decrypt mode")
	print("-i     input file for program to process (default is stdin)")
	print("-o     outfile for program output (default is stdout)")
	sys.exit(2)

def main(argv):
	#global variables
	global inputFile
	global outputFile
	global encrypt
	global decrypt

	try:
		opts, args = getopt.getopt(argv, "hedi:o:",)
	except getopt.GetoptError as e:
		print(str(e))
		usage()

	for opt, arg in opts:
		if opt == "-h":
			usage()

		if opt == "-e":
			encrypt = True

		if opt == "-d":
			decrypt = True

		if opt == "-i":
			inputFile = arg

		if opt == "-o":
			outputFile = arg

	if not encrypt and not decrypt:
		print("[!!] Error setting core variables:")
		print("Encrypt mode: {}").format(encrypt)
		print("Decrypt mode: {}").format(decrypt)
		usage()

	if encrypt and decrypt:
		print("[!!] Error setting core variables:")
		print("Encrypt mode: {}").format(encrypt)
		print("Decrypt mode: {}").format(decrypt)
		usage()

	if not outputFile:
		print("[*] no output file selected, outputting to terminal")
	if not inputFile:
		print("[*] no input file selected, input through stdin")

	if encrypt:
		encryptMode()
	elif decrypt:
		decryptMode()
	else:
		print("how on Earth did you manage that?")

if __name__ == "__main__":
	main(sys.argv[1:])
