'''@function_name: clean_text
@arg: array of string
@Summary: Removes nonalphanumeric characters and extra white spaces
'''
def clean_text(raw_text):
    print('Clean Text')
    return raw_text

'''@function_name: tokenize
@arg: array of strings
@summary: Takes in the cleaned text and tokenizes the text into a frequency hashmap
'''
def tokenize(cleaned_text):
    print('Tokenize')
    return cleaned_text

'''@function_name: build_vocab
@arg: array of strings
@summary: Takes in the cleaned text and tokenizes the text into a frequency hashmap
'''
def build_vocab(token):
    print(token)
    return token

'''@function_name: vectorization
@arg: array of strings
@summary: Takes in the cleaned text and tokenizes the text into a frequency hashmap
'''
def vectorization(vocab_list):
    print(vocab_list)
    return vocab_list

'''@function_name: generate_vector
@arg: array of strings
@summary: Takes in the cleaned text and tokenizes the text into a frequency hashmap
'''
def generate_vector(array):
    cleaned_text = clean_text(array)
    token = tokenize(cleaned_text)
    vocab_list = build_vocab(token)
    return vectorization(vocab_list)