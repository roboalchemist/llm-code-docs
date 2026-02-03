# Source: https://docs.aimlapi.com/api-references/image-models/bytedance/uso.md

# USO (Image-to-Image)

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `bytedance/uso`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/bytedance/uso" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

USO (Unified Style-Subject Optimized) — a single model that seamlessly combines style-based and subject-based image generation.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["bytedance/uso"]},"image_urls":{"type":"array","items":{"type":"string","format":"uri"},"minItems":1,"maxItems":3,"description":"An array of up to 3 image URLs. The first image is always treated as the primary input for image-to-image generation, while the remaining images (if provided) serve as visual style references for the output."},"image_size":{"anyOf":[{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"]},{"type":"object","properties":{"width":{"type":"number"},"height":{"type":"number"}},"required":["width","height"]}],"default":"square_hd","description":"The size of the generated image."},"negative_prompt":{"type":"string","default":"","description":"The description of elements to avoid in the generated image."},"num_inference_steps":{"type":"integer","minimum":1,"maximum":50,"default":28,"description":"The number of inference steps to perform."},"guidance_scale":{"type":"number","minimum":1,"maximum":20,"default":4,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you."},"keep_size":{"type":"boolean"},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"sync_mode":{"type":"boolean","default":false,"description":"If set to true, the function will wait for the image to be generated and uploaded before returning the response. This will increase the latency of the function but it allows you to get the image directly in the response without going through the CDN."},"enable_safety_checker":{"type":"boolean","default":true,"description":"If set to True, the safety checker will be enabled."},"output_format":{"type":"string","enum":["jpeg","png"],"default":"png","description":"The format of the generated image."},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."}},"required":["model","image_urls","prompt"],"title":"bytedance/uso"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate an image of the specified size using a simple prompt.

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import json  # for getting a structured output with indentation

response = requests.post(
    "https://api.aimlapi.com/v1/images/generations",
    headers={
        # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
        "Authorization":"Bearer <YOUR_AIMLAPI_KEY>",
        "Content-Type":"application/json",
    },
    json={
        "model":"bytedance/uso",
        "prompt": "The T-Rex is wearing a business suit, sitting in a cozy small café, drinking from a mug. Blur the background slightly to create a bokeh effect.",
        "image_urls": [ 
             "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png"
        ]
    }
)

data = response.json()
print(json.dumps(data, indent=2, ensure_ascii=False))
```

{% endcode %}
{% endtab %}

{% tab title="JS" %}
{% code overflow="wrap" %}

```javascript
const response = await fetch('https://api.aimlapi.com/v1/images/generations', {
  method: 'POST',
  headers: {
    // Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
    'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'bytedance/uso',
    prompt: 'The T-Rex is wearing a business suit, sitting in a cozy small café, drinking from a mug. Blur the background slightly to create a bokeh effect.',
    image_urls: [
      'https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png'
    ],        
  }),
});

const data = await response.json();
console.log(JSON.stringify(data, null, 2));
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
      "url": "https://cdn.aimlapi.com/eagle/files/penguin/sMMWnB7wyBK8o_XiAohle.png",
      "content_type": "image/png",
      "file_name": null,
      "file_size": null,
      "width": 1024,
      "height": 1024
    }
  ],
  "seed": 351168504,
  "has_nsfw_concepts": [
    false
  ],
  "prompt": "The T-Rex is wearing a business suit, sitting in a cozy small café, drinking from a mug. Blur the background slightly to create a bokeh effect.",
  "timings": {
    "inference": 10.547778039996047
  },
  "data": [
    {
      "url": "https://cdn.aimlapi.com/eagle/files/penguin/sMMWnB7wyBK8o_XiAohle.png",
      "content_type": "image/png",
      "file_name": null,
      "file_size": null,
      "width": 1024,
      "height": 1024
    }
  ],
  "meta": {
    "usage": {
      "tokens_used": 420000
    }
  }
}
```

{% endcode %}

</details>

<table data-full-width="false"><thead><tr><th>Reference Image</th><th>Generated Image</th></tr></thead><tbody><tr><td><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-fa899176b9c4b1be07345bfea5c792a8f6480c19%2Ft-rex%20(1).png?alt=media" alt=""><figcaption><p>(original)</p></figcaption></figure></div></td><td><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-d51bdd5e36d5067330bb72dfa269a550c6dc8172%2FsMMWnB7wyBK8o_XiAohle.png?alt=media" alt=""><figcaption><p><code>"The T-Rex is wearing a business suit, sitting in a cozy small café, drinking from a mug. Blur the background slightly to create a bokeh effect."</code></p></figcaption></figure></div></td></tr></tbody></table>
