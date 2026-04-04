# Source: https://docs.aimlapi.com/api-references/image-models/google/imagen-4-ultra-generate.md

# Imagen 4 Ultra Generate

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `google/imagen-4.0-ultra-generate-001`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/google/imagen-4-0-ultra-generate-001" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview <a href="#model-overview" id="model-overview"></a>

A model built for photorealistic image generation and precise text rendering, suited for high-fidelity professional use.

## Setup your API Key <a href="#setup-your-api-key" id="setup-your-api-key"></a>

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["google/imagen-4.0-ultra-generate-001"]},"prompt":{"type":"string","maxLength":400,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"convert_base64_to_url":{"type":"boolean","default":true,"description":"If True, the URL to the image will be returned; otherwise, the file will be provided in base64 format."},"num_images":{"type":"integer","maximum":4,"default":1,"description":"The number of images to generate."},"seed":{"type":"integer","minimum":0,"maximum":4294967295,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"enhance_prompt":{"type":"boolean","default":true,"description":"Optional parameter to use an LLM-based prompt rewriting feature for higher-quality images that better match the original prompt. Disabling it may affect image quality and prompt alignment."},"aspect_ratio":{"type":"string","enum":["1:1","9:16","16:9","3:4","4:3"],"default":"1:1","description":"The aspect ratio of the generated image."},"person_generation":{"type":"string","enum":["dont_allow","allow_adult"],"default":"allow_adult","description":"Allow generation of people."},"safety_setting":{"type":"string","enum":["block_low_and_above","block_medium_and_above","block_only_high"],"default":"block_medium_and_above","description":"Adds a filter level to safety filtering."},"add_watermark":{"type":"boolean","default":false,"description":"Add an invisible watermark to the generated images."}},"required":["model","prompt"],"title":"google/imagen-4.0-ultra-generate-001"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image of the specified aspect ratio using a simple prompt.

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import json   # for getting a structured output with indentation

def main():
    response = requests.post(
        "https://api.aimlapi.com/v1/images/generations",
        headers={
            # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
            "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
            "Content-Type": "application/json",
        },
        json={
            "prompt": "Racoon eating ice-cream",
            "model": "google/imagen-4.0-ultra-generate-001",
            "aspect_ratio": "16:9"
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
      model: 'google/imagen-4.0-ultra-generate-001',
      prompt: 'Racoon eating ice-cream',
      aspect_ratio: '16:9'
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
      "mime_type": "image/png",
      "url": "https://cdn.aimlapi.com/generations/guepard/1758237214798-b22381b0-cc4c-466c-92f4-c3b2531d7ebf.png",
      "prompt": "A curious raccoon sitting upright on a park bench, intently focused on licking a melting scoop of vanilla ice cream in a waffle cone. The raccoon has its small paws wrapped around the cone, and a tiny bit of ice cream is smeared on its nose and whiskers. The fur is ruffled and slightly damp from the treat. The park setting is sunny with dappled light filtering through the leaves of a large oak tree in the background. Autumn leaves are scattered on the ground near the bench. The ice cream is dripping slightly down the cone, and a small puddle is forming on the wooden bench. The image is captured at eye level with the raccoon."
    }
  ],
  "meta": {
    "usage": {
      "tokens_used": 126000
    }
  }
}
```

{% endcode %}

</details>

So we obtained the following 1408x768 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-70d05cc60f300d555e0a93116b28f45622a5a424%2F1758237214798-b22381b0-cc4c-466c-92f4-c3b2531d7ebf.png?alt=media" alt=""><figcaption><p>In reality, raccoons shouldn’t be given ice cream or chocolate—it’s harmful to their metabolism.<br>But in the AI world, raccoons party like there’s no tomorrow.</p></figcaption></figure>
