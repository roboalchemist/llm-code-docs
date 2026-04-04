# Source: https://docs.aimlapi.com/api-references/video-models/luma-ai/luma-ai-v2.md

# Luma Ray 1.6 (Text-to-Video)

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `luma/ray-1-6`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/luma/ray-1-6" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Overview

The Luma AI Dream Machine API allows developers to generate and extend AI-generated videos based on text prompts.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

Generating a video using this model involves making two sequential API calls:

* The first one is for creating and sending a video generation task to the server (returns a generation ID). This can be either a generation from a reference image/prompt or a video extension operation that adds length to an existing video.
* The second one is for requesting the generated or extended video from the server using the generation ID received from the first endpoint. Within this API call, you can use either the standard endpoint to retrieve the generated/extended video or a special endpoint to request multiple generations at once.

Below, you can find three corresponding API schemas and examples for all endpoint calls.

</details>

## API Schemas

### Generate video

`loop` parameter controls if the generated video will be looped.

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["luma/ray-1-6"]},"prompt":{"type":"string","description":"The text description of the scene, subject, or action to generate in the video."},"aspect_ratio":{"type":"string","enum":["1:1","16:9","9:16","4:3","3:4","21:9","9:21"],"default":"16:9","description":"The aspect ratio of the generated video."},"keyframes":{"type":"object","properties":{"frame0":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","enum":["image"]},"url":{"type":"string","format":"uri"}},"required":["type","url"]},{"type":"object","properties":{"type":{"type":"string","enum":["generation"]},"id":{"type":"string","format":"uuid"}},"required":["type","id"]},{"nullable":true}]},"frame1":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","enum":["image"]},"url":{"type":"string","format":"uri"}},"required":["type","url"]},{"type":"object","properties":{"type":{"type":"string","enum":["generation"]},"id":{"type":"string","format":"uuid"}},"required":["type","id"]},{"nullable":true}]}},"description":"Keyframes for image-to-video, extend, or interpolate"},"loop":{"type":"boolean","default":false,"description":"Whether to loop the video"}},"required":["model","prompt"],"title":"luma/ray-1-6"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Fetch generation

After sending a request for video generation, this task is added to the queue. Based on the service's load, the generation can be completed in seconds or take a bit more.&#x20;

## GET /v2/generate/video/luma-ai/generation

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}}},"paths":{"/v2/generate/video/luma-ai/generation":{"get":{"operationId":"LumaAiControllerV2_fetchGeneration_v2","parameters":[{"name":"generation_id","required":true,"in":"query","schema":{"type":"string"}},{"name":"state","required":false,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"description":""}},"tags":["Luma AI"]}}}}
```

### Example: Fetch Single Generation

For example, if you are waiting for video dreaming (when the video is popped from the queue and generation is in processing), then you can send the following request:

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests


def main():
    response = requests.get(
        "https://api.aimlapi.com/v2/generate/video/luma-ai/generation",
        params={
            "generation_id": "755f9bbb-d99b-4880-992b-f05244ddba61",
            "status": "dreaming"
        },
        headers={
            "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
            "Content-Type": "application/json",
        },
    )

    response.raise_for_status()
    data = response.json()
    print("Generation:", data)


if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
const main = async () => {
  const url = new URL('https://api.aimlapi.com/v2/generate/video/luma-ai/generation');
  url.searchParams.set('generation_id', '755f9bbb-d99b-4880-992b-f05244ddba61');
  url.searchParams.set('state', 'dreaming');

  const data = await fetch(url, {
    method: 'GET',
    headers: {
      Authorization: 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
  }).then((res) => res.json());

  console.log('Generation:', data);
};

main();

```

{% endcode %}
{% endtab %}
{% endtabs %}

### Fetch Multiple Generations

Instead of using the `generation_id` parameter, you will pass `generation_ids`, which can be an array of IDs. This parameter can also accept IDs separated by commas.

## GET /v2/generate/video/luma-ai/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}}},"paths":{"/v2/generate/video/luma-ai/generations":{"get":{"operationId":"LumaAiControllerV2_fetchGenerations_v2","parameters":[{"name":"generation_ids","required":true,"in":"query","schema":{"anyOf":[{"type":"array","items":{"type":"string","format":"uuid"},"minItems":1},{"type":"string"}]}},{"name":"status","required":false,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"description":""}},"tags":["Luma AI"]}}}}
```

### Example: Fetch Multiple Generations

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests


def main():
    response = requests.get(
        "https://api.aimlapi.com/v2/generate/video/luma-ai/generations",
        params={
            "generation_ids[]": "755f9bbb-d99b-4880-992b-f05244ddba61",
            "status": "streaming",
        },
        headers={
            "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
            "Content-Type": "application/json",
        },
    )

    response.raise_for_status()
    data = response.json()
    print("Generation:", data)


if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
const main = async () => {
  const url = new URL('https://api.aimlapi.com/v2/generate/video/luma-ai/generations');
  url.searchParams.set('generation_ids[]', '755f9bbb-d99b-4880-992b-f05244ddba61');
  url.searchParams.set('state', 'dreaming');

  const data = await fetch(url, {
    method: 'GET',
    headers: {
      Authorization: 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
  }).then((res) => res.json());

  console.log('Generation:', data);
};

main();

```

{% endcode %}
{% endtab %}
{% endtabs %}

### Example: Fetch Multiple Generations

{% hint style="info" %}
Ensure you replace `<YOUR_AIMLAPI_KEY>` with your actual API key before running the code.
{% endhint %}

{% tabs %}
{% tab title="Python" %}

```python
import requests


def main():
  url = "https://api.aimlapi.com/v2/generate/video/luma-ai/generation"
  payload = {
    "prompt": "Flying jellyfish",
    "aspect_ratio": "16:9"
  }
  headers = {
    "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
    "Content-Type": "application/json"
  }
  
  response = requests.post(url, json=payload, headers=headers)
  print("Generation:",  response.json())
  
if __name__ == "__main__":
    main()
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const main = async () => {
  const response = await fetch('https://api.aimlapi.com/v2/generate/video/luma-ai/generation', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      prompt: 'A jellyfish in the ocean',
      aspect_ratio: '19:9',
      loop: false
    }),
  }).then((res) => res.json());

  console.log('Generation:', response);
};

main();
```

{% endtab %}
{% endtabs %}

### Extend video

You can extend a video using an existing video you generated before (using its generation ID) or by using an image (via URL). The extension can be done by appending to or prepending from the original content.

The `keywords` parameter controls the following extensions. It can include parameters for defining frames:

* **first frame** (`frame0`)
* **last frame** (`frame1`)

For example, if you want to use an image as a reference for a frame:

```json
{
        "keyframes": {
            "frame0": {
                "type": "image",
                "url": "https://example.com/image1.png"
            }
        }
}
```

Or, in the case of using a previously generated video:

```json
{
    "keyframes": {
        "frame1": {
            "type": "generation",
            "id": "0f3ea4aa-10e7-4dae-af0b-263ab4ac45f9"
        }
    }
}
```

## POST /v2/generate/video/luma-ai/generation

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"LumaAi.v2.CreateGenerationPayload":{"type":"object","properties":{"generation_type":{"type":"string","nullable":true,"enum":["video"]},"prompt":{"type":"string"},"aspect_ratio":{"type":"string","enum":["1:1","16:9","9:16","4:3","3:4","21:9","9:21"]},"loop":{"type":"boolean","default":false},"keyframes":{"type":"object","nullable":true,"properties":{"frame0":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","enum":["generation"]},"id":{"type":"string","format":"uuid"}},"required":["type","id"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","enum":["image"]},"url":{"type":"string","format":"uri"}},"required":["type","url"],"additionalProperties":false},{"nullable":true}]},"frame1":{"anyOf":[{"type":"object","properties":{"type":{"type":"string","enum":["generation"]},"id":{"type":"string","format":"uuid"}},"required":["type","id"],"additionalProperties":false},{"type":"object","properties":{"type":{"type":"string","enum":["image"]},"url":{"type":"string","format":"uri"}},"required":["type","url"],"additionalProperties":false},{"nullable":true}]}}},"callback_url":{"type":"string","nullable":true,"format":"uri"},"model":{"type":"string","enum":["ray-1-6","ray-2","ray-flash-2"],"default":"ray-2"},"resolution":{"type":"string","nullable":true,"enum":["540p","720p","1080p","4k"]},"duration":{"type":"string","nullable":true,"enum":["5s","9s"]}},"required":["prompt"],"additionalProperties":false}}},"paths":{"/v2/generate/video/luma-ai/generation":{"post":{"operationId":"LumaAiControllerV2_createGeneration_v2","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/LumaAi.v2.CreateGenerationPayload"}}}},"responses":{"201":{"description":""}},"tags":["Luma AI"]}}}}
```

## Examples

{% hint style="warning" %}
Ensure you replace `<YOUR_AIMLAPI_KEY>` with your actual API key before running the code.
{% endhint %}

### Extension with the Image

{% tabs %}
{% tab title="Python" %}

```python
import requests


def main()
  url = "https://api.aimlapi.com/v2/generate/video/luma-ai/generation"
  headers = {
    "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
    "Content-Type": "application/json"
  }
  payload = {
    "prompt": "Flying jellyfish",
    "aspect_ratio": "16:9",
    "keyframes": {
      "frame0": {
        "type": "image",
        "url": "https://example.com/image1.png"
      }
    }
  }
  
  response = requests.post(url, json=payload, headers=headers)
  print("Generation:",  response.json())
  
  
if __name__ == "__main__":
    main()
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const main = async () => {
  const response = await fetch('https://api.aimlapi.com/v2/generate/video/luma-ai/generation', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      prompt: 'A jellyfish in the ocean',
      aspect_ratio: '19:9',
      keyframes: {
        frame0: {
          type: 'image',
          url: 'https://example.com/image1.png',
        },
      },
    }),
  }).then((res) => res.json());

  console.log('Generation:', response);
};

main();

```

{% endtab %}
{% endtabs %}

### Extension with the Generation

{% tabs %}
{% tab title="Python" %}

```python
import requests


def main()
  url = "https://api.aimlapi.com/v2/generate/video/luma-ai/generation"
  headers = {
    "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
    "Content-Type": "application/json"
  }
  payload = {
    "prompt": "Flying jellyfish",
    "aspect_ratio": "16:9",
    "keyframes": {
      "frame0": {
        "type": "generation",
        "id": "0f3ea4aa-10e7-4dae-af0b-263ab4ac45f9"
      }
    }
  }
  
  response = requests.post(url, json=payload, headers=headers)
  print("Generation:",  response.json())
  
if __name__ == "__main__":
    main()
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const main = async () => {
  const response = await fetch('https://api.aimlapi.com/v2/generate/video/luma-ai/generation', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      prompt: 'A jellyfish in the ocean',
      aspect_ratio: '19:9',
      keyframes: {
        frame0: {
          type: 'generation',
          id: '0f3ea4aa-10e7-4dae-af0b-263ab4ac45f9',
        },
      },
    }),
  }).then((res) => res.json());

  console.log('Generation:', response);
};

main();

```

{% endtab %}
{% endtabs %}
