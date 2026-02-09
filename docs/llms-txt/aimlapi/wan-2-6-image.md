# Source: https://docs.aimlapi.com/api-references/image-models/alibaba-cloud/wan-2-6-image.md

# wan2.6-image

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `alibaba/wan-2-6-image`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/alibaba/wan-2-6-image" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

Text-to-Image and Image-to-Image generator in a single model, providing artists and creators with complete creative freedom.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["alibaba/wan-2-6-image"]},"prompt":{"type":"string","maxLength":2000,"description":"A positive prompt that describes the desired elements and visual features in the edited image."},"image_urls":{"type":"array","items":{"type":"string","format":"uri"},"minItems":1,"maxItems":3,"description":"List of URLs or local Base64 encoded images to edit."},"image_size":{"anyOf":[{"type":"object","properties":{"width":{"type":"integer","minimum":512,"maximum":1440},"height":{"type":"integer","minimum":512,"maximum":1440}},"required":["width","height"],"description":"For both height and width, the value must be a multiple of 32."},{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"],"description":"The size of the generated image."}],"default":"landscape_4_3","description":"The size of the generated image."},"enhance_prompt":{"type":"boolean","default":true,"description":"Optional parameter to use an LLM-based prompt rewriting feature for higher-quality images that better match the original prompt. Disabling it may affect image quality and prompt alignment."},"negative_prompt":{"type":"string","maxLength":500,"description":"The description of elements to avoid in the generated image."},"seed":{"type":"integer","minimum":0,"maximum":2147483647,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"watermark":{"type":"boolean","default":false,"description":"Add an invisible watermark to the generated images."}},"required":["model","prompt"],"title":"alibaba/wan-2-6-image"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image using two input images and a prompt that defines how they should be edited.

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
            "model": "alibaba/wan-2-6-image",
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
      model: 'alibaba/wan-2-6-image',
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
```

{% endcode %}

</details>

<table data-full-width="true"><thead><tr><th width="442.0667724609375" valign="top">Reference Images</th><th valign="top">Generated Image</th></tr></thead><tbody><tr><td valign="top"><div><figure><img src="https://content.gitbook.com/content/ROMd1X5PuqtikJ48n2N9/blobs/v3cLiIpoUW6WNdClpIHP/t%20rex.png" alt=""><figcaption><p>Image #1</p></figcaption></figure></div></td><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FqujY69Mm0nLbkVWbQCQW%2Falibaba-wan-2-6-image_output.png?alt=media&#x26;token=603f5438-1bd9-4ded-94d6-e0ca7c2c4a33" alt=""><figcaption><p><kbd><code>"Combine the images so the T-Rex is wearing a business suit, sitting in a cozy small café, drinking from the mug. Blur the background slightly to create a bokeh effect."</code></kbd></p></figcaption></figure></div></td></tr><tr><td valign="top"><div><figure><img src="https://content.gitbook.com/content/ROMd1X5PuqtikJ48n2N9/blobs/LssToAEUPuQ5jp7rB29z/blue%20mug.jpg" alt=""><figcaption><p>Image #2</p></figcaption></figure></div></td><td valign="top"></td></tr></tbody></table>
