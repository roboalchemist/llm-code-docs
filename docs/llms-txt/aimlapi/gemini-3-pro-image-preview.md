# Source: https://docs.aimlapi.com/api-references/image-models/google/gemini-3-pro-image-preview.md

# Nano Banana Pro (Gemini 3 Pro Image)

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `google/nano-banana-pro`
* `google/gemini-3-pro-image-preview`
  {% endhint %}

{% hint style="success" %}
Both IDs listed above refer to the same model; we support them for backward compatibility.
{% endhint %}
{% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/google/gemini-3-pro-image-preview" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview <a href="#model-overview" id="model-overview"></a>

Google’s smartest text-to-image model as of the November 2025 preview release.

## Setup your API Key <a href="#setup-your-api-key" id="setup-your-api-key"></a>

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["google/nano-banana-pro","google/gemini-3-pro-image-preview"]},"prompt":{"type":"string","description":"The text prompt describing the content, style, or composition of the image to be generated."},"aspect_ratio":{"type":"string","enum":["21:9","1:1","4:3","3:2","2:3","5:4","4:5","3:4","16:9","9:16"],"default":"1:1","description":"The aspect ratio of the generated image."},"resolution":{"type":"string","enum":["1K","2K","4K"],"default":"1K","description":"The size of the generated image."},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."}},"required":["model","prompt"],"title":"google/gemini-3-pro-image-preview"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image of the specified aspect ratio using a simple prompt.

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import json

def main():
    response = requests.post(
        "https://api.aimlapi.com/v1/images/generations",
        headers={
            # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
            "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
            "Content-Type": "application/json",
        },
        json={
            "model": "google/nano-banana-pro",
            "prompt": "Racoon eating ice-cream",
            "aspect_ratio": "1:1",
            "resolution": "1K"
        }
    )

    data = response.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}

{% tab title="JS" %}
{% code overflow="wrap" %}

```javascript
async function main() {
  const response = await fetch('https://api.aimlapi.com/v1/images/generations', {
    method: 'POST',
    headers: {
      // Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
      'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'google/nano-banana-pro',
      prompt: 'Racoon eating ice-cream',
      aspect_ratio: '1:1',
      resolution: '1K'
    }),
  });

  const data = await response.json();
  console.log(data);
}

main();
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
{
  "description": "",
  "data": [
    {
      "url": "https://cdn.aimlapi.com/flamingo/files/b/monkey/rvEPfEJe--7Nf41TwCGy3.png",
      "content_type": "image/png",
      "width": null,
      "height": null,
      "file_name": "rvEPfEJe--7Nf41TwCGy3.png"
    }
  ],
  "meta": {
    "usage": {
      "tokens_used": 315000
    }
  }
}
```

{% endcode %}

</details>

So we obtained the following 1024x1024 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-e17c95ac06a86b09f733d90d7bb1a60ca5fea6f4%2FoeX2RJ3jPIKcBueLZSAGL.png?alt=media" alt=""><figcaption><p><code>"aspect_ratio": "1:1"</code>,  <code>"resolution": "1K"</code></p></figcaption></figure>

Here’s an example of the output using alternative `resolution` and `aspect_ratio` parameters:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FVog4TKfFWbOu9BVqp7YF%2Fnanobananapro_output.png?alt=media&#x26;token=163b2c6d-e318-4d98-97ab-7e9572b91320" alt=""><figcaption><p><code>"aspect_ratio": "16:9"</code>,  <code>"resolution": "2K"</code></p></figcaption></figure>
