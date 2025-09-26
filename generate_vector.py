'''@function_name: clean_text
@arg: array<string>
@return: array<string>
@Summary: Removes nonalphanumeric characters, extra white spaces, and stopwords
'''
def clean_text(raw_text):
    print('Clean Text')
    return raw_text

'''@function_name: tokenize
@arg: array<string>
@return: array<int>
@summary: Takes in the cleaned text and breaks up the sequence of strings into words, 
keywords, phrases, symbols and other elements. In our project we will simply break
the sequence of strings into words.
'''
def tokenize(cleaned_text):
    print('Tokenize')
    return cleaned_text

'''@function_name: build_vocab
@arg: array<string>
@return: frequency hashmap <string>:<int>
@summary: Takes in the cleaned text and tokenizes the text into a
frequency hashmap with key/value pair of <string>word:<int>freq
'''
def build_vocab(token):
    print(token)
    return token

'''@function_name: vectorization
@arg: array<int>
@return: array<array<int>>
@summary: Takes the vocabulary list and performs vectorization on each sentence
'''
def vectorization(vocab_list):
    print(vocab_list)
    return vocab_list

'''@function_name: generate_vector
@arg: array<string>
@return: array<array<int>>
@summary: Takes raw text data and transforms it into vectors for nlp
'''
def generate_vector(array):
    cleaned_text = clean_text(array)
    token = tokenize(cleaned_text)
    vocab_list = build_vocab(token)
    return vectorization(vocab_list)