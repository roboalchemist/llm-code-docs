# Source: https://docs.verda.com/inference/image-models/flux2.md

# FLUX.2

## Overview

FLUX.2 is a completely new base model from Black Forest Labs, trained for visual intelligence, not just pixel generation, setting a new standard for both image generation and image editing. With FLUX.2 models you can expect the highest quality, higher resolutions (up to 4MP), and new capabilities like multi-ref images.

Text-to-image prompting with FLUX.2 gives a high degree of control over different aspects of output, such as subject, action, style, and context. FLUX.2 is trained to understand structured JSON prompts and allows the use of HEX codes to describe object color palettes.

FLUX.2 similarly advances image-to-image editing. The model's core capabilities cover a wide range of editing tasks, from composite edits with reference inputs and natural language to precise edits such as color change.

FLUX.2 comes in multiple different versions that we offer.

#### FLUX.2 \[dev]

The new base model from Black Forest Labs, trained to set a new standard for image generation and image editing.

An ultra-fast and cost-efficient inference endpoint by Verda - ensuring secure access and seamless integration with API.

The endpoint for FLUX.2 \[dev] is **inference.datacrunch.io/flux2-dev/runsync**. See examples below.

#### FLUX.2 \[flex]

A variant of FLUX.2 that offers the highest output quality and character consistency at the expense of higher latency.

Available via the Verda Cloud Platform, running on the Black Forest Labs infrastructure.

The endpoint for FLUX.2 \[flex] is **relay.datacrunch.io/bfl/flux-2-flex**. The endpoint can be used with examples below by just replacing the endpoint URL.

#### FLUX.2 \[pro]

A variant of FLUX.2 that emphasizes output quality over inference speed, delivering the highest possible quality in image generation and editing.

Available via the Verda Cloud Platform, running on the Black Forest Labs infrastructure.

The endpoint for FLUX.2 \[pro] is **relay.datacrunch.io/bfl/flux-2-pro**. The endpoint can be used with examples below by just replacing the endpoint URL.

### **Getting Started**

Before generating images, make sure your account is ready to use the Inference API. Follow the [Getting Started](https://docs.verda.com/inference/getting-started) guide to create an account and top up your balance.

### Authorization

To access and use these API endpoints, authorization is required. Please visit our [Authorization page](https://docs.verda.com/inference/authorization) for detailed instructions on obtaining and using a bearer token for secure API access.

## Generating images

### Image to image

{% tabs %}
{% tab title="cURL" %}

```bash
INPUT_BASE64="data:image/png;base64,$(base64 -i <your_picture>.png)"
read -r -d '' PAYLOAD <<EOF
{
  "prompt": "Replace the color of the car to blue",
  "reference_images": [
    "$INPUT_BASE64"
  ]
  "steps": 50,
  "guidance": 3.0
}
EOF
curl --request POST "https://inference.datacrunch.io/flux2-dev/runsync" \
--header "Content-Type: application/json" \
--header "Authorization: Bearer <your_api_key>" \
--data "$PAYLOAD"
```

{% endtab %}

{% tab title="Python" %}

```python
import requests
import os
import base64
from PIL import Image
from io import BytesIO

token = <your_api_key>
bearer_token = f"Bearer {token}"

url = "https://inference.datacrunch.io/flux2-dev/runsync"
headers = {
    "Content-Type": "application/json",
    "Authorization": bearer_token
}

image = Image.open("green_car.png")
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = base64.b64encode(buffered.getvalue()).decode()

data = {
    "prompt": "Replace the color of the car to blue",
    "output_format": "jpeg",
    "reference_images": [ img_str ],
    "steps": 50,
    "guidance": 3.0,
    "enable_base64_output": True
}

resp = requests.post(url, headers=headers, json=data)
resp.raise_for_status()

ct = resp.headers.get("Content-Type", "")
outfile = "picture.png"

if ct.startswith("image/"):
    with open(outfile, "wb") as f:
        f.write(resp.content)
    print(f"Saved raw image to {outfile}")
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const axios = require('axios');
const fs = require('fs');

const url = 'https://inference.datacrunch.io/flux2-dev/runsync';
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <your_api_key>'
};
const data = {
  promp": "Replace the color of the car to blue",
  output_format: "jpeg",
  reference_images: [
    "https://img.freepik.com/free-psd/black-isolated-car_23-2151852894.jpg?semt=ais_hybrid&w=740&q=80"
  ],
  steps: 50,
  guidance: 3.0,
  enable_base64_output: true
};

axios.post(url, data, {
    headers,
    responseType: 'arraybuffer'
  })
  .then(response => {
    fs.writeFileSync('picture.png', response.data);
    console.log('Saved image to picture.png');
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

{% endtab %}
{% endtabs %}

### Text to image

{% tabs %}
{% tab title="cURL" %}

```bash
curl --request POST "https://inference.datacrunch.io/flux2-dev/runsync" \
--header "Content-Type: application/json" \
--header "Authorization: Bearer <your_api_key>" \
--data '{
  "prompt": "cat in a spacesuit flying over moon"
}'
```

{% endtab %}

{% tab title="Python" %}

```python
import os
import requests

token = <your_api_key>
bearer_token = f"Bearer {token}"

url = "https://inference.datacrunch.io/flux2-dev/runsync"
headers = {
    "Content-Type": "application/json",
    "Authorization": bearer_token
}

data = {
    "prompt": "a scientist racoon eating icecream in a datacenter",
    "enable_base64_output": True,
}

resp = requests.post(url, headers=headers, json=data)
resp.raise_for_status()

ct = resp.headers.get("Content-Type", "")
outfile = "picture.png"

if ct.startswith("image/"):
    with open(outfile, "wb") as f:
        f.write(resp.content)
    print(f"Saved raw image to {outfile}")
```

{% endtab %}

{% tab title="JavaScript" %}

```javascript
const axios = require('axios');

const url = 'https://inference.datacrunch.io/flux2-dev/runsync';
const headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <your_api_key>'
};
const data = {
  prompt: 'a scientist racoon eating icecream in a datacenter',
  enable_base64_output: true
};

axios.post(url, data, {
    headers,
    responseType: 'arraybuffer'
  })
  .then(response => {
    fs.writeFileSync('picture.png', response.data);
    console.log('Saved image to picture.png');
  })
  .catch(error => {
    console.error('Error:', error);
  });
```

{% endtab %}
{% endtabs %}
