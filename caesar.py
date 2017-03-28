import string

def alphabet_position(letter):

	lowercase = string.ascii_lowercase
	uppercase = string.ascii_uppercase

	if letter in lowercase:
		indexOfletter = lowercase.index(letter)

		return indexOfletter

	elif letter in uppercase:
		indexOfletter = uppercase.index(letter)

		return indexOfletter

	else:
		return None

def rotate_character(char, rot):

	if alphabet_position(char) == None:
		return char

	else:
		newCharIndex = (alphabet_position(char) + rot) % 26

		if char in string.ascii_lowercase:
			return string.ascii_lowercase[newCharIndex]

		else:
			return string.ascii_uppercase[newCharIndex]

def encrypt(text, rot):
	originalText = text
	newText = ""

	for i in originalText:
		newLetter = rotate_character(i, rot)
		newText += newLetter

	return newText
