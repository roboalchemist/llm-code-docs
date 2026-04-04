# Source: https://docs.baseten.co/examples/deploy-your-first-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy your first model

> Learn how to package and deploy an AI model as a production-ready API endpoint on Baseten.

Deploying a model to Baseten turns your model code into a production-ready API endpoint. You package your model with [Truss](https://pypi.org/project/truss/), push it to Baseten, and receive a URL you can call from any application.

This guide walks through deploying [Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct), a 3.8B parameter LLM, from local code to a production API. You'll create a Truss project, write model code, configure dependencies and GPU resources, deploy to Baseten, and call your model's API endpoint.

## Set up your environment

Before you begin, [sign up](https://app.baseten.co/signup) or [sign in](https://app.baseten.co/login) to Baseten.

### Install Truss

[Truss](https://pypi.org/project/truss/) is Baseten's model packaging framework. It handles containerization, dependencies, and deployment configuration.

<Note>
  Using a virtual environment is recommended to avoid dependency conflicts with other Python projects.
</Note>

<Tabs>
  <Tab title="uv (recommended)">
    [uv](https://docs.astral.sh/uv/) is a fast Python package manager. These commands create a virtual environment, activate it, and install Truss:

    ```sh  theme={"system"}
    uv venv && source .venv/bin/activate
    uv pip install truss
    ```
  </Tab>

  <Tab title="pip (macOS/Linux)">
    These commands create a virtual environment, activate it, and install Truss:

    ```sh  theme={"system"}
    python -m venv .venv && source .venv/bin/activate
    pip install --upgrade truss
    ```
  </Tab>

  <Tab title="pip (Windows)">
    These commands create a virtual environment, activate it, and install Truss:

    ```sh  theme={"system"}
    python -m venv .venv && .venv\Scripts\activate
    pip install --upgrade truss
    ```
  </Tab>
</Tabs>

<Tip>
  New accounts include free credits; this guide should use less than \$1 in GPU
  costs.
</Tip>

***

## Create a Truss

A **Truss** packages your model into a deployable container with all dependencies and configurations.

Create a new Truss:

```sh  theme={"system"}
truss init phi-3-mini && cd phi-3-mini
```

When prompted, give your Truss a name like `Phi 3 Mini`.

This command scaffolds a project with the following structure:

```
phi-3-mini/
  model/
    __init__.py
    model.py
  config.yaml
  data/
  packages/
```

The key files are:

* `model/model.py`: Your model code with `load()` and `predict()` methods.
* `config.yaml`: Dependencies, resources, and deployment settings.
* `data/`: Optional directory for data files bundled with your model.
* `packages/`: Optional directory for local Python packages.

Truss uses this structure to build and deploy your model automatically. You
define your model in `model.py` and your infrastructure in `config.yaml`, no
Dockerfiles or container management required.

***

## Implement model code

In this example, you'll implement the model code for
[Phi-3-mini-4k-instruct](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct).
You'll use the `transformers` library to load the model and tokenizer and PyTorch to run inference.
Replace the contents of `model/model.py` with the following code:

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

Truss models follow a three-method pattern that separates initialization from inference:

| Method     | When it's called                     | What to do here                                           |
| ---------- | ------------------------------------ | --------------------------------------------------------- |
| `__init__` | Once when the class is created       | Initialize variables, store configuration, set secrets    |
| `load`     | Once at startup, before any requests | Load model weights, tokenizers, and other heavy resources |
| `predict`  | On every API request                 | Process input, run inference, return response             |

**Why separate `load` from `__init__`?**

The `load` method runs during the container's cold start, before your model
receives traffic. This keeps expensive operations (like downloading
large model weights) out of the request path.

### Understand the request/response flow

The `predict` method receives `request`, a dictionary containing the JSON body
from the API call:

```python  theme={"system"}
# API call with: {"messages": [{"role": "user", "content": "Hello"}]}
def predict(self, request):
    messages = request.pop("messages")  # Extract from request
    # ... run inference ...
    return {"output": result}  # Return dict becomes JSON response
```

Whatever dictionary you return becomes the API response. You control the input
parameters and output format.

### GPU and memory patterns

A few patterns in this code are common across GPU models:

* **`device_map="cuda"`**: Loads model weights directly to GPU.
* **`.to("cuda")`**: Moves input tensors to GPU for inference.
* **`torch.no_grad()`**: Disables gradient tracking to save memory (gradients aren't needed for inference).

***

## Configure dependencies and GPU

The `config.yaml` file defines your model's environment and compute resources.
This configuration determines how your container is built and what hardware it
runs on.

### Set Python version and dependencies

```yaml config.yaml theme={"system"}
python_version: py311
requirements:
  - six==1.17.0
  - accelerate==0.30.1
  - einops==0.8.0
  - transformers==4.41.2
  - torch==2.3.0
```

**Key configuration options:**

| Field             | Purpose                                  | Example                           |
| ----------------- | ---------------------------------------- | --------------------------------- |
| `python_version`  | Python version for your container        | `py39`, `py310`, `py311`, `py312` |
| `requirements`    | Python packages to install (pip format)  | `torch==2.3.0`                    |
| `system_packages` | System-level dependencies (apt packages) | `ffmpeg`, `libsm6`                |

For the complete list of configuration options, see the [Truss reference config](/reference/truss-configuration).

<Note>
  Always pin exact versions (e.g., `torch==2.3.0` not `torch>=2.0`). This
  ensures reproducible builds and your model behaves the same way every time it's
  deployed.
</Note>

### Allocate a GPU

The `resources` section specifies what hardware your model runs on:

```yaml config.yaml theme={"system"}
resources:
  accelerator: T4
  use_gpu: true
```

**Choosing the right GPU:** Match your GPU to your model's VRAM requirements. For Phi-3-mini (\~7.6GB), a T4 (16GB) provides headroom for inference.

| GPU  | VRAM    | Good for                                    |
| ---- | ------- | ------------------------------------------- |
| T4   | 16GB    | Small models, embeddings, fine-tuned models |
| L4   | 24GB    | Medium models (7B parameters)               |
| A10G | 24GB    | Medium models, image generation             |
| A100 | 40/80GB | Large models (13B-70B parameters)           |
| H100 | 80GB    | Very large models, high throughput          |

<Tip>
  **Estimating VRAM:** A rough rule is 2GB of VRAM per billion parameters for float16 models. A 7B model needs \~14GB VRAM minimum.
</Tip>

***

## Deploy the model

### Authenticate with Baseten

First, generate an API key from the [Baseten settings](https://app.baseten.co/settings/account/api_keys). Then log in:

```sh  theme={"system"}
truss login
```

The expected output is:

```output  theme={"system"}
💻 Let's add a Baseten remote!
🤫 Quietly paste your API_KEY:
```

Paste your API key when prompted. Truss saves your credentials for future deployments.

### Push your model to Baseten

For development with live reload:

```sh  theme={"system"}
truss push --watch
```

The expected output is:

```output  theme={"system"}
Deploying truss using T4x4x16 instance type.
✨ Model Phi 3 Mini was successfully pushed ✨

🪵  View logs for your deployment at https://app.baseten.co/models/abc1d2ef/logs/xyz123
```

<Note>
  When no flag is specified, `truss push` defaults to a published deployment. Use `--watch` for development deployments with live reload support.
</Note>

In this example, the logs URL contains two IDs:

* **Model ID**: The string after `/models/` (e.g., `abc1d2ef`) which you'll use this to call the model API.
* **Deployment ID**: The string after `/logs/` (e.g., `xyz123`) identifies this specific deployment.

You can also find your model ID in [your Baseten dashboard](https://app.baseten.co/models/) by clicking on your model.

***

## Call the model API

After the deployment is complete, you can call the model API:

<Tabs>
  <Tab title="Truss CLI">
    From your Truss project directory, run:

    ```sh  theme={"system"}
    truss predict --data '{"messages": [{"role": "user", "content": "What is AGI?"}]}'
    ```

    The expected output is:

    ```output  theme={"system"}
    Calling predict on development deployment...
    {
      "output": "AGI stands for Artificial General Intelligence..."
    }
    ```

    The Truss CLI uses your saved credentials and automatically targets the correct deployment.
  </Tab>

  <Tab title="cURL">
    Set your API key and replace `YOUR_MODEL_ID` with your model ID (e.g., `abc1d2ef`):

    ```sh  theme={"system"}
    export BASETEN_API_KEY=YOUR_API_KEY

    curl -X POST https://model-YOUR_MODEL_ID.api.baseten.co/development/predict \
      -H "Authorization: Api-Key $BASETEN_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{"messages": [{"role": "user", "content": "What is AGI?"}]}'
    ```

    The expected output is:

    ```output  theme={"system"}
    {'output': 'AGI stands for Artificial General Intelligence...'}
    ```
  </Tab>

  <Tab title="Python">
    Set your API key as an environment variable, then replace `YOUR_MODEL_ID` with your model ID:

    ```sh  theme={"system"}
    export BASETEN_API_KEY=YOUR_API_KEY
    ```

    ```python main.py theme={"system"}
    import requests
    import os

    model_id = "YOUR_MODEL_ID"  # Replace with your model ID (e.g., "abc1d2ef")
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/development/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "messages": [
                {"role": "user", "content": "What is AGI?"}
            ]
        }
    )

    print(resp.json())
    ```

    The expected output is:

    ```output  theme={"system"}
    {'output': 'AGI stands for Artificial General Intelligence...'}
    ```
  </Tab>
</Tabs>

***

## Use live reload for development

To avoid long deploy times when testing changes, use **live reload**:

```sh  theme={"system"}
truss watch
```

The expected output is:

```output  theme={"system"}
🪵  View logs for your deployment at https://app.baseten.co/models/<model_id>/logs/<deployment_id>
🚰 Attempting to sync truss with remote
No changes observed, skipping patching.
👀 Watching for changes to truss...
```

When you save changes to `model.py`, Truss automatically patches the deployed model:

```output  theme={"system"}
Changes detected, creating patch...
Created patch to update model code file: model/model.py
Model Phi 3 Mini patched successfully.
```

This saves time by patching only the updated code without rebuilding Docker containers or restarting the model server.

***

## Promote to production

Once you're happy with the model, deploy it to production:

```sh  theme={"system"}
truss push --publish
```

This changes the API endpoint from `/development/predict` to `/production/predict`:

```sh  theme={"system"}
curl -X POST https://model-YOUR_MODEL_ID.api.baseten.co/production/predict \
  -H "Authorization: Api-Key $BASETEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "What is AGI?"}]}'
```

<Tip>
  To call your production endpoint, you need your model ID. The output of `truss push --publish` includes a logs URL:

  ```output  theme={"system"}
  🪵  View logs for your deployment at https://app.baseten.co/models/abc1d2ef/logs/xyz123
  ```

  Your model ID is the string after `/models/` (e.g., `abc1d2ef`). You can also find it in your [Baseten dashboard](https://app.baseten.co/models/).
</Tip>

***

## Next steps

Now that you've deployed your first model, continue learning:

* [Model serving with Truss](/development/model/overview): Configure dependencies, secrets, and resources.
* [Example implementations](https://github.com/basetenlabs/truss-examples): Deploy dozens of open source models.
* [Autoscaling settings](/deployment/autoscaling): Scale GPU replicas based on demand.
