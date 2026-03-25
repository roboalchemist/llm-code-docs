# Source: https://docs.verda.com/containers/tutorials/deploy-with-vllm-quick.md

# Quick: Deploy with vLLM

In this tutorial, we will deploy a vLLM endpoint in a few easy steps. [vLLM](https://docs.vllm.ai/) has become one of the leading libraries for LLM-serving and inference, supporting [many architectures](https://docs.vllm.ai/en/v0.6.2/models/supported_models.html) and models that use them.

## Model Weights

vLLM depends on the model weights being fetched from Hugging Face.

In this tutorial we are loading `deepseek-ai/deepseek-llm-7b-chat` [model from Hugging Face](https://huggingface.co/deepseek-ai/deepseek-llm-7b-chat).

{% hint style="success" %}
Some models on Hugging Face require the user to accept their usage policy, so please verify this for any model you are deploying. If you have not Agreed to the policy previously, you will see a similar dialog on the model page on Hugging Face:
{% endhint %}

You will also require the `User Access Token` in order to fetch the weights. You can obtain the Access Token in your [Hugging Face account](https://huggingface.co/) by clicking the Profile icon (top right corner) and selecting **Access Tokens**.

For deploying the vLLM endpoint, the `READ` permissions are sufficient.

{% hint style="success" %}
Please store the obtained token safely. You will need it for the next steps!
{% endhint %}

## Create the Deployment

In this tutorial, we will deploy `deepseek-ai/deepseek-llm-7b-chat` on a General Compute (24 GB VRAM) GPU type. For larger models, you may need to choose one of the other GPU types we offer.

1. Log in to the [Verda cloud console](https://console.verda.com/signin), and go to **Containers -> New deployment.** Name your deployment and select the Compute Type.
2. We will be using the official [vLLM Docker container](https://hub.docker.com/r/vllm/vllm-openai), set **Container Image** to `docker.io/vllm/vllm-openai`
3. Toggle on the **Public** location for your image
4. Select the Tag to deploy
5. Set the Exposed HTTP port to `8000`
6. Set the Healthcheck port to `8000`
7. Set the Healthcheck path to `/health`
8. Toggle **Start Command** on
9. Add the following parameters to **CMD**: `--model deepseek-ai/deepseek-llm-7b-chat --gpu-memory-utilization 0.9 --model-loader-extra-config '{"enable_multithread_load": true}'`
10. Add your Hugging Face User Access Token to the **Environment Variables** as `HF_TOKEN`
11. **Deploy container**

(You can leave the **Scaling** options to their default values.)

That's it you should now have a running deployment!

{% hint style="warning" %}
For production use, we recommend authenticating/using private registries to avoid potential rate limits imposed by public container registries.
{% endhint %}

## Connect to the Endpoint

Before you can connect to the endpoint, you will need to generate an authentication token, by going to **Keys -> Inference API Keys**, and click **Create.**

The **base endpoint URL** for your deployment is in the **Containers API** section in the top left of the screen.

### Test Request

Below is an example cURL command for running your test request:

{% hint style="info" %}
Notice the added subpath `/v1/chat/completions` to the base endpoint URL
{% endhint %}

```bash
curl -X POST <YOUR_CONTAINERS_API_URL>/v1/chat/completions \
--header 'Authorization: Bearer <YOUR_INFERENCE_API_KEY>' \
--header 'Content-Type: application/json' \
--data '{
        "model": "deepseek-ai/deepseek-llm-7b-chat",
        "messages": [
          { "role": "system", "content": "You are a helpful writer assistant." },
          { "role": "user", "content": "What is deep learning?" }
        ],
        "stream": false
    }'
```

### Example Response

You should see a response that looks like this:

{% code overflow="wrap" fullWidth="false" %}

```json
{
   "id": "chatcmpl-97e62d475c0f42d390d5a816a3219793",
   "object": "chat.completion",
   "created": 1739436716,
   "model": "deepseek-ai/deepseek-llm-7b-chat",
   "choices": [
      {
         "index": 0,
         "message": {
            "role": "assistant",
            "reasoning_content": null,
            "content": "Deep learning is a subset of machine learning that uses artificial neural networks with multiple layers toLearn about the input data itself. This is called a deep neural network. Deep learning has made significant progress in the field of artificial intelligence, especially in image and speech recognition, natural language processing, and other areas. The most widely used frameworks for deep learning are TensorFlow and Keras. In deep learning, a deep neural network is trained on large amounts of data through a supervised or unsupervised learning process.",
            "tool_calls": [
               
            ]
         },
         "logprobs": null,
         "finish_reason": "stop",
         "stop_reason": null
      }
   ],
   "usage":{
      "prompt_tokens": 21,
      "total_tokens": 120,
      "completion_tokens": 99,
      "prompt_tokens_details": null
   },
   "prompt_logprobs": null
}
```

{% endcode %}
