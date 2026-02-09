# Source: https://docs.aimlapi.com/api-references/image-models/openai/gpt-image-1-mini-1.md

# gpt-image-1-5

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `openai/gpt-image-1-5`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/?model=openai/gpt-image-1-5" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A powerful image generation and editing model that supports text-to-image, image-to-image, and inpainting with masks and reference inputs — all guided by a text prompt.

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

:digit\_one: **Setup You Can’t Skip**

:black\_small\_square: [**Create an Account**](https://aimlapi.com/app/sign-up): Visit the AI/ML API website and create an account (if you don’t have one yet). :black\_small\_square: [**Generate an API Key**](https://aimlapi.com/app/keys): After logging in, navigate to your account dashboard and generate your API key. Ensure the key is enabled on the UI.

:digit\_two: **Copy the code example**

At the bottom of this page, you'll find a code example that shows how to structure the request. Choose the code snippet in your preferred programming language and copy it into your development environment.

:digit\_three: **Modify the code example**

:black\_small\_square: Replace `<YOUR_AIMLAPI_KEY>` with your actual AI/ML API key. :black\_small\_square: Adjust the input field used by this model (for example, prompt, input text, instructions, media source, or other model-specific input) to match your request.

:digit\_four: <sup><sub><mark style="background-color:yellow;">**(Optional)**<mark style="background-color:yellow;"><sub></sup> **Adjust other optional parameters if needed**

Only the required parameters shown in the example are needed to run the request, but you can include optional parameters to fine-tune behavior. Below, you can find the corresponding **API schema**, which lists all available parameters and usage notes.

:digit\_five: **Run your modified code**

Run your modified code inside your development environment. Response time depends on many factors, but for simple requests it rarely exceeds a few seconds.

{% hint style="success" %}
If you need a more detailed walkthrough for setting up your development environment and making a request step-by-step, feel free to use our [**Quickstart guide.**](https://docs.aimlapi.com/quickstart/setting-up)
{% endhint %}

</details>

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"GPT-Image-1.5 - AI/ML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["openai/gpt-image-1-5"]},"prompt":{"type":"string","maxLength":32000,"description":"The text prompt describing the content, style, or composition of the image to be generated."},"background":{"type":"string","enum":["transparent","opaque","auto"],"default":"auto","description":"Allows to set transparency for the background of the generated image(s). When auto is used, the model will automatically determine the best background for the image.\nIf transparent, the output format needs to support transparency, so it should be set to either png (default value) or webp."},"moderation":{"type":"string","enum":["low","auto"],"default":"auto","description":"Control the content-moderation level for images."},"n":{"type":"number","enum":[1],"default":1,"description":"The number of images to generate."},"output_compression":{"type":"integer","minimum":0,"maximum":100,"default":100,"description":"The compression level (0-100%) for the generated images."},"output_format":{"type":"string","enum":["png","jpeg","webp"],"default":"png","description":"The format of the generated image."},"quality":{"type":"string","enum":["low","high","medium"],"default":"medium","description":"The quality of the image that will be generated."},"size":{"type":"string","enum":["1024x1024","1024x1536","1536x1024"],"default":"1024x1024","description":"The size of the generated image."},"response_format":{"type":"string","enum":["url","b64_json"],"default":"url","description":"The format in which the generated images are returned."}},"required":["model","prompt"],"title":"openai/gpt-image-1-5"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Code Example

{% tabs %}
{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

response = requests.post(
    "https://api.aimlapi.com/v1/images/generations",
    headers={
        "Content-Type":"application/json",
        "Authorization":"Bearer <YOUR_AIMLAPI_KEY>",
    },
    json={
        "model":"openai/gpt-image-1-5",
        "prompt": "A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses."
    }
)

data = response.json()
print(data)
```

{% endcode %}
{% endtab %}

{% tab title="JavaScript" %}
{% code overflow="wrap" %}

```javascript
async function main() {
  const response = await fetch('https://api.aimlapi.com/v1/images/generations', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer <YOUR_AIMLAPI_KEY>',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: 'openai/gpt-image-1-5',
      prompt: 'A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses.',
    }),
  });

  const data = await response.json();
  console.log(JSON.stringify(data, null, 2));
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
  'id': 'gen-1733832000-example',
  'object': 'image',
  'created': 1733832000,
  'model': 'openai/gpt-image-1-5',
  'data': [
    {
      'url': 'https://cdn.aimlapi.com/generated-images/openai/gpt-image-1-5/example-output.png',
      'revised_prompt': 'Example output for documentation.'
    }
  ],
  'usage': {
    'prompt_tokens': 0,
    'completion_tokens': 0,
    'total_tokens': 0
  }
}
```

{% endcode %}

</details>

We obtained the following 1536×1024 image by running this code example (\~26 s):

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2FlxDa573ZHlycCcaSn9RV%2F1765998570696-6a7fa56d-b5ba-4f29-ba20-501aa08a4273.png?alt=media&#x26;token=4af10999-818f-4056-be2d-b2ceef83bd74" alt=""><figcaption><p><code>"A T-Rex relaxing on a beach, lying on a sun lounger and wearing sunglasses. Realistic photo."</code></p></figcaption></figure>
