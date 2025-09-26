# Bag of Words Model for NLP

How Bag of Words in NLP works:

1. Todo: We must preprocess the text
- Converting text to lowercase
- Removing non-word characters
- Removing extra spaces

How:

2. Todo We break down text into sentences and from sentences into words

Example:
Hi my name is Brandon. Nice to meet you. How is your family doing?

We can analyze that we have a total of three sentences. We can split this into three sentences

- Hi my name is Brandon
- Nice to meet you
- How is your family doing

How:

3. Once we break down the text into sentences, we next have to break the text into words

- [hi,my,name,is,brandon]
- [nice,to,meet,you]
- [how,is,your,family,doing]

How:

4. Todo: We must remove stopwords from our word lists

Stopwords are common words that don't add much meaning like "is", "the", "a", "to"

After removing stopwords:
- [hi,name,brandon]
- [nice,meet]
- [family,doing]

How:

5. Todo: We build our vocabulary from all unique words

From our example, our vocabulary would be:
[brandon,doing,family,hi,meet,name,nice]

This is sorted alphabetically and contains each unique word only once

We also create a frequency hashmap to track how many times each word appears across all sentences:
{brandon:1, doing:1, family:1, hi:1, meet:1, name:1, nice:1}

How:


How:

6. Todo: We create vectors for each sentence based on our vocabulary

Each sentence is represented as a vector where each position corresponds to a word in our vocabulary. We mark with the frequency if the word is present, 0 if not

- Hi my name is Brandon → [1,0,0,1,0,1,0]
- Nice to meet you → [0,0,0,0,1,0,1]
- How is your family doing → [0,1,1,0,0,0,0]

How:

7. Todo: These vectors can now be used for machine learning

Each sentence is now represented as a numerical vector that can be:
- Compared with other sentences
- Used for classification tasks
- Used for similarity measurements