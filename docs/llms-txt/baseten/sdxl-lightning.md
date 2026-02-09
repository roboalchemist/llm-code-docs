# Source: https://docs.baseten.co/examples/models/stable-diffusion/sdxl-lightning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# SDXL Lightning

> A variant of Stable Diffusion XL that generates 1024x1024 px images in 4 UNet steps, enabling near real-time image creation.

export const LightningIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M14.944 18.587L13.24 18.142V10.01L15.064 9.54801C16.064 9.29401 16.904 9.08701 16.944 9.09501C16.976 9.09501 17 11.33 17 14.067V19.04L16.824 19.032C16.72 19.032 15.872 18.826 14.944 18.587Z" fill="#00C8D2" />
<path d="M7 16.5421C7 13.8061 7.024 11.5621 7.064 11.5621C7.096 11.5541 7.936 11.7621 8.944 12.0161L10.76 12.4771L10.744 16.5271L10.72 20.5761L9.088 20.9981C8.192 21.2281 7.352 21.4431 7.232 21.4671L7 21.5231V16.5421Z" fill="#3C8CFF" />
<path d="M19.24 12.477C19.24 3.44703 19.248 2.96203 19.384 3.00203C19.456 3.02603 20.168 3.20903 20.96 3.40803C21.752 3.61503 22.536 3.81303 22.704 3.85303L23 3.93303L22.984 12.493L22.96 21.061L21.336 21.475C20.448 21.705 19.608 21.912 19.48 21.945L19.24 22V12.477Z" fill="#78E6DC" />
<path fill-rule="evenodd" clip-rule="evenodd" d="M1 12.509C1 7.83103 1.024 4.00403 1.064 4.00403C1.096 4.00403 1.936 4.21103 2.936 4.45803L4.76 4.91903V12.501C4.76 16.661 4.744 20.075 4.728 20.075C4.704 20.075 3.856 20.29 2.848 20.545L1 21.013V12.509Z" fill="#325AB4" />
</svg>} horizontal />;

<LightningIconCard title="Deploy SDXL Lightning" href="https://app.baseten.co/deploy/sdxl_lightning" />

# Example usage

The model accepts a single input, prompt, and returns a base64 string of the image as the key `result`.

This implementation uses the 4-step UNet checkpoint to balance speed and quality. You can [deploy your own version](https://github.com/basetenlabs/truss-examples/tree/main/stable-diffusion/sdxl-lightning) with either 2 steps for even faster results or 8 steps for even higher quality.

```python  theme={"system"}
import base64
import requests
import os

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]
BASE64_PREAMBLE = "data:image/png;base64,"

data = {
    "prompt": "a picture of a rhino wearing a suit",
}

# Call model endpoint
res = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)

# Get output image
res = res.json()
img_b64 = res.get("result")
img = base64.b64decode(img_b64)

# Save the base64 string to a PNG
img_file = open("sdxl-output-1.png", "wb")
img_file.write(img)
img_file.close()
os.system("open sdxl-output-1.png")
```

**JSON Output**

```json  theme={"system"}
{
  "result": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAA..."
}
```
