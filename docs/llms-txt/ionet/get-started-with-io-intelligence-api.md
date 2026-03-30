# Source: https://io.net/docs/reference/ai-models/get-started-with-io-intelligence-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with AI Models API

<iframe width="100%" src="https://www.youtube.com/embed/6kVSfjt1P8s" title="Get Started with the IO Intelligence API" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Important Note on Usage Limits

Each model within **IO Intelligence** has its own value and credit consumption rate based on its complexity, capability, and computational cost.

For **plan subscribers** (*Basic*, *Professional*, or higher tiers), all model interactions draw from a **shared usage pool**. This means you can use any model available under your plan, and your total usage will count toward a single shared credit allowance — rather than having separate limits for each model.

This shared system provides maximum flexibility, allowing you to switch between models seamlessly while staying within your daily or hourly quota.

This limit is designed to ensure fair and balanced usage for all users. If you anticipate needing a higher request limit, please consider optimizing your implementation or reach out to us for assistance.

For further details on **usage limits, full breakdown of rates, and how IO Credits are billed**, refer to the [**IO Intelligence Payments**](/guides/payment/io-intelligence-payments) page.

## Introduction

You can interact with the API using HTTP requests from any programming language or by using the official Python and Node.js libraries.

To install the official Python library, run the following command:

```
pip install openai
```

To install the official Node.js library, run this command in your Node.js project directory:

```
npm install openai
```

### Example: Using the IO Intelligence API with Python

Here’s an example of how you can use the `openai Python` library to interact with the IO Intelligence API:

<CodeGroup>
  ```python openai Python theme={null}
  import openai

  client = openai.OpenAI(
      api_key="$IOINTELLIGENCE_API_KEY",
      base_url="https://api.intelligence.io.solutions/api/v1/",
  )

  response = client.chat.completions.create(
      model="meta-llama/Llama-3.3-70B-Instruct",
      messages=[
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hi, I am doing a project using IO Intelligence."},
      ],
      temperature=0.7,
      stream=False,
      max_completion_tokens=50
  )

  print(response.choices[0].message.content)
  ```
</CodeGroup>

This snippet demonstrates how to configure the client, send a chat completion request using the `Llama-3.3-70B-Instruct` model, and retrieve a response.

## Authentication

### API keys

IO Intelligence APIs authenticate requests using API keys. You can [generate API keys from your user](https://ai.io.net/ai/api-keys) account:

<Warning>
  Always treat your API key as a secret. Do not share it or expose it in client-side code (e.g., browsers or mobile apps). Instead, store it securely in an environment variable or a key management service on your backend server.
</Warning>

Include the API key in an `Authorization` HTTP header for all API requests:

```
Authorization: Bearer \$IOINTELLIGENCE_API_KEY
```

### Example: List Available Models

Here's an example `curl` command to list all models available in IO Intelligence:

<CodeGroup>
  ```curl curl theme={null}
  curl https://api.intelligence.io.solutions/api/v1/models /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY" 
  ```
</CodeGroup>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/e3e8c7c183fa588fc355c7bd42d70b93735d2c229da84c09310b5df20e27ca3f-chatetest-1.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=3a9b26c9f2876f96c760c8fff28f82c8" alt="" data-og-width="1870" width="1870" data-og-height="1184" height="1184" data-path="images/reference/e3e8c7c183fa588fc355c7bd42d70b93735d2c229da84c09310b5df20e27ca3f-chatetest-1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/e3e8c7c183fa588fc355c7bd42d70b93735d2c229da84c09310b5df20e27ca3f-chatetest-1.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=3a69de35979aba8cdcf6d2f103f29b67 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/e3e8c7c183fa588fc355c7bd42d70b93735d2c229da84c09310b5df20e27ca3f-chatetest-1.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=d2495d46bdb0b15fe804ab6416b867d2 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/e3e8c7c183fa588fc355c7bd42d70b93735d2c229da84c09310b5df20e27ca3f-chatetest-1.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=9854c8db3a92fcdd25d55527e809288d 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/e3e8c7c183fa588fc355c7bd42d70b93735d2c229da84c09310b5df20e27ca3f-chatetest-1.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=00553bb04b4c5fd14b7dad5dac93efb5 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/e3e8c7c183fa588fc355c7bd42d70b93735d2c229da84c09310b5df20e27ca3f-chatetest-1.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=defd5c51244cbddb6c186233cf1de8ee 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/e3e8c7c183fa588fc355c7bd42d70b93735d2c229da84c09310b5df20e27ca3f-chatetest-1.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=87b095210dbd01f9ed4346cfb53c0f06 2500w" />
</Frame>

An example response is as follows:

<CodeGroup>
  ```json json theme={null}
  {
    "object": "list",
    "data": [
      {
        "id": "meta-llama/Llama-3.3-70B-Instruct",
        "object": "model",
        "created": 1736168795,
        "owned_by": "io-intelligence",
        "root": null,
        "parent": null,
        "max_model_len": null,
        "permission": [
          {
            "id": "modelperm-30ac078e67ab456a9279d53cf83155bb",
            "object": "model_permission",
            "created": 1736755239,
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
      },
      ...
    ]
  }
  ```
</CodeGroup>

## Making requests

The example below demonstrates how to make a request to the Chat Completions endpoint using `curl`. To test the API, replace `$IOINTELLIGENCE_API_KEY` with your actual API key and modify the input values as shown.

<CodeGroup>
  ```curl curl theme={null}
  curl https://api.intelligence.io.solutions/api/v1/chat/completions /
    -H "Content-Type: application/json" /
    -H "Authorization: Bearer \$IOINTELLIGENCE_API_KEY" /
    -d '{
       "model": "meta-llama/Llama-3.3-70B-Instruct",
       "messages": [{"role": "user", "content": "Say this is a test!"}],
       "reasoning_content": true,
       "temperature": 0.7
     }'
  ```
</CodeGroup>

<Frame>
    <img src="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/24379dbcfebcf3e58eb79022144a5a88a4f41a2d59df9b06c0991675ccccb86c-chatetest-2.jpg?fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=dd68c9c36b0eb33d798f6494aad77b89" alt="" data-og-width="1870" width="1870" data-og-height="1440" height="1440" data-path="images/reference/24379dbcfebcf3e58eb79022144a5a88a4f41a2d59df9b06c0991675ccccb86c-chatetest-2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/24379dbcfebcf3e58eb79022144a5a88a4f41a2d59df9b06c0991675ccccb86c-chatetest-2.jpg?w=280&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=651715619aa147ff4dd31271f574a0c2 280w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/24379dbcfebcf3e58eb79022144a5a88a4f41a2d59df9b06c0991675ccccb86c-chatetest-2.jpg?w=560&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=4cc263abf59cb57dadcce4fc455cb564 560w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/24379dbcfebcf3e58eb79022144a5a88a4f41a2d59df9b06c0991675ccccb86c-chatetest-2.jpg?w=840&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=5cffbe7b0f1b5898537082078a03d6bd 840w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/24379dbcfebcf3e58eb79022144a5a88a4f41a2d59df9b06c0991675ccccb86c-chatetest-2.jpg?w=1100&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=a441a8aed7e9aa313b5580aa3f52dd6f 1100w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/24379dbcfebcf3e58eb79022144a5a88a4f41a2d59df9b06c0991675ccccb86c-chatetest-2.jpg?w=1650&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=f89c474aa0772f1b1436dd751525432a 1650w, https://mintcdn.com/ionet-cca8037f/s2w54-m8LpJVz2ID/images/reference/24379dbcfebcf3e58eb79022144a5a88a4f41a2d59df9b06c0991675ccccb86c-chatetest-2.jpg?w=2500&fit=max&auto=format&n=s2w54-m8LpJVz2ID&q=85&s=e9a56c0591260d01bd42041e0f7ce3b7 2500w" />
</Frame>

This example queries the `meta-llama/Llama-3.3-70B-Instruct` model to generate a chat completion for the input: "*Say this is a test!*".

### Example Response

The API should return a response as follows:

<CodeGroup>
  ```json json theme={null}
  {
    "id": "01945ea6-1d9f-9d46-efbc-2608dcc78169",
    "object": "chat.completion",
    "created": 1736754732,
    "model": "meta-llama/Llama-3.3-70B-Instruct",
    "choices": [
      {
        "index": 0,
        "message": {
          "role": "assistant",
          "content": "This is a test!"
        },
        "logprobs": null,
        "finish_reason": "stop",
        "stop_reason": null
      }
    ],
    "usage": {
      "prompt_tokens": 12,
      "total_tokens": 18,
      "completion_tokens": 6,
      "prompt_tokens_details": null
    },
    "prompt_logprobs": null
  }
  ```
</CodeGroup>

### Key Details in the Response

* **finish\_reason**: Indicates why the generation stopped (e.g., "stop").
* **choices**: Contains the generated response(s). Adjust the n parameter to generate multiple response choices.
