# Source: https://docs.aimlapi.com/api-references/image-models/alibaba-cloud/wan2.5-t2i-preview.md

# wan2.5-t2i-preview

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `alibaba/wan2.5-t2i-preview`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/alibaba/wan2.5-t2i-preview" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A text-to-image model capable of producing high-fidelity, visually accurate images.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["alibaba/wan2.5-t2i-preview"]},"prompt":{"type":"string","maxLength":2000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"negative_prompt":{"type":"string","maxLength":500,"description":"The description of elements to avoid in the generated image."},"num_images":{"type":"integer","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."},"image_size":{"anyOf":[{"type":"object","properties":{"width":{"type":"integer","minimum":512,"maximum":1440},"height":{"type":"integer","minimum":512,"maximum":1440}},"required":["width","height"],"description":"For both height and width, the value must be a multiple of 32."},{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"],"description":"The size of the generated image."}],"default":"landscape_4_3","description":"The size of the generated image."},"enhance_prompt":{"type":"boolean","default":true,"description":"Optional parameter to use an LLM-based prompt rewriting feature for higher-quality images that better match the original prompt. Disabling it may affect image quality and prompt alignment."},"watermark":{"type":"boolean","default":false,"description":"Add an invisible watermark to the generated images."},"seed":{"type":"integer","minimum":0,"maximum":2147483647,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."}},"required":["model","prompt"],"title":"alibaba/wan2.5-t2i-preview"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image of the specified size using a simple prompt.

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
            "model": "alibaba/wan2.5-t2i-preview",
            "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.",
            "image_size": {
                "width": 1440,
                "height": 512
            },
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
      model: 'alibaba/wan2.5-t2i-preview',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.',
      image_size: {
        width: 1440,
        height: 512
      },
    }),
  });

  const data = await response.json();
  console.log('Generation:', data);
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
  "created": 1769537446493,
  "data": [
    {
      "url": "https://cdn.aimlapi.com/alpaca/1d/b0/20260128/f599ada6/50628345-4c1440df-86b3-464b-89f6-3c7b19611f6e.png?Expires=1769623835&OSSAccessKeyId=LTAI5tRcsWJEymQaTsKbKqGf&Signature=CWLemI3Pnxxa9XzWGHblYHv9tvg%3D"
    }
  ],
  "meta": {
    "usage": {
      "credits_used": 63000
    }
  }
}
```

{% endcode %}

</details>

We obtained the following 1440x512 image by running this code example:

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Ff2W97E7bx9rt3LrD4xeP%2Falibaba-wan2.5-t2i-preview_output.png?alt=media&#x26;token=e85f01e2-e002-43e1-8db3-c08fad62e899" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses."</code></p></figcaption></figure></div>
