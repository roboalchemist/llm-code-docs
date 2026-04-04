# Source: https://docs.runpod.io/hub/public-endpoints.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.runpod.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Test and deploy production-ready AI models using Public Endpoints.

<Frame alt="Public Endpoints homepage">
  <img src="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoints-home.png?fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=dc2a33005fbc8bbda9b699b2fcac03d1" data-og-width="1641" width="1641" data-og-height="1313" height="1313" data-path="images/public-endpoints-home.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoints-home.png?w=280&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=a2f5b37255f8b477519c91b1e1d44518 280w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoints-home.png?w=560&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=032ee9f902e65bc7a9980866890d0711 560w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoints-home.png?w=840&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=deb96272c8f66b96f78ae1eb64a48acf 840w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoints-home.png?w=1100&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=b9fe16f1447d09babc5292e51a993ff9 1100w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoints-home.png?w=1650&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=d5f18a2b51028c16aae7f4da422694d7 1650w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoints-home.png?w=2500&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=fb6677bedfe524504c4d9e5c235ac6c0 2500w" />
</Frame>

Runpod Public Endpoints provide instant access to state-of-the-art AI models through simple API calls, with an API playground available through the [Runpod Hub](/hub/overview).

<Tip>
  Public Endpoints are pre-deployed models hosted by Runpod. If you want to deploy your own AI/ML APIs, use [Runpod Serverless](/serverless/overview).
</Tip>

## Available models

For a list of available models and model-specific parameters, see the [Public Endpoint model reference](/hub/public-endpoint-reference).

## Public Endpoint playground

<Frame alt="Public Endpoint playground">
  <img src="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-playground.png?fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=dbc247403aadc7ed52f4c922cacf4a0d" data-og-width="1626" width="1626" data-og-height="1287" height="1287" data-path="images/public-endpoint-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-playground.png?w=280&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=80853a7c5f981544502926f8ba64437b 280w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-playground.png?w=560&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=beeab6eda5dd86c2f9ea0f4780fb54c4 560w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-playground.png?w=840&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=8917b5b5245e8b09add2d4dfa797f0b8 840w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-playground.png?w=1100&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=b5a1568ea025cb0bc219a20786caa76b 1100w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-playground.png?w=1650&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=9986c3e89672b994c4aff825af0f7e0e 1650w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-playground.png?w=2500&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=0d54072ed48ba3bb7a99c7412bfd48ec 2500w" />
</Frame>

The Public Endpoint playground provides a streamlined way to discover and experiment with AI models.

The playground offers:

* **Interactive parameter adjustment**: Modify prompts, dimensions, and model settings in real-time.
* **Instant preview**: Generate images directly in the browser.
* **Cost estimation**: See estimated costs before running generation.
* **API code generation**: Create working code examples for your applications.

### Access the playground

1. Navigate to the [Runpod Hub](https://www.runpod.io/console/hub) in the console.
2. Select the **Public Endpoints** section.
3. Browse the [available models](#available-models) and select one that fits your needs.

### Test a model

To test a model in the playground:

1. Select a model from the [Runpod Hub](https://www.console.runpod.io/hub).
2. Under **Input**, enter a prompt in the text box.
3. Enter a negative prompt if needed. Negative prompts tell the model what to exclude from the output.
4. Under **Additional settings**, you can adjust the seed, aspect ratio, number of inference steps, guidance scale, and output format.
5. Click **Run** to start generating.

Under **Result**, you can use the dropdown menu to show either a preview of the output, or the raw JSON.

### Create a code example

<Frame alt="Public Endpoint code example">
  <img src="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-api-playground.png?fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=b70b00d2e1aeeff198884712b9e108ed" data-og-width="1904" width="1904" data-og-height="858" height="858" data-path="images/public-endpoint-api-playground.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-api-playground.png?w=280&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=dbfeb8ef4872d5c09f2b241ca786c3dd 280w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-api-playground.png?w=560&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=c411a09ed1d68534c60af834ed585b8c 560w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-api-playground.png?w=840&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=0bb5bea40916848ed17aa11f85b28f8e 840w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-api-playground.png?w=1100&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=017308bed7172dd40506ad5cee469d10 1100w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-api-playground.png?w=1650&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=bd9bd4e754a6cebd2d1e662e896427e9 1650w, https://mintcdn.com/runpod-b18f5ded/_BeZqveqZvW4ISvJ/images/public-endpoint-api-playground.png?w=2500&fit=max&auto=format&n=_BeZqveqZvW4ISvJ&q=85&s=bee38ff1a81ec815ed02ae6be637c88b 2500w" />
</Frame>

After inputting parameters using the playground, you can automatically generate an API request to use in your application.

1. Click **API Playground** (above the **Prompt** field).
2. Using the dropdown menu, select the programming language (Python, JavaScript, cURL, etc.) and POST command you want to use (`/run` or `/runsync`).
3. Click the **Copy** icon to copy the code to your clipboard.

## Make API requests to Public Endpoints

You can make API requests to Public Endpoints using any HTTP client. The endpoint URL is specific to the model you want to use.

All requests require authentication using your Runpod API key, passed in the `Authorization` header. You can find and create [API keys](/get-started/api-keys) in the [Runpod console](https://www.runpod.io/console/user/settings) under **Settings > API Keys**.

<Tip>
  To learn more about the difference between synchronous and asynchronous requests, see [Endpoint operations](/serverless/endpoints/operations).
</Tip>

### Synchronous request example

Here's an example of a synchronous request to Flux Dev using the `/runsync` endpoint:

```bash curl theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "https://api.runpod.ai/v2/black-forest-labs-flux-1-dev/runsync" \
  -H "Authorization: Bearer RUNPOD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "prompt": "A serene mountain landscape at sunset",
      "width": 1024,
      "height": 1024,
      "num_inference_steps": 20,
      "guidance": 7.5
    }
  }'
```

### Asynchronous request example

Here's an example of an asynchronous request to Flux Dev using the `/run` endpoint:

```bash curl theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "https://api.runpod.ai/v2/black-forest-labs-flux-1-dev/run" \
  -H "Authorization: Bearer RUNPOD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "prompt": "A futuristic cityscape with flying cars",
      "width": 1024,
      "height": 1024,
      "num_inference_steps": 50,
      "guidance": 8.0
    }
  }'
```

You can check the status and retrieve results using the `/status` endpoint, replacing `{job-id}` with the job ID returned from the `/run` request:

```bash curl theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X GET "https://api.runpod.ai/v2/black-forest-labs-flux-1-dev/status/{job-id}" \
  -H "Authorization: Bearer RUNPOD_API_KEY"
```

### Response format

All endpoints return a consistent JSON response format:

```json  theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "delayTime": 17,
  "executionTime": 3986,
  "id": "sync-0965434e-ff63-4a1c-a9f9-5b705f66e176-u2",
  "output": {
    "cost": 0.02097152,
    "image_url": "https://image.runpod.ai/6/6/mCwUZlep6S/453ad7b7-67c6-43a1-8348-3ad3428ef97a.png"
  },
  "status": "COMPLETED",
  "workerId": "oqk7ao1uomckye"
}
```

<Warning>
  Output URLs (`image_url`, `video_url`, and `audio_url`) expire after 7 days. Download and store your generated files immediately if you need to keep them longer.
</Warning>

## Python example

Here is an example Python API request to Flux Dev using the `/run` endpoint:

```python  theme={"theme":{"light":"github-light","dark":"github-dark"}}
import requests

headers = {"Content-Type": "application/json", "Authorization": "Bearer RUNPOD_API_KEY"}

data = {
    "input": {
        "prompt": "A serene mountain landscape at sunset",
        "image_format": "png",
        "num_inference_steps": 25,
        "guidance": 7,
        "seed": 50,
        "width": 1024,
        "height": 1024,
    }
}

response = requests.post(
    "https://api.runpod.ai/v2/black-forest-labs-flux-1-dev/run",
    headers=headers,
    json=data,
)
```

You can generate Public Endpoints API requests for Python and other programming languages using the [Public Endpoints playground](#public-endpoints-playground).

## JavaScript/TypeScript integration with Vercel AI SDK

For JavaScript and TypeScript projects, you can use the `@runpod/ai-sdk-provider` package to integrate Runpod's Public Endpoints with the [Vercel AI SDK](https://ai-sdk.dev/docs/introduction).

Run this command to install the package:

```bash  theme={"theme":{"light":"github-light","dark":"github-dark"}}
npm install @runpod/ai-sdk-provider ai
```

To call a Public Endpoint for text generation:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { runpod } from '@runpod/ai-sdk-provider';
import { generateText } from 'ai';

const { text } = await generateText({
  model: runpod('qwen3-32b-awq'),
  prompt: 'Write a Python function that sorts a list:',
});
```

For image generation:

```typescript  theme={"theme":{"light":"github-light","dark":"github-dark"}}
import { runpod } from '@runpod/ai-sdk-provider';
import { experimental_generateImage as generateImage } from 'ai';

const { image } = await generateImage({
  model: runpod.imageModel('flux/flux-dev'),
  prompt: 'A serene mountain landscape at sunset',
  aspectRatio: '4:3',
});
```

For comprehensive documentation and examples, see the [Node package documentation](https://www.npmjs.com/package/@runpod/ai-sdk-provider).

## Pricing

Public Endpoints use transparent, usage-based pricing. For example:

| Model            | Price    | Billing unit                             |
| ---------------- | -------- | ---------------------------------------- |
| Flux Dev         | \$0.02   | Per megapixel                            |
| Flux Schnell     | \$0.0024 | Per megapixel                            |
| WAN 2.5          | \$0.5    | Per 5 seconds of video                   |
| Whisper V3 Large | \$0.05   | Per 1000 characters of audio transcribed |
| Qwen3 32B AWQ    | \$0.01   | Per 1000 tokens of text generated        |

<Note>
  Pricing is calculated based on the actual output resolution. You will not be charged for failed generations.
</Note>

Here are some pricing examples that demonstrate how you can estimate costs for image generation:

* 512×512 image (0.25 megapixels)
  * Flux Dev: (512 \* 512 / 1,000,000) \* \$0.02 = \$0.00524288
  * Flux Schnell: (512 \* 512 / 1,000,000) \* \$0.0024 = \$0.0006291456
* 1024×1024 image (1 megapixel)
  * Flux Dev: (1024 \* 1024 / 1,000,000) \* \$0.02 = \$0.02097152
  * Flux Schnell: (1024 \* 1024 / 1,000,000) \* \$0.0024 = \$0.0025165824

<Note>
  Runpod's billing system rounds up after the first 10 decimal places.
</Note>

For complete pricing information for each model, see the [Public Endpoint model reference](/hub/public-endpoint-reference) page.

## Best practices

When working with Public Endpoints, following best practices will help you achieve better results and optimize performance.

### Prompt engineering

For prompt engineering, be specific with detailed prompts as they generally produce better results. Include style modifiers such as art styles, camera angles, or lighting conditions. For Flux Dev, use negative prompts to exclude unwanted elements from your images.

A good prompt example would be: "A professional portrait of a woman in business attire, studio lighting, high quality, detailed, corporate headshot style."

### Performance optimization

For performance optimization, choose the right model for your needs. Use Flux Schnell when you need speed, and Flux Dev when you need higher quality. Standard dimensions like 1024×1024 render fastest, so stick to these unless you need specific aspect ratios. For multiple images, use asynchronous endpoints to batch your requests. Consider caching results by storing generated images to avoid regenerating identical prompts.
