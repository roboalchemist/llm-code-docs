# Source: https://docs.aimlapi.com/api-references/image-models/flux/flux-kontext-max-image-to-image.md

# flux/kontext-max/image-to-image

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `flux/kontext-max/image-to-image`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/flux/kontext-max/image-to-image" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

An image-to-image model that modifies only what the prompt instructs, leaving the rest of the image untouched.

<table data-full-width="true"><thead><tr><th width="287.06671142578125">Model</th><th width="593">Properties of Generated Images</th></tr></thead><tbody><tr><td><code>flux/kontext-max/image-to-image</code></td><td>Format: <strong>JPEG, PNG</strong><br>Image size can't be set directly — only a preset aspect ratio can be chosen.<br>Default aspect ratio and size: <strong>16:9</strong>, <strong>1184</strong>x<strong>880</strong> (well, not quite 16:9)</td></tr></tbody></table>

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["flux/kontext-max/image-to-image"]},"prompt":{"type":"string","maxLength":4000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"num_images":{"type":"number","minimum":1,"maximum":4,"default":1,"description":"Number of image variations to generate. Each image is a different attempt to combine the reference images (from the image_url parameter) according to the prompt."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."},"guidance_scale":{"type":"number","minimum":1,"maximum":20,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt when looking for a related image to show you."},"safety_tolerance":{"type":"string","enum":["1","2","3","4","5","6"],"default":"2","description":"The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive."},"output_format":{"type":"string","enum":["jpeg","png"],"default":"jpeg","description":"The format of the generated image."},"aspect_ratio":{"type":"string","enum":["21:9","16:9","4:3","3:2","1:1","2:3","3:4","9:16","9:21"],"default":"16:9","description":"The aspect ratio of the generated image."},"image_url":{"anyOf":[{"type":"string","format":"uri"},{"type":"array","items":{"type":"string","format":"uri"},"maxItems":4}],"description":"One or more image URLs used as visual references. The model merges them into a single image following the prompt instructions."}},"required":["model","prompt","image_url"],"title":"flux/kontext-max/image-to-image"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's generate a new image using the one from the [flux/dev Quick Example](https://docs.aimlapi.com/api-references/image-models/flux-dev#quick-example) as a reference — and make a simple change to it with a prompt.

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
            "model": "flux/kontext-max/image-to-image",
            "image_url": "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png",  # URL of the reference picture
            "prompt": "Add a bird to the foreground of the photo.",
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
const response = await fetch('https://api.aimlapi.com/v1/images/generations', {
  method: 'POST',
  headers: {
    // Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
    'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    model: 'flux/kontext-max/image-to-image',
    prompt: 'Add a bird to the foreground of the photo.',
    image_url: 'https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/t-rex.png',        
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
      "url": "https://cdn.aimlapi.com/squirrel/files/rabbit/4LZOccB3ChjGNDi3G8zTK_202357995b8642f5b7c73925cc388b3d.jpg",
      "content_type": "image/jpeg",
      "file_name": null,
      "file_size": null,
      "width": 1184,
      "height": 880
    }
  ],
  "timings": {},
  "seed": 1415518620,
  "has_nsfw_concepts": [
    false
  ],
  "prompt": "Add a bird to the foreground of the photo."
}
```

{% endcode %}

</details>

| Reference Image                                                                                                                                                                                                                                                               | Generated Image                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-fa899176b9c4b1be07345bfea5c792a8f6480c19%2Ft-rex%20(1).png?alt=media" alt=""><figcaption></figcaption></figure></div> | <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-2cf8e4551627f3578afba9c237e480da834e5c8d%2F5HOXEk0JInhVwkMbBTEAB_4c7b647485034d03ad06cf7c58331371.jpg?alt=media" alt=""><figcaption></figcaption></figure></div> |

<details>

<summary>More generated images</summary>

| <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-58b87f8205f2c57305140352dcd452b3e6acbc53%2Fc31GyYsC9y5m4EBmRipNj_b0f30b1e73524d9abc3a1958ee1a12b6.png?alt=media" alt=""><figcaption><p><code>"Add a crown to the T-rex's head."</code></p></figcaption></figure></div>                                                                                                                                                                   | <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-0de5e65ac5fe8f6b765c220b5176aaa5e5324dd3%2Fhk-uLsRnCuJkuAh8QgOE-_19773fb3d51a40809420d6bc353cc27a.png?alt=media" alt=""><figcaption><p><code>"Add a couple of silver wings"</code></p></figcaption></figure></div>                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-129b64e9759cad1e227be31b40e579f0086b0383%2FIeAYtsCAAW0Ha5-NIASHP_a6f137e462da40bfba0044beddb9f4e9.jpg?alt=media" alt=""><figcaption><p><code>"Remove the dinosaur. Place a book and a bouquet of wildflowers in blue and pink tones on the lounge chair. Let a light foamy surf gently wash the bottom of the chair. Don't change anything else."</code></p></figcaption></figure></div> | <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-ad5143b385c9fb502bb6f646d18958971e0ec92d%2FRfnycKDno-HgrDwQI5SAe_a6b1d4e2af8b42f9a0b5df2daae563a1.jpg?alt=media" alt=""><figcaption><p><code>"Make the dinosaur sit on a lounge chair with its back to the camera, looking toward the water. The setting sun has almost disappeared below the horizon."</code></p></figcaption></figure></div> |

</details>

## Example #2: Combine two images

This time, we’ll pass two images to the model: our dinosaur and a solid blue mug. We'll ask the model to place the dinosaur onto the mug as a print.

<details>

<summary>Our input images</summary>

| <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-fa899176b9c4b1be07345bfea5c792a8f6480c19%2Ft-rex%20(1).png?alt=media" alt=""><figcaption><p>Our chilling T-rex</p></figcaption></figure></div> | <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-21cc1f1cf38504cb4c59d82e91dd184f26539e36%2Fblue-mug.jpg?alt=media" alt=""><figcaption><p>Our blue mug</p></figcaption></figure></div> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

</details>

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests
import json  # for getting a structured output with indentation

# URLs of two reference pictures
images = ["https://zovi0.github.io/public_misc/flux-dev-t-rex.png", "https://zovi0.github.io/public_misc/blue-mug.jpg"]

def main():
    response = requests.post(
        "https://api.aimlapi.com/v1/images/generations",
        headers={
            # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
            "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
            "Content-Type": "application/json",
        },
        json={
            "prompt": "Place this image with the t-rex on this mug from the second image as a print. Make it look fit and natural.",
            "model": "flux/kontext-max/image-to-image",
            "image_url": images 
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
const main = async () => {
  const response = await fetch('https://api.aimlapi.com/v1/images/generations', {
    method: 'POST',
    headers: {
      Authorization: 'Bearer <YOUR_API_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'flux/kontext-max/text-to-image',
      prompt: 'Place this image with the t-rex on this mug from the second image as a print. Make it look fit and natural.',
      image_url: ['https://zovi0.github.io/public_misc/flux-dev-t-rex.png', 'https://zovi0.github.io/public_misc/blue-mug.jpg'],
    }),
  }).then((res) => res.json());

  console.log(response);
};

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
      "url": "https://cdn.aimlapi.com/squirrel/files/zebra/DIXc328YCO52TIo5WEhXM_560d09b975e34c1498ebba71bf0e4eb6.jpg",
      "width": 1184,
      "height": 880,
      "content_type": "image/jpeg"
    }
  ],
  "timings": {},
  "seed": 2103864242,
  "has_nsfw_concepts": [
    false
  ],
  "prompt": "Place this image with the t-rex on this mug from the second image as a print. Make it look fit and natural."
}
```

{% endcode %}

</details>

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-1e495ed9004b0341d5a404e3a4ab69d06f01203c%2FDIXc328YCO52TIo5WEhXM_560d09b975e34c1498ebba71bf0e4eb6.jpg?alt=media" alt=""><figcaption><p><code>"Place this image with the t-rex on this mug from the second image as a print. Make it look fit and natural."</code></p></figcaption></figure>
