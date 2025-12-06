# Nomic Documentation

Source: https://docs.nomic.ai/reference/python-api/generate-embeddings

The embed module in the Nomic Python SDK provides embedding functionality using the Nomic Embedding API.

```
embed
```

See the embeddings user guide for more information on usage & capabilities.

## Text Embeddings​

embed.text generates embeddings for a list of texts.

```
embed.text
```

```
from nomic import embedoutput = embed.text(    texts=['Nomic Embedding API', '#keepAIOpen'],    model='nomic-embed-text-v1.5',    task_type='search_document',)print(output)
```

Output:

```
{'embeddings': [    [0.008766174, 0.014785767, -0.13134766, ...],    [0.017822266, 0.018585205, -0.12683105, ...]], 'inference_mode': 'remote', 'model': 'nomic-embed-text-v1.5', 'usage': {'prompt_tokens': 10, 'total_tokens': 10}}
```

### embed.text API Reference​

```
def text(texts: list[str],         *,         model: str = "nomic-embed-text-v1.5",         task_type: str = "search_document",         dimensionality: int | None = None,         long_text_mode: str = "truncate",         inference_mode: str = "remote",         device: str | None = None,         **kwargs: Any) -> dict[str, Any]
```

Generates embeddings for the given text.

Arguments:

- texts - The text to embed.
```
texts
```

- model - The model to use when embedding.
```
model
```

- task_type - The task type to use when embedding. One of search_query, search_document, classification, clustering.
```
task_type
```

```
search_query
```

```
search_document
```

```
classification
```

```
clustering
```

- dimensionality - The embedding dimension, for use with Matryoshka-capable models. Defaults to full-size.
```
dimensionality
```

- long_text_mode - How to handle texts longer than the model can accept. One of mean or truncate.
```
long_text_mode
```

```
mean
```

```
truncate
```

- inference_mode - How to generate embeddings. One of remote, local (Embed4All), or dynamic (automatic).
Defaults to remote.
```
inference_mode
```

```
remote
```

```
local
```

```
dynamic
```

```
remote
```

- device - The device to use for local embeddings. Defaults to CPU, or Metal on Apple Silicon. It can be set to:

"gpu": Use the best available GPU.
"amd", "nvidia": Use the best available GPU from the specified vendor.
A specific device name from the output of GPT4All.list_gpus()
```
device
```

- "gpu": Use the best available GPU.
- "amd", "nvidia": Use the best available GPU from the specified vendor.
- A specific device name from the output of GPT4All.list_gpus()
```
GPT4All.list_gpus()
```

- kwargs - Remaining arguments are passed to the Embed4All contructor.
```
kwargs
```

Returns:

A dict containing your embeddings and request metadata

## Image Embeddings​

embed.image generates embeddings for a list of images.

```
embed.image
```

```
from nomic import embedoutput = embed.image(    images=['/path/to/image1.jpg', '/path/to/image2.jpg'],    model='nomic-embed-vision-v1.5',)print(output)
```

Output:

```
{'embeddings': [    [0.008766174, 0.014785767, -0.13134766, ...],    [0.017822266, 0.018585205, -0.12683105, ...]], 'model': 'nomic-embed-vision-v1.5', 'usage': {'prompt_tokens': 10, 'total_tokens': 10}}
```

### embed.text API Reference​

```
def image(images: Sequence[Union[str, PIL.Image.Image]],          model: str = "nomic-embed-vision-v1.5")
```

Generates embeddings for the given images.

Arguments:

- images - the images to embed. Can be file paths to images, image-file bytes or Pillow objects
```
images
```

- model - the model to use when embedding
```
model
```

Returns:

An object containing your embeddings and request metadata

## Additional methods​

### free_embedding_model API Reference​

```
def free_embedding_model() -> None
```

Free the current Embed4All instance and its associated system resources.

- Text Embeddings
- Image Embeddings
- Additional methods
