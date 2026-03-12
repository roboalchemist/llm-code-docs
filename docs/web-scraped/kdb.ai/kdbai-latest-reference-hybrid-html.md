# Source: https://code.kx.com/kdbai/latest/reference/hybrid.html

Title: About hybrid search in KDB.AI

URL Source: https://code.kx.com/kdbai/latest/reference/hybrid.html

Markdown Content:
_This page explains the KDB.AI hybrid search feature._

Hybrid search is a technique that combines multiple search algorithms to improve the accuracy and relevance of the results.

Hybrid search in KDB.AI
-----------------------

In KDB.AI, hybrid search leverages the power of keyword and semantic searches by combining sparse vectors with dense vectors.

The key components of a KDB.AI hybrid search are:

*   [dense vectors](https://code.kx.com/kdbai/latest/reference/hybrid.html#dense-vectors)
*   [sparse vectors](https://code.kx.com/kdbai/latest/reference/hybrid.html#sparse-vectors)
*   [tokenization](https://code.kx.com/kdbai/latest/reference/hybrid.html#tokenization)
*   [Best Matching 25 (BM25) algorithm](https://code.kx.com/kdbai/latest/reference/hybrid.html#the-best-matching-25-bm25-algorithm)

A hybrid search allows you to:

*   use the BM25 algorithm to search for a phrase and find the most relevant results through advanced string matching.
*   perform a similarity search to find the most relevant results from a semantic perspective.
*   rank the combined results with a weighting term `alpha`; the lower its value, the more relevant the results from the text search are, compared to the semantic search results.

Dense vectors
-------------

Dense vectors are information-rich representations that capture meaning and context, which makes them valuable tools for understanding and processing complex data. A dense vector has significant values in a high proportion of its elements.

If in sparse vectors most entries are zeros, dense vectors have a large amount of non-zero elements. Each element in a dense vector carries meaningful information. Dense vectors are the basic vector type in KDB.AI. They encode the semantic meaning of words, enabling semantic search.

Sparse vectors
--------------

Sparse vectors are mathematical representations where most of the elements are zero. In other words, a sparse vector contains relatively few non-zero elements compared to its total size. By having significant empty or zero values, sparse vectors conserve memory and improve computation while representing only the essential information.

A basic example of a sparse vector is a bag-of-words representation of a sentence. Let's consider the sentence:

```
the cow jumped over the moon
```

Its bag of words is given by the count of each word:

```
{ "the":2 , "cow":1, "jumped":1, "over":1, "moon":1 }
```

Tokenization
------------

Tokenization is the process of segmenting text into discrete units (tokens) that are then represented as learnable high-dimensional vectors. These tokens serve as the fundamental input for various architectures, including transformer-based models like BERT, GPT, and their variants.

Modern tokenizers make the first layer of encoding for large language models by assigning to each sentence a list of integer tokens. So for our example we have:

```
from transformers import BertTokenizerFast
from collections import Counter

tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
Counter(tokenizer("The cow jumped over the moon")['input_ids'])
```

The result is a sparse vector with `101` and `102` delimiting the start and end of the text:

```
{1996: 2, 101: 1, 11190: 1, 5598: 1, 2058: 1, 4231: 1, 102: 1}
```

Sparse vectors will be as above - dictionaries with `32bit` integer keys and values.

The Best Matching 25 (BM25) algorithm
-------------------------------------

The BM25 algorithm is a scoring method developed in the 1970's for document retrieval. BM25 is part of a family of ranking functions, with roots in the probabilistic information retrieval model.

For each token in the sparse query vector, the algorithm gives a positive weight to any element of the collection that contains that token. The weights are proportional to the rarity of the word in the collection and dependent on two search parameters `k` and `b`.

### Example

For a query vector Q with tokens q i and document D, we apply the following:

*   f(q i,D) is the number of times the token q i occurs in the document D.
*   |D| is the number of tokens in the document D. 
*   a v g d l is the average document length. 

![Image 1](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20%20{\fontsize{10}{10}%20\text{score}(D,Q)=\sum%20_{i=1}^{n}{\text{IDF}}(q_{i})\cdot%20{\frac%20{f(q_{i},D)\cdot%20(k+1)}{f(q_{i},D)+k\cdot%20\left(1-b+b\cdot%20{\frac%20{|D|}{\text{avgdl}}}\right)%20%20}}}})

In this case, The Inverse Document Frequency, I D F, is a scaling factor based on how rare a word is, calculated with the following formula, where:

*   N is the number of documents in the collection.
*   n(q i) is the number of documents containing q i.

![Image 2](https://latex.codecogs.com/svg.latex?{\color{NavyBlue}%20%20{\fontsize{10}{10}%20\text{IDF}(q_i)=%20\ln%20\left(\frac{N-n(q_i)+0.5}{n(q_i)+0.5}%20+%201%20\right)}})

Search engines rely on this algorithm for text searches due to its:

*   effective handling of term frequency and document length
*   proven performance in ranking documents by relevance in a computationally efficient manner
*   flexibility in using parameters like `k` and `b` that can be tuned to fit specific datasets or types of queries

To facilitate BM25 searches, KDB.AI uses an [inverted index](https://code.kx.com/kdbai/latest/reference/index.html#33-inverted-index).

Next steps
----------

Now that you're familiar with the hybrid search concepts, you can do the following:

*   Go to the [How to perform a hybrid search](https://code.kx.com/kdbai/latest/use/hybrid-search.html) page and follow the steps.
*   Go to the KDB.AI Learning hub to discover [how to improve accuracy with hybrid search](https://kdb.ai/learning-hub/articles/improve-accuracy-with-hybrid-search/).
*   Watch a session on [the advantages of hybrid search in vector databases](https://www.youtube.com/watch?v=fx6UXkkDdB8).
