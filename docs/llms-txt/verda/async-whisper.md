<!-- Source: https://docs.verda.com/containers/tutorials/async-whisper.md -->

# In-Depth: Asynchronous Inference Requests with Whisper

In this tutorial, we will deploy a container with `openai/whisper-large-v3-turbo` and demonstrate how to send asynchronous inference requests when communicating with the model. Whisper is a popular model for automatic speech recognition (ASR) and speech translation.

You can find more information about the model itself from the [Hugging Face model hub](https://huggingface.co/openai/whisper-large-v3-turbo).

We will create a simplified container image that hosts whisper using [Python 3.12](https://www.python.org/), [FastAPI](https://fastapi.tiangolo.com/) [Uvicorn](https://www.uvicorn.org/) and [Huggingface transformers package](https://huggingface.co/docs/transformers/en/index)

This tutorial also includes an optional step to send inference results to a webhook, and for this option we use [webhook.site](https://webhook.site/).

## Prerequisites

For this example you need a Python environment running on your local machine, a [Docker](https://www.docker.com/) (or Docker-compatible) container runtime installed on your computer. A container registry to store the image we create and Verda cloud account to create a deployment.

### Python environment

We are using Python version 3.12 for this tutorial. You can set up your Python environment as you see fit, however we are using [venv](https://docs.python.org/3/library/venv.html) combined with bash shell for this example.

### Container Registry

You will need a container registry to store the container image. You can use any container registry you prefer. In this example we use GitHub Container Registry. You can find more information about GitHub Container Registry from the [official GitHub documentation](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

For the sake of our example, we will use nonexistent GitHub registry url `ghcr.io/username/container-image` In the examples remember to replace this with your own GitHub registry url.

Please make sure that you have credentials to login to your registry. You can login to GitHub container registry by typing the following command:

```bash
docker login <registry-url> -u <registry-username>
```

## Create a container image

Next we will create a container image out of our inference service.

### Create a webhook for uploading (optional)

This step is optional if you don't want to upload the inference result using a webhook.

First visit [webhook.site](https://webhook.site/). We will use the site to demonstrate how to send inference result to a webhook. You will get an url for webhook from their site. The url looks something like this: `https://webhook.site/5bdbe974-713f-4b92-89ea-acb79be5b68f`. Save this for later, as we'll send our inference result to this url.

Note that you can also set up your own webhook for uploading the inference results and host it as you please, however that is not part of this tutorial.

### Inference service container image

Next we will create a container image. Please create a folder named `whisper-example-mp3` and save the following files in it, starting with `Dockerfile`:

```docker
FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 8989

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8989"]
```

Next we create a `requirements.txt` file, with following entries:

```txt
fastapi
uvicorn
torch
torchaudio
numpy
pydub
requests
transformers
```

Next, please create `main.py`, containing the following python implementation. Notice that you'll need the url from [webhook.site](https://webhook.site/), should you want to upload the results of the inference to a webhook. Look for the comment in the `async def generate_webhook(body: Dict) -> Dict:` function.

```python
import uvicorn
import io
import os
import numpy as np
import torch
import requests
from fastapi import FastAPI, HTTPException, BackgroundTasks, status
from starlette.responses import JSONResponse
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from pydub import AudioSegment
from typing import Dict


def create_app() -> FastAPI:
    fast_api = FastAPI()

    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    fast_api.state.webhook = os.getenv('WEBHOOK', None)

    model_id = "openai/whisper-large-v3-turbo"
    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id,
        torch_dtype=torch_dtype,
        low_cpu_mem_usage=True,
        use_safetensors=True
    )
    model.to(device)

    processor = AutoProcessor.from_pretrained(model_id)
    speech_pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        torch_dtype=torch_dtype,
        device=device
    )

    @fast_api.get("/health")
    async def health_check() -> Dict:
        return {"status": "ok"}

    @fast_api.post("/generate")
    async def generate(body: Dict) -> Dict:
        url = await get_audio_url(body)
        response = await get_audio_file(url)
        return await execute_pipeline(response)

    @fast_api.post("/generate_webhook")
    async def generate_webhook(body: Dict, background_tasks: BackgroundTasks) -> JSONResponse:
        # Please set WEBHOOK environment variable if you want to use webhooks
        if fast_api.state.webhook is None:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={"status": "error", "details": "webhook not defined"}
            )
        background_tasks.add_task(process_and_send, body)
        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={"status": "accepted"}
        )

    async def process_and_send(body: Dict):
        try:
            url = await get_audio_url(body)
            response = await get_audio_file(url)
            result = await execute_pipeline(response)
            await send_to_webhook(fast_api.state.webhook, result)
        except Exception as e:
            print(f"[background task] error: {e}")

    async def send_to_webhook(webhook_url: str, payload: dict):
        try:
            requests.post(webhook_url, json=payload, headers={"Content-Type": "application/json"}, timeout=30)
        except Exception as e:
            print(f"Failed to send webhook: {e}")

    async def get_audio_url(body: Dict) -> str:
        url = body.get("url")
        if not url:
            raise HTTPException(status_code=400, detail="Request JSON must include a top‑level `url` field")

        return url

    async def get_audio_file(url: str) -> requests.Response:
        resp = requests.get(url)
        if resp.status_code != 200:
            raise HTTPException(status_code=400, detail=f"Could not fetch audio file (status {resp.status_code})")

        return resp

    async def execute_pipeline(response: requests.Response) -> Dict:
        audio = AudioSegment.from_file(io.BytesIO(response.content), format="mp3")
        samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
        samples /= (1 << (audio.sample_width * 8 - 1))

        if audio.channels > 1:
            samples = samples.reshape((-1, audio.channels)).mean(axis=1)

        sampling_rate = audio.frame_rate
        max_secs = 30
        step = max_secs * sampling_rate
        transcripts = []
        for start in range(0, len(samples), step):
            chunk = samples[start: start + step]
            out = speech_pipe(
                {"array": chunk, "sampling_rate": sampling_rate},
            )
            transcripts.append(out["text"])
        full_text = " ".join(transcripts)
        return {"result": full_text}

    return fast_api

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8989)
```

Next, run the following command to build the container image:

```bash
docker build --no-cache --platform linux/amd64 -t ghcr.io/username/whisper-example-mp3:latest -f ./Dockerfile .
```

This step will use the configuration defined in the `Dockerfile` to create the container image and store it in local container registry. The step can take quite some time to complete.

### Push the container image to a remote container registry

When the previous step has completed, you should see the container image in your local container registry. To verify, please run:

```bash
docker image ls
```

You should see something similar to this (this may be different, if you used a different folder name).

```text
REPOSITORY                                         TAG       IMAGE ID       CREATED       SIZE
ghcr.io/username/whisper-example-mp3               latest    8794f120a61b   5 minutes ago 7.21GB
...
```

Next, tag the image and push it to your remote container registry. We do not support pulling containers with the `:latest` tag in order to make sure that all deployments are consistent. Please make sure you use distinct tags for your container updates.

```bash
docker tag ghcr.io/username/whisper-example-mp3:latest ghcr.io/username/whisper-example-mp3:1
docker push ghcr.io/username/whisper-example-mp3:1
```

This will push the container image to your remote registry. Uploading the image to the container registry can take some time, depending on your network connection.

## Create the deployment

Next as a part of this example, we will deploy the image we created earlier on General Compute (24 GB VRAM) GPU type.

1. Log in to the [Verda cloud console](https://console.verda.com/signin)
2. Create a new project or use existing one, open the project
3. On the left you'll see a navigation menu. Go to **Containers -> New deployment.** Name your deployment and select the General Compute Type.
4. Set **Container Image** to point to your repository where you pushed the image you created earlier. For example to`ghcr.io/username/whisper-example-mp3:1`
5. You can use the **Public** option for your image, if you pushed the image to a public repository. You can use the **Private** if you have a private registry, paired with credentials.
6. Make sure your preferred tag is selected
7. Set the Exposed HTTP port to `8989`
8. Set the Healthcheck port to `8989`
9. Set **Health Check** to `/health`
10. Make sure **Start Command** is off
11. (Optional) If you want to test webhook functionality, please add an environment variable `WEBHOOK` pointing to your webhook URL.
12. **Deploy container**

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

Once the deployment has been created and is ready to accept requests, you can test that it responds correctly by sending a `/health` request to the endpoint. Below is an example cURL command for running your test deployment:

{% hint style="info" %}
Notice the added subpath `/health` to the base endpoint URL
{% endhint %}

```bash
#!/bin/bash
curl -X GET <YOUR_CONTAINERS_API_URL>/health \
--header 'Authorization: Bearer <YOUR_INFERENCE_API_KEY>' \
--header 'Content-Type: application/json'
```

This should return an status ok response:

```json
{
    "status":"ok"
}
```

After `/health` returns ok, we are ready to send an inference requests to the model.

## Sending asynchronous inference requests

Enabling asynchronous inference with Verda cloud is done by using `Prefer` header and `X-Inference-Id` header. The inference services recognize 3 values for `Prefer` header:

* `Prefer: respond-async`
* `Prefer: respond-async-proxy`
* `Prefer: respond-async-container`

These values and their functionalities are explained in more detail [here](https://docs.verda.com/containers/synchronous-and-asynchronous-inference). In this example we will use two of the possible options to address two asynchronous inference scenarios.

`X-Inference-Id` header can be set by the client on sending an inference request, should they want to use some identifier of their own, but if omitted the inference services will create one. More about this header later in the tutorial.

### Generate text from audio

Navigate to your project directory and create a new virtual environment and run commands below:

```bash
python -m venv venv
source ./venv/bin/activate
```

You may also need to install some required packages,

```bash
pip install requests
```

In the same folder, create a new file named `inference.py` and add the following code:

```python
import requests
import sys
import os
import signal

def do_test_request() -> None:
    token = os.environ['DATACRUNCH_BEARER_TOKEN']
    deployment_name = os.environ['DATACRUNCH_DEPLOYMENT']
    baseurl = "https://containers.datacrunch.io"
    inference_url = f"{baseurl}/{deployment_name}/generate"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Prefer": "respond-async"
    }

    payload = {
        "url": "https://tile.loc.gov/storage-services/media/ls/sagan/1958124-3-1.mp3"
    }

    response = requests.post(inference_url, headers=headers, json=payload)
    if response.status_code == 202:
        print(response.json())
    else:
        print(f"inference failed. status code: {response.status_code}")
        print(response.text, file=sys.stderr)


def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)

    do_test_request()
```

After you have saved the python script to file, execute it:

```bash
python inference.py
```

The output you'll see is similar to the example below:

```json
{
   "Id":"f251ffb7-13d4-4e3d-bc37-cf24fc1177e8",
   "StatusPath":"/status/whisper-example-mp3",
   "ResultPath":"/result/whisper-example-mp3"
}
```

In the result, `Id` is the asynchronous inference id, which will also be found in the response headers named as `X-Inference-Id`. This header is needed to identify the inference request when requesting status or results.`StatusPath` contains path where to request the inference status and `ResultPath` is a path to where fetch the results of the inference request.

Next we will check the status of the inference. When requesting the status of the inference request you must provide an identifier for the inference request that you want to access. This is done by setting the `X-Inference-Id` header to the value you received in the response json as `Id`, or the one you received in the response headers as `X-Inference-Id`.

Save the following file to disk as `status.py`. Notice the `X-Inference-Id` variable. Set this to your `X-Inference-Id`

```python
import requests
import sys
import os
import signal

def get_status() -> None:
    token = os.environ['DATACRUNCH_BEARER_TOKEN']
    deployment_name = os.environ['DATACRUNCH_DEPLOYMENT']
    async_task_id = os.environ['DATACRUNCH_TASK_ID']
    baseurl = "https://containers.datacrunch.io"
    result_url = f"{baseurl}/status/{deployment_name}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Inference-Id": async_task_id
    }

    response = requests.get(result_url, headers=headers)
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"inference failed. status code: {response.status_code}")
        print(response.text, file=sys.stderr)

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)

    get_status()
```

After saving run the following, (please `DATACRUNCH_TASK_ID` with your current task id):

```bash
export DATACRUNCH_TASK_ID=<uuid>
python status.py
```

This script will output following:

```json
{
    "Id": "be248e6b-66e6-41f1-8bcb-b26548dace0a",
    "Error": null,
    "Status": 2
}
```

Where `Id` is again the identifier. `Error` will have an error where you'll find an error text if the inference resulted in an error and `Status` is one of the following:

`0` means inference has been initialized,`1` inference request has been sent to the queue,`2` inference request has been received from queue and delivered to the actual workload container,`3` the workload has completed and result is ready for fetching

If your status is not yet `3`, it means the workload is still in progress. Wait for a short period and run the `python status.py` again, untill you recive a status of `3`, as follows:

```json
{
    "Id": "be248e6b-66e6-41f1-8bcb-b26548dace0a",
    "Error": null,
    "Status": 3
}
```

Now our inference has completed and we are ready to fetch the results. Save the following file to the disk as `result.py`\
Again, notice that you need to set the identifier header:

```python
import requests
import sys
import os
import signal

def get_result() -> None:
    token = os.environ['DATACRUNCH_BEARER_TOKEN']
    deployment_name = os.environ['DATACRUNCH_DEPLOYMENT']
    async_task_id = os.environ['DATACRUNCH_TASK_ID']
    baseurl = "https://containers.datacrunch.io"
    status_url = f"{baseurl}/result/{deployment_name}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Inference-Id": async_task_id
    }

    response = requests.get(status_url, headers=headers)
    if response.status_code == 202:
        print(response.json())
    else:
        print(f"inference failed. status code: {response.status_code}")
        print(response.text, file=sys.stderr)

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)

    get_result()
```

This will return you text generated by whisper. It will look similar to the following:

```json
{ 
    "result":"The Voyagers were guaranteed to work only until the Saturn encounter..."
}
```

This concludes the first part of our tutorial on how to run asynchronous inference requests.

#### Upload the generated result to a webhook

In the tutorial above we sent fully asynchronous inference request, where access to the inference status and result are provided by Verda and we access them directly using our api.\
However, there might a scenario where you want your container to do asynchronous work, but you want to send synchronous requests to the container or you just don't want to save the status and result to Verda systems.

The next example shows how to use utilize partially asynchronous workflow where we send a synchronous request to the inference container which will trigger an asynchronous operation that will upload the results of the inference to a webhook while returning a status indicator that the operation has started.

In our example of a inference service above (the `main.py` file we saved earlier), you'll find a function that looks like `async def generate_webhook(body: Dict, background_tasks: BackgroundTasks) -> JSONResponse:`

Save the following file to disk as `inference_webhook.sh`

```bash
#!/bin/bash
if [ -z "$DATACRUNCH_DEPLOYMENT" ] || [ -z "$DATACRUNCH_BEARER_TOKEN" ]; then
  echo "Error: DATACRUNCH_DEPLOYMENT and DATACRUNCH_BEARER_TOKEN environment variables must be set"
  exit 1
fi

PAYLOAD='{
  "url": "https://tile.loc.gov/storage-services/media/ls/sagan/1958124-3-1.mp3"
}'

ENDPOINT=https://containers.datacrunch.io/$DATACRUNCH_DEPLOYMENT/generate_webhook
echo "Connecting to the generate_webhook endpoint at $ENDPOINT..."

curl -v -X POST $ENDPOINT \
--header "Authorization: Bearer $DATACRUNCH_BEARER_TOKEN" \
--header "Content-Type: application/json" \
--header "Prefer: respond-async-container" \
--data "$PAYLOAD"
```

Running the above command should return the following once the request has been received by your endpoint:

```json
{"status":"accepted"}
```

The model output should then be available for your webhook endpoint after completion.
