# Source: https://docs.aimlapi.com/api-references/image-models/alibaba-cloud/qwen-image-edit.md

# qwen-image-edit

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `alibaba/qwen-image-edit`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/alibaba/qwen-image-edit" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

The image editing variant of our 20B [qwen-image](https://docs.aimlapi.com/api-references/image-models/alibaba-cloud/qwen-image) model. It expands the model’s distinctive text rendering abilities to editing tasks, making accurate text modifications within images possible.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["alibaba/qwen-image-edit"]},"prompt":{"type":"string","maxLength":800,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"image":{"type":"string","description":"The image to be edited. Enter the Base64 encoding of the picture or an accessible URL. Image URL: Make sure that the image URL is accessible. Base64-encoded content: The format must be in lowercase."},"negative_prompt":{"type":"string","maxLength":500,"description":"The description of elements to avoid in the generated image."},"watermark":{"type":"boolean","default":false,"description":"Add an invisible watermark to the generated images."}},"required":["model","prompt","image"],"title":"alibaba/qwen-image-edit"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image using an input image and a prompt that defines how it should be edited.

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
            "model": "alibaba/qwen-image-edit",
            "prompt": "Make the dinosaur sit on a lounge chair with its back to the camera, looking toward the water. The setting sun has almost disappeared below the horizon.",
            "image": "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png"
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

const response = await fetch('https://api.aimlapi.com/v1/images/generations', {
  method: 'POST',
  headers: {
    // Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
    'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'alibaba/qwen-image-edit',
    prompt: 'Make the dinosaur sit on a lounge chair with its back to the camera, looking toward the water. The setting sun has almost disappeared below the horizon.',
    image: 'https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png',        
  }),
});

const data = await response.json();
console.log(JSON.stringify(data, null, 2));
```

{% endcode %}
{% endtab %}
{% endtabs %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
{
  "created": 1756832341,
  "data": [
    {
      "url": "https://dashscope-result-sgp.oss-ap-southeast-1.aliyuncs.com/7d/06/20250903/1955eee6/ac748d89-d6b1-4d4e-bc65-eea543098bb9-1.png?Expires=1757438140&OSSAccessKeyId=LTAI5tRcsWJEymQaTsKbKqGf&Signature=aDhUphXV84V1nPMmdRl49ShSKxY%3D"
    }
  ]
}
```

{% endcode %}

</details>

We obtained the following 1184x896 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-2c3b18dd3b6188a3bbca946318de35c3dfb578fb%2Fac748d89-d6b1-4d4e-bc65-eea543098bb9-1.png?alt=media" alt=""><figcaption><p><code>'Make the dinosaur sit on a lounge chair with its back to the camera, looking toward the water.</code><br><code>The setting sun has almost disappeared below the horizon.'</code></p></figcaption></figure>
