# Source: https://docs.aimlapi.com/api-references/image-models/openai/dall-e-3.md

# DALL·E 3

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `dall-e-3`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/dall-e-3" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

This model represents a significant leap forward in AI-driven image creation, capable of generating images from text inputs. This model processes prompts with enhanced neural network architectures, resulting in images that are not only relevant but also rich in detail and diversity. DALL·E 3's deep learning techniques analyze and understand complex descriptions, allowing for the generation of visuals across a wide range of styles and subjects.

You can also view [a detailed comparison of this model](https://aimlapi.com/comparisons/flux-1-vs-dall-e-3) on our main website.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["dall-e-3"]},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"n":{"type":"number","enum":[1],"default":1,"description":"The number of images to generate."},"quality":{"type":"string","enum":["standard","hd"],"default":"standard","description":"The quality of the image that will be generated."},"size":{"type":"string","enum":["1024x1024","1024x1792","1792x1024"],"default":"1024x1024","description":"The size of the generated image."},"style":{"type":"string","enum":["vivid","natural"],"default":"vivid","description":"The style of the generated images."},"response_format":{"type":"string","enum":["url","b64_json"],"default":"url","description":"The format in which the generated images are returned."}},"required":["model","prompt"],"title":"dall-e-3"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image using a simple prompt.

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
            "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.",
            "model": "dall-e-3",
            "quality": "hd"
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
      model: 'dall-e-3',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.',
      quality: 'hd',
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

{% hint style="info" %}
Note that the model applies automatic prompt enhancement, and this behavior cannot be disabled. The enhanced prompt is also returned in the response (see the `revised_prompt` parameter in the response).
{% endhint %}

<details>

<summary>Response</summary>

{% code overflow="wrap" %}

```json5
{
  created: 1756973055,
  data: [
    {
      revised_prompt: 'A massive T-Rex is taking a well-deserved vacation at a tranquil beach. The charismatic dinosaur lies leisurely on a large, comfortable sun lounger. Its tiny, clawed hands hold a pair of fashionable sunglasses in place over its sharp, menacing eyes, adding an air of humor to the otherwise intimidating figure. The soothing sound of the waves and the gentle warmth of the sun create a calming atmosphere around the chilling predator, lending the scene an amusing contradiction.',
      url: 'https://oaidalleapiprodscus.blob.core.windows.net/private/org-5drZvxmo1TGoMx2jeKKGAGSh/user-eKr1xiaNRxSYqgKrXfgZzSAJ/img-B7BCSmDWQgWlGA2vu24HSzqS.png?st=2025-09-04T07%3A04%3A15Z&se=2025-09-04T09%3A04%3A15Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=38e27a3b-6174-4d3e-90ac-d7d9ad49543f&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-09-04T02%3A45%3A18Z&ske=2025-09-05T02%3A45%3A18Z&sks=b&skv=2024-08-04&sig=fGRfHnpFybyg6wwJw7PYXJKM1AF1NWwD/W5qPKIha7U%3D'
    }
  ]
}
```

{% endcode %}

</details>

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-bbcda2aa4dd5c89e5caf63f139ce9ceea0bcb2ce%2Fimg-4BSO0AAOQo7DPgFCzpzLOibU.png?alt=media" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses."</code></p></figcaption></figure>
