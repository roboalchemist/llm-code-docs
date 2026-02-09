# Source: https://docs.aimlapi.com/api-references/3d-generating-models/stability-ai/triposr.md

# triposr

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `triposr`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/triposr" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

A transformer-based model designed for rapid 3D object reconstruction from a single RGB image, capable of generating high-quality 3D meshes in under 0.5 seconds on an NVIDIA A100 GPU.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["triposr"]},"image_url":{"type":"string","format":"uri","description":"The URL of the reference image."},"output_format":{"type":"string","enum":["glb","obj"],"default":"glb","description":"The format of the generated image."},"do_remove_background":{"type":"boolean","description":"Enables removing the background from the input image."},"foreground_ratio":{"type":"number","minimum":0.5,"maximum":1,"default":0.9,"description":"Ratio of the foreground image to the original image."},"mc_resolution":{"type":"integer","minimum":32,"maximum":1024,"default":256,"description":"Resolution of the marching cubes. Above 512 is not recommended."}},"required":["model","image_url"],"title":"triposr"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
```

## Example

{% code overflow="wrap" %}

```python
import requests


def main():
    response = requests.post(
        "https://api.aimlapi.com/v1/images/generations",
        headers={
            # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
            "Authorization": "Bearer <YOUR_AIMLAPI_KEY>",
            "Content-Type": "application/json",
        },
        json={
            "model": "triposr",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Fly_Agaric_mushroom_05.jpg/576px-Fly_Agaric_mushroom_05.jpg",
        },
    )

    response.raise_for_status()
    data = response.json()
    url = data["model_mesh"]["url"]
    file_name = data["model_mesh"]["file_name"]

    mesh_response = requests.get(url, stream=True)

    with open(file_name, "wb") as file:
        for chunk in mesh_response.iter_content(chunk_size=8192):
            file.write(chunk)


if __name__ == "__main__":
    main()
```

{% endcode %}

**Response**:

The example returns a textured 3D mesh in GLB file format. You can view it [here](https://drive.google.com/file/d/1pfA6PGgDY31rEGcoea7qoZW6uhhPYSE6/view?usp=sharing).

For clarity, we took several screenshots of our mushroom from different angles in an online GLB viewer. As you can see, the model understands the shape, but preserving the pattern on the back side (which was not visible on the reference image) could be improved:

<table data-header-hidden><thead><tr><th valign="top"></th><th></th><th></th></tr></thead><tbody><tr><td valign="top"><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-663a1db26e7cf9d546cc75d3be89b9f6d04ee7be%2Fimage.png?alt=media" alt="" data-size="original"></td><td><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-a40a0726f1ebbcbab0f537ded507f26d2466bb3f%2Fimage.png?alt=media" alt="" data-size="original"></td><td><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-042f150a465bc21b1f1cb40b8893d7570290a9f6%2Fimage.png?alt=media" alt="" data-size="original"></td></tr></tbody></table>

Compare them with the [reference image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Fly_Agaric_mushroom_05.jpg/576px-Fly_Agaric_mushroom_05.jpg):

<table data-header-hidden><thead><tr><th width="279"></th><th data-hidden></th><th data-hidden></th></tr></thead><tbody><tr><td><img src="https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-bba4302b7b2f7b1eb3990aed794237bb1a3adcf7%2F576px-Fly_Agaric_mushroom_05.jpg?alt=media" alt="" data-size="original"></td><td></td><td></td></tr></tbody></table>

{% hint style="info" %}
Try to choose reference images where the target object is not obstructed by other objects and does not blend into the background. Depending on the complexity of the object, you may need to experiment with the resolution of the reference image to achieve a satisfactory mesh.
{% endhint %}
