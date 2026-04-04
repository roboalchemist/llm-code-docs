# Source: https://docs.baseten.co/inference/calling-your-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Call your model

> Run inference on deployed models

Once deployed, your model is accessible through an [API endpoint](/reference/inference-api/overview). To make an inference request, you'll need:

* **Model ID**: Found in the Baseten dashboard or returned when you deploy.
* **[API key](/organization/api-keys)**: Authenticates your requests.
* **JSON-serializable model input**: The data your model expects.

## Authentication

Include your API key in the `Authorization` header:

```sh  theme={"system"}
curl -X POST https://model-YOUR_MODEL_ID.api.baseten.co/environments/production/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello, world!"}'
```

In Python with requests:

```python  theme={"system"}
import requests
import os

api_key = os.environ["BASETEN_API_KEY"]
model_id = "YOUR_MODEL_ID"

response = requests.post(
    f"https://model-{model_id}.api.baseten.co/environments/production/predict",
    headers={"Authorization": f"Api-Key {api_key}"},
    json={"prompt": "Hello, world!"},
)

print(response.json())
```

## Predict API endpoints

Baseten provides multiple endpoints for different inference modes:

* [`/predict`](/reference/inference-api/overview#predict-endpoints) – Standard synchronous inference.
* [`/async_predict`](/reference/inference-api/overview#predict-endpoints) – Asynchronous inference for long-running tasks.

Endpoints are available for environments and all deployments. See the [API reference](/reference/inference-api/overview) for details.

## Sync API endpoints

Custom servers support both `predict` endpoints as well as a special `sync` endpoint. By using the `sync` endpoint you are able to call different routes in your custom server.

```
https://model-{model-id}.api.baseten.co/environments/{production}/sync/{route}
```

Here are a few examples that show how the sync endpoint maps to the custom server's routes.

* `https://model-{model_id}.../sync/health` -> `/health`
* `https://model-{model_id}.../sync/items` -> `/items`
* `https://model-{model_id}.../sync/items/123` -> `/items/123`

## OpenAI SDK

When deploying a model with Engine-Builder, you will get an OpenAI compatible server. If you are already using one of the OpenAI SDKs, you will simply need to update the base url to your Baseten model URL and include your Baseten API Key.

```python  theme={"system"}
import os
from openai import OpenAI

model_id = "abcdef" # TODO: replace with your model id
api_key = os.environ.get("BASETEN_API_KEY")
model_url = f"https://model-{model_id}.api.baseten.co/environments/production/sync/v1"

client = OpenAI(
    base_url=model_url,
    api_key=api_key,
)

stream = client.chat.completions.create(
    model="baseten",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"}
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

## Alternative invocation methods

* **Truss CLI**: [`truss predict`](/reference/cli/truss/predict)
* **Model Dashboard**: "Playground" button in the Baseten UI
