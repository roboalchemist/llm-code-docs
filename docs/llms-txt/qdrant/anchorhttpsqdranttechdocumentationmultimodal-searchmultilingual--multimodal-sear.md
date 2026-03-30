# [Anchor](https://qdrant.tech/documentation/multimodal-search/\#multilingual--multimodal-search-with-llamaindex) Multilingual & Multimodal Search with LlamaIndex

![Snow prints](https://qdrant.tech/documentation/examples/multimodal-search/image-1.png)

| Time: 15 min | Level: Beginner | Output: [GitHub](https://github.com/qdrant/examples/blob/master/multimodal-search/Multimodal_Search_with_LlamaIndex.ipynb) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://githubtocolab.com/qdrant/examples/blob/master/multimodal-search/Multimodal_Search_with_LlamaIndex.ipynb) |
| --- | --- | --- | --- |

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#overview) Overview

We often understand and share information more effectively when combining different types of data. For example, the taste of comfort food can trigger childhood memories. We might describe a song with just “pam pam clap” sounds. Instead of writing paragraphs. Sometimes, we may use emojis and stickers to express how we feel or to share complex ideas.

Modalities of data such as **text**, **images**, **video** and **audio** in various combinations form valuable use cases for Semantic Search applications.

Vector databases, being **modality-agnostic**, are perfect for building these applications.

In this simple tutorial, we are working with two simple modalities: **image** and **text** data. However, you can create a Semantic Search application with any combination of modalities if you choose the right embedding model to bridge the **semantic gap**.

> The **semantic gap** refers to the difference between low-level features (aka brightness) and high-level concepts (aka cuteness).

For example, the [vdr-2b-multi-v1 model](https://huggingface.co/llamaindex/vdr-2b-multi-v1) from LlamaIndex is designed for multilingual embedding, particularly effective for visual document retrieval across multiple languages and domains. It allows for searching and querying visually rich multilingual documents without the need for OCR or other data extraction pipelines.

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#setup) Setup

First, install the required libraries `qdrant-client` and `llama-index-embeddings-huggingface`.

```bash
pip install qdrant-client llama-index-embeddings-huggingface

```

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#dataset) Dataset

To make the demonstration simple, we created a tiny dataset of images and their captions for you.

Images can be downloaded from [here](https://github.com/qdrant/examples/tree/master/multimodal-search/images). It’s **important** to place them in the same folder as your code/notebook, in the folder named `images`.

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#vectorize-data) Vectorize data

`LlamaIndex`’s `vdr-2b-multi-v1` model supports cross-lingual retrieval, allowing for effective searches across languages and domains. It encodes document page screenshots into dense single-vector representations, eliminating the need for OCR and other complex data extraction processes.

Let’s embed the images and their captions in the **shared embedding space**.

```python
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

model = HuggingFaceEmbedding(
    model_name="llamaindex/vdr-2b-multi-v1",
    device="cpu",  # "mps" for mac, "cuda" for nvidia GPUs
    trust_remote_code=True,
)

documents = [\
    {"caption": "An image about plane emergency safety.", "image": "images/image-1.png"},\
    {"caption": "An image about airplane components.", "image": "images/image-2.png"},\
    {"caption": "An image about COVID safety restrictions.", "image": "images/image-3.png"},\
    {"caption": "An confidential image about UFO sightings.", "image": "images/image-4.png"},\
    {"caption": "An image about unusual footprints on Aralar 2011.", "image": "images/image-5.png"},\
]

text_embeddings = model.get_text_embedding_batch([doc["caption"] for doc in documents])
image_embeddings = model.get_image_embedding_batch([doc["image"] for doc in documents])

```

## [Anchor](https://qdrant.tech/documentation/multimodal-search/\#upload-data-to-qdrant) Upload data to Qdrant

1. **Create a client object for Qdrant**.

```python
from qdrant_client import QdrantClient, models