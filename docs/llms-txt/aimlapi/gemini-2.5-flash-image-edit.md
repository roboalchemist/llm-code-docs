# Source: https://docs.aimlapi.com/api-references/image-models/google/gemini-2.5-flash-image-edit.md

# Gemini 2.5 Flash Image Edit (Nano Banana)

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `google/gemini-2.5-flash-image-edit`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/google/gemini-2.5-flash-image-edit" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

The model takes multiple images as input, with the prompt defining how they are used or combined.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

<details>

<summary>Aspect ratio/Resolution Table</summary>

| Aspect ratio | Resolution | Credits |
| ------------ | ---------- | ------- |
| 1:1          | 1024×1024  | 84 000  |
| 2:3          | 832×1248   | 84 000  |
| 3:2          | 1248×832   | 84 000  |
| 3:4          | 864×1184   | 84 000  |
| 4:3          | 1184×864   | 84 000  |
| 4:5          | 896×1152   | 84 000  |
| 5:4          | 1152×896   | 84 000  |
| 9:16         | 768×1344   | 84 000  |
| 16:9         | 1344×768   | 84 000  |
| 21:9         | 1536×672   | 84 000  |

</details>

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["google/gemini-2.5-flash-image-edit"]},"prompt":{"type":"string","description":"The text prompt describing the content, style, or composition of the image to be generated."},"image_urls":{"type":"array","items":{"type":"string","format":"uri"},"description":"List of URLs or local Base64 encoded images to edit."},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."}},"required":["model","prompt","image_urls"],"title":"google/gemini-2.5-flash-image-edit"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image using two input images and a prompt that defines how they should be edited.

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
            "model": "google/gemini-2.5-flash-image-edit",
            "image_urls": [
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png",
                "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/blue-mug.jpg"
            ],
            "prompt": "Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect.",
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
        model: 'google/gemini-2.5-flash-image-edit',
        image_urls: [
                'https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png',
                'https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/blue-mug.jpg'
        ],
        prompt: 'Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect.',
      }),
    });
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
  "images": [
    {
      "url": "https://cdn.aimlapi.com/eagle/files/panda/9g3PokYLjWoygTVrRgfvG_output.png",
      "content_type": "image/png",
      "file_name": "output.png",
      "file_size": 2273159,
      "width": null,
      "height": null
    }
  ],
  "description": "Here is your T-Rex in a business suit, enjoying a drink in a cozy cafe! "
}
```

{% endcode %}

</details>

<table data-full-width="false"><thead><tr><th width="339.6666259765625" valign="top">Reference Images</th><th valign="top">Generated Image</th></tr></thead><tbody><tr><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-fa899176b9c4b1be07345bfea5c792a8f6480c19%2Ft-rex%20(1).png?alt=media" alt=""><figcaption><p>Image #1</p></figcaption></figure></div></td><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-e2ed13cd8f04e76f1c82115608f2289d6dcd47dd%2Fgemini_2.5_flash_image_edit_output.png?alt=media" alt=""><figcaption><p><kbd><code>"Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect."</code></kbd></p></figcaption></figure></div></td></tr><tr><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-21cc1f1cf38504cb4c59d82e91dd184f26539e36%2Fblue-mug.jpg?alt=media" alt=""><figcaption><p>Image #2</p></figcaption></figure></div></td><td valign="top"></td></tr></tbody></table>
