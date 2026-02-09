# Source: https://docs.aimlapi.com/api-references/image-models/flux/flux-pro.md

# flux-pro

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `flux-pro`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/flux-pro" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

This is first version of Flux Pro, but it generates images of unmatched quality, outperforming popular models like Midjourney v6.0, DALL·E 3 (HD), and SD3-Ultra.

You can also view [a detailed comparison of this model](https://aimlapi.com/comparisons/flux-1-vs-dall-e-3) on our main website.

<table data-full-width="true"><thead><tr><th width="149">Model</th><th width="593">Properties of Generated Images</th></tr></thead><tbody><tr><td><code>flux-pro</code></td><td>Format: <strong>JPEG, PNG</strong><br>Min size: <strong>256</strong>x<strong>256</strong><br>Max size: <strong>1440</strong>x<strong>1440</strong><br>Default size: <strong>1024</strong>x<strong>768</strong><br><mark style="background-color:orange;">For both height and width, the value must be a multiple of 32.</mark></td></tr></tbody></table>

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["flux-pro"]},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"image_size":{"anyOf":[{"type":"object","properties":{"width":{"type":"integer","minimum":256,"maximum":1440,"default":1024},"height":{"type":"integer","minimum":256,"maximum":1440,"default":768}},"description":"For both height and width, the value must be a multiple of 32."},{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"],"description":"The size of the generated image."}],"default":"landscape_4_3"},"num_inference_steps":{"type":"integer","minimum":1,"maximum":50,"default":50,"description":"The number of inference steps to perform."},"guidance_scale":{"type":"number","minimum":1,"maximum":20,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you."},"safety_tolerance":{"type":"string","enum":["1","2","3","4","5","6"],"default":"2","description":"The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive."},"output_format":{"type":"string","enum":["jpeg","png"],"default":"jpeg","description":"The format of the generated image."}},"required":["model","prompt"],"title":"flux-pro"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image of the specified size using a simple prompt.

{% hint style="warning" %}
The maximum value for both width and height is `1440`, and the minimum is `256`.\
The value must be a multiple of 32.
{% endhint %}

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
            "Content-Type": "application/json"
        },
        json={
            "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.",
            "model": "flux-pro",
            "image_size": {
                "width": 1024,
                "height": 320 
            }
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
      model: 'flux-pro',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.',
      image_size: {
        width: 1024,
        height: 320
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

```json
{
  images: [
    {
      url: 'https://cdn.aimlapi.com/squirrel/files/elephant/G1UYumZngIkBozNrfiztZ_8d758419045c4c16b563511d6f5f3966.jpg',
      width: 1024,
      height: 320,
      content_type: 'image/jpeg'
    }
  ],
  timings: {},
  seed: 711728385,
  has_nsfw_concepts: [ false ],
  prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.'
}
```

{% endcode %}

</details>

We obtained the following nice 1024x320 image by running this code example:

<div align="left"><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-b8c07aa7694d12ce3e6e8f5b4913ffd885a064c3%2FG1UYumZngIkBozNrfiztZ_8d758419045c4c16b563511d6f5f3966.jpg?alt=media" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses."</code></p></figcaption></figure></div>
