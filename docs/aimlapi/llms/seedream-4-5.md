# Source: https://docs.aimlapi.com/api-references/image-models/bytedance/seedream-4-5.md

# Seedream 4.5

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `bytedance/seedream-4-5`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/bytedance/seedream-4-5" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

The model combines both text-to-image and image-to-image capabilities. Compared to [Seedream 4.0](https://docs.aimlapi.com/api-references/image-models/bytedance/seedream-v4-edit-image-to-image), this model significantly improves editing consistency (preserving subject details, lighting, and color tone), the quality of portraits and small text.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["bytedance/seedream-4-5"]},"prompt":{"type":"string","description":"The text prompt describing the content, style, or composition of the image to be generated."},"image_urls":{"type":"array","items":{"type":"string","format":"uri"},"minItems":1,"maxItems":14,"description":"List of URLs or local Base64 encoded images to edit."},"image_size":{"anyOf":[{"type":"object","properties":{"width":{"type":"integer","minimum":1440,"maximum":4096,"default":2048},"height":{"type":"integer","minimum":1440,"maximum":4096,"default":2048}}},{"type":"string","enum":["2K","4K"]}],"description":"The size of the generated image."},"response_format":{"type":"string","enum":["url","b64_json"],"default":"url","description":"The format in which the generated images are returned."},"seed":{"type":"integer","description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"watermark":{"type":"boolean","default":false,"description":"Add an invisible watermark to the generated images."}},"required":["model","prompt"],"title":"bytedance/seedream-4-5"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate a new image using the one from [the flux/dev Quick Example](https://docs.aimlapi.com/api-references/flux/flux-dev#quick-example) as a reference — and make a simple change to it with a prompt.

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import json  # for getting a structured output with indentation

def main():
    response = requests.post(
        "https://api.aimlapi.com/v1/images/generations",
        headers={
            # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
            "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
            "Content-Type": "application/json",
        },
        json={
            "model": "bytedance/seedream-4-5",
            "prompt": "Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect.",
            "image_urls": [
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png",
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/blue-mug.jpg"
            ]
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
      model: 'bytedance/seedream-4-5',
      prompt: 'Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect.',
      image_urls: [
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png",
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/blue-mug.jpg"
            ]
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
  "data": [
    {
      "url": "https://cdn.aimlapi.com/bison/seedream-4-5/02176522545211712014becacfaf8a37949eaec3c8139753caaae_0.jpeg?X-Tos-Algorithm=TOS4-HMAC-SHA256&X-Tos-Credential=AKLTYWJkZTExNjA1ZDUyNDc3YzhjNTM5OGIyNjBhNDcyOTQ%2F20251208%2Fap-southeast-1%2Ftos%2Frequest&X-Tos-Date=20251208T202437Z&X-Tos-Expires=86400&X-Tos-Signature=9be05c928d39a74abc5c06bff5759a28449256d72f1d062933479f279bc672cb&X-Tos-SignedHeaders=host",
      "size": "2048x2048"
    }
  ],
  "meta": {
    "usage": {
      "credits_used": 84000
    }
  }
}
```

{% endcode %}

</details>

<table data-full-width="true"><thead><tr><th width="442.0667724609375" valign="top">Reference Images</th><th valign="top">Generated Image</th></tr></thead><tbody><tr><td valign="top"><div><figure><img src="https://content.gitbook.com/content/ROMd1X5PuqtikJ48n2N9/blobs/ErJeEBi0oKPxfxUcAtXy/t%20rex.png" alt=""><figcaption><p>Image #1</p></figcaption></figure></div></td><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FU2Skze8vWQs2gzl5hvtP%2Fbytedance-seedream-4-5_output.jpeg?alt=media&#x26;token=1c956886-d16b-4d83-ae2d-fbf132144242" alt=""><figcaption><p><kbd><code>"Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect."</code></kbd></p></figcaption></figure></div></td></tr><tr><td valign="top"><div><figure><img src="https://content.gitbook.com/content/ROMd1X5PuqtikJ48n2N9/blobs/hhe9x9exQFNjPIE8gbpn/blue%20mug.jpg" alt=""><figcaption><p>Image #2</p></figcaption></figure></div></td><td valign="top"></td></tr></tbody></table>
