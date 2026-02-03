# Source: https://docs.aimlapi.com/api-references/3d-generating-models/tencent/hunyuan-part.md

# Hunyuan Part

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `tencent/hunyuan-part`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/tencent/hunyuan-part" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

## Model Overview

The model analyzes a 3D mesh and performs high-fidelity, structure-coherent shape decomposition, splitting the original mesh into multiple parts that can then be used independently in 3D editors, for example for texturing or animation.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## API Schema

## POST /v1/images/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v1/images/generations":{"post":{"operationId":"_v1_images_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["tencent/hunyuan-part"]},"mesh_url":{"type":"string","format":"uri","description":"URL of the 3D model file (.glb or .obj) to process for segmentation."},"point_prompt_x":{"type":"number","minimum":-1,"maximum":1,"description":"X coordinate of the point prompt for segmentation."},"point_prompt_y":{"type":"number","minimum":-1,"maximum":1,"description":"Y coordinate of the point prompt for segmentation."},"point_prompt_z":{"type":"number","minimum":-1,"maximum":1,"description":"Z coordinate of the point prompt for segmentation."},"point_num":{"type":"integer","default":100000,"description":"Number of points to sample from the mesh."},"use_normal":{"type":"boolean","default":true,"description":"Whether to use normal information for segmentation."},"noise_std":{"type":"number","description":"Standard deviation of noise to add to sampled points."},"seed":{"type":"integer","minimum":1,"description":"The same seed and the same prompt given to the same version of the model will output the same image every time."}},"required":["model","mesh_url"],"title":"tencent/hunyuan-part"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"data":{"type":"array","nullable":true,"items":{"type":"object","properties":{"url":{"type":"string","nullable":true,"description":"The URL where the file can be downloaded from."},"b64_json":{"type":"string","nullable":true,"description":"The base64-encoded JSON of the generated image."}}},"description":"The list of generated images."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}}}}}}}}}}}
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
            "Authorization": "Bearer d09bc3015a66486e9bd4e6d1942934e1",
            "Content-Type": "application/json",
        },
        json={
            "model": "tencent/hunyuan-part",
            "mesh_url": "https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb",
        },
    )

    response.raise_for_status()
    data = response.json()

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
      model: 'tencent/hunyuan-part',
      mesh_url: 'https://storage.googleapis.com/falserverless/model_tests/video_models/base_basic_shaded.glb',
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
  "segmented_mesh": {
    "url": "https://cdn.aimlapi.com/flamingo/files/b/0a8a7d7b/gG3-a4ScI4yBswdMQ8CYQ_segmented.glb",
    "content_type": "application/octet-stream",
    "file_name": "segmented.glb",
    "file_size": 1600920
  },
  "mask_1_mesh": {
    "url": "https://cdn.aimlapi.com/flamingo/files/b/0a8a7d7b/Csp8ZOZQsxpaOtDrvbe2G_mask_1.glb",
    "content_type": "application/octet-stream",
    "file_name": "mask_1.glb",
    "file_size": 1600912
  },
  "mask_2_mesh": {
    "url": "https://cdn.aimlapi.com/flamingo/files/b/0a8a7d7b/fStkD-Pq6RZrlooYcZ34__mask_2.glb",
    "content_type": "application/octet-stream",
    "file_name": "mask_2.glb",
    "file_size": 1600920
  },
  "mask_3_mesh": {
    "url": "https://cdn.aimlapi.com/flamingo/files/b/0a8a7d7b/YVHy9A0XgUMehoLCA7z5o_mask_3.glb",
    "content_type": "application/octet-stream",
    "file_name": "mask_3.glb",
    "file_size": 1600920
  },
  "best_mask_index": 2,
  "iou_scores": [
    0.49007099866867065,
    0.5047933459281921,
    0.4866638779640198
  ],
  "seed": 3285486654,
  "requestId": "74e75e9a-7965-4348-a84d-d8663b0906dd",
  "meta": {
    "usage": {
      "credits_used": 84000
    }
  }
}
```

{% endcode %}

</details>
