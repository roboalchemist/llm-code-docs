# Source: https://docs.aurelio.ai/semantic-router/client-reference/encoders/google.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.aurelio.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# semantic_router.encoders.google

## GoogleEncoder Objects

```python  theme={null}
class GoogleEncoder(DenseEncoder)
```

GoogleEncoder class for generating embeddings using Google's AI Platform.

The GoogleEncoder class is a subclass of DenseEncoder and utilizes the TextEmbeddingModel from the
Google AI Platform to generate embeddings for given documents. It requires a Google Cloud project ID
and supports customization of the pre-trained model, score threshold, location, and API endpoint.

Example usage:

```python  theme={null}
from semantic_router.encoders.google_encoder import GoogleEncoder

encoder = GoogleEncoder(project_id="your-project-id")
embeddings = encoder(["document1", "document2"])
```

**Attributes**:

* `client` - An instance of the TextEmbeddingModel client.
* `type` - The type of the encoder, which is "google".

#### \_\_init\_\_

```python  theme={null}
def __init__(name: Optional[str] = None,
             score_threshold: float = 0.75,
             project_id: Optional[str] = None,
             location: Optional[str] = None,
             api_endpoint: Optional[str] = None)
```

Initializes the GoogleEncoder.

**Arguments**:

* `model_name` (`str`): The name of the pre-trained model to use for embedding.
  If not provided, the default model specified in EncoderDefault will
  be used.
* `score_threshold` (`float`): The threshold for similarity scores.
* `project_id` (`str`): The Google Cloud project ID.
  If not provided, it will be retrieved from the GOOGLE\_PROJECT\_ID
  environment variable.
* `location` (`str`): The location of the AI Platform resources.
  If not provided, it will be retrieved from the GOOGLE\_LOCATION
  environment variable, defaulting to "us-central1".
* `api_endpoint` (`str`): The API endpoint for the AI Platform.
  If not provided, it will be retrieved from the GOOGLE\_API\_ENDPOINT
  environment variable.

**Raises**:

* `str`0: If the Google Project ID is not provided or if the AI Platform
  client fails to initialize.

#### \_\_call\_\_

```python  theme={null}
def __call__(docs: List[str]) -> List[List[float]]
```

Generates embeddings for the given documents.

**Arguments**:

* `docs` (`List[str]`): A list of strings representing the documents to embed.

**Raises**:

* `ValueError`: If the Google AI Platform client is not initialized or if the
  API call fails.

**Returns**:

`List[List[float]]`: A list of lists, where each inner list contains the embedding values for a
document.


Built with [Mintlify](https://mintlify.com).