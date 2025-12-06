# Nomic Documentation

Source: https://docs.nomic.ai/platform/embeddings-and-retrieval/generate-embeddings

Nomic Atlas allows anyone to access the power of embeddings.

An embedding is a vector representation of an unstructured datapoint that enables computers to manipulate the data based on semantics and meaning.

Learn more about Nomic Embed Text, Nomic Embed Vision, and the Embedding Inference API.

You can generate text and image embeddings with Nomic Atlas by using the Nomic Embedding API.

For text embeddings,

```
from nomic import embedimport numpy as npoutput = embed.text(    texts=['The text you want to embed.'],    model='nomic-embed-text-v1.5',    task_type='search_document',)embeddings = np.array(output['embeddings'])
```

and vision embeddings,

```
from nomic import embedimport numpy as npoutput = embed.image(    images=["paths to images"],    model='nomic-embed-vision-v1.5',)embeddings = np.array(output['embeddings'])
```

Now, explore your embedding in Atlas.

```
from nomic import AtlasDatasetdataset = AtlasDataset('my-embeddings')dataset.add_data(embeddings=embeddings)atlas_map = dataset.create_index()
```

### Embedding task types​

When using Nomic Text embeddings models you must specify a task_type.
The task_type allows the embedding to specialize for specific use cases and defaults to search_document.

There are four task type options for Nomic Embed

#### Retrieval task types​

- search_query: Use this when you want to encode a query for question-answering over text that was embedded with search_document.
```
search_query
```

- search_document: The default embedding task type. Any document you want to use for retrieval or store in a vector database should use this task type.
```
search_document
```

#### Semantic search​

If you want to do semantic similarity search instead of question answering, you should encode both queries and document with the search_document task type.

#### Classification and clustering tasks​

- classification: Use this if your embeddings are for classification (e.g. training a linear probe for a target classification task)
```
classification
```

- clustering: Use this if your embeddings need very high linear separability (e.g. building a topic model on your embeddings)
```
clustering
```

## Resizable embeddings​

You can resize the output dimensionality of your Nomic embeddings with Nomic Embed v1.5. This model
allows you to specify a dimensionality ranging from 64 to 768 for your embedding size.

Shorter embeddings tradeoff small amounts of performance for space so require less storage, memory and bandwidth to use.

Specify a dimensionality to control the embedding size.

```
dimensionality
```

```
from nomic import embedoutput = embed.text(    texts=['Nomic Embedding API', '#keepAIOpen'],    model='nomic-embed-text-v1.5',    task_type='search_document',    dimensionality=512,)
```

### Local inference​

The Nomic Python client can optionally use GPT4All to generate text embeddings locally. Local embeddings are fully
compatible with embeddings from the Atlas API, and should be the same within a small margin of error.

GPT4All is not included by default, but it can be installed with pip install nomic[local].

```
pip install nomic[local]
```

To enable local mode, use inference_mode='local'. The local model will be downloaded automatically. The first call to
embed.text will be slower due to initialization, but successive calls with the same model and parameters reuse the
Embed4All instance.

```
inference_mode='local'
```

```
embed.text
```

```
Embed4All
```

```
from nomic import embedoutput = embed.text(    texts=['Nomic Embedding API', '#keepAIOpen'],    model='nomic-embed-text-v1.5',    task_type='search_document',    inference_mode='local',)mode = output['inference_mode']  # 'local'
```

### Dynamic local inference​

Local embeddings are free to generate, but generally take longer than remote embeddings, especially on a less capable
machine. Dynamic mode can be enabled with inference_mode='dynamic', which uses the local model to speed up smaller
embedding requests, while automatically using the remote API for larger ones.

```
inference_mode='dynamic'
```

```
from nomic import embedoutput = embed.text(    texts=['Nomic Embedding API', '#keepAIOpen'],    model='nomic-embed-text-v1.5',    task_type='search_document',    inference_mode='dynamic',)mode = output['inference_mode']  # 'local'output = embed.text(    texts=['Nomic Embedding API'] * 50,    model='nomic-embed-text-v1.5',    task_type='search_document',    inference_mode='remote',)mode = output['inference_mode']  # 'remote'
```

### Selecting a device​

The device parameter of embed.text allows you to use a different device for local inference. By default, the CPU is
used on Windows and Linux, while the Metal backend is used on Apple Silicon. You can use the GPU on Windows or Linux
with device='gpu'. See the GPT4All documentation for more information.

```
device
```

```
embed.text
```

```
device='gpu'
```

## Explore your embeddings​

At it's core,  Atlas is an engine for embedding exploration and understanding. This
is crucial for debugging your data, finding anomalies and refining your embedding powered applications.

T 10,000 Wikipedia documents through the latent space of nomic-embed-text-v1.5.

```
from nomic import embed, AtlasDatasetimport numpy as npfrom datasets import load_dataset, Datasetwiki_10k = Dataset.from_generator(    lambda: load_dataset(        'wikimedia/wikipedia',        '20231101.en',        split='train',        streaming=True    ).take(10_000))wiki_10k_embeddings = embed.text(    texts=[row['text'][:1200] for row in wiki_10k],    model='nomic-embed-text-v1.5')['embeddings']wiki_10k_embeddings = np.array(wiki_10k_embeddings)dataset = AtlasDataset('my-embeddings')dataset.add_data(embeddings=wiki_10k_embeddings)atlas_map = dataset.create_index()
```

- Embedding task types
- Resizable embeddingsLocal inferenceDynamic local inferenceSelecting a device
- Local inference
- Dynamic local inference
- Selecting a device
- Explore your embeddings
