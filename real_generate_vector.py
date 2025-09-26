import tensorflow as tf

def print_bow(sentences) -> None:
    # Set parameters
    max_tokens = 10  
    output_mode = "count" 

    # Create the vectorization layer
    vectorizer = tf.keras.layers.TextVectorization(max_tokens=max_tokens, output_mode=output_mode)

    # Adapt the vectorizer to the dataset
    vectorizer.adapt(sentences)

    bow_representation = vectorizer(sentences)

    # Display results
    print("Vocabulary:", vectorizer.get_vocabulary())
    print("Bag-of-Words Representation:\n", bow_representation.numpy())