# [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#neural-search-101-a-comprehensive-guide-and-step-by-step-tutorial) Neural Search 101: A Comprehensive Guide and Step-by-Step Tutorial

Information retrieval technology is one of the main technologies that enabled the modern Internet to exist.
These days, search technology is the heart of a variety of applications.
From web-pages search to product recommendations.
For many years, this technology didn’t get much change until neural networks came into play.

In this guide we are going to find answers to these questions:

- What is the difference between regular and neural search?
- What neural networks could be used for search?
- In what tasks is neural network search useful?
- How to build and deploy own neural search service step-by-step?

## [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#what-is-neural-search) What is neural search?

A regular full-text search, such as Google’s, consists of searching for keywords inside a document.
For this reason, the algorithm can not take into account the real meaning of the query and documents.
Many documents that might be of interest to the user are not found because they use different wording.

Neural search tries to solve exactly this problem - it attempts to enable searches not by keywords but by meaning.
To achieve this, the search works in 2 steps.
In the first step, a specially trained neural network encoder converts the query and the searched objects into a vector representation called embeddings.
The encoder must be trained so that similar objects, such as texts with the same meaning or alike pictures get a close vector representation.

![Encoders and embedding space](https://gist.githubusercontent.com/generall/c229cc94be8c15095286b0c55a3f19d7/raw/e52e3f1a320cd985ebc96f48955d7f355de8876c/encoders.png)

Having this vector representation, it is easy to understand what the second step should be.
To find documents similar to the query you now just need to find the nearest vectors.
The most convenient way to determine the distance between two vectors is to calculate the cosine distance.
The usual Euclidean distance can also be used, but it is not so efficient due to [the curse of dimensionality](https://en.wikipedia.org/wiki/Curse_of_dimensionality).

## [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#which-model-could-be-used) Which model could be used?

It is ideal to use a model specially trained to determine the closeness of meanings.
For example, models trained on Semantic Textual Similarity (STS) datasets.
Current state-of-the-art models can be found on this [leaderboard](https://paperswithcode.com/sota/semantic-textual-similarity-on-sts-benchmark?p=roberta-a-robustly-optimized-bert-pretraining).

However, not only specially trained models can be used.
If the model is trained on a large enough dataset, its internal features can work as embeddings too.
So, for instance, you can take any pre-trained on ImageNet model and cut off the last layer from it.
In the penultimate layer of the neural network, as a rule, the highest-level features are formed, which, however, do not correspond to specific classes.
The output of this layer can be used as an embedding.

## [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#what-tasks-is-neural-search-good-for) What tasks is neural search good for?

Neural search has the greatest advantage in areas where the query cannot be formulated precisely.
Querying a table in an SQL database is not the best place for neural search.

On the contrary, if the query itself is fuzzy, or it cannot be formulated as a set of conditions - neural search can help you.
If the search query is a picture, sound file or long text, neural network search is almost the only option.

If you want to build a recommendation system, the neural approach can also be useful.
The user’s actions can be encoded in vector space in the same way as a picture or text.
And having those vectors, it is possible to find semantically similar users and determine the next probable user actions.

## [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#step-by-step-neural-search-tutorial-using-qdrant) Step-by-step neural search tutorial using Qdrant

With all that said, let’s make our neural network search.
As an example, I decided to make a search for startups by their description.
In this demo, we will see the cases when text search works better and the cases when neural network search works better.

I will use data from [startups-list.com](https://www.startups-list.com/).
Each record contains the name, a paragraph describing the company, the location and a picture.
Raw parsed data can be found at [this link](https://storage.googleapis.com/generall-shared-data/startups_demo.json).

### [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#step-1-prepare-data-for-neural-search) Step 1: Prepare data for neural search

To be able to search for our descriptions in vector space, we must get vectors first.
We need to encode the descriptions into a vector representation.
As the descriptions are textual data, we can use a pre-trained language model.
As mentioned above, for the task of text search there is a whole set of pre-trained models specifically tuned for semantic similarity.

One of the easiest libraries to work with pre-trained language models, in my opinion, is the [sentence-transformers](https://github.com/UKPLab/sentence-transformers) by UKPLab.
It provides a way to conveniently download and use many pre-trained models, mostly based on transformer architecture.
Transformers is not the only architecture suitable for neural search, but for our task, it is quite enough.

We will use a model called `all-MiniLM-L6-v2`.
This model is an all-round model tuned for many use-cases. Trained on a large and diverse dataset of over 1 billion training pairs.
It is optimized for low memory consumption and fast inference.

The complete code for data preparation with detailed comments can be found and run in [Colab Notebook](https://colab.research.google.com/drive/1kPktoudAP8Tu8n8l-iVMOQhVmHkWV_L9?usp=sharing).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1kPktoudAP8Tu8n8l-iVMOQhVmHkWV_L9?usp=sharing)

### [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#step-2-incorporate-a-vector-search-engine) Step 2: Incorporate a Vector search engine

Now as we have a vector representation for all our records, we need to store them somewhere.
In addition to storing, we may also need to add or delete a vector, save additional information with the vector.
And most importantly, we need a way to search for the nearest vectors.

The vector search engine can take care of all these tasks.
It provides a convenient API for searching and managing vectors.
In our tutorial, we will use [Qdrant vector search engine](https://github.com/qdrant/qdrant) vector search engine.
It not only supports all necessary operations with vectors but also allows you to store additional payload along with vectors and use it to perform filtering of the search result.
Qdrant has a client for Python and also defines the API schema if you need to use it from other languages.

The easiest way to use Qdrant is to run a pre-built image.
So make sure you have Docker installed on your system.

To start Qdrant, use the instructions on its [homepage](https://github.com/qdrant/qdrant).

Download image from [DockerHub](https://hub.docker.com/r/qdrant/qdrant):

```bash
docker pull qdrant/qdrant

```

And run the service inside the docker:

```bash
docker run -p 6333:6333 \
    -v $(pwd)/qdrant_storage:/qdrant/storage \
    qdrant/qdrant

```

You should see output like this

```text
...
[2021-02-05T00:08:51Z INFO  actix_server::builder] Starting 12 workers
[2021-02-05T00:08:51Z INFO  actix_server::builder] Starting "actix-web-service-0.0.0.0:6333" service on 0.0.0.0:6333

```

This means that the service is successfully launched and listening port 6333.
To make sure you can test [http://localhost:6333/](http://localhost:6333/) in your browser and get qdrant version info.

All uploaded to Qdrant data is saved into the `./qdrant_storage` directory and will be persisted even if you recreate the container.

### [Anchor](https://qdrant.tech/articles/neural-search-tutorial/\#step-3-upload-data-to-qdrant) Step 3: Upload data to Qdrant

Now once we have the vectors prepared and the search engine running, we can start uploading the data.
To interact with Qdrant from python, I recommend using an out-of-the-box client library.

To install it, use the following command

```bash
pip install qdrant-client

```

At this point, we should have startup records in file `startups.json`, encoded vectors in file `startup_vectors.npy`, and running Qdrant on a local machine.
Let’s write a script to upload all startup data and vectors into the search engine.

First, let’s create a client object for Qdrant.

```python