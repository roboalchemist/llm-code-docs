# Source: https://docs.aimlapi.com/api-references/image-models/topaz-labs/sharpen-generative.md

# Sharpen Generative

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `topaz-labs/sharpen-gen`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/topaz-labs/sharpen-gen" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A next-level sharpening model powered by generative AI, capable of recovering missing details during the refocusing/resharpening process.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["topaz-labs/sharpen-gen"]},"mode":{"type":"string","enum":["Super Focus","Super Focus V2"]},"image_url":{"type":"string","format":"uri","description":"The URL of the reference image."},"output_format":{"type":"string","enum":["jpeg","jpg","png","tiff","tif"],"default":"jpeg","description":"The format of the generated image."},"subject_detection":{"type":"string","enum":["All","Foreground","Background"],"default":"All","description":"Specifies which subjects to detect and process. Options: 'All' (detect all subjects), 'Foreground' (detect only foreground subjects), 'Background' (detect background subjects)."},"face_enhancement":{"type":"boolean","default":true,"description":"Whether to enhance faces in the image. When true, the model applies face-specific improvements."},"face_enhancement_creativity":{"type":"number","minimum":0,"maximum":1,"default":0,"description":"Level of creativity for face enhancement (0-1). Higher values allow more creative, less conservative changes."},"face_enhancement_strength":{"type":"number","minimum":0,"maximum":1,"default":0.8,"description":"How sharp enhanced faces are relative to background (0-1). Lower values blend changes subtly; higher values make faces more pronounced."},"strength":{"type":"number","minimum":0,"maximum":1,"description":"Defines the overall intensity of the sharpening effect. Increases details. Too much sharpening can create an unrealistic result."},"focus_boost":{"type":"number","minimum":0.25,"maximum":1,"description":"Corrects images that are missing detail by downscaling your image then upscaling the results back to the original size. Use on very blurry images!"},"seed":{"type":"integer","description":"Optional fixed seed for repeatable results."}},"required":["model","mode","image_url"],"title":"topaz-labs/sharpen-gen"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's sharpen a relatively strongly blurred image using the *Strong* mode while adjusting the *strength* parameter.

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
          "model": "topaz-labs/sharpen",
          "image_url": "https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/blurred-landscape.png",
          "mode": "Super Focus V2",
          "strength": 0.6,
          "output_format": "jpeg",
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
        model: 'topaz-labs/sharpen',
        image_url: 'https://raw.githubusercontent.com/aimlapi/api-docs/main/reference-files/blurred-landscape.png',
        mode: 'Super Focus V2',
        strength: 0.6,
        output_format: 'jpeg',
      }),
    });
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
      "url": "https://cdn.aimlapi.com/komodo/output/6435616/5cff080e-5d24-4fc3-85f5-0e57621ead7d.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ccc352dcd71a436e5fd697125a1be9f8%2F20251027%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20251027T202819Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=d6d1d9c641c33bde33b14090d579d490d30f75e82283764705acd28b18765a70"
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

<table data-full-width="true"><thead><tr><th valign="top">Blurred Image</th><th valign="top">Deblurred Image</th><th></th></tr></thead><tbody><tr><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-24bf0e440d3c31fa4a1073a2c09a57aa9872c43a%2Fblurred-face.jpeg?alt=media" alt=""><figcaption></figcaption></figure></div></td><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-8cbbc9ba27152f13434e3465a4f721230fc26359%2F5cff080e-5d24-4fc3-85f5-0e57621ead7d.jpeg?alt=media" alt=""><figcaption><p>"mode": "Super Focus V2"<br>"strength": 0.6</p></figcaption></figure></div></td><td></td></tr></tbody></table>
