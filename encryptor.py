#ROT 13 with a twist (gettit?)

#Auth: Lysergic
#Name: ROT13_stylized.py
#Desc: Encrypts a string by using each character as a new key
 
def main():
	original_message = raw_input("Enter a message: ")
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
	print("Encrypted message: {}").format(final_message_string) 	#output message
if __name__ == "__main__":
	main()
