# Source: https://docs.aimlapi.com/api-references/image-models/google/imagen-4-generate.md

# Imagen 4 Generate

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `google/imagen-4.0-generate-001`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/google/imagen-4-0-generate-001" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview <a href="#model-overview" id="model-overview"></a>

An advanced text-to-image model delivering a balance of speed and image quality.

## Setup your API Key <a href="#setup-your-api-key" id="setup-your-api-key"></a>

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["google/imagen-4.0-generate-001"]},"prompt":{"type":"string","maxLength":400,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"convert_base64_to_url":{"type":"boolean","default":true,"description":"If True, the URL to the image will be returned; otherwise, the file will be provided in base64 format."},"num_images":{"type":"integer","maximum":4,"default":1,"description":"The number of images to generate."},"seed":{"type":"integer","minimum":0,"maximum":4294967295,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"enhance_prompt":{"type":"boolean","default":true,"description":"Optional parameter to use an LLM-based prompt rewriting feature for higher-quality images that better match the original prompt. Disabling it may affect image quality and prompt alignment."},"aspect_ratio":{"type":"string","enum":["1:1","9:16","16:9","3:4","4:3"],"default":"1:1","description":"The aspect ratio of the generated image."},"person_generation":{"type":"string","enum":["dont_allow","allow_adult"],"default":"allow_adult","description":"Allow generation of people."},"safety_setting":{"type":"string","enum":["block_low_and_above","block_medium_and_above","block_only_high"],"default":"block_medium_and_above","description":"Adds a filter level to safety filtering."},"add_watermark":{"type":"boolean","default":false,"description":"Add an invisible watermark to the generated images."}},"required":["model","prompt"],"title":"google/imagen-4.0-generate-001"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
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
            "model": "google/imagen-4.0-generate-001",
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
      model: 'google/imagen-4.0-generate-001',
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
      "url": "https://cdn.aimlapi.com/generations/guepard/1758236160134-5fcac25f-0c87-4145-b24b-98ccebab5c0c.png",
      "prompt": "A mischievous racoon, with beady eyes and a striped tail, is caught mid-lick, enjoying a stolen ice cream cone. Its small paws cradle the melting treat, and its face is smeared with the creamy sweetness, indicating a thorough and enthusiastic indulgence. The scene is set in a cluttered alleyway, with discarded boxes and old bricks forming a backdrop to the racoon's illicit feast."
    }
  ],
  "meta": {
    "usage": {
      "tokens_used": 84000
    }
  }
}
```

{% endcode %}

</details>

So we obtained the following 1408x768 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-09527195c3c3e095afb65798ba92659b4cc72c27%2F1758236160134-5fcac25f-0c87-4145-b24b-98ccebab5c0c.png?alt=media" alt=""><figcaption><p>In reality, raccoons shouldn’t be given ice cream or chocolate—it’s harmful to their metabolism.<br>But in the AI world, raccoons party like there’s no tomorrow.</p></figcaption></figure>
