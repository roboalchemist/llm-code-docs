# Source: https://docs.baseten.co/examples/models/flux/flux-schnell.md

# Flux-Schnell

> Flux-Schnell is a state-of-the-art image generation model

export const BFLIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M0 20.683L12.01 2.5L24 20.683H21.767L12.009 5.878L3.471 18.806H15.593L16.832 20.683H0Z" fill="black" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M8.069 16.724L10.142 13.609L12.216 16.724H8.069ZM18.24 20.683L12.572 11.976H14.749L20.435 20.683H18.24ZM19.74 11.676L21.87 8.48602L24 11.676H19.74Z" fill="black" />
</svg>} horizontal />;

<BFLIconCard title="Deploy Flux-Schnell" href="https://app.baseten.co/deploy/flux.1-schnell" />

## Example usage

The model accepts a `prompt` which is some text describing the image you want to generate. The output images tend to get better as you add more descriptive words to the prompt.

The output JSON object contains a key called `data` which represents the generated image as a base64 string.

### Input

```python  theme={"system"}
import httpx
import os
import base64
from PIL import Image
from io import BytesIO
# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
# Function used to convert a base64 string to a PIL image
def b64_to_pil(b64_str):
    return Image.open(BytesIO(base64.b64decode(b64_str)))
data = {
  "prompt": 'red velvet cake spelling out the words "FLUX SCHNELL", tasty, food photography, dynamic shot'
}
# Call model endpoint
res = httpx.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)
# Get output image
res = res.json()
output = res.get("data")
# Convert the base64 model output to an image
img = b64_to_pil(output)
img.save("output_image.jpg")
```

### JSON output

```json  theme={"system"}
{
  "output": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAA..."
}
```
