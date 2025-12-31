# Source: https://docs.aimlapi.com/api-references/image-models/alibaba-cloud/z-image-turbo-lora.md

# z-image-turbo-lora

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `alibaba/z-image-turbo-lora`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/alibaba/z-image-turbo-lora" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

An ultra-fast 6B-parameter text-to-image model with LoRA[^1] support \
(see [a separate example](#example-2-text-to-image-with-lora-fine-tuning) of how to use it).

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["alibaba/z-image-turbo-lora"]},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"image_size":{"anyOf":[{"type":"object","properties":{"width":{"type":"integer","minimum":512,"maximum":2048,"default":1024},"height":{"type":"integer","minimum":512,"maximum":2048,"default":768}},"description":"For both height and width, the value must be a multiple of 32."},{"type":"string","enum":["square_hd","square","portrait_4_3","portrait_16_9","landscape_4_3","landscape_16_9"],"description":"The size of the generated image."}],"default":"landscape_4_3"},"output_format":{"type":"string","enum":["jpeg","png","webp"],"default":"png","description":"The format of the generated image."},"enable_prompt_expansion":{"type":"boolean","default":true,"description":"If set to True, prompt will be upsampled with more details."},"num_inference_steps":{"type":"integer","minimum":1,"maximum":8,"description":"The number of inference steps to perform."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"The number of images to generate."},"enable_safety_checker":{"type":"boolean","default":true,"description":"If set to True, the safety checker will be enabled."},"acceleration":{"type":"string","enum":["none","regular","high"],"default":"regular","description":"The speed of the generation. The higher the speed, the faster the generation."},"loras":{"type":"array","items":{"type":"object","properties":{"path":{"type":"string","description":"URL, HuggingFace repo ID (owner/repo)."},"scale":{"type":"number","minimum":0,"maximum":4,"description":"Scale factor for LoRA application."}},"required":["path"]},"maxItems":3,"description":"List of LoRA weights to apply (maximum 3). Each LoRA can be a URL, HuggingFace repo ID, or local path."}},"required":["model","prompt"],"title":"alibaba/z-image-turbo-lora"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Example #1: Standard Text-to-Image

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
            "model": "alibaba/z-image-turbo-lora",
            "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.",
            "image_size": {
                "width": 1440,
                "height": 512
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
      model: 'alibaba/z-image-turbo-lora',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.',
      image_size: {
        width: 1440,
        height: 512
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

```json5
{
  "data": [
    {
      "url": "https://cdn.aimlapi.com/flamingo/files/b/0a84de54/-IaUBYEQiYqRaeT7oZvus.png"
    }
  ],
  "meta": {
    "usage": {
      "tokens_used": 17850
    }
  }
}
```

{% endcode %}

</details>

We obtained the following 1440x512 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FxmsEpB3nHJLQk6TM3x2k%2F-IaUBYEQiYqRaeT7oZvus.png?alt=media&#x26;token=3602bda6-94e3-4543-8b88-de35962d99d0" alt=""><figcaption></figcaption></figure>

***

## Example #2: Text-to-Image with LoRA Fine-Tuning

The `alibaba/z-image-turbo-lora` model supports applying up to three LoRA adapters to modify the style or behavior of the base model.

The `loras` parameter is an **array of objects**, not strings. Each object describes a single LoRA:

* `path` — where to load the LoRA from (Hugging Face repo ID, direct URL to the weights file, or local path).
* `scale` — how strongly this LoRA should influence the result (typically between `0.6` and `1.0`).

<details>

<summary>Community LoRAs on Hugging Face that are compatible with Z-Image Turbo</summary>

**Style LoRAs**

* `renderartist/Classic-Painting-Z-Image-Turbo-LoRA` – classic oil painting / “old masters” look, museum-like style.
* `renderartist/Coloring-Book-Z-Image-Turbo-LoRA` – “coloring book” style with clear outlines and flat fills, good for children’s illustrations and icons.
* `ostris/z_image_turbo_childrens_drawings` — a stylish LoRA adaptation for generating artistic children's drawings.&#x20;
* `renderartist/Technically-Color-Z-Image-Turbo` – vivid, cinematic Technicolor-style colors and dramatic lighting.
* `suayptalha/Z-Image-Turbo-Realism-LoRA` – boosts photorealism; includes the trigger word `Realism`.
* `AlekseyCalvin/HistoricColor_Z-image-Turbo-LoRA` – historical early-1900s color photography inspired by three-color processes.
* `MGRI/Z-Image-Turbo-Panyue-Lora` – character LoRA for the digital persona **Panyue** (triggers: `Panyue`, `潘悦`).

**Technical / utility LoRAs**

* `GuangyuanSD/Z-Image-Re-Turbo-LoRA` – Re-Turbo adapter that restores Turbo-level speed while behaving like a de-turbo model for training and advanced workflows.
* `ostris/zimage_turbo_training_adapter` – training adapter / de-distill LoRA used as a base for building new LoRAs on top of Z-Image Turbo.

</details>

***

Let's generate an image using a LoRA to influence the visual style.

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
            "model": "alibaba/z-image-turbo-lora",
            "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.",
            "image_size": {
                "width": 1440,
                "height": 512
            },
            "loras":[
                {
                  "path": "ostris/z_image_turbo_childrens_drawings",
                  "scale": 0.85
                }
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
      model: 'alibaba/z-image-turbo-lora',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.',
      image_size: {
        width: 1440,
        height: 512
      },
      loras:[
        {
          path: 'ostris/z_image_turbo_childrens_drawings',
          scale: 0.85
        }
      ]
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
{
  "data": [
    {
      "url": "https://cdn.aimlapi.com/flamingo/files/b/0a85ed1b/j-z8clom9AqL_2ZTsGygk.png"
    }
  ],
  "meta": {
    "usage": {
      "credits_used": 17850
    }
  }
}
```

{% endcode %}

</details>

We obtained the following 1440x512 image by running this code example:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FqZUs92FJ695C8XtVvcEC%2Fj-z8clom9AqL_2ZTsGygk.png?alt=media&#x26;token=e3d7a03d-ce77-41c4-9ea6-cfb809f35787" alt=""><figcaption></figcaption></figure>

The scale parameter significantly affects the output. The previous example was generated with `scale` = `0.85`, and here’s what happens when we increase it to `1.0`:

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FYABgNREgJQFbAgbDMLip%2FyYDEEEN5bzcsn-6MeiHHM.png?alt=media&#x26;token=bc84d8a2-2aab-4730-8fb4-3ecd477ec6c9" alt=""><figcaption></figcaption></figure>

[^1]: The **LoRA algorithm** (Low-Rank Adaptation) is a parameter-efficient fine-tuning technique used to adapt large language models (LLMs) and stable diffusion models to new tasks or domains without retraining the entire model. This process is faster and requires significantly less memory and computational resources than full fine-tuning.
