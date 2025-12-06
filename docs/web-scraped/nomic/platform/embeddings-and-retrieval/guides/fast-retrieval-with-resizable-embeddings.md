# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/guides/fast-retrieval-with-resizable-embeddings

In this cookbook, we show how to perform retrieval using nomic-embed-text-v1.5, Nomic's open-source text encoder with a resizable output dimension. You can also view this cookbook on our github, and view more information for nomic-embed-text-v1.5 on HuggingFace.

```
nomic-embed-text-v1.5
```

```
nomic-embed-text-v1.5
```

With its resizable output dimension (minimum ~64 and maximum 768), nomic-embed-text-v1.5 gives users control and flexibility over the speed of using embedding vectors.

```
nomic-embed-text-v1.5
```

## Getting Started​

Make sure you have the necessary libraries installed:

```
pip install datasets nomic numpy
```

## Embedding Wikipedia Documents​

First, let's embed some text documents:

```
from datasets import load_dataset, Datasetimport nomic.embed as embedwiki100k = Dataset.from_generator(lambda: load_dataset('wikimedia/wikipedia', '20231101.en', split='train', streaming=True).take(100_000))wiki100k_embeddings = embed.text([row['text'][:1200] for row in wiki100k], model='nomic-embed-text-v1.5')['embeddings']import numpy as npwiki100k_embeddings = np.array(wiki100k_embeddings)wiki100k_embeddings.shape
```

```
(100000, 768)
```

And embed a query:

```
def embed_query(query: str):    query = np.array(        embed.text(            [query],            model="nomic-embed-text-v1.5",            task_type="search_query",        )["embeddings"]    )[0]    return querytest_query = embed_query("tree data structures")test_query.shape
```

```
(768,)
```

And search over our documents by comparing our query embedding with every other embedding:

```
def knn_scan(query, k=10): return np.argsort(query @ wiki100k_embeddings.T)[-k:]full_top10 = knn_scan(test_query)[doc[:100] for doc in wiki100k[full_top10]['text']]
```

```
['Gene structure is the organisation of specialised sequence elements within a gene. Genes contain mos', 'In computer science, an AVL tree (named after inventors Adelson-Velsky and Landis) is a self-balanci', 'In computer science, a binary search tree (BST), also called an ordered or sorted binary tree, is a ', 'An adaptive k-d tree is a tree for multidimensional points where successive levels may be split alon', 'In computer science, an (a,b) tree is a kind of balanced search tree.\n\nAn (a,b)-tree has all of its ', 'In computer science, a binary tree is a tree data structure in which each node has at most two child', 'XML documents have a hierarchical structure and can conceptually be interpreted as a tree structure,', 'In computer science, a B-tree is a self-balancing tree data structure that maintains sorted data and', 'TreeFam (Tree families database) is a database of phylogenetic trees of animal genes. It aims at dev', 'Tree Description Language (TreeDL) is a computer language for description of strictly-typed tree dat']
```

How long does it take to compare a query embedding with 100,000 768-dimensional embeddings?

```
import timeitdef timed(f, n=100):    ntime = timeit.timeit(f, number=n)    print(f'{ntime/n}s per run / {n/ntime} runs/sec')timed(lambda: knn_scan(test_query))
```

```
0.0454774563999672s per run / 21.988916688856886 runs/sec
```

Now let's try smaller embeddings:

```
def truncated_scanner(embeddings, d):    truncated_embeddings = embeddings[:,:d]    truncated_embeddings /= np.linalg.norm(truncated_embeddings, axis=1)[np.newaxis].T    print(truncated_embeddings.shape)    def trunc_knn(query, k=10):        trunc_query = query[:d]        trunc_query /= np.linalg.norm(trunc_query)        return np.argsort(trunc_query @ truncated_embeddings.T)[-k:]    return trunc_knnknn_512d = truncated_scanner(wiki100k_embeddings, 512)
```

```
(100000, 512)
```

```
top10_512d = knn_512d(test_query)len(set(top10_512d) & set(full_top10))
```

```
9
```

```
timed(lambda: knn_512d(test_query))
```

```
0.032940823050012114s per run / 30.357468557532968 runs/sec
```

That's a bit faster and gets almost all of the same answers for our query! What if we go smaller?

```
knn_256d = truncated_scanner(wiki100k_embeddings, 256)top10_256d = knn_256d(test_query)len(set(top10_256d) & set(full_top10))
```

```
(100000, 256)
```

```
7
```

```
timed(lambda: knn_256d(test_query))
```

```
0.02735897060003481s per run / 36.55108281006478 runs/sec
```

Even faster, but losing more accuracy now - we can recover most of this lost accuracy and keep most of the speedup by collecting extra smaller dimension results and reranking against the full size embeddings:

```
def reranking_scanner(embeddings, d):    truncated_embeddings = embeddings[:,:d]    truncated_embeddings /= np.linalg.norm(truncated_embeddings, axis=1)[np.newaxis].T    def rerank_knn(query, k=10, expand=10):        expanded_k = k * expand        trunc_query = query[:d]        trunc_query /= np.linalg.norm(trunc_query)        candidate_indices = np.argsort(trunc_query @ truncated_embeddings.T)[-expanded_k:]        full_d_candidates = embeddings[candidate_indices]        return candidate_indices[np.argsort(query @ full_d_candidates.T)][-k:]    return rerank_knnrr_256d = reranking_scanner(wiki100k_embeddings, 256)
```

```
top10_rr256d = rr_256d(test_query)len(set(top10_rr256d) & set(full_top10))
```

```
10
```

```
timed(lambda: rr_256d(test_query))
```

```
0.03115591519002919s per run / 32.096633782082876 runs/sec
```

Just as fast, but we've gotten all our accuracy back!

- Getting Started
- Embedding Wikipedia Documents
