# Source: https://docs.vast.ai/documentation/serverless/overview.md

> ## Documentation Index
>>
> Fetch the complete documentation index at: https://docs.vast.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# The PyWorker

> Learn about the Vast PyWorker and how it integrates with model instances.

<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
__html: JSON.stringify({
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "Vast.ai PyWorker Overview",
  "description": "Understanding the Vast PyWorker Python web server for serverless compatibility, including integration with model instances and communication with the serverless system.",
  "author": {
    "@type": "Organization",
    "name": "Vast.ai"
  },
  "articleSection": "Serverless Documentation",
  "keywords": ["PyWorker", "serverless", "Python", "web server", "model integration", "vast.ai", "custom backend"]
})
}}
/>

The Vast PyWorker is a Python web server designed to run alongside a machine learning model instance, providing serverless compatibility. It serves as the primary entry point for API requests, forwarding them to the model’s API hosted on the same instance. Additionally, it monitors performance metrics and estimates current workload, reporting these metrics to the serverless system.

<Note>
  All of Vast’s serverless templates use the Vast PyWorker. If you are using a recommended serverless template from Vast, the PyWorker is already integrated with the template and will automatically startup when a Workergroup is created.&#x20;
</Note>

<img src="https://mintcdn.com/vastai-80aa3a82/Wp3R6uoNeIDZvzDI/images/serverless-pyworker.webp?fit=max&auto=format&n=Wp3R6uoNeIDZvzDI&q=85&s=c72a382427d134cc0d7040d3264a2eda" alt="Pyworker Diagram" data-og-width="1254" width="1254" data-og-height="819" height="819" data-path="images/serverless-pyworker.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/Wp3R6uoNeIDZvzDI/images/serverless-pyworker.webp?w=280&fit=max&auto=format&n=Wp3R6uoNeIDZvzDI&q=85&s=affc610bc9da4d67bfb16275b0bc3e51 280w, https://mintcdn.com/vastai-80aa3a82/Wp3R6uoNeIDZvzDI/images/serverless-pyworker.webp?w=560&fit=max&auto=format&n=Wp3R6uoNeIDZvzDI&q=85&s=26446ff0a801b94e1d135ebf2d14dcc6 560w, https://mintcdn.com/vastai-80aa3a82/Wp3R6uoNeIDZvzDI/images/serverless-pyworker.webp?w=840&fit=max&auto=format&n=Wp3R6uoNeIDZvzDI&q=85&s=af2c9f2ba408fe01b023c0a6a22e2f93 840w, https://mintcdn.com/vastai-80aa3a82/Wp3R6uoNeIDZvzDI/images/serverless-pyworker.webp?w=1100&fit=max&auto=format&n=Wp3R6uoNeIDZvzDI&q=85&s=fd8f8e1eee822dd50ea959fd5a9d8d7b 1100w, https://mintcdn.com/vastai-80aa3a82/Wp3R6uoNeIDZvzDI/images/serverless-pyworker.webp?w=1650&fit=max&auto=format&n=Wp3R6uoNeIDZvzDI&q=85&s=ed1e64ac9cb0631836abed52d09ba4fd 1650w, https://mintcdn.com/vastai-80aa3a82/Wp3R6uoNeIDZvzDI/images/serverless-pyworker.webp?w=2500&fit=max&auto=format&n=Wp3R6uoNeIDZvzDI&q=85&s=293321da88543ed0d9543dee61f302e7 2500w" />

In the diagram's example, a user's client is attempting to infer from a machine learning model. With Vast's Serverless setup, the client:

1. Sends a `/route/` POST request to the serverless engine. This asks the system for a GPU instance to send the inference request.
2. The serverless system selects a ready and available worker instance from the user's endpoint and replies with a JSON object containing the URL of the selected instance.
3. The client then constructs a new POST request with it's payload, authentication data, and the URL of the worker instance. This is sent to the worker.
4. The PyWorker running on that specific instance validates the request and extracts the payload. It then sends the payload to the model inference server, which runs on the same instance as the PyWorker.
5. The model generates it's output and returns the result to the PyWorker.
6. The PyWorker formats the model's response as needed, and sends the response back to the client.&#x20;
7. Independently and concurrently, the PyWorker periodically sends it's operational metrics to the serverless system, which is used to make scaling decisions.

The [Vast PyWorker repository](https://github.com/vast-ai/pyworker/) gives examples that are useful for learning how to create a custom PyWorker for your custom template and integrate with Vast’s Serverless system. Even with a custom PyWorker, the PyWorker code runs on your Vast instance, and we automate its installation and activation during instance creation. The graphic below shows how the files and entities for the Serverless system are organized.

<img src="https://mintcdn.com/vastai-80aa3a82/_4z8utTktrZmQOU6/images/serverless-pyworker-2.webp?fit=max&auto=format&n=_4z8utTktrZmQOU6&q=85&s=869303362e8072da8a86d83f1873290e" alt="" data-og-width="800" width="800" data-og-height="286" height="286" data-path="images/serverless-pyworker-2.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/vastai-80aa3a82/_4z8utTktrZmQOU6/images/serverless-pyworker-2.webp?w=280&fit=max&auto=format&n=_4z8utTktrZmQOU6&q=85&s=a545883f8697bc6b8fcb64802ef3aa3b 280w, https://mintcdn.com/vastai-80aa3a82/_4z8utTktrZmQOU6/images/serverless-pyworker-2.webp?w=560&fit=max&auto=format&n=_4z8utTktrZmQOU6&q=85&s=86116e519dc7391082ef9c13b624f542 560w, https://mintcdn.com/vastai-80aa3a82/_4z8utTktrZmQOU6/images/serverless-pyworker-2.webp?w=840&fit=max&auto=format&n=_4z8utTktrZmQOU6&q=85&s=1145536e0895620a01f18ddf97f0d03a 840w, https://mintcdn.com/vastai-80aa3a82/_4z8utTktrZmQOU6/images/serverless-pyworker-2.webp?w=1100&fit=max&auto=format&n=_4z8utTktrZmQOU6&q=85&s=f22c53a387af6abb48e1d40e065313b2 1100w, https://mintcdn.com/vastai-80aa3a82/_4z8utTktrZmQOU6/images/serverless-pyworker-2.webp?w=1650&fit=max&auto=format&n=_4z8utTktrZmQOU6&q=85&s=4d88f79cdd33348f20d32c16ffe75ec4 1650w, https://mintcdn.com/vastai-80aa3a82/_4z8utTktrZmQOU6/images/serverless-pyworker-2.webp?w=2500&fit=max&auto=format&n=_4z8utTktrZmQOU6&q=85&s=3248be1e9b8309d488303f9917ca064a 2500w" />

## Integration with Model Instance

The Vast PyWorker wraps the backend code of the model instance you are running. The PyWorker calls the appropriate backend function when the PyWorker's corresponding API endpoint is invoked. For example, if you are running a text generation inference (TGI) server, your PyWorker might receive the following JSON body from a `/generate` endpoint:&#x20;

```json JSON icon="js" theme={null}
{
  "auth_data": {
    "signature": "a_base64_encoded_signature_string_from_route_endpoint",
    "cost": 256,
    "endpoint": "Your-TGI-Endpoint-Name",
    "reqnum": 1234567890,
    "url": "http://worker-ip-address:port",
    "request_idx": 10203040
  },
  "payload": {
    "inputs": "What is the answer to the universe?",
    "parameters": {
      "max_new_tokens": 256,
      "temperature": 0.7,
      "top_p": 0.9,
      "do_sample": true
    }
  }
}
```

When it receives this request, your PyWorker will internally send the following to the TGI model sever:

```json JSON icon="js" theme={null}
{
  "inputs": "What is the answer to the universe?",
  "parameters": {
    "max_new_tokens": 256,
    "temperature": 0.7,
    "top_p": 0.9,
    "do_sample": true
  }
}
```

Your PyWorker would similarily receive the output result from the TGI server, and forward a formatted version to the client.
