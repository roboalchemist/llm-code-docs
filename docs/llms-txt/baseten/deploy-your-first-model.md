# Source: https://docs.baseten.co/examples/deploy-your-first-model.md

# Deploy your first model

> From model weights to API endpoint

This guide walks through packaging and deploying [Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct), a 3.8B parameter LLM, as a production-ready API endpoint.

We'll cover:

1. **Loading model weights** from Hugging Face
2. **Running inference** on a GPU
3. **Configuring dependencies and infrastructure**
4. **Iterating with live reload development**
5. **Deploying to production with autoscaling**

By the end, you’ll have an AI model running on scalable infrastructure, callable via an API.

## 1. Setup

Before you begin:

1. [Sign up](https://app.baseten.co/signup) or [sign in](https://app.baseten.co/login) to Baseten
2. Generate an [API key](https://app.baseten.co/settings/account/api_keys) and store it securely
3. Install [Truss](https://pypi.org/project/truss/), our model packaging framework

```sh  theme={"system"}
pip install --upgrade truss
```

<Tip>
  New accounts include free credits—this guide should use less than \$1 in GPU
  costs.
</Tip>

***

## 2. Create a Truss

A **Truss** packages your model into a **deployable container** with all dependencies and configurations.

Create a new Truss:

```sh  theme={"system"}
truss init phi-3-mini && cd phi-3-mini
```

When prompted, give your Truss a name like `Phi 3 Mini`.

You should see the following file structure:

```arduino  theme={"system"}
phi-3-mini/
  data/
  model/
    __init__.py
    model.py
  packages/
  config.yaml
```

You'll primarily edit `model/model.py` and `config.yaml`.

***

## 3. Load model weights

[Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) is available on Hugging Face. We’ll **load its weights using** transformers.

Edit `model/model.py`:

```python model/model.py theme={"system"}
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class Model:
    def __init__(self, **kwargs):
        self._model = None
        self._tokenizer = None

    def load(self):
        self._model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct",
            device_map="cuda",
            torch_dtype="auto"
        )
        self._tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct"
        )
```

***

## 4. Implement Model Inference

Define how the model processes incoming requests by implementing the `predict()` function:

```python model/model.py theme={"system"}
class Model:
    ...
    def predict(self, request):
        messages = request.pop("messages")
        model_inputs = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(model_inputs, return_tensors="pt").to("cuda")
        with torch.no_grad():
            outputs = self._model.generate(input_ids=inputs["input_ids"], max_length=256)
        return {"output": self._tokenizer.decode(outputs[0], skip_special_tokens=True)}
```

This function:

* ✅ Accepts a list of messages
* ✅ Uses Hugging Face’s tokenizer
* ✅ Generates a response with max 256 tokens

***

## 5. Configure Dependencies & GPU

In `config.yaml`, define the **Python environment** and **compute resources**:

### Set Dependencies

```yaml config.yaml theme={"system"}
requirements:
  - six==1.17.0
  - accelerate==0.30.1
  - einops==0.8.0
  - transformers==4.41.2
  - torch==2.3.0
```

### Allocate a GPU

Phi-3-mini needs \~7.6GB VRAM. A T4 GPU (16GB VRAM) is a good choice.

```yaml config.yaml theme={"system"}
resources:
  accelerator: T4
  use_gpu: true
```

***

## 6. Deploy the Model

### 1. Get Your API Key

🔗 Generate an API Key

You can generate the API key from the Baseten UI. Click on the User icon at the top-right, then click API keys. Save your API-key, because we will use it in the next step.

### 2. Push Your Model to Baseten

```sh  theme={"system"}
truss push
```

Since this is a first-time deployment, `truss` will ask for your API-key and save it for future runs.

Monitor the deployment from [your Baseten dashboard](https://app.baseten.co/models/).

***

## 7. Call the Model API

After the deployment is complete, we can call the model API. First, store the Baseten API key as an environment variable:

```sh  theme={"system"}
export BASETEN_API_KEY=<your_api_key>
```

Below is the client code. Be sure to replace `model_id` from your deployment.

```python  theme={"system"}
import requests
import os

model_id = "your_model_id"
baseten_api_key = os.environ["BASETEN_API_KEY"]

resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/development/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={"messages": ["What is AGI?"]}
)

print(resp.json())
```

***

## 8. Live Reload for Development

Avoid long deploy times when testing changes—use **live reload**:

```sh  theme={"system"}
truss watch
```

* Saves time by **patching only the updated code**
* Skips rebuilding Docker containers
* Keeps the model server running while iterating

Make changes to `model.py`, save, and test the API again.

## 9. Promote to Production

Once you're happy with the model, deploy it to production:

```sh  theme={"system"}
truss push --publish
```

This updates the **API endpoint** from:

* ❌ **Development**: /development/predict
* ✅ **Production**: /production/predict

```python  theme={"system"}
resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={
        "messages": [
            {"role": "user", "content": "What is AGI?"}
        ],
    }
)
```

***

## Next Steps

🚀 You’ve successfully packaged, deployed, and invoked an AI model with Truss!

Explore more:

* Learning more about [model serving with Truss](/development/model/overview).
* [Example implementations](https://github.com/basetenlabs/truss-examples) for dozens of open source models.
* [Inference examples](/inference/concepts) and [Baseten integrations](/inference/integrations).
* Using [autoscaling settings](/deployment/autoscaling) to spin up and down multiple GPU replicas.
