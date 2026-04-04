# Source: https://docs.verda.com/containers/tutorials/migrate-from-runpod.md

# Quick: Migrate from Runpod

In this tutorial, we will migrate a container that runs in Runpod to our serverless containers platform.

## Get an access token

This example depends on the model weights being fetched from Hugging Face.

In this tutorial we are loading `meta-llama/Meta-Llama-3.1-8B-Instruct` [model from Hugging Face](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct).

{% hint style="success" %}
Some models on Hugging Face require the user to accept their usage policy, so please verify this for any model you are deploying. If you have not Agreed to the policy previously, you will see a similar dialog on the model page on Hugging Face:
{% endhint %}

You will also require the `User Access Token` in order to fetch the weights. You can obtain the Access Token in your [Hugging Face account](https://huggingface.co/) by clicking the Profile icon (top right corner) and selecting **Access Tokens**.

For deploying the endpoint, the `READ` permissions are sufficient.

{% hint style="success" %}
Please store the obtained token safely. You will need it for the next steps!
{% endhint %}

## Build and push the container

We have a simple LLM model running Llama on Runpod's platform.

```python
import os
import transformers
import torch
import runpod

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
    token=os.environ.get("HF_TOKEN", ""),
)


def run_llama(event):
    input = event['input']
    
    prompt = input.get('prompt')
    
    print(f"Prompt: {prompt}")

    messages = [
        {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
        {"role": "user", "content": prompt},
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=256,
    )

    print(outputs[0]["generated_text"][-1])
    return outputs[0]["generated_text"][-1]

if __name__ == '__main__':
    runpod.serverless.start({"handler": run_llama})
```

We will modify the code to run on Verda's serverless containers platform. Simply put, we remove runpod's scaffolding and have the container serve an API to be used by the platform. For this, we use 2 common Python projects, FastAPI framework and the Uvicorn server.

```python
import os
import transformers
import torch
import uvicorn
import fastapi

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
    token=os.environ.get("HF_TOKEN", ""),
)

def run_llama(event):
    input = event['input']
    
    prompt = input.get('prompt')
    
    print(f"Prompt: {prompt}")

    messages = [
        {"role": "system", "content": "You are a pirate chatbot who always responds in pirate speak!"},
        {"role": "user", "content": prompt},
    ]

    outputs = pipeline(
        messages,
        max_new_tokens=256,
    )

    print(outputs[0]["generated_text"][-1])
    return outputs[0]["generated_text"][-1]

def create_app():
    app = fastapi.FastAPI()

    @app.get("/health")
    async def health_check():
        return {"status": "ok"}

    @app.post("/query")
    async def llama_endpoint(request: fastapi.Request):
        event = await request.json()
        result = run_llama(event)
        return {"result": result}

    return app

if __name__ == '__main__':
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
```

You should be able to run the application locally with just `python your_app.py` assuming the dependencies have been installed. To run it in the platform, it needs to be packaged into a container and made available. We will do this next.

The Dockerfile you have used to package your application for Runpod's platform should work nicely, just remember to change the runpod package into uvicorn and fastapi. You can also use the example file to package it.

```docker
FROM python:3.12-slim

WORKDIR /

RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
RUN pip install --no-cache-dir fastapi uvicorn transformers accelerate

COPY llama.py /

CMD ["python3", "-u", "llama.py"]
```

The choice to include the weights depends on your needs. Adding them makes the container image considerably larger (around 26Gb in this example), but the application will also start faster as it doesn't need to download them on every startup. If you want to scale your application to zero and want to have it start up faster when the image has already been downloaded (which also takes time), you might want to include them, but if your workload is more stable, or you want it to run constantly, it might be better to leave them out.

Once done, build your application into a container (`docker build -t username/your-app:v1`) and push it to your registry (`docker push username/your-app:v1`). You are now ready to create a new serverless container deployment!

## Create a deployment

1. Log in to the [Verda cloud console](https://console.verda.com/signin), and go to **Containers -> New deployment.** Name your deployment and select the Compute Type.
2. Add your registry credentials and type in your container's name, `username/your-app:v1` for example.
3. Set the exposed HTTP port to what you have in your application. Our example listens on port `8000`, which is the default.
4. Set the healthcheck path correctly. The example uses the default, `/health` path.
5. Add your Hugging Face User Access Token to **Environment Variables** as `HF_TOKEN`. Also add your shared disk location as `HF_HOME` so containers don't need to re-download model weights after the first time. If your general storage mount path is /data *(default value)*, the value for HF\_HOME could be `/data/.huggingface`, and this should be available by default.
6. Deploy your container and start using it!

{% hint style="warning" %}
For production use, we recommend authenticating/using private registries to avoid potential rate limits imposed by public container registries.
{% endhint %}

## Connect to the Endpoint

Before you can connect to the endpoint, you will need to generate an authentication token, by going to **Keys -> Inference API Keys**, and click **Create.**

The **base endpoint URL** for your deployment is in the **Containers API** section in the top left of the screen.

### Test Request

Your containers API url should be visible in the deployment details page. Below is an example cURL command for running your test request:

```bash
curl -X POST <YOUR_CONTAINERS_API_URL>/query \
--header 'Authorization: Bearer <YOUR_INFERENCE_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
  "input": {
    "prompt": "Who are you?"
  }
}'
```

### Example Response

You should see a response that looks like this:

{% code overflow="wrap" fullWidth="false" %}

```json
{
  "result": {
    "role": "assistant",
    "content": "Arrr, ye landlubber! Yer askin' who be me, eh? Well, matey, I be a swashbucklin' pirate chatbot, here to bring ye treasure o' knowledge and swashbucklin' fun! Me name be Captain Chat, and I be here to chart ye through the seven seas o' information, answerin' yer questions and tellin' tales o' adventure! So hoist the sails and set course fer a pirate-tastic conversation, me hearty!"
  }
}
```

{% endcode %}

Feel free to try our different amount of minimum and maximum replicas to best serve your request amounts. They can be easily adjusted in the Replicas section. We will charge for running replicas so make sure that your minimum amount has enough traffic. If there are more requests than what your containers can handle, we'll scale it up to your maximum amount to serve the increased traffic, and scale down when things settle.
