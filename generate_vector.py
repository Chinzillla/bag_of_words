#if you get error for stopwords not found read the comment in like 1 in main.py
from nltk.corpus import stopwords
import re

'''@function_name: clean_text
@arg: array<string>
@return: array<array<string>>
@Summary: Removes nonalphanumeric characters, extra white spaces, and stopwords.
We will use NLTK to provide a preset of stopwords.
'''
def clean_text(sentences):
    stopword_list = stopwords.words('english')
    cleaned_sentences = []
    
    for sentence in sentences:
        words = re.sub(r"[^\w]", " ", sentence).split()
        result = [word.lower() for word in words if word not in stopword_list]
        cleaned_sentences.append(result)
    
    return cleaned_sentences
    
'''@function_name: tokenize
@arg: array<array<string>>
@return: array<string>
@summary: Takes in the cleaned text and breaks up the sequence of strings into words, 
keywords, phrases, symbols and other elements. In our project we will simply break
the sequence of strings into words then sort.
'''
def tokenize(cleaned_sentences):
    words = []
    for cleaned_sentence in cleaned_sentences:
        words.extend(cleaned_sentence)
    return sorted(words)

'''@function_name: build_vocab
@arg: array<string>
@return: frequency hashmap <string>:<int>
@summary: Takes in the cleaned text and tokenizes the text into a
frequency hashmap with key/value pair of <string>word:<int>freq
'''
def build_vocab(token):
    vocab_list = {}
    for word in token:
        if word not in vocab_list:
            vocab_list[word] = 1
        else:
            vocab_list[word] += 1
    return vocab_list

'''@function_name: vectorization
@arg: vocab_list<dict>, cleaned_sentences<array<array<string>>>
@return: array<array<int>>
@summary: Takes the vocabulary list and performs vectorization on each sentence
'''
def vectorization(vocab_list, cleaned_sentence):
    vector_size = len(vocab_list)
    return vocab_list

'''@function_name: generate_vector
@arg: array<string>
@return: array<array<int>>
@summary: Takes raw text data and transforms it into vectors for nlp
'''
def generate_vector(sentences):
    cleaned_sentences = clean_text(sentences)
    token = tokenize(cleaned_sentences)
    vocab_list = build_vocab(token)
    return vectorization(vocab_list, cleaned_sentences)