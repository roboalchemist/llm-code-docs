# Source: https://docs.baseten.co/examples/models/kokoro/kokoro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Kokoro

> Kokoro is a frontier TTS model for its size of 82 million parameters (text in/audio out).

export const LibraryIconCard = ({title, href}) => <Card title={title} href={href} icon={<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3.33334 16.25C3.33334 15.6975 3.55283 15.1676 3.94353 14.7769C4.33423 14.3862 4.86413 14.1667 5.41667 14.1667H16.6667" stroke="#8999AC" stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round" />
<path d="M5.41667 1.66669H16.6667V18.3334H5.41667C4.86413 18.3334 4.33423 18.1139 3.94353 17.7232C3.55283 17.3325 3.33334 16.8026 3.33334 16.25V3.75002C3.33334 3.19749 3.55283 2.66758 3.94353 2.27688C4.33423 1.88618 4.86413 1.66669 5.41667 1.66669V1.66669Z" stroke="#8999AC" stroke-width="1.33333" stroke-linecap="round" stroke-linejoin="round" />
</svg>} horizontal />;

<LibraryIconCard title="Deploy Kokoro" href="https://app.baseten.co/deploy/kokoro" />

## Example usage

Kokoro uses the following request and response format:

```
request:
{"text": "Hello", "voice": "af", "speed": 1.0}

text: str = defaults to "Hi, I'm kokoro"
voice: str = defaults to "af", available options: "af", "af_bella", "af_sarah", "am_adam", "am_michael", "bf_emma", "bf_isabella", "bm_george", "bm_lewis", "af_nicole", "af_sky"
speed: float = defaults to 1.0. The speed of the audio generated

response:
{"base64": "base64 encoded bytestring"}
```

```python  theme={"system"}
import httpx
import base64

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

with httpx.Client() as client:
    # Make the API request
    resp = client.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {API_KEY}"},
        json={"text": "Hello world", "voice": "af", "speed": 1.0},
        timeout=None,
    )

# Get the base64 encoded audio
response_data = resp.json()
audio_base64 = response_data["base64"]

# Decode the base64 string
audio_bytes = base64.b64decode(audio_base64)

# Write to a WAV file
with open("output.wav", "wb") as f:
    f.write(audio_bytes)

print("Audio saved to output.wav")
```

**JSON Output**

```json  theme={"system"}
null
```
