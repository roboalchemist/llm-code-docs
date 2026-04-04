# What is a Sparse Vector? How to Achieve Vector-based Hybrid Search

Nirant Kasliwal

·

December 09, 2023

![What is a Sparse Vector? How to Achieve Vector-based Hybrid Search](https://qdrant.tech/articles_data/sparse-vectors/preview/title.jpg)

Think of a library with a vast index card system. Each index card only has a few keywords marked out (sparse vector) of a large possible set for each book (document). This is what sparse vectors enable for text.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#what-are-sparse-and-dense-vectors) What are sparse and dense vectors?

Sparse vectors are like the Marie Kondo of data—keeping only what sparks joy (or relevance, in this case).

Consider a simplified example of 2 documents, each with 200 words. A dense vector would have several hundred non-zero values, whereas a sparse vector could have, much fewer, say only 20 non-zero values.

In this example: We assume it selects only 2 words or tokens from each document. The rest of the values are zero. This is why it’s called a sparse vector.

```python
dense = [0.2, 0.3, 0.5, 0.7, ...]  # several hundred floats
sparse = [{331: 0.5}, {14136: 0.7}]  # 20 key value pairs

```

The numbers 331 and 14136 map to specific tokens in the vocabulary e.g. `['chocolate', 'icecream']`. The rest of the values are zero. This is why it’s called a sparse vector.

The tokens aren’t always words though, sometimes they can be sub-words: `['ch', 'ocolate']` too.

They’re pivotal in information retrieval, especially in ranking and search systems. BM25, a standard ranking function used by search engines like [Elasticsearch](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors), exemplifies this. BM25 calculates the relevance of documents to a given search query.

BM25’s capabilities are well-established, yet it has its limitations.

BM25 relies solely on the frequency of words in a document and does not attempt to comprehend the meaning or the contextual importance of the words. Additionally, it requires the computation of the entire corpus’s statistics in advance, posing a challenge for large datasets.

Sparse vectors harness the power of neural networks to surmount these limitations while retaining the ability to query exact words and phrases.
They excel in handling large text data, making them crucial in modern data processing a and marking an advancement over traditional methods such as BM25.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#understanding-sparse-vectors) Understanding sparse vectors

Sparse Vectors are a representation where each dimension corresponds to a word or subword, greatly aiding in interpreting document rankings. This clarity is why sparse vectors are essential in modern search and recommendation systems, complimenting the meaning-rich embedding or dense vectors.

Dense vectors from models like OpenAI Ada-002 or Sentence Transformers contain non-zero values for every element. In contrast, sparse vectors focus on relative word weights per document, with most values being zero. This results in a more efficient and interpretable system, especially in text-heavy applications like search.

Sparse Vectors shine in domains and scenarios where many rare keywords or specialized terms are present.
For example, in the medical domain, many rare terms are not present in the general vocabulary, so general-purpose dense vectors cannot capture the nuances of the domain.

| Feature | Sparse Vectors | Dense Vectors |
| --- | --- | --- |
| **Data Representation** | Majority of elements are zero | All elements are non-zero |
| **Computational Efficiency** | Generally higher, especially in operations involving zero elements | Lower, as operations are performed on all elements |
| **Information Density** | Less dense, focuses on key features | Highly dense, capturing nuanced relationships |
| **Example Applications** | Text search, Hybrid search | [RAG](https://qdrant.tech/articles/what-is-rag-in-ai/), many general machine learning tasks |

Where do sparse vectors fail though? They’re not great at capturing nuanced relationships between words. For example, they can’t capture the relationship between “king” and “queen” as well as dense vectors.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#splade) SPLADE

Let’s check out [SPLADE](https://europe.naverlabs.com/research/computer-science/splade-a-sparse-bi-encoder-bert-based-model-achieves-effective-and-efficient-full-text-document-ranking/?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors), an excellent way to make sparse vectors. Let’s look at some numbers first. Higher is better:

| Model | MRR@10 (MS MARCO Dev) | Type |
| --- | --- | --- |
| BM25 | 0.184 | Sparse |
| TCT-ColBERT | 0.359 | Dense |
| doc2query-T5 [link](https://github.com/castorini/docTTTTTquery) | 0.277 | Sparse |
| SPLADE | 0.322 | Sparse |
| SPLADE-max | 0.340 | Sparse |
| SPLADE-doc | 0.322 | Sparse |
| DistilSPLADE-max | 0.368 | Sparse |

All numbers are from [SPLADEv2](https://arxiv.org/abs/2109.10086). MRR is [Mean Reciprocal Rank](https://www.wikiwand.com/en/Mean_reciprocal_rank#References), a standard metric for ranking. [MS MARCO](https://microsoft.github.io/MSMARCO-Passage-Ranking/?utm_source=qdrant&utm_medium=website&utm_campaign=sparse-vectors&utm_content=article&utm_term=sparse-vectors) is a dataset for evaluating ranking and retrieval for passages.

SPLADE is quite flexible as a method, with regularization knobs that can be tuned to obtain [different models](https://github.com/naver/splade) as well:

> SPLADE is more a class of models rather than a model per se: depending on the regularization magnitude, we can obtain different models (from very sparse to models doing intense query/doc expansion) with different properties and performance.

First, let’s look at how to create a sparse vector. Then, we’ll look at the concepts behind SPLADE.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#creating-a-sparse-vector) Creating a sparse vector

We’ll explore two different ways to create a sparse vector. The higher performance way to create a sparse vector from dedicated document and query encoders. We’ll look at a simpler approach – here we will use the same model for both document and query. We will get a dictionary of token ids and their corresponding weights for a sample text - representing a document.

If you’d like to follow along, here’s a [Colab Notebook](https://colab.research.google.com/gist/NirantK/ad658be3abefc09b17ce29f45255e14e/splade-single-encoder.ipynb), [alternate link](https://gist.github.com/NirantK/ad658be3abefc09b17ce29f45255e14e) with all the code.

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#setting-up) Setting Up

```python
from transformers import AutoModelForMaskedLM, AutoTokenizer

model_id = "naver/splade-cocondenser-ensembledistil"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForMaskedLM.from_pretrained(model_id)

text = """Arthur Robert Ashe Jr. (July 10, 1943 – February 6, 1993) was an American professional tennis player. He won three Grand Slam titles in singles and two in doubles."""

```

### [Anchor](https://qdrant.tech/articles/sparse-vectors/\#computing-the-sparse-vector) Computing the sparse vector

```python
import torch

def compute_vector(text):
    """
    Computes a vector from logits and attention mask using ReLU, log, and max operations.
    """
    tokens = tokenizer(text, return_tensors="pt")
    output = model(**tokens)
    logits, attention_mask = output.logits, tokens.attention_mask
    relu_log = torch.log(1 + torch.relu(logits))
    weighted_log = relu_log * attention_mask.unsqueeze(-1)
    max_val, _ = torch.max(weighted_log, dim=1)
    vec = max_val.squeeze()

    return vec, tokens

vec, tokens = compute_vector(text)
print(vec.shape)

```

You’ll notice that there are 38 tokens in the text based on this tokenizer. This will be different from the number of tokens in the vector. In a TF-IDF, we’d assign weights only to these tokens or words. In SPLADE, we assign weights to all the tokens in the vocabulary using this vector using our learned model.

## [Anchor](https://qdrant.tech/articles/sparse-vectors/\#term-expansion-and-weights) Term expansion and weights

```python
def extract_and_map_sparse_vector(vector, tokenizer):
    """
    Extracts non-zero elements from a given vector and maps these elements to their human-readable tokens using a tokenizer. The function creates and returns a sorted dictionary where keys are the tokens corresponding to non-zero elements in the vector, and values are the weights of these elements, sorted in descending order of weights.

    This function is useful in NLP tasks where you need to understand the significance of different tokens based on a model's output vector. It first identifies non-zero values in the vector, maps them to tokens, and sorts them by weight for better interpretability.

    Args:
    vector (torch.Tensor): A PyTorch tensor from which to extract non-zero elements.
    tokenizer: The tokenizer used for tokenization in the model, providing the mapping from tokens to indices.

    Returns:
    dict: A sorted dictionary mapping human-readable tokens to their corresponding non-zero weights.
    """

    # Extract indices and values of non-zero elements in the vector
    cols = vector.nonzero().squeeze().cpu().tolist()
    weights = vector[cols].cpu().tolist()

    # Map indices to tokens and create a dictionary
    idx2token = {idx: token for token, idx in tokenizer.get_vocab().items()}
    token_weight_dict = {
        idx2token[idx]: round(weight, 2) for idx, weight in zip(cols, weights)
    }

    # Sort the dictionary by weights in descending order
    sorted_token_weight_dict = {
        k: v
        for k, v in sorted(
            token_weight_dict.items(), key=lambda item: item[1], reverse=True
        )
    }

    return sorted_token_weight_dict