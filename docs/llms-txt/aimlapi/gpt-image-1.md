# Source: https://docs.aimlapi.com/api-references/image-models/openai/gpt-image-1.md

# gpt-image-1

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `openai/gpt-image-1`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/openai/gpt-image-1" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A powerful multimodal model capable of generating new images, combining existing ones, and applying image masks — all guided by a text prompt.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schemas

{% hint style="info" %}
Note that by default, the `quality` parameter is set to `'medium'`. The output image will still look great, but for even more detailed results, consider setting this parameter to `'high'`.
{% endhint %}

### Generate image

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["openai/gpt-image-1"]},"prompt":{"type":"string","maxLength":32000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"background":{"type":"string","enum":["transparent","opaque","auto"],"default":"auto","description":"Allows to set transparency for the background of the generated image(s). When auto is used, the model will automatically determine the best background for the image.\nIf transparent, the output format needs to support transparency, so it should be set to either png (default value) or webp."},"moderation":{"type":"string","enum":["low","auto"],"default":"auto","description":"Control the content-moderation level for images."},"n":{"type":"number","enum":[1],"default":1,"description":"The number of images to generate."},"output_compression":{"type":"integer","minimum":0,"maximum":100,"default":100,"description":"The compression level (0-100%) for the generated images."},"output_format":{"type":"string","enum":["png","jpeg","webp"],"default":"png","description":"The format of the generated image."},"quality":{"type":"string","enum":["low","high","medium"],"default":"medium","description":"The quality of the image that will be generated."},"size":{"type":"string","enum":["1024x1024","1024x1536","1536x1024"],"default":"1024x1024","description":"The size of the generated image."},"response_format":{"type":"string","enum":["url","b64_json"],"default":"url","description":"The format in which the generated images are returned."}},"required":["model","prompt"],"title":"openai/gpt-image-1"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

### Edit image

{% hint style="warning" %}
Unfortunately, this model only accepts local files specified by their file paths.\
It does not support image input via URLs or base64 encoding.
{% endhint %}

## POST /v1/images/edits

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"security":[{"access-token":[]}],"components":{"securitySchemes":{"access-token":{"scheme":"bearer","bearerFormat":"<YOUR_AIMLAPI_KEY>","type":"http","description":"Bearer key"}},"schemas":{"Image.v1.EditImageDTO":{"type":"object","properties":{"model":{"type":"string","enum":["openai/gpt-image-1","openai/gpt-image-1-mini"]},"prompt":{"type":"string","maxLength":32000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"image":{"type":"string","description":"The image(s) to edit. Must be a supported image file or an array of images. Each image should be a png, webp, or jpg file less than 50MB. You can provide up to 16 images.","format":"binary"},"mask":{"type":"string","description":"An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where image should be edited. If there are multiple images provided, the mask will be applied on the first image. Must be a valid PNG file, less than 4MB, and have the same dimensions as image.","format":"binary"},"background":{"type":"string","enum":["transparent","opaque","auto"],"default":"auto","description":"Allows to set transparency for the background of the generated image(s). When auto is used, the model will automatically determine the best background for the image.\nIf transparent, the output format needs to support transparency, so it should be set to either png (default value) or webp."},"n":{"type":"number","minimum":1,"maximum":10,"default":1,"description":"The number of images to generate."},"output_compression":{"type":"integer","minimum":0,"maximum":100,"default":100,"description":"The compression level (0-100%) for the generated images."},"output_format":{"type":"string","enum":["png","jpeg","webp"],"default":"png","description":"The format of the generated image."},"quality":{"type":"string","enum":["low","medium","high"],"default":"medium","description":"The quality of the image that will be generated."},"size":{"type":"string","enum":["1024x1024","1024x1536","1536x1024"],"default":"1024x1024","description":"The size of the generated image."},"response_format":{"type":"string","enum":["url","b64_json"],"default":"url","description":"The format in which the generated images are returned."}},"required":["model","prompt","image"]},"Image.v1.GenerateImageResponseDTO":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}},"paths":{"/v1/images/edits":{"post":{"operationId":"ImageEditingController_editImage_v1","parameters":[],"requestBody":{"required":true,"content":{"application/json":{"schema":{"$ref":"#/components/schemas/Image.v1.EditImageDTO"}}}},"responses":{"201":{"description":"Successfully edited image","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Image.v1.GenerateImageResponseDTO"}}}}},"tags":["Images"]}}}}
```

## Quick Examples

### Generate image

Let's generate an image of the specified size using a simple prompt.

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
            "prompt": "Add a crown",
            "model": "openai/gpt-image-1",
            "size": "1024x1024"
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
      model: 'openai/gpt-image-1',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses. Realistic photo.',
      size: '1536x1024'
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
  "created": 1749730922,
  "background": "opaque",
  "data": [
    {
      "url": "https://cdn.aimlapi.com/generations/hedgehog/1749730923700-29fe35d2-4aef-4bc5-a911-6c39884d16a8.png"
    }
  ],
  "output_format": "png",
  "quality": "medium",
  "size": "1536x1024",
  "usage": {
    "input_tokens": 29,
    "input_tokens_details": {
      "image_tokens": 0,
      "text_tokens": 29
    },
    "output_tokens": 1568,
    "total_tokens": 1597
  }
}
```

{% endcode %}

</details>

We obtained the following 1536x1024 image by running this code example (\~ 26 s):

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-6a3ae3128311202004180fbe5561263e9cf858dd%2Ft-rex.png?alt=media" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses. Realistic photo."</code></p></figcaption></figure>

<details>

<summary>More images</summary>

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-b29cd9abafb1ba519659c28b174eaff8e780245a%2F1749730482361-dd6507ff-57da-4077-8774-735936749de9.png?alt=media" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses."</code></p></figcaption></figure>

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-4c67cc7327c0ba7884e15615a651d7b8781d7310%2F1749730310081-78afd54b-e184-485a-9864-98026eadbc76.png?alt=media" alt=""><figcaption><p><code>"Racoon eating ice-cream"</code></p></figcaption></figure>

</details>

### Edit image: Combine images

Let's generate an image using two input images and a prompt that defines how they should be edited.

<details>

<summary>Our input images</summary>

| <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-6a3ae3128311202004180fbe5561263e9cf858dd%2Ft-rex.png?alt=media" alt=""><figcaption><p>t-rex.png</p></figcaption></figure></div> | <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-09c57c1409a7511463742b3cce295e7adccb3ee1%2Fcrown.png?alt=media" alt=""><figcaption><p>crown.png</p></figcaption></figure></div> |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

</details>

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
from openai import OpenAI


def main():
    client = OpenAI(
        api_key="<YOUR_AIMLAPI_KEY>",
        base_url="https://api.aimlapi.com/v1",
    )

    result = client.images.edit(
        model="openai/gpt-image-1",
        image=[
            open("t-rex.png", "rb"),
            open("crown.png", "rb"),
        ],
        prompt="Put the crown on the T-rex's head"
    )

    print("Generation:", result)


if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
import fs from 'fs';
import OpenAI, { toFile } from 'openai';


const main = async () => {
  const client = new OpenAI({
    baseURL: 'https://api.aimlapi.com/v1',
    apiKey: '<YOUR_API_KEY>',
  });

  const imageFiles = ['t-rex.png', 'crown.png'];

  const images = await Promise.all(
    imageFiles.map(
      async (file) =>
        await toFile(fs.createReadStream(file), null, {
          type: 'image/png',
        }),
    ),
  );

  const result = await client.images.edit({
    model: 'openai/gpt-image-1',
    image: images,
    prompt: "Put the crown on the T-rex's head",
  });

  console.log('Generation', result);
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
Generation: ImagesResponse(created=1750278299, data=[Image(b64_json=None, revised_prompt=None, url='https://cdn.aimlapi.com/generations/hedgehog/1750278300281-023df523-e986-431c-bb61-5b9e43301cef.png')], usage=Usage(input_tokens=574, input_tokens_details=UsageInputTokensDetails(image_tokens=517, text_tokens=57), output_tokens=1056, total_tokens=1630), background='opaque', output_format='png', quality='medium', size='1024x1024')
```

{% endcode %}

</details>

We obtained the following 1024x1024 image by running this code example (\~ 34 s):

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-c7b7fe0004754424a5f3e6812a349f5018d8ccf4%2F1750278300281-023df523-e986-431c-bb61-5b9e43301cef.png?alt=media" alt=""><figcaption><p>A true king of the monsters. On vacation.</p></figcaption></figure>

### Edit image: Use an image mask

In this example, we’ll provide the model with our previously generated image of a T-rex on a beach, along with a same-sized mask where the area occupied by the dinosaur is transparent (alpha = 0). In the prompt, we’ll ask the model to remove the masked object from the image and see how well it handles the task.

<details>

<summary>Image &#x26; Mask</summary>

| <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-6a3ae3128311202004180fbe5561263e9cf858dd%2Ft-rex.png?alt=media" alt=""><figcaption><p>Image</p></figcaption></figure></div> | <div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-1beed34b94011226092fc688a679ff6bc8aa6a8a%2Ft-rex-alpha_mask.png?alt=media" alt=""><figcaption><p>Mask</p></figcaption></figure></div> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

</details>

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
from openai import OpenAI


def main():
    client = OpenAI(
        api_key="<YOUR_AIMLAPI_KEY>",
        base_url="https://api.aimlapi.com/v1",
    )

    result = client.images.edit(
        model="openai/gpt-image-1",
        image=open("t-rex.png", "rb"),
        mask=open('t-rex-alpha_mask.png', 'rb'),
        prompt="Remove this from the picture"
    )

    print("Generation:", result)


if __name__ == "__main__":
    main()
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```python
import fs from 'fs';
import OpenAI, { toFile } from 'openai';


const main = async () => {
  const client = new OpenAI({
    baseURL: 'https://api.aimlapi.com/v1',
    apiKey: '<YOUR_AIMLAPI_KEY>',
  });

  const image = await toFile(
    fs.createReadStream('t-rex.png'),
    null,
    {
      type: 'image/png',
    },
  );
  
  const mask = await toFile(
    fs.createReadStream('t-rex-alpha_mask.png'),
    null,
    {
      type: 'image/png',
    },
  );

  const result = await client.images.edit({
    model: 'openai/gpt-image-1',
    image: image,
    mask: mask,
    prompt: 'Remove this from the picture',
  });

  console.log('Generation', result);
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
Generation: ImagesResponse(created=1750275775, data=[Image(b64_json=None, revised_prompt=None, url='https://cdn.aimlapi.com/generations/hedgehog/1750275776080-3fbcf9fc-b8ec-47f1-bb77-4a7e370a3a0c.png')], usage=Usage(input_tokens=360, input_tokens_details=UsageInputTokensDetails(image_tokens=323, text_tokens=37), output_tokens=1056, total_tokens=1416), background='opaque', output_format='png', quality='medium', size='1024x1024')
```

{% endcode %}

</details>

We obtained the following 1024x1024 image by running this code example (\~ 32 s).

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-e10c174a07ad8c49b038e82802eb75d5236fcf1b%2F1750276983662-c46a4f81-4b85-4e74-b5bf-9866c210de25.png?alt=media" alt=""><figcaption><p>Our dinosaur has disappeared into thin air!</p></figcaption></figure>
