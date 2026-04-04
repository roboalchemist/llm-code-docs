# [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#how-to-generate-sparse-vectors-with-splade) How to Generate Sparse Vectors with SPLADE

SPLADE is a novel method for learning sparse text representation vectors, outperforming BM25 in tasks like information retrieval and document classification. Its main advantage is generating efficient and interpretable sparse vectors, making it effective for large-scale text data.

## [Anchor](https://qdrant.tech/documentation/fastembed/fastembed-splade/\#setup) Setup

First, install FastEmbed.

```python
pip install -q fastembed

```

Next, import the required modules for sparse embeddings and Python’s typing module.

```python
from fastembed import SparseTextEmbedding, SparseEmbedding

```

You may always check the list of all supported sparse embedding models.

```python
SparseTextEmbedding.list_supported_models()

```

This will return a list of models, each with its details such as model name, vocabulary size, description, and sources.

```python
[\
    {\
        'model': 'prithivida/Splade_PP_en_v1',\
        'sources': {'hf': 'Qdrant/Splade_PP_en_v1', ...},\
        'model_file': 'model.onnx',\
        'description': 'Independent Implementation of SPLADE++ Model for English.',\
        'license': 'apache-2.0',\
        'size_in_GB': 0.532,\
        'vocab_size': 30522,\
        ...\
    },\
    ...\
]  # part of the output was omitted

```

Now, load the model.

```python
model_name = "prithivida/Splade_PP_en_v1"