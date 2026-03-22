# Source: https://docs.verda.com/containers/tutorials/deploy-with-vllm-indepth.md

# In-Depth: Deploy with vLLM

In this tutorial, we will deploy a [vLLM](https://docs.vllm.ai/) endpoint hosting `deepseek-ai/deepseek-llm-7b-chat` large language model. [vLLM](https://docs.vllm.ai/) is one of the leading libraries for large language model inference, supporting [many architectures](https://docs.vllm.ai/en/v0.6.2/models/supported_models.html) and models that use them.

You can find more information about the model itself from the [Hugging Face model hub](https://huggingface.co/deepseek-ai/deepseek-llm-7b-chat).

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

For this example you need a Python environment running on your local machine, a Hugging Face account to create a Hugging Face token that is used to fetch the model weights and Verda cloud account to create a deployment.

## Model Weights

[vLLM](https://docs.vllm.ai/) deployment fetches the model weights from Hugging Face.

In this tutorial we are loading `deepseek-ai/deepseek-llm-7b-chat` model.

{% hint style="success" %}
Some models on Hugging Face require the user to accept their usage policy, so please verify this for any model you are deploying. If you have not Agreed to the policy previously, you will see a similar dialog on the model page on Hugging Face:
{% endhint %}

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-f5a78402c73a93733b511a8e00623b69e0a754c7%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

You will also require the `User Access Token` in order to fetch the weights. You can obtain the Access Token in your [Hugging Face account](https://huggingface.co/) by clicking the Profile icon (top right corner) and selecting **Access Tokens**.

For deploying the [vLLM](https://docs.vllm.ai/) endpoint, the `READ` permissions are sufficient.

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-70227745b8094b8861c8ab8ff8bb1f6de18acbcd%2Fimage.png?alt=media" alt=""><figcaption><p>Hugging Face Access Tokens panel</p></figcaption></figure>

{% hint style="success" %}
Please store the obtained token safely. You will need it for the next steps!
{% endhint %}

## Create the deployment

In this example, we will deploy `deepseek-ai/deepseek-llm-7b-chat` on a General Compute (24 GB VRAM) GPU type. For larger models, you may need to choose one of the other GPU types we offer.

1. Log in to the [Verda cloud console](https://console.verda.com/signin)
2. Create a new project or use existing one, open the project
3. On the left you'll see a navigation menu. Go to **Containers -> New deployment.** Name your deployment and select the Compute Type.
4. We will be using the official [vLLM Docker image](https://hub.docker.com/r/vllm/vllm-openai), set **Container Image** to `docker.io/vllm/vllm-openai:v0.7.1` You can select another version from the list if you prefer, or leave the version out of the url given and select the one that you wish to use. For this example we use `v0.7.1`.
5. Toggle on the **Public** location for your image. You can use the **Private** if you have a private registry, paired with credentials. For this example we use the public registry.
6. Make sure your preferred tag is selected
7. Set the Exposed HTTP port to `8000`
8. Set the Healthcheck port to `8000`
9. Set the Healthcheck path to `/health`
10. Toggle **Start Command** on
11. Add the following parameters to **CMD**: `--model deepseek-ai/deepseek-llm-7b-chat --gpu-memory-utilization 0.9 --model-loader-extra-config '{"enable_multithread_load": true}'` . If you're using the standard image and the model you're using has safetensor weights (deepseek does not), you also have support for a faster RunAI's Model Streamer, and you can enable it with `--load-format runai_streamer` instead of the `--model-loader-extra-config` option.
12. Add your Hugging Face User Access Token to the **Environment Variables** as `HF_TOKEN`. Note that in some examples you might see `HUGGING_FACE_HUB_TOKEN` environment variable used. The `HF_TOKEN` is the new name for the environment variable. The old name `HUGGING_FACE_HUB_TOKEN` is still supported, but going forwards we recommend using the new name.
13. **Deploy container**

(You can leave the **Scaling** options to their default values, however if you wish to enable LLM batching, you can set the **Concurrent requests per replica** option to a value greater than 1. This number represents the number of concurrent requests the deployment accepts)

That's it! You have now created a deployment. You can check the logs of the deployment from the logs tab. When the deployment starts it'll download the model weights from Hugging Face and start the [vLLM](https://docs.vllm.ai/) server. This will take few minutes to complete.

{% hint style="warning" %}
For production use, we recommend authenticating/using private registries to avoid potential rate limits imposed by public container registries.
{% endhint %}

## Accessing the deployment

Before you can connect to the endpoint, you will need to generate an authentication token, by going to **Keys -> Inference API Keys**, and click **Create.**

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2Fgit-blob-ebbcbcae10353563f31b1e9dcc54c324fda49dbd%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

The **base endpoint URL** for your deployment is in the **Containers API** section in the top left of the screen. This will be in the form of: `https://containers.datacrunch.io/<NAME-OF-OUR-DEPLOYMENT>/`

### Test Deployment

Once the deployment has been created and is ready to accept requests, you can test that it responds correctly by sending a `List Models` request to the endpoint.

[vLLM](https://docs.vllm.ai/) can be deployed as a server that implements the [OpenAI API protocol](https://platform.openai.com/docs/api-reference/introduction). This allows [vLLM](https://docs.vllm.ai/) to be used as a drop-in replacement for applications using OpenAI API. More information about [vLLM](https://docs.vllm.ai/) in general and available endpoints can be found in the [official documentation of vLLM](https://docs.vllm.ai/)

Below is an example cURL command for running your test deployment:

{% hint style="info" %}
Notice the added subpath `/v1/models` to the base endpoint URL
{% endhint %}

```bash
#!/bin/bash
curl -X GET <YOUR_CONTAINERS_API_URL>/v1/models \
--header 'Authorization: Bearer <YOUR_INFERENCE_API_KEY>' \
--header 'Content-Type: application/json'
```

This should return a response that shows `deepseek-ai/deepseek-llm-7b-chat` model is available for use.

```json
{
  "object": "list",
  "data": [
    {
      "id": "deepseek-ai/deepseek-llm-7b-chat",
      "object": "model",
      "created": 1737380356,
      "owned_by": "vllm",
      "root": "deepseek-ai/deepseek-llm-7b-chat",
      "parent": null,
      "max_model_len": 8192,
      "permission": [
        {
          "id": "modelperm-e3d0f87e19a548b2be64ca274a4550a6",
          "object": "model_permission",
          "created": 1737380356,
          "allow_create_engine": false,
          "allow_sampling": true,
          "allow_logprobs": true,
          "allow_search_indices": false,
          "allow_view": true,
          "allow_fine_tuning": false,
          "organization": "*",
          "group": null,
          "is_blocking": false
        }
      ]
    }
  ]
}
```

## Sending inference requests

As the `List Models` request show us `deepseek-ai/deepseek-llm-7b-chat`, we are ready to send an inference requests to the model.

### Completions API

Completions API `/v1/completions` offers a quick way to get completions for a given prompt.

#### Synchronous request

Below is a Python script that calls the completions endpoint `/v1/completions` with a prompt and returns the completion. Save it to a file named `test_request.py` and run it with `python test_request.py`. Remember to replace `<YOUR_CONTAINERS_API_URL>` and `<YOUR_INFERENCE_API_KEY>` with the values from your deployment.

```python
import requests
import sys
import signal

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

def do_test_request() -> None:
    url = '<YOUR_CONTAINERS_API_URL>/v1/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <YOUR_INFERENCE_API_KEY>',
    }

    data = {
        "model": "deepseek-ai/deepseek-llm-7b-chat",
        "prompt": "The sun is a star. Explain to me the consept of solar wind.",
        "max_tokens": 128,
        "temperature": 0.7,
        "top_p": 0.9
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        try:
            print(response.json())
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

This returns a synchronous response with the completion of the prompt:

```json
{
  "id": "cmpl-45b35fb2cb474389bb118491374c38d2",
  "object": "text_completion",
  "created": 1737382666,
  "model": "deepseek-ai/deepseek-llm-7b-chat",
  "choices": [
    {
      "index": 0,
      "text": "\n\nSolar wind is a stream of charged particles, mainly electrons and protons, that are released from the sun's corona (the outermost layer of the sun's atmosphere) and travel through space at high speeds. The solar wind is driven by the sun's magnetic field and the heat generated by the sun's fusion reactions.\n\nThe solar wind has a significant impact on the solar system. It creates a bubble-like region around the sun called the heliosphere, which protects the inner solar system from cosmic rays and other interstellar particles. It also affects the magnetic fields of planets, such as Earth, and can cause phenomena like the aurora borealis (Northern Lights).\n\nThe speed of the solar wind varies, but it typically travels at speeds of 300 to 800 kilometers per second (670,000 to 1,800,000 miles per hour). The solar wind is strongest during periods of high solar activity, such as solar flares and coronal mass ejections. During these events, the solar wind can be faster and more intense, and can have a more noticeable effect on Earth'",
      "logprobs": "None",
      "finish_reason": "length",
      "stop_reason": "None",
      "prompt_logprobs": "None"
    }
  ],
  "usage": {
    "prompt_tokens": 18,
    "total_tokens": 274,
    "completion_tokens": 256,
    "prompt_tokens_details": "None"
  }
}
```

#### Streaming request

Same example as above, but streaming out the response. Save it to a file named `test_request.py` and run it with `python test_request.py`.

```python
import requests
import sys
import signal

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

def do_test_request() -> None:
    url = '<YOUR_CONTAINERS_API_URL>/v1/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <YOUR_INFERENCE_API_KEY>',
        'Accept': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
    }

    data = {
        "model": "deepseek-ai/deepseek-llm-7b-chat",
        "prompt": "Solar wind is a curious phenomenon. Tell me more about it",
        "max_tokens": 128,
        "temperature": 0.7,
        "top_p": 0.9,
        "stream": True
    }

    try:
        with requests.post(url, headers=headers, json=data, stream=True) as response:
            if response.status_code == 200:
                print("Stream started. Receiving events...\n")
                for line in response.iter_lines(decode_unicode=True):
                    if line:
                        print(line)
            else:
                print(f"Request failed with status code {response.status_code}", file=sys.stderr)
                print("Response body:", file=sys.stderr)
                print(response.text, file=sys.stderr)
    except requests.RequestException as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)
    do_test_request()
```

## Response

This returns a streaming response with the completion of the prompt:

```text
Stream started. Receiving events...

event:response
data:{"id":"cmpl-5d21014e411647349fe55ab234290190","object":"text_completion","created":1737384350,"model":"deepseek-ai/deepseek-llm-7b-chat","choices":[{"index":0,"text":",","logprobs":null,"finish_reason":null,"stop_reason":null}],"usage":null}
event:response
data:{"id":"cmpl-5d21014e411647349fe55ab234290190","object":"text_completion","created":1737384350,"model":"deepseek-ai/deepseek-llm-7b-chat","choices":[{"index":0,"text":" we","logprobs":null,"finish_reason":null,"stop_reason":null}],"usage":null}
event:response
data:{"id":"cmpl-5d21014e411647349fe55ab234290190","object":"text_completion","created":1737384350,"model":"deepseek-ai/deepseek-llm-7b-chat","choices":[{"index":0,"text":" can","logprobs":null,"finish_reason":null,"stop_reason":null}],"usage":null}
event:response
data:{"id":"cmpl-5d21014e411647349fe55ab234290190","object":"text_completion","created":1737384350,"model":"deepseek-ai/deepseek-llm-7b-chat","choices":[{"index":0,"text":" learn","logprobs":null,"finish_reason":null,"stop_reason":null}],"usage":null}

...
```

### Chat Completions API

The chat completions API `/v1/chat/completions` is a more dynamic, interactive way to communicate with the model, allowing back-and-forth exchanges that can be stored in the chat history. Notice that the prompt format is different from the completions API.

### Synchronous request (Chat Completions)

Below is a Python script that calls the chat completions endpoint `/v1/chat/completions` with a prompt and returns the completion. Save it to a file named `test_request.py` and run it with `python test_request.py`. . Remember to replace `<YOUR_CONTAINERS_API_URL>` and `<YOUR_INFERENCE_API_KEY>` with the values from your deployment.

```python
import requests
import sys
import signal

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

def do_test_request() -> None:
    url = '<YOUR_CONTAINERS_API_URL>/v1/chat/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <YOUR_INFERENCE_API_KEY>',
    }

    data = {
        "model": "deepseek-ai/deepseek-llm-7b-chat",
        "messages":[
             {"role": "user", "content": "What is deep learning?"}
         ],
         "stream":False
    }

    try:
        with requests.post(url, headers=headers, json=data, stream=False) as response:
            print(response.json())
    except requests.RequestException as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)
    do_test_request()
```

## Response (Chat Completions)

This returns a synchronous response with the completion of the prompt:

```json
{
  "id": "chatcmpl-d656d307019e44e49079688744feea58",
  "object": "chat.completion",
  "created": 1737385723,
  "model": "deepseek-ai/deepseek-llm-7b-chat",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": " Deep learning is a subset of machine learning, a field of artificial intelligence. It's based on artificial neural networks with many layers, also known as deep neural networks. Deep learning algorithms are designed to automatically and adaptively learn patterns in data, enabling the recognition of complex patterns and abstractions.\n\nDeep learning models try to mimic the way a human brain operates, using interconnected layers of artificial neurons to process and analyze large volumes of data, often used in image recognition, speech recognition, natural language processing, and more.\n\nThe \"deeper\" the network, the more layers it has, which allows the model to learn increasingly complex representations of the data. These deeper models, however, require more computational power and larger datasets for training.\n\nDeep learning has achieved state-of-the-art results in many fields, such as image and speech recognition, recommendation systems, and game playing, among others.",
        "tool_calls": []
      },
      "logprobs": "None",
      "finish_reason": "stop",
      "stop_reason": "None"
    }
  ],
  "usage": {
    "prompt_tokens": 8,
    "total_tokens": 199,
    "completion_tokens": 191,
    "prompt_tokens_details": "None"
  },
  "prompt_logprobs": "None"
}
```

### Streaming request (Chat Completions)

Same example as above, but streaming out the response. Save it to a file named `test_request.py` and run it with `python test_request.py`.

```python
import requests
import sys
import signal

def graceful_shutdown(signum, frame) -> None:
    print(f"\nSignal {signum} received at line {frame.f_lineno} in {frame.f_code.co_filename}")
    sys.exit(0)

def do_test_request() -> None:
    url = '<YOUR_CONTAINERS_API_URL>/v1/chat/completions'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer <YOUR_INFERENCE_API_KEY>',
        'Accept': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
    }

    data = {
        "model": "deepseek-ai/deepseek-llm-7b-chat",
        "messages":[
             {"role": "user", "content": "What is deep learning?"}
        ],
        "stream":True,
        "stream_options": {
            "include_usage": True
        },
        "temperature": 0.8,
        "top_p": 0.95
    }

    try:
        with requests.post(url, headers=headers, json=data, stream=True) as response:
            if response.status_code == 200:
                print("Stream started. Receiving events...\n")
                for line in response.iter_lines(decode_unicode=True):
                    if line:
                        print(line)
            else:
                print(f"Request failed with status code {response.status_code}", file=sys.stderr)
                print("Response body:", file=sys.stderr)
                print(response.text, file=sys.stderr)
    except requests.RequestException as e:
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)
    do_test_request()
```

## Response (Chat Completions Streaming)

This returns a streaming response with the completion of the prompt.

```text
Stream started. Receiving events...

event:response
data:{"id":"chatcmpl-77eba6ba8e774764a43904cd6d7f2025","object":"chat.completion.chunk","created":1737386087,"model":"deepseek-ai/deepseek-llm-7b-chat","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}
event:response
data:{"id":"chatcmpl-77eba6ba8e774764a43904cd6d7f2025","object":"chat.completion.chunk","created":1737386087,"model":"deepseek-ai/deepseek-llm-7b-chat","choices":[{"index":0,"delta":{"content":" Deep"},"logprobs":null,"finish_reason":null}]}
event:response
data:{"id":"chatcmpl-77eba6ba8e774764a43904cd6d7f2025","object":"chat.completion.chunk","created":1737386087,"model":"deepseek-ai/deepseek-llm-7b-chat","choices":[{"index":0,"delta":{"content":" learning"},"logprobs":null,"finish_reason":null}]}

...
```

## Conclusion <a href="#conclusion" id="conclusion"></a>

This concludes our tutorial how to call the [vLLM](https://docs.vllm.ai/) endpoint with `deepseek-ai/deepseek-llm-7b-chat` model. You can now use the [vLLM](https://docs.vllm.ai/) endpoint to generate completions for your prompts.

Also check out also other [vLLM](https://docs.vllm.ai/) standard endpoints such as `/health` or `/metrics` to monitor the health of the deployment.
