import source.encryptor as encryptor


def encrypt_text(text, method):
	i = 0
	begword = 0
	result = ''
	while i != len(text):
		if not text[i].isalpha() and not text[i].isdigit():
			result += method(text[begword:i]) + text[i]
			begword = i + 1
		i = i + 1
	else:
		result += text[begword:i][::-1]
	return result


def reverse_horizontal_permutation(text):
	return encryptor.reverse_horizontal_permutation(text)


def increasing_alternative_horizontal_permutation_for_word(word):
	wordout_ls = [""]*len(word)
	for i in range(len(word)):
		if i%2 == 0:
			wordout_ls[i] = word[i//2]
		else:
			wordout_ls[i] = word[-(i//2)-1]
	return ''.join(wordout_ls)


def increasing_alternative_horizontal_permutation(text):
	return encrypt_text(text, increasing_alternative_horizontal_permutation_for_word)


def increasing_reverse_horizontal_permutation(text):
	return encrypt_text(text, (lambda word: increasing_alternative_horizontal_permutation_for_word(word[::-1])))


def decreasing_alternative_horizontal_permutation_for_word(word):
	wordout_ls = [""] * len(word)
	if len(word) % 2 == 0:
		for i in range(len(word)):
			if i % 2 == 0:
				wordout_ls[-i-1] = word[i // 2]
			else:
				wordout_ls[-i-1] = word[-(i // 2) - 1]
		return ''.join(wordout_ls)
	else:
		for i in range(len(word)):
			if i % 2 == 1:
				wordout_ls[-i-1] = word[i // 2]
			else:
				wordout_ls[-i-1] = word[-(i // 2) - 1]
		return ''.join(wordout_ls)


def decreasing_alternative_horizontal_permutation(text):
	return encrypt_text(text, decreasing_alternative_horizontal_permutation_for_word)


def decreasing_reverse_alternative_horizontal_permutation(text):
	return encrypt_text(text, (lambda word: decreasing_alternative_horizontal_permutation_for_word(word[::-1])))


def sequential_permutation_for_word(word):
	result = []
	for i in range(len(word)):
		if i % 2 == 0:
			result.append(word[len(word)//2+i//2])
		else:
			result.append((word[i//2]))
	return ''.join(result)


def sequential_permutation(text):
	return encrypt_text(text, sequential_permutation_for_word)


def encrypting_with_odd_symbols(text):
	return encrypt_text(text, (lambda word: word[::2]))
    
