# Source: https://docs.aimlapi.com/api-references/image-models/topaz-labs/sharpen.md

# Sharpen

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `topaz-labs/sharpen`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/topaz-labs/sharpen" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

The model produces sharper visuals, eliminating blur and improving clarity across the subject or the entire frame.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["topaz-labs/sharpen"]},"mode":{"type":"string","enum":["Standard","Strong","Lens Blur","Lens Blur V2","Motion Blur","Natural","Refocus"]},"image_url":{"type":"string","format":"uri","description":"The URL of the reference image."},"output_format":{"type":"string","enum":["jpeg","jpg","png","tiff","tif"],"default":"jpeg","description":"The format of the generated image."},"subject_detection":{"type":"string","enum":["All","Foreground","Background"],"default":"All","description":"Specifies which subjects to detect and process. Options: 'All' (detect all subjects), 'Foreground' (detect only foreground subjects), 'Background' (detect background subjects)."},"face_enhancement":{"type":"boolean","default":true,"description":"Whether to enhance faces in the image. When true, the model applies face-specific improvements."},"face_enhancement_creativity":{"type":"number","minimum":0,"maximum":1,"default":0,"description":"Level of creativity for face enhancement (0-1). Higher values allow more creative, less conservative changes."},"face_enhancement_strength":{"type":"number","minimum":0,"maximum":1,"default":0.8,"description":"How sharp enhanced faces are relative to background (0-1). Lower values blend changes subtly; higher values make faces more pronounced."},"strength":{"type":"number","minimum":0.01,"maximum":1,"description":"Defines the overall intensity of the sharpening effect. Increases details. Too much sharpening can create an unrealistic result."},"minor_denoise":{"type":"number","minimum":0.01,"maximum":1,"description":"Removes noisy pixels to increase clarity. Can slightly increase image sharpness."}},"required":["model","mode","image_url"],"title":"topaz-labs/sharpen"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Quick Example

Let's sharpen a relatively strongly blurred image using the `Strong` mode while adjusting the `strength` parameter.

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
          "mode": "Strong",
          "strength": 0.9,
          "minor_denoise": 0.9,
          "output_format": "png",
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
        mode: 'Strong',
        strength: 0.9,
        minor_denoise: 0.9,
        output_format: 'png',
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
      "url": "https://cdn.aimlapi.com/komodo/output/6435616/ddb723c4-ed16-42f4-8818-9ca4de176ea7.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Checksum-Mode=ENABLED&X-Amz-Credential=ccc352dcd71a436e5fd697125a1be9f8%2F20251027%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20251027T162246Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=4f4c449772b258bcf53e7257444698e2e486832e77ab5835728afc4aabfa0f8c"
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

<table data-full-width="true"><thead><tr><th valign="top">Blurred Image</th><th valign="top">Deblurred Image</th><th></th></tr></thead><tbody><tr><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-dba15d4f779e5be0087d16598af19df347b2c714%2Fblurred-landscape.png?alt=media" alt=""><figcaption></figcaption></figure></div></td><td valign="top"><div><figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-1fd6b0f5bcc18b2210778ab8c511410bfce27eaa%2Fsharpen_strength_0.9.png?alt=media" alt=""><figcaption><p>"mode": "Strong"<br>"strength": 0.9</p></figcaption></figure></div></td><td></td></tr></tbody></table>

For clarity, we’ve created a split image showing the results of different parameter settings.

<figure><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a9e0261d11a8f3d4902f086e7cd7852df772af72%2Ftriple-with-statements.png?alt=media" alt=""><figcaption></figcaption></figure>
