# [Anchor](https://qdrant.tech/documentation/beginner-tutorials/neural-search/\#build-a-neural-search-service-with-sentence-transformers-and-qdrant) Build a Neural Search Service with Sentence Transformers and Qdrant

| Time: 30 min | Level: Beginner | Output: [GitHub](https://github.com/qdrant/qdrant_demo/tree/sentense-transformers) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kPktoudAP8Tu8n8l-iVMOQhVmHkWV_L9?usp=sharing) |
| --- | --- | --- | --- |

This tutorial shows you how to build and deploy your own neural search service to look through descriptions of companies from [startups-list.com](https://www.startups-list.com/) and pick the most similar ones to your query. The website contains the company names, descriptions, locations, and a picture for each entry.

A neural search service uses artificial neural networks to improve the accuracy and relevance of search results. Besides offering simple keyword results, this system can retrieve results by meaning. It can understand and interpret complex search queries and provide more contextually relevant output, effectively enhancing the user’s search experience.

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/neural-search/\#workflow) Workflow

To create a neural search service, you will need to transform your raw data and then create a search function to manipulate it. First, you will 1) download and prepare a sample dataset using a modified version of the BERT ML model. Then, you will 2) load the data into Qdrant, 3) create a neural search API and 4) serve it using FastAPI.

![Neural Search Workflow](https://qdrant.tech/docs/workflow-neural-search.png)

> **Note**: The code for this tutorial can be found here: \| [Step 1: Data Preparation Process](https://colab.research.google.com/drive/1kPktoudAP8Tu8n8l-iVMOQhVmHkWV_L9?usp=sharing) \| [Step 2: Full Code for Neural Search](https://github.com/qdrant/qdrant_demo/tree/sentense-transformers). \|

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/neural-search/\#prerequisites) Prerequisites

To complete this tutorial, you will need:

- Docker - The easiest way to use Qdrant is to run a pre-built Docker image.
- [Raw parsed data](https://storage.googleapis.com/generall-shared-data/startups_demo.json) from startups-list.com.
- Python version >=3.8

## [Anchor](https://qdrant.tech/documentation/beginner-tutorials/neural-search/\#prepare-sample-dataset) Prepare sample dataset

To conduct a neural search on startup descriptions, you must first encode the description data into vectors. To process text, you can use a pre-trained models like [BERT](https://en.wikipedia.org/wiki/BERT_%28language_model%29) or sentence transformers. The [sentence-transformers](https://github.com/UKPLab/sentence-transformers) library lets you conveniently download and use many pre-trained models, such as DistilBERT, MPNet, etc.

1. First you need to download the dataset.

```bash
wget https://storage.googleapis.com/generall-shared-data/startups_demo.json

```

2. Install the SentenceTransformer library as well as other relevant packages.

```bash
pip install sentence-transformers numpy pandas tqdm

```

3. Import the required modules.

```python
from sentence_transformers import SentenceTransformer
import numpy as np
import json
import pandas as pd
from tqdm.notebook import tqdm

```

You will be using a pre-trained model called `all-MiniLM-L6-v2`.
This is a performance-optimized sentence embedding model and you can read more about it and other available models [here](https://www.sbert.net/docs/pretrained_models.html).

4. Download and create a pre-trained sentence encoder.

```python
model = SentenceTransformer(
    "all-MiniLM-L6-v2", device="cuda"
)  # or device="cpu" if you don't have a GPU

```

5. Read the raw data file.

```python
df = pd.read_json("./startups_demo.json", lines=True)

```

6. Encode all startup descriptions to create an embedding vector for each. Internally, the `encode` function will split the input into batches, which will significantly speed up the process.

```python
vectors = model.encode(
    [row.alt + ". " + row.description for row in df.itertuples()],
    show_progress_bar=True,
)

```

All of the descriptions are now converted into vectors. There are 40474 vectors of 384 dimensions. The output layer of the model has this dimension

```python
vectors.shape