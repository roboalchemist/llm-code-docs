# Source: https://docs.aimlapi.com/api-references/image-models/tencent/hunyuan-image-v3-text-to-image.md

# Hunyuan Image v3

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `hunyuan/hunyuan-image-v3-text-to-image`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/hunyuan/hunyuan-image-v3-text-to-image" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

An advanced capabilities of Hunyuan Image 3.0 to generate compelling visuals that seamlessly enhance and communicate your written content.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["hunyuan/hunyuan-image-v3-text-to-image"]},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"negative_prompt":{"type":"string","description":"The description of elements to avoid in the generated image."},"image_size":{"anyOf":[{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"]},{"type":"object","properties":{"width":{"type":"number"},"height":{"type":"number"}},"required":["width","height"]}],"default":"square_hd","description":"The size of the generated image."},"num_inference_steps":{"type":"integer","minimum":1,"maximum":50,"default":28,"description":"The number of inference steps to perform."},"guidance_scale":{"type":"number","minimum":1,"maximum":20,"default":7.5,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you."},"enable_safety_checker":{"type":"boolean","default":true,"description":"If set to True, the safety checker will be enabled."},"sync_mode":{"type":"boolean","default":false,"description":"If set to true, the function will wait for the image to be generated and uploaded before returning the response. This will increase the latency of the function but it allows you to get the image directly in the response without going through the CDN."},"output_format":{"type":"string","enum":["jpeg","png"],"default":"png","description":"The format of the generated image."},"enable_prompt_expansion":{"type":"boolean","description":"If set to True, prompt will be upsampled with more details."}},"required":["model","prompt"],"title":"hunyuan/hunyuan-image-v3-text-to-image"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
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
            "model": "hunyuan/hunyuan-image-v3-text-to-image",
            "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.",
            "image_size": "landscape_16_9"
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
      model: 'hunyuan/hunyuan-image-v3-text-to-image',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses. Realistic photo.',
      image_size: 'landscape_16_9'
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
            "url": "https://v3b.fal.media/files/b/lion/JdrvNguTlt29LmURRbKKN.png",
            "content_type": "image/png",
            "file_name": null,
            "file_size": null,
            "width": 1280,
            "height": 768
        }
    ],
    "meta": {
        "usage": {
            "tokens_used": 210000
        }
    }
}
```

{% endcode %}

</details>

We obtained the following 1280x768 image by running this code example:

<figure><img src="https://v3b.fal.media/files/b/lion/JdrvNguTlt29LmURRbKKN.png" alt=""><figcaption><p><code>A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.</code></p></figcaption></figure>
