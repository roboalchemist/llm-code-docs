# Source: https://docs.anyscale.com/services/fast-loading-tutorial.md

# Tutorial: Load a custom PyTorch model

[View Markdown](/services/fast-loading-tutorial.md)

# Tutorial: Load a custom PyTorch model

This tutorial walks you through using fast model loading to load model weights stored as safetensors for a PyTorch model on Anyscale. For full documentation on fast loading, see [Fast model loading for PyTorch models](/services/fast-loading.md).

This example loads weights for a generic `torch` model. For simplicity, it uses a model and pretrained weights from [Hugging Face](https://huggingface.co/), but you can replace these with your own custom model and weights.

## Step 0: Configure environment[​](#step-0-configure-environment "Direct link to Step 0: Configure environment")

Start an Anyscale workspace, making sure to use the following options:

* Select the **Auto select worker nodes** option in the compute config.
* Use a CUDA image with Ray 2.36.0 or later, such as `anyscale/ray:2.36.0-slim-py312-cu123`

Then install required dependencies:

```
pip install -U accelerate safetensors torch transformers
```

The example uses [Mistral-7B-Instruct-v0.1 from Hugging Face](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1). To use the model, you need to [accept the terms in the model repository](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) and retrieve your [access token](https://huggingface.co/docs/transformers.js/en/guides/private).

Run the following code to add your Hugging Face token to your work as an environment variable:

```
export HUGGING_FACE_HUB_TOKEN=<your-hugging-face-token>
```

You must also add the `HUGGING_FACE_HUB_TOKEN` to the **Dependencies** tab of your workspace to make sure Anyscale includes it when launching a service.

## Step 1: Save model weights in safetensors format[​](#step-1-save-model-weights-in-safetensors-format "Direct link to Step 1: Save model weights in safetensors format")

First, download the weights from Hugging Face and save them to a single safetensors file in [cluster local storage](/storage/local.md). For a custom model, this would likely be the output of the training step.

```
import torch
from safetensors.torch import save_file
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1", torch_dtype=torch.float16)
save_file(model.state_dict(), "/mnt/local_storage/Mistral-7B-Instruct-v0.1.safetensors")
```

Save this code in a local file named `download_model.py` and run it:

```
python download_model.py
```

Sample output:

```
Loading checkpoint shards: 100%|██████████████████████████| 2/2 [00:24<00:00, 12.35s/it]
```

## Step 2: Upload model weights to remote storage[​](#step-2-upload-model-weights-to-remote-storage "Direct link to Step 2: Upload model weights to remote storage")

Now upload the safetensors file to the [artifact storage bucket](/storage.md#artifact-storage) for the cloud your workspace is running in.

```
aws s3 cp /mnt/local_storage/Mistral-7B-Instruct-v0.1.safetensors $ANYSCALE_ARTIFACT_STORAGE/
```

Sample output:

```
upload: ../../../mnt/local_storage/Mistral-7B-Instruct-v0.1.safetensors to s3://anyscale-test-data-cld-i2w99rzq8b6lbjkke9y94vi5/org_7c1Kalm9WcX2bNIjW53GUT/cld_kvedZWag2qA8i5BjxUevf5i7/artifact_storage/Mistral-7B-Instruct-v0.1.safetensors
```

## Step 3: Construct the model and load its weights in a Serve app[​](#step-3-construct-the-model-and-load-its-weights-in-a-serve-app "Direct link to Step 3: Construct the model and load its weights in a Serve app")

```
import torch
from accelerate import init_empty_weights
from fastapi import FastAPI
from transformers import AutoTokenizer, MistralConfig, MistralForCausalLM
from typing import Dict

from ray import serve
from ray.anyscale.safetensors.torch import load_file

fastapi_app = FastAPI()

@serve.deployment(
    # Configure the replica to use an Nvidia T4 GPU.
    ray_actor_options={"num_gpus": 1, "accelerator_type": "T4"},
)
@serve.ingress(fastapi_app)
class Mistral7BApp:
    def __init__(self, model_weights_uri: str):
        # IMPORTANT: Initialize the model with *empty weights*.
        # When using your own `torch.nn.Module`, you can use torch.nn.utils.skip_init, see:
        # https://pytorch.org/tutorials/prototype/skip_param_init.html
        with init_empty_weights():
            self._model = MistralForCausalLM(
                MistralConfig.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1", torch_dtype=torch.float16)
            )

        # Download the model weights directly to the GPU.
        state_dict: Dict[str, torch.Tensor] = load_file(model_weights_uri, device="cuda")

        # Populate the weights in the model class.
        self._model.load_state_dict(state_dict, assign=True)
        self._model.to("cuda")

        # Load the tokenizer for the model.
        self._tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")

    @fastapi_app.get("/")
    def predict(self, prompt: str) -> str:
        messages = [{"role": "user", "content": prompt}]
        encodeds = self._tokenizer.apply_chat_template(messages, return_tensors="pt").to("cuda")
        generated_ids = self._model.generate(encodeds, max_new_tokens=1000, do_sample=True)
        decoded = self._tokenizer.batch_decode(generated_ids.to("cpu"))
        return decoded[0]


# Pass the URI to the uploaded model weights.
# The 'anyscale://' URI resolves to Anyscale-managed artifact storage when running inside an Anyscale cluster.
app = Mistral7BApp.bind("anyscale://Mistral-7B-Instruct-v0.1.safetensors")
```

To run the serve app, save the Python file locally as `main.py` and use `serve run`:

```
serve run main:app
```

Sample output:

```
2024-09-20 14:50:16,217 INFO scripts.py:499 -- Running import path: 'main:app'.
2024-09-20 14:50:18,804 INFO worker.py:1601 -- Connecting to existing Ray cluster at address: 10.0.58.159:6379...
2024-09-20 14:50:18,810 INFO worker.py:1777 -- Connected to Ray cluster. View the dashboard at https://session-nf13dmw1fmld6bei4v7czihhhh.i.anyscaleuserdata.com
2024-09-20 14:50:18,812 INFO packaging.py:359 -- Pushing file package 'gcs://_ray_pkg_5cbc1f5ea201895259da328911c3241cb56311e9.zip' (0.02MiB) to Ray cluster...
2024-09-20 14:50:18,812 INFO packaging.py:372 -- Successfully pushed file package 'gcs://_ray_pkg_5cbc1f5ea201895259da328911c3241cb56311e9.zip'.
(ProxyActor pid=49865) INFO 2024-09-20 14:50:22,805 proxy 10.0.58.159 proxy.py:1235 - Proxy starting on node 4c64508eea53f54920fdf1be0286974e95a3945af03178e0160b6d39 (HTTP port: 8000).
INFO 2024-09-20 14:50:22,828 serve 49656 api.py:277 - Started Serve in namespace "serve".
INFO 2024-09-20 14:50:22,828 serve 49656 api.py:259 - Connecting to existing Serve app in namespace "serve". New http options will not be applied.
(ServeController pid=49775) INFO 2024-09-20 14:50:22,920 controller 49775 deployment_state.py:1598 - Deploying new version of Deployment(name='Mistral7BApp', app='default') (initial target replicas: 1).
(ServeController pid=49775) INFO 2024-09-20 14:50:23,023 controller 49775 deployment_state.py:1844 - Adding 1 replica to Deployment(name='Mistral7BApp', app='default').
(ServeReplica:default:Mistral7BApp pid=49960) 2024-09-20 14:50:27,987 anytensor INFO - Got 1 file to download (13.49 GB total)
(ServeReplica:default:Mistral7BApp pid=49960) 2024-09-20 14:50:33,464 anytensor INFO - Downloaded 7.16/13.49 GB (53.1%, 1.43 GB/s)
(ServeReplica:default:Mistral7BApp pid=49960) 2024-09-20 14:50:37,716 anytensor INFO - Downloaded 13.49/13.49 GB (100.0%, 1.45 GB/s)
(ServeReplica:default:Mistral7BApp pid=49960) 2024-09-20 14:50:37,788 anytensor INFO - Finished download in 9.41s (1.43 GB/s)
INFO 2024-09-20 14:50:38,879 serve 49656 client.py:492 - Deployment 'Mistral7BApp:tbd5s25i' is ready at `http://127.0.0.1:8000/`. component=serve deployment=Mistral7BApp
INFO 2024-09-20 14:50:38,882 serve 49656 api.py:549 - Deployed app 'default' successfully.
```

Open another terminal and test the endpoint:

```
curl -X GET http://localhost:8000?prompt=hello
```

Sample return:

```
"<s> [INST] hello [/INST] Hello! It's great to have you here. Is there anything you would like to ask or talk about?</s>"
```
