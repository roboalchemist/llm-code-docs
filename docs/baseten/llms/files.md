# Source: https://docs.baseten.co/inference/output-format/files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Model I/O with files

> Call models by passing a file or URL

Baseten supports a wide variety of file-based I/O approaches. These examples show our recommendations for working with files during model inference, whether local or remote, public or private, in the Truss or in your invocation code.

## Files as input

### Example: Send a file with JSON-serializable content

The Truss CLI has a `-f` flag to pass file input. If you're using the API endpoint via Python, get file contents with the standard `f.read()` function.

<CodeGroup>
  ```sh Truss CLI theme={"system"}
  truss predict -f input.json
  ```

  ```python Python script theme={"system"}
  import urllib3
  import json

  model_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  # Read input as JSON
  with open("input.json", "r") as f:
      data = json.loads(f.read())

  resp = urllib3.request(
      "POST",
      # Endpoint for production deployment, see API reference for more
      f"https://model-{model_id}.api.baseten.co/production/predict",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json=data
  )

  print(resp.json())
  ```
</CodeGroup>

### Example: Send a file with non-serializable content

The `-f` flag for `truss predict` only applies to JSON-serializable content. For other files, like the audio files required by [MusicGen Melody](https://www.baseten.co/library/musicgen-melody), the file content needs to be base64 encoded before it is sent.

```python  theme={"system"}
import urllib3

model_id = ""
# Read secrets from environment variables
baseten_api_key = os.environ["BASETEN_API_KEY"]

# Open a local file
with open("mymelody.wav", "rb") as f: # mono wav file, 48khz sample rate
    # Convert file contents into JSON-serializable format
    encoded_data = base64.b64encode(f.read())
    encoded_str = encoded_data.decode("utf-8")
# Define the data payload
data = {"prompts": ["happy rock", "energetic EDM", "sad jazz"], "melody": encoded_str, "duration": 8}
# Make the POST request
response = requests.post(url, headers=headers, data=data)
resp = urllib3.request(
    "POST",
    # Endpoint for production deployment, see API reference for more
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json=data
)
data = resp.json()["data"]
# Save output to files
for idx, clip in enumerate(data):
    with open(f"clip_{idx}.wav", "wb") as f:
        f.write(base64.b64decode(clip))
```

### Example: Send a URL to a public file

Rather than encoding and serializing a file to send in the HTTP request, you can instead write a Truss that takes a URL as input and loads the content in the `preprocess()` function.

Here's an example from [Whisper in the model library](https://www.baseten.co/library/whisper-v3).

```python  theme={"system"}
from tempfile import NamedTemporaryFile
import requests

# Get file content without blocking GPU
def preprocess(self, request):
    resp = requests.get(request["url"])
    return {"content": resp.content}

# Use file content in model inference
def predict(self, model_input):
    with NamedTemporaryFile() as fp:
        fp.write(model_input["content"])
        result = whisper.transcribe(
            self._model,
            fp.name,
            temperature=0,
            best_of=5,
            beam_size=5,
        )
        segments = [
            {"start": r["start"], "end": r["end"], "text": r["text"]}
            for r in result["segments"]
        ]
    return {
        "language": whisper.tokenizer.LANGUAGES[result["language"]],
        "segments": segments,
        "text": result["text"],
    }
```

## Files as output

### Example: Save model output to local file

When saving model output to a local file, there's nothing Baseten-specific about the code. Just use the standard `>` operator in bash or `file.write()` function in Python to save the model output.

<CodeGroup>
  ```sh Truss CLI theme={"system"}
  truss predict -d '"Model input!"' > output.json
  ```

  ```python Python script theme={"system"}
  import urllib3
  import json

  model_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  # Call model
  resp = urllib3.request(
      "POST",
      # Endpoint for production deployment, see API reference for more
      f"https://model-{model_id}.api.baseten.co/production/predict",
      headers={"Authorization": f"Api-Key {baseten_api_key}"},
      json=json.dumps("Model input!")
  )
  # Write results to file
  with open("output.json", "w") as f:
      f.write(resp.json())
  ```
</CodeGroup>

Output for some models, like image and audio generation models, may need to be decoded before you save it. See our [image generation example](/examples/image-generation) for how to parse base64 output.
