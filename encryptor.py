#ROT 13 with a twist (gettit?)

#Auth: Lysergic
#Name: ROT13_stylized.py
#Desc: Encrypts a string by using each character as a new key
 
def main():
	message = raw_input("Enter a message: ")
	encrypted_message_array = list(message)
	# print(encrypted_message_array)

	key_char = ord(encrypted_message_array[0])
	prev_char = 13
	new_encrypted_message_array = []
	char_encrypted_message_array = []

	for char in encrypted_message_array:

		char_code = ord(char)
		new_char = char_code + prev_char

		char_encrypted_message_array.append(char_code)

		while new_char > 126 or 32 > new_char:
			# print("subtracting")
			if new_char > 126:
				new_char -= 126
			elif new_char < 32:
				new_char += 32


		new_encrypted_message_array.append(new_char)
		# print(prev_char)
		# print(new_char)
		prev_char = new_char

	key_char += ord(encrypted_message_array[(len(encrypted_message_array)-1)])

	while key_char > 126 or 32 > key_char:
		# print("subtracting")
		if key_char > 126:
			key_char -= 126
		elif key_char < 32:
			key_char += 32
	

	new_encrypted_message_array[0] = key_char
	# print(char_encrypted_message_array)
	# print(new_encrypted_message_array)

	final_message = []

	for char in new_encrypted_message_array:
		final_message.append(chr(char))

	# print(final_message)
	final_message_string = "".join(final_message)
	print("Encrypted message: {}").format(final_message_string)
if __name__ == "__main__":
	main()
