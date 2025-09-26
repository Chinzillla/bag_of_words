# Naive implementation of Bag of Words Model for NLP

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

## Difference between my implementation and tensorflow implementaion:

```bash
(.venv) C:\Users\Chinzilla\bag_of_words>python main.py
2025-09-26 15:53:36.594281: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2025-09-26 15:53:37.658635: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.

My Bag of words implementation output:

[1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0]
[0, 1, 0, 0, 0, 1, 1, 0, 2, 0, 0, 1, 1, 1, 1]

Tensorflow Bag of words output

2025-09-26 15:53:37.895705: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
Vocabulary: ['[UNK]', np.str_('the'), np.str_('bus'), np.str_('samantha'), np.str_('mary'), np.str_('for'), np.str_('and'), np.str_('waited'), np.str_('train'), np.str_('station')]
Bag-of-Words Representation:
 [[1 1 0 0 0 1 0 1 1 0]
 [2 1 0 0 0 0 0 0 1 0]
 [1 1 1 1 1 0 1 0 0 0]
 [3 1 1 1 1 1 1 0 0 1]
 [6 2 2 1 1 1 1 1 0 1]]

(.venv) C:\Users\Chinzilla\bag_of_words>
```