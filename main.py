# Uncomment import and download code below if you did not download nltk stopword list on your environment yet
# import nltk
# nltk.download('stopwords')
import generate_vector
import real_generate_vector

sentence = ["Joe waited for the train", "The train was late", "Mary and Samantha took the bus",
"I looked for Mary and Samantha at the bus station",
"Mary and Samantha arrived at the bus station early but waited until noon for the bus"]

def main():
    print('\nMy Bag of words implementation output:\n')
    generate_vector.generate_vector(sentence)
    print('\nTensorflow Bag of words output\n')
    real_generate_vector.print_bow(sentence)

if __name__ == '__main__':
    main()