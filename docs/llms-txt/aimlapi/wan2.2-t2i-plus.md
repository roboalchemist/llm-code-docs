# Source: https://docs.aimlapi.com/api-references/image-models/alibaba-cloud/wan2.2-t2i-plus.md

# wan2.2-t2i-plus

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `alibaba/wan2.2-t2i-plus`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/alibaba/wan2.2-t2i-plus" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

The Professional edition of a text-to-image model, designed for high-quality image generation with rich detail.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["alibaba/wan2.2-t2i-plus"]},"prompt":{"type":"string","maxLength":2000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"negative_prompt":{"type":"string","maxLength":500,"description":"The description of elements to avoid in the generated image."},"num_images":{"type":"integer","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."},"image_size":{"anyOf":[{"type":"object","properties":{"width":{"type":"integer","minimum":512,"maximum":1440},"height":{"type":"integer","minimum":512,"maximum":1440}},"required":["width","height"],"description":"For both height and width, the value must be a multiple of 32."},{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"],"description":"The size of the generated image."}],"default":"landscape_4_3","description":"The size of the generated image."},"enhance_prompt":{"type":"boolean","default":true,"description":"Optional parameter to use an LLM-based prompt rewriting feature for higher-quality images that better match the original prompt. Disabling it may affect image quality and prompt alignment."},"watermark":{"type":"boolean","default":false,"description":"Add an invisible watermark to the generated images."},"seed":{"type":"integer","minimum":0,"maximum":2147483647,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."}},"required":["model","prompt"],"title":"alibaba/wan2.2-t2i-plus"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
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
            "model": "alibaba/wan2.2-t2i-plus",
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
      model: 'alibaba/wan2.2-t2i-plus',
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
  "created": 1769537248382,
  "data": [
    {
      "url": "https://cdn.aimlapi.com/alpaca/1d/6b/20260128/42f0a931/37d29071-c065-46c7-b5f5-42a2796957743542318529.png?Expires=1769623633&OSSAccessKeyId=LTAI5tRcsWJEymQaTsKbKqGf&Signature=qCzOS4JIOE9Y3nuZLvlqm3NHBZU%3D"
    }
  ],
  "meta": {
    "usage": {
      "credits_used": 105000
    }
  }
}
```

{% endcode %}

</details>

We obtained the following 1440x512 image by running this code example:

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2F169ve6UAq72AWmLPM1Dz%2Falibaba-wan2.2-t2i-plus_output.png?alt=media&#x26;token=ccbe0d9d-662d-41a0-b732-0a0c54f43933" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses."</code></p></figcaption></figure></div>
