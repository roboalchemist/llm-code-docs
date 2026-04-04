# Source: https://docs.aimlapi.com/api-references/image-models/bytedance/seedream-3.0.md

# Seedream 3.0

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `bytedance/seedream-3.0`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/bytedance/seedream-3-0" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

This bilingual (Chinese-English) image generation model supports arbitrary image dimensions — as long as the product of width and height remains within a generous limit (up to 2K). It offers faster response times, improved rendering of small text and layouts, stronger visual aesthetics and structural consistency, and high fidelity in fine details.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["bytedance/seedream-3.0"]},"prompt":{"type":"string","description":"The text prompt describing the content, style, or composition of the image to be generated."},"response_format":{"type":"string","enum":["url","b64_json"],"default":"url","description":"The format in which the generated images are returned."},"size":{"type":"string","description":"Specifies the dimensions (width x height in pixels) of the generated image. Must be between [512x512, 2048x2048]."},"seed":{"type":"integer","description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"guidance_scale":{"type":"number","minimum":1,"maximum":10,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you."},"watermark":{"type":"boolean","default":false,"description":"Add an invisible watermark to the generated images."}},"required":["model","prompt"],"title":"bytedance/seedream-3.0"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
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
            "model": "bytedance/seedream-3.0",
            "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.",
            "aspect_ratio": "16:9",        
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
      model: 'bytedance/seedream-3.0',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.',
      aspect_ratio: '16:9',
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
Generation: {'created': 1751616711, 'data': [{'url': 'https://ark-content-generation-v2-ap-southeast-1.tos-ap-southeast-1.volces.com/seedream-3-0-t2i/02175161671039622600af416b2ca58c9c8a1e1bf93fac0335693.jpeg?X-Tos-Algorithm=TOS4-HMAC-SHA256&X-Tos-Credential=AKLTYjg3ZjNlOGM0YzQyNGE1MmI2MDFiOTM3Y2IwMTY3OTE%2F20250704%2Fap-southeast-1%2Ftos%2Frequest&X-Tos-Date=20250704T081151Z&X-Tos-Expires=86400&X-Tos-Signature=76ad6d2e0eb218521b9ce0bfdc98eaf2aa683e9a0d3840624fb4d413a1fd360e&X-Tos-SignedHeaders=host&x-tos-process=image%2Fwatermark%2Cimage_YXNzZXRzL3dhdGVybWFyay5wbmc_eC10b3MtcHJvY2Vzcz1pbWFnZS9yZXNpemUsUF81'}]}
```

{% endcode %}

</details>

We obtained the following 1888x301 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-f605696ed4daa2ed5b0754ec5b13923e472cfa1c%2F02175161671039622600af416b2ca58c9c8a1e1bf93fac0335693.jpg?alt=media" alt=""><figcaption><p><code>'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.'</code></p></figcaption></figure>

Here’s an example of a 555×543 image generated using the same prompt:

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-6642e5286bc4facc8f5e4913f45797b3001d4799%2F0217516196916226a3647c198681a7c9ea0518c738c92d3286bc4.jpg?alt=media" alt=""><figcaption><p><code>'A T-Rex relaxing on a beach, lying on a sun lounger</code><br><code>and wearing sunglasses.'</code></p></figcaption></figure></div>
