# Source: https://docs.salad.com/container-engine/how-to-guides/ai-machine-learning/deploy-blip-cog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy SLIP with Cog HTTP Prediction Server

*Last Updated: October 10, 2024*

[Cog](https://cog.run/) is an open-source tool that helps simplify the work of building inference applications for
various AI models. It provides CLI tools, Python modules for prediction and fine-tuning, and an HTTP prediction server
using FastAPI.

Using [the Cog HTTP prediction server](https://github.com/replicate/cog/blob/main/python/cog/server/http.py), we mainly
need to provide two functions in Python: one for downloading/loading the models and another for running the inference.
The server handles everything else, such as input/output, logging, health checks, and exception handling. It supports
synchronous prediction, streaming output and asynchronous prediction with a webhook; its health-check feature is
impressive, providing different running statuses (STARTING, READY, BUSY and FAILED) within the server.

The Cog prediction server can be further customized to meet specific needs. For instance, its path operation functions
for the health checks and predictions are, by default, declared with `async def`, running in the same main thread. By
declaring the predictions function with `def`, a new thread will be spawned to run the prediction when a new request
arrives.This setup can prevent long-running synchronous predictions from blocking timely responses to health queries.
Another example is IPv6 support: the server is hardcoded to listen on an IPv4 port, we can modify the code to use IPv6
by replacing `0.0.0.0` with `::` when launching its underlying Uvicorn server.

The [BLIP](https://arxiv.org/pdf/2201.12086) (Bootstrapping Language-Image Pre-training) supports multiple image-to-text
tasks, such as Image Captioning, Visual Question Answering and Image Text Matching. Each task requires a dedicated and
fine-tuned BLIP model that is 1\~2 GB in size. We can run inference for the three models of these three tasks
simultaneously on a SaladCloud node that has a GPU with 8GB VRAM.

[LAVIS](https://github.com/salesforce/LAVIS) (A Library for Language-Vision Intelligence) is the Python deep learning
library, and provides the unified access to the pretrained models, datasets and tasks for multimodal applications,
including BLIP, CLIP and others.

Let’s use BLIP as an example to see how to build a publicly-accessible and scalable inference endpoint using the Cog
HTTP prediction server on SaladCloud, capable of handling various image-to-text tasks.

# Build the container image

The following 4 files are necessary for building the image, and we also provide some test code in
[the Github Repo](https://github.com/SaladTechnologies/cog-deploy).

```yml  theme={null}
build:
  gpu: true

predict: 'predict.py:Predictor'
```

The yaml file defines how to build a Docker image and how to run predictions. In this example, We only use the Cog HTTP
prediction server (not its CLI tools), the file is quite simple. When the prediction server is launched, it will read
the file, and then set the number of Uvicorn worker processes to 1 (when the GPU is enabled) and run the provided code -
predict.py for inference.

```
salesforce-lavis==1.0.2
cog==0.9.8
```

Based on the PyTorch base image, we only need to install two Python packages and their dependencies for this
application.

```Dockerfile  theme={null}
# Base Image
FROM docker.io/pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

RUN apt-get update && apt-get install -y curl
RUN pip install --upgrade pip

WORKDIR /app

# Install LAVIS and Cog HTTP prediction server
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Optional, build the downloaded models into the container image.
# The models can also be downloaded dynamically when the container is running.
# COPY ./torch /root/.cache/torch

COPY cog.yaml /app
COPY predict.py /app

#  Modify the installed Cog prediction server to use IPv6
RUN  sed -i 's/0.0.0.0/::/g' /opt/conda/lib/python3.10/site-packages/cog/server/http.py

# Run the Cog HTTP prediction server
CMD ["python", "-m", "cog.server.http"]

EXPOSE 5000
```

You can download the models first and build them into the container image. This way, when the workload is running on
SaladCloud, it can start the inference immediately. Alternatively, the models can also be downloaded dynamically when
the container is running. This approach has the advantage of smaller image sizes, allowing for faster builds and pushes.

For the inbound connection, the containers running on SaladCloud need to listen on an IPv6 port. The Cog HTTP prediction
server is currently hardcoded to use an IPv4 port, but this can be easily modified by a `sed` command in the Dockerfile.

```python  theme={null}
from cog import BasePredictor, Input, Path
import time
import torch
from lavis.models import load_model_and_preprocess
from PIL import Image

class Predictor(BasePredictor):
    def setup(self) -> None:

        ......

    def predict(
        self,
        image: Path = Input( description="Input image" ),
        task: str = Input( choices=[ "image_captioning", "visual_question_answering", "image_text_matching" ],
            default="image_captioning", description="Choose a task." ),
        question: str = Input( default=None, description="Type question for the input image for visual question answering task." ),
        caption: str = Input( default=None, description="Type caption for the input image for image text matching task." ),
    ) -> str:

        ......
```

The Predictor Class is implemented with 2 member functions that will be called by the Cog prediction server:

setup(), download and load the 3 models into the GPU.

predict(), run the inference based on inputs and return the results.

# Test the image

```
# Build
docker image build -t docker.io/saladtechnologies/sip:0.0.3-blip -f Dockerfile .

# Run with GPU
docker run --rm --gpus all docker.io/saladtechnologies/sip:0.0.3-blip

# Run without GPU
docker run --rm docker.io/saladtechnologies/sip:0.0.3-blip

# Push to Docker Hub
docker push docker.io/saladtechnologies/sip:0.0.3-blip
```

After the container is running, you can log into it and do some tests for health checks and predictions.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog1.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a99aae175e68630fda002da6f7afaf3a" data-og-width="1125" width="1125" data-og-height="191" height="191" data-path="container-engine/images/blip-cog1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog1.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d4ebfacf6797a8eec01ee1f70239fd36 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog1.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=d4a08176bff5b076e1389eb78f026625 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog1.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2001609693513d6bd6bd9992bca89795 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog1.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=841672ccd759794c8578b7694dd04c09 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog1.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=3402f1d3de2a8fb9a654987664b9bf39 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog1.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2a71079c63635973901da4c4651098ba 2500w" />

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog2.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=4effdda100973f147ed8537819b1e25f" data-og-width="1114" width="1114" data-og-height="458" height="458" data-path="container-engine/images/blip-cog2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog2.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=98be03a85e3c187d269ac9ff7eff83cb 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog2.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c78aaf704192a8540870212fffc69125 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog2.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=c3e7bffec204b4cc1371902bea79369f 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog2.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=47182c4674421c6e1ee07087bf452715 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog2.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=84e3b45fb22cdef9dd369c2d14dab3a6 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog2.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=bf8ad19f38a9bc448a7bff205fecf9cd 2500w" />

The Cog HTTP prediction server is now using IPv6. The port number is configurable via the environment variable - ‘PORT’.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog3.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=119adb042cf6e48c81ea4fb9f3060a0d" data-og-width="1122" width="1122" data-og-height="135" height="135" data-path="container-engine/images/blip-cog3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog3.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=17efe0ab3964fdcbc5122e23e827c651 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog3.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a2258254e35a2035526435833241d1d0 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog3.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=5c79e1b050161eedc86f67be280bb0ba 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog3.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=95a0fadf93f0b0422f404b18bbad014a 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog3.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=f48ca27a2a0cbd61d645aef7643d0978 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog3.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=99285fe4c85affaa18076ca123d3f3e9 2500w" />

# Deploy the image on SaladCloud

Create a container group with the following parameters:

```md  theme={null}
# Image Source

saladtechnologies/sip:0.0.3-blip

# Replica Count

3

# Resource

2 vCPUs, 8GB Memory Any GPU types with 8 GB or more VRAM

# Container Gateway

Enabled, Port 5000

# Readiness Probe (Protocol: exec)

Enabled Protocol: exec

Command: python Argument1: -c Argument2: import requests,sys;sys.exit(0 if 'READY' in
requests.get('http://[::1]:5000/health-check').text else -1)

Initial Delay Seconds: 60 Period Seconds: 10 Timeout Seconds: 5 Success Threshold: 1 Failure Threshold: 3

# Environment Variables (Optional)

COG_LOG_LEVEL, INFO (Default) / DEBUG / WARNING PORT, 5000 (Default) or others
```

The Readiness Probe is used to evaluate whether a container is ready to accept the traffic from the load balancer. The
probe with the protocol - exec, will run the given command inside the container, if the command returns an exit code of
0, the container is considered in a healthy state. Any other exit codes indicate the container is not ready yet. A
Python script is provided here and run regularly to check whether the models have been loaded successfully and the Cog
HTTP prediction server is ready.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog6.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2c3ce7092fa5b4a9b506133a1800fc9a" data-og-width="914" width="914" data-og-height="914" height="914" data-path="container-engine/images/blip-cog6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog6.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=298fce39550f78b8c5111a45b915ac27 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog6.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=a7b54a65a6c09020d2e5cd71a8c72252 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog6.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=1861873b22d521d393fb46e7fec9a303 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog6.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=5248da013a62fd2cd3facb4ecdbd5275 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog6.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=1d472210c3ba2f4b555bac91fc6421eb 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog6.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=85292660168f4f7a625426bd2d4f0f42 2500w" />

# Test the inference endpoint

After the container group is deployed, an access domain name will be created and can be used to access the application.

<img src="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog5.png?fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=2b7e57b9a9033fd68b73f66fa863e4f9" data-og-width="714" width="714" data-og-height="607" height="607" data-path="container-engine/images/blip-cog5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog5.png?w=280&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=92811b34fa4d4213e36e1629bb6d6772 280w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog5.png?w=560&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=312fd390bfc5a5a3c437874fef3fc2b5 560w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog5.png?w=840&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=b2eac5334a256fd47b20d242c0f17d95 840w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog5.png?w=1100&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=63c151525cac11d349f827ae0c2a0174 1100w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog5.png?w=1650&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=e65748687203fa3aaaf9aa88569cb279 1650w, https://mintcdn.com/salad/8o1ParSgmJGbpSYb/container-engine/images/blip-cog5.png?w=2500&fit=max&auto=format&n=8o1ParSgmJGbpSYb&q=85&s=08cdbba2d886dc11c99d484016b72e8b 2500w" />

```shell  theme={null}
# image_captioning

curl -s -X POST \
  -H "Content-Type: application/json" \
  -d $'{ "input": {
      "task": "image_captioning",
      "image": "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg" } }' \
  https://salmon-tubers-69f52h0zu3qrrtn6.salad.cloud/predictions


# visual_question_answering

curl -s -X POST \
  -H "Content-Type: application/json" \
  -d $'{ "input": {
      "task": "visual_question_answering",
      "question": "where is the dog?",
      "image": "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg" } }' \
  https://salmon-tubers-69f52h0zu3qrrtn6.salad.cloud/predictions


# image_text_matching

curl -s -X POST \
  -H "Content-Type: application/json" \
  -d $'{ "input": {
      "task": "image_text_matching",
      "caption": "a dog and a women are sitting at the beach",
      "image": "https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg" } }' \
  https://salmon-tubers-69f52h0zu3qrrtn6.salad.cloud/predictions
```
