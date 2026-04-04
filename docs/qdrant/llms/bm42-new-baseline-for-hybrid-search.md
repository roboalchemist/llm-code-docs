# BM42: New Baseline for Hybrid Search

Andrey Vasnetsov

·

July 01, 2024

![BM42: New Baseline for Hybrid Search](https://qdrant.tech/articles_data/bm42/preview/title.jpg)

For the last 40 years, BM25 has served as the standard for search engines.
It is a simple yet powerful algorithm that has been used by many search engines, including Google, Bing, and Yahoo.

Though it seemed that the advent of vector search would diminish its influence, it did so only partially.
The current state-of-the-art approach to retrieval nowadays tries to incorporate BM25 along with embeddings into a hybrid search system.

However, the use case of text retrieval has significantly shifted since the introduction of RAG.
Many assumptions upon which BM25 was built are no longer valid.

For example, the typical length of documents and queries vary significantly between traditional web search and modern RAG systems.

In this article, we will recap what made BM25 relevant for so long and why alternatives have struggled to replace it. Finally, we will discuss BM42, as the next step in the evolution of lexical search.

## [Anchor](https://qdrant.tech/articles/bm42/\#why-has-bm25-stayed-relevant-for-so-long) Why has BM25 stayed relevant for so long?

To understand why, we need to analyze its components.

The famous BM25 formula is defined as:

score(D,Q)=∑i=1NIDF(qi)×f(qi,D)⋅(k1+1)f(qi,D)+k1⋅(1−b+b⋅\|D\|avgdl)

Let’s simplify this to gain a better understanding.

- The score(D,Q) \- means that we compute the score for each pair of document D and query Q.

- The ∑i=1N \- means that each of N terms in the query contribute to the final score as a part of the sum.

- The IDF(qi) \- is the inverse document frequency. The more rare the term qi is, the more it contributes to the score. A simplified formula for this is:


IDF(qi)=Number of documentsNumber of documents with qi

It is fair to say that the `IDF` is the most important part of the BM25 formula.
`IDF` selects the most important terms in the query relative to the specific document collection.
So intuitively, we can interpret the `IDF` as **term importance within the corpora**.

That explains why BM25 is so good at handling queries, which dense embeddings consider out-of-domain.

The last component of the formula can be intuitively interpreted as **term importance within the document**.
This might look a bit complicated, so let’s break it down.

Term importance in document (qi)=f(qi,D)⋅(k1+1)f(qi,D)+k1⋅(1−b+b⋅\|D\|avgdl)

- The f(qi,D) \- is the frequency of the term qi in the document D. Or in other words, the number of times the term qi appears in the document D.
- The k1 and b are the hyperparameters of the BM25 formula. In most implementations, they are constants set to k1=1.5 and b=0.75. Those constants define relative implications of the term frequency and the document length in the formula.
- The \|D\|avgdl \- is the relative length of the document D compared to the average document length in the corpora. The intuition befind this part is following: if the token is found in the smaller document, it is more likely that this token is important for this document.

#### [Anchor](https://qdrant.tech/articles/bm42/\#will-bm25-term-importance-in-the-document-work-for-rag) Will BM25 term importance in the document work for RAG?

As we can see, the _term importance in the document_ heavily depends on the statistics within the document. Moreover, statistics works well if the document is long enough.
Therefore, it is suitable for searching webpages, books, articles, etc.

However, would it work as well for modern search applications, such as RAG? Let’s see.

The typical length of a document in RAG is much shorter than that of web search. In fact, even if we are working with webpages and articles, we would prefer to split them into chunks so that
a) Dense models can handle them and
b) We can pinpoint the exact part of the document which is relevant to the query

As a result, the document size in RAG is small and fixed.

That effectively renders the term importance in the document part of the BM25 formula useless.
The term frequency in the document is always 0 or 1, and the relative length of the document is always 1.

So, the only part of the BM25 formula that is still relevant for RAG is `IDF`. Let’s see how we can leverage it.

## [Anchor](https://qdrant.tech/articles/bm42/\#why-splade-is-not-always-the-answer) Why SPLADE is not always the answer

Before discussing our new approach, let’s examine the current state-of-the-art alternative to BM25 - SPLADE.

The idea behind SPLADE is interesting—what if we let a smart, end-to-end trained model generate a bag-of-words representation of the text for us?
It will assign all the weights to the tokens, so we won’t need to bother with statistics and hyperparameters.
The documents are then represented as a sparse embedding, where each token is represented as an element of the sparse vector.

And it works in academic benchmarks. Many papers report that SPLADE outperforms BM25 in terms of retrieval quality.
This performance, however, comes at a cost.

- **Inappropriate Tokenizer**: To incorporate transformers for this task, SPLADE models require using a standard transformer tokenizer. These tokenizers are not designed for retrieval tasks. For example, if the word is not in the (quite limited) vocabulary, it will be either split into subwords or replaced with a `[UNK]` token. This behavior works well for language modeling but is completely destructive for retrieval tasks.

- **Expensive Token Expansion**: In order to compensate the tokenization issues, SPLADE uses _token expansion_ technique. This means that we generate a set of similar tokens for each token in the query. There are a few problems with this approach:

  - It is computationally and memory expensive. We need to generate more values for each token in the document, which increases both the storage size and retrieval time.
  - It is not always clear where to stop with the token expansion. The more tokens we generate, the more likely we are to get the relevant one. But simultaneously, the more tokens we generate, the more likely we are to get irrelevant results.
  - Token expansion dilutes the interpretability of the search. We can’t say which tokens were used in the document and which were generated by the token expansion.
- **Domain and Language Dependency**: SPLADE models are trained on specific corpora. This means that they are not always generalizable to new or rare domains. As they don’t use any statistics from the corpora, they cannot adapt to the new domain without fine-tuning.

- **Inference Time**: Additionally, currently available SPLADE models are quite big and slow. They usually require a GPU to make the inference in a reasonable time.


At Qdrant, we acknowledge the aforementioned problems and are looking for a solution.
Our idea was to combine the best of both worlds - the simplicity and interpretability of BM25 and the intelligence of transformers while avoiding the pitfalls of SPLADE.

And here is what we came up with.

## [Anchor](https://qdrant.tech/articles/bm42/\#the-best-of-both-worlds) The best of both worlds

As previously mentioned, `IDF` is the most important part of the BM25 formula. In fact it is so important, that we decided to build its calculation into the Qdrant engine itself.
Check out our latest [release notes](https://github.com/qdrant/qdrant/releases/tag/v1.10.0). This type of separation allows streaming updates of the sparse embeddings while keeping the `IDF` calculation up-to-date.

As for the second part of the formula, _the term importance within the document_ needs to be rethought.

Since we can’t rely on the statistics within the document, we can try to use the semantics of the document instead.
And semantics is what transformers are good at. Therefore, we only need to solve two problems:

- How does one extract the importance information from the transformer?
- How can tokenization issues be avoided?

### [Anchor](https://qdrant.tech/articles/bm42/\#attention-is-all-you-need) Attention is all you need

Transformer models, even those used to generate embeddings, generate a bunch of different outputs.
Some of those outputs are used to generate embeddings.

Others are used to solve other kinds of tasks, such as classification, text generation, etc.

The one particularly interesting output for us is the attention matrix.

![Attention matrix](https://qdrant.tech/articles_data/bm42/attention-matrix.png)

Attention matrix

The attention matrix is a square matrix, where each row and column corresponds to the token in the input sequence.
It represents the importance of each token in the input sequence for each other.

The classical transformer models are trained to predict masked tokens in the context, so the attention weights define which context tokens influence the masked token most.

Apart from regular text tokens, the transformer model also has a special token called `[CLS]`. This token represents the whole sequence in the classification tasks, which is exactly what we need.

By looking at the attention row for the `[CLS]` token, we can get the importance of each token in the document for the whole document.

```python
sentences = "Hello, World - is the starting point in most programming languages"

features = transformer.tokenize(sentences)