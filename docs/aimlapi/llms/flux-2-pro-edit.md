# Source: https://docs.aimlapi.com/api-references/image-models/flux/flux-2-pro-edit.md

# flux-2-pro-edit

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `blackforestlabs/flux-2-pro-edit`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/blackforestlabs/flux-2-pro-edit" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

An advanced image editing model optimized for high-quality manipulation, style transfer, and sequential editing tasks.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["blackforestlabs/flux-2-pro-edit"]},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"image_urls":{"type":"array","items":{"type":"string","format":"uri"},"minItems":1,"maxItems":3,"description":"List of URLs or local Base64 encoded images to edit."},"image_size":{"anyOf":[{"type":"object","properties":{"width":{"type":"integer","minimum":512,"maximum":2048,"default":1024},"height":{"type":"integer","minimum":512,"maximum":2048,"default":768}},"description":"For both height and width, the value must be a multiple of 32."},{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"],"description":"The size of the generated image."}],"default":"landscape_4_3"},"output_format":{"type":"string","enum":["jpeg","png","webp"],"default":"png","description":"The format of the generated image."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"enable_safety_checker":{"type":"boolean","default":true,"description":"If set to True, the safety checker will be enabled."},"safety_tolerance":{"type":"string","enum":["1","2","3","4","5","6"],"default":"2","description":"The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive."}},"required":["model","prompt","image_urls"],"title":"blackforestlabs/flux-2-pro-edit"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image of the specified size using two input images and a prompt that defines how they should be edited.

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
            "model": "blackforestlabs/flux-2-pro-edit",
            "prompt": "Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect.",
            "image_urls": [
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png",
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/blue-mug.jpg"
            ],
            "guidance_scale": 19
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
      model: 'blackforestlabs/flux-2-pro-edit',
      prompt: 'Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect.',
      image_urls: [
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png",
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/blue-mug.jpg"
            ],
      guidance_scale: 19
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
      "url": "https://cdn.aimlapi.com/flamingo/files/b/0a847bef/yW2QPKFJueCjSc-o-JpXk.png"
    }
  ],
  "meta": {
    "usage": {
      "tokens_used": 189000
    }
  }
}
```

{% endcode %}

</details>

<table data-full-width="true"><thead><tr><th width="442.0667724609375" valign="top">Reference Images</th><th valign="top">Generated Image</th></tr></thead><tbody><tr><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-fa899176b9c4b1be07345bfea5c792a8f6480c19%2Ft-rex%20(1).png?alt=media" alt=""><figcaption><p>Image #1</p></figcaption></figure></div></td><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-1cea322d45837c7dc124207de1d5c819a2babd95%2FyW2QPKFJueCjSc-o-JpXk.png?alt=media" alt=""><figcaption><p><kbd><code>"Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect."</code></kbd></p></figcaption></figure></div></td></tr><tr><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-21cc1f1cf38504cb4c59d82e91dd184f26539e36%2Fblue-mug.jpg?alt=media" alt=""><figcaption><p>Image #2</p></figcaption></figure></div></td><td valign="top"></td></tr></tbody></table>
