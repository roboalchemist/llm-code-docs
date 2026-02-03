# Source: https://docs.aimlapi.com/api-references/image-models/flux/flux-kontext-pro-text-to-image.md

# flux/kontext-pro/text-to-image

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `flux/kontext-pro/text-to-image`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/flux/kontext-pro/text-to-image" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A new Flux model optimized for faster generation speed.

<table data-full-width="true"><thead><tr><th width="277.46661376953125">Model</th><th width="593">Properties of Generated Images</th></tr></thead><tbody><tr><td><code>flux/kontext-pro/text-to-image</code></td><td>Format: <strong>JPEG, PNG</strong><br>Image size can't be set directly — only a preset aspect ratio can be chosen.<br>Default aspect ratio and size: <strong>1:1</strong>, <strong>1024</strong>x<strong>1024</strong></td></tr></tbody></table>

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["flux/kontext-pro/text-to-image"]},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"guidance_scale":{"type":"number","minimum":1,"maximum":20,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you."},"safety_tolerance":{"type":"string","enum":["1","2","3","4","5","6"],"default":"2","description":"The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive."},"output_format":{"type":"string","enum":["jpeg","png"],"default":"jpeg","description":"The format of the generated image."},"aspect_ratio":{"type":"string","enum":["21:9","16:9","4:3","3:2","1:1","2:3","3:4","9:16","9:21"],"default":"16:9","description":"The aspect ratio of the generated image."}},"required":["model","prompt"],"title":"flux/kontext-pro/text-to-image"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
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
            "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.",
            "model": "flux/kontext-pro/text-to-image",
            "aspect_ratio": "21:9"   
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
      model: 'flux/kontext-pro/text-to-image',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.',
      aspect_ratio: '21:9',
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
  "images": [
    {
      "url": "https://cdn.aimlapi.com/squirrel/files/koala/6e4yw7_YnA8tEe03QW8wW_5298e11de5a24f1f9cf4f277cbdd3316.jpg",
      "width": 1568,
      "height": 672,
      "content_type": "image/jpeg"
    }
  ],
  "timings": {},
  "seed": 2561481494,
  "has_nsfw_concepts": [
    false
  ],
  "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses."
}
```

{% endcode %}

</details>

We obtained the following 1568x672 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a8c1ca6d3b77cd4e9758eadc0cca3c37be82fe31%2FEgskSnirzZYljpVeLSTNR_917caa60fb8f450cbd9576756171cd68.jpg?alt=media" alt=""><figcaption><p><code>'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.'</code></p></figcaption></figure>
