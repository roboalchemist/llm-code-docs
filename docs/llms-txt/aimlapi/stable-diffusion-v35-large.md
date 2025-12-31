# Source: https://docs.aimlapi.com/api-references/image-models/stability-ai/stable-diffusion-v35-large.md

# Stable Diffusion v3.5 Large

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `stable-diffusion-v35-large`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/stable-diffusion-v35-large" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A state-of-the-art text-to-image generative model designed to create high-resolution images based on textual prompts. It excels in producing diverse and high-quality outputs, making it suitable for professional applications.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["stable-diffusion-v35-large"]},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"image_size":{"anyOf":[{"type":"object","properties":{"width":{"type":"integer","minimum":64,"maximum":1536,"default":1024},"height":{"type":"integer","minimum":64,"maximum":1536,"default":768}},"description":"For both height and width, the value must be a multiple of 32."},{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"],"description":"The size of the generated image."}],"default":"square_hd"},"negative_prompt":{"type":"string","description":"The description of elements to avoid in the generated image."},"guidance_scale":{"type":"number","minimum":1,"maximum":20,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you."},"num_inference_steps":{"type":"integer","minimum":1,"maximum":50,"description":"The number of inference steps to perform."},"enable_safety_checker":{"type":"boolean","default":true,"description":"If set to True, the safety checker will be enabled."},"output_format":{"type":"string","enum":["jpeg","png"],"default":"jpeg","description":"The format of the generated image."}},"required":["model","prompt"],"title":"stable-diffusion-v35-large"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
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
            "model": "stable-diffusion-v35-large",
            "image_size": "landscape_16_9"
            "num_inference_steps": 40,
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
      model: 'stable-diffusion-v35-large',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses. Realistic photo.',
      image_size: 'landscape_16_9',
      num_inference_steps: 40,
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
  images: [
    {
      url: 'https://cdn.aimlapi.com/eagle/files/elephant/4vP0cAmlTNsadiYaMFE30.jpeg',
      width: 1024,
      height: 576,
      content_type: 'image/jpeg'
    }
  ],
  timings: { inference: 4.855678029009141 },
  seed: 6199662706750842000,
  has_nsfw_concepts: [ false ],
  prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.'
}
```

{% endcode %}

</details>

We obtained the following 1024x576 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-9c24f80266d7521e0841a56695d52c939a8ccc48%2Fj_c4eu3gJwADYRTb7_3M1.jpeg?alt=media" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses."</code></p></figcaption></figure>

<details>

<summary>Extra pictures</summary>

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-4f06608c798013e1d38bc2bd59a67263e7f70bb1%2F4Y0_aIaOmYmtz2mqVxaPU-1.jpeg?alt=media" alt=""><figcaption><p><code>"A highly detailed T-Rex relaxing on a sunny beach, lying on a wooden sun lounger and wearing stylish sunglasses. Its skin is covered in realistic, finely textured scales with natural color variations — rough and weathered like that of large reptiles. Sunlight reflects subtly off the individual scales. The background includes palm trees, gentle waves, and soft sand partially covering the T-Rex's feet. The scene is rendered with cinematic lighting and a natural color palette."</code><br><code>"num_inference_steps": 40</code></p></figcaption></figure>

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-eaf047b2db5364963b7e0d328748afd974af59e7%2FpxbrdyW0RCvPtTLh-y8ej.jpeg?alt=media" alt=""><figcaption><p><code>"Racoon eating ice-cream"</code></p></figcaption></figure>

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-5099265cc27c7f81d95c39b71a70f95a36f94268%2FCz4d2s4FvejqwpoS4_i0C.jpeg?alt=media" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses. Vector illustration style. Top-down view, with visible palm trees, seagulls, and a strip of water."</code><br><code>"num_inference_steps": 40</code></p></figcaption></figure>

</details>
