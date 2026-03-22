# Source: https://docs.verda.com/containers/tutorials/deploy-with-replicate-cog-indepth.md

# In-Depth: Deploy with Replicate Cog

In this tutorial, we will deploy an endpoint built with [Cog](https://cog.run/) framework by [Replicate](https://replicate.com/), for packaging and running machine learning models.

We will deploy the [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) image generation model.

`black-forest-labs/FLUX.1-schnell` is a 12 billion parameter rectified flow transformer by [Black Forest Labs](https://blackforestlabs.ai/), capable of generating images from text descriptions.

## Prerequisites

For this example you need a Python environment running on your local machine, a [Docker](https://www.docker.com/) (or Docker-compatible) container runtime installed on your computer. A container registry to store the image created by [Cog](https://cog.run/) and Verda cloud account to create a deployment.

### Docker container runtime

Docker is a platform for developing, shipping, and running applications. You can learn how to set up Docker from the [official Docker website](https://docs.docker.com/get-started/). Note that you can use any Docker-compatible container runtime, such as:

* [OrbStack](https://orbstack.dev/)
* [Colima](https://github.com/abiosoft/colima)
* [Podman](https://podman.io/)

### Python environment

We are using Python version 3.12 for this tutorial. You can set up your Python environment as you see fit, however we are using [venv](https://docs.python.org/3/library/venv.html) combined with bash shell for this example.

### Cog

You will need to have Cog installed on your computer. Please follow the [installation instructions](https://cog.run/) and choose your preferred method of setting up Cog.

### Container Registry

You will need a container registry to store the container image. You can use any container registry you prefer. In this example we use GitHub Container Registry. You can find more information about GitHub Container Registry from the [official GitHub documentation](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

For the sake of our example, we will use nonexistent GitHub registry url `ghcr.io/username/container-image` In the examples remember to replace this with your own GitHub registry url.

Please make sure that you have credentials to login to your registry. You can login to GitHub container registry by typing the following command:

```bash
docker login <registry-url> -u <registry-username>
```

## Create a container image

Next we will create a container image. Please create a folder named `flux-schnell` and save the following files in it, starting with `cog.yaml`, defining the dependencies and the predictor class required to run the model:

```yaml
build:
  gpu: true
  python_version: "3.12"
  python_packages:
    - diffusers
    - transformers
    - accelerate
    - torch
    - cog
    - sentencepiece
    - protobuf
    - hf_transfer
predict: "predict.py:Predictor"
```

Next, please create `predict.py`, containing the `Predictor` class needed for setting up and running the model:

```python
from typing import Any
from cog import BasePredictor, Input
from diffusers import FluxPipeline
from io import BytesIO
import torch
import base64

class Predictor(BasePredictor):
    def __init__(self):
        self.pipe = None

    def setup(self) -> None:
        self.pipe = FluxPipeline.from_pretrained(
            "black-forest-labs/FLUX.1-schnell",
            torch_dtype=torch.float16,
            use_safetensors=True
        )
        self.pipe.to("cuda")

    def predict(
        self,
            prompt: str = Input(
                description="The text prompt to generate the image.",
                default="A photo of a cat"
            ),
            guidance_scale: float = Input(
                description="Guidance scale parameter.",
                default=0.0
            ),
            height: int = Input(
                description="Height of the generated image.",
                default=1024
            ),
            width: int = Input(
                description="Width of the generated image.",
                default=1024
            ),
            num_inference_steps: int = Input(
                description="Number of inference steps.",
                default=4
            ),
            max_sequence_length: int = Input(
                description="Maximum sequence length.",
                default=256
            )
    ) -> Any:
        images = self.pipe(
            prompt=prompt,
            guidance_scale=guidance_scale,
            height=height,
            width=width,
            num_inference_steps=num_inference_steps,
            max_sequence_length=max_sequence_length,
        ).images[0]

        buffered = BytesIO()
        images.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        images_64 = base64.b64encode(img_bytes)

        return images_64
```

Next, run the following command to build the container image:

```bash
cog build
```

This step will use the configuration defined in the `cog.yaml` to create the container image and store it in local container registry. The step can take quite some time to complete, as it downloads all the dependencies, such as required libraries and the model weights, and builds the container image.

### Push the container image to a remote container registry

When the previous step has completed, you should see the container image in your local container registry. To verify, please run:

```bash
docker image ls
```

You should see something similar to this, where you have the prefix `cog-` followed by folder name `flux-schnell` (this may be different, if you used a different folder name).

```text
REPOSITORY                                         TAG       IMAGE ID       CREATED       SIZE
cog-flux-schnell                                   latest    8794f120a61b   5 minutes ago 17.1GB
...
```

Next, tag the image and push it to your remote container registry. We do not support pulling containers with the `:latest` tag in order to make sure that all deployments are consistent. Please make sure you use distinct tags for your container updates.

```bash
docker tag cog-flux-schnell:latest ghcr.io/username/cog-flux-schnell:v1
docker push ghcr.io/username/cog-flux-schnell:v1
```

This will push the container image to your remote registry. Uploading the image to the container registry can take some time, depending on your network connection.

## Create the deployment

In this example, we will deploy the image we created earlier on NVIDIA L40S (48 GB VRAM) GPU type. For larger models, you may need to choose one of the other GPU types we offer.

1. Log in to the [Verda cloud console](https://console.verda.com/signin)
2. Create a new project or use existing one, open the project
3. On the left you'll see a navigation menu. Go to **Containers -> New deployment.** Name your deployment and select the L40S Compute Type.
4. Set **Container Image** to point to your repository where you pushed the image you created earlier. For example to`ghcr.io/username/cog-flux-schnell:v1`
5. You can use the **Public** option for your image, if you pushed the image to a public repository. You can use the **Private** if you have a private registry, paired with credentials.
6. Make sure your preferred tag is selected
7. Set the Exposed HTTP port to `5000`
8. Set the Healthcheck port to `5000`
9. Set **Health Check** to `/health-check`
10. Make sure **Start Command** is off
11. **Deploy container**

(You can leave the **Scaling** options to their default values for now)

That's it! You have now created a deployment. You can check the logs of the deployment from the logs tab. This will take few minutes to complete.

{% hint style="warning" %}
For production use, we recommend authenticating/using private registries to avoid potential rate limits imposed by public container registries.
{% endhint %}

## Accessing the deployment

Before you can connect to the endpoint, you will need to generate an authentication token, by going to **Keys -> Inference API Keys**, and click **Create.**

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-ebbcbcae10353563f31b1e9dcc54c324fda49dbd%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

The **base endpoint URL** for your deployment is in the **Containers API** section in the top left of the screen. This will be in the form of: `https://containers.datacrunch.io/<NAME-OF-OUR-DEPLOYMENT>/`

### Test Deployment

Once the deployment has been created and is ready to accept requests, you can test that it responds correctly by sending a `/health-check` request to the endpoint. Below is an example cURL command for running your test deployment:

{% hint style="info" %}
Notice the added subpath `/health-check` to the base endpoint URL
{% endhint %}

```bash
#!/bin/bash
curl -X GET <YOUR_CONTAINERS_API_URL>/health-check \
--header 'Authorization: Bearer <YOUR_INFERENCE_API_KEY>' \
--header 'Content-Type: application/json'
```

This should return a response that shows the deployment is available for use.

```json
{
  "status":"READY",
  "setup":{
    "started_at":"2025-01-22T16:12:48.859125+00:00",
    "completed_at":"2025-01-22T16:14:01.224369+00:00",
    "logs":"\rLoading pipeline components...:   0%|  ...",
    "status":"succeeded"
  }
}
```

## Sending inference requests

After `/health-check` we are ready to send an inference requests to the model.

### Generate image from text

Navigate to your project directory and create a new virtual environment and run commands below:

```bash
python -m venv venv
source ./venv/bin/activate
```

You may also need to install some required pacakges,

```bash
pip install requests
```

In the same folder, create a new file named `inference.py` and add the following code:

```python
import requests
import base64
import sys
import signal
import time

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

def do_test_request() -> None:
    url = '<YOUR_CONTAINERS_API_URL>/predictions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <YOUR_INFERENCE_API_KEY>',
    }

    data = {
        "input": {
            "prompt": "Create me an artistic and psychedelic picture of a man flying a hot air balloon above a city. The city is on fire and the balloon is made out of cotton candy.",
            "guidance_scale":"0.0",
            "height": "512",
            "width": "512",
            "num_inference_steps": "4",
            "max_sequence_length": "256",
        }
    }

    start_time = time.time()
    formatted_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
    print(f"{formatted_start_time} Sending inference request")
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            response_json = response.json()
            base64_image = response_json.get('output')

            if base64_image:
                image_data = base64.b64decode(base64_image)

                with open(f'output.png', 'wb') as f:
                    f.write(image_data)

                end_time = time.time()
                formatted_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
                print(f"{formatted_end_time} Image saved as output.png, Duration: {end_time - start_time} seconds")
            else:
                print("No image data found in the response.", file=sys.stderr)
        except ValueError:
            print("Response content is not valid JSON.", file=sys.stderr)
            print("Response body:", file=sys.stderr)
            print(response.text, file=sys.stderr)
    else:
        print(f"Request failed with status code {response.status_code}", file=sys.stderr)
        print("Response body:", file=sys.stderr)
        print(response.text, file=sys.stderr)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)
    do_test_request()
```

Run it with the following command:

```bash
python inference.py
```

The image you generated is located in the folder you ran the script in, named `output.png`.

## Conclusion

This concludes our tutorial how create images from text using [Cog](https://cog.run/) with `black-forest-labs/FLUX.1-schnell` model. You can now use the [Cog](https://cog.run/) endpoint to generate more images from text descriptions.
