# Source: https://docs.baseten.co/examples/text-to-speech.md

# Text to speech

> Building a text-to-speech model with Kokoro

<Card title="View example on GitHub" horizontal icon="github" iconType="light" href="https://github.com/basetenlabs/truss-examples/tree/main/kokoro" />

In this example, we go through a Truss that serves Kokoro, a frontier text-to-speech model.

# Set up imports

We import necessary libraries and enable Hugging Face file transfers. We also download the NLTK tokenizer data.

```python model/model.py theme={"system"}
import logging
import os

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
import base64
import io
import sys
import time

import nltk
import numpy as np
import scipy.io.wavfile as wav
import torch
from huggingface_hub import snapshot_download
from nltk.tokenize import sent_tokenize

from models import build_model
from kokoro import generate

logger = logging.getLogger(__name__)

nltk.download("punkt")
```

# Downloading model weights

We need to prepare model weights by doing the following:

* Create a directory for the model data
* Download the Kokoro model from Hugging Face into the created model data directory
* Add the model data directory to the system path

```python model/model.py theme={"system"}
# Ensure data directory exists
os.makedirs("/app/data/Kokoro-82M", exist_ok=True)

# Download model
snapshot_download(
    repo_id="hexgrad/Kokoro-82M",
    repo_type="model",
    revision="c97b7bbc3e60f447383c79b2f94fee861ff156ac",
    local_dir="/app/data/Kokoro-82M",
    ignore_patterns=["*.onnx", "kokoro-v0_19.pth", "demo/"],
    max_workers=8,
)

# Add data_dir to the system path
sys.path.append("/app/data/Kokoro-82M")
```

# Define the `Model` class and `load` function

In the `load` function of the Truss, we download and set up the model. This `load` function handles setting up the device, loading the model weights, and loading the default voice. We also define the available voices.

```python model/model.py theme={"system"}
class Model:
    def __init__(self, **kwargs):
        self._data_dir = kwargs["data_dir"]
        self.model = None
        self.device = None
        self.default_voice = None
        self.voices = None
        return

    def load(self):
        logger.info("Starting setup...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Using device: {self.device}")

        # Load model
        logger.info("Loading model...")
        model_path = "/app/data/Kokoro-82M/fp16/kokoro-v0_19-half.pth"
        logger.info(f"Model path: {model_path}")
        if not os.path.exists(model_path):
            logger.info(f"Error: Model file not found at {model_path}")
            raise FileNotFoundError(f"Model file not found at {model_path}")

        try:
            self.model = build_model(model_path, self.device)
            logger.info("Model loaded successfully")
        except Exception as e:
            logger.info(f"Error loading model: {str(e)}")
            raise

        # Load default voice
        logger.info("Loading default voice...")
        voice_path = "/app/data/Kokoro-82M/voices/af.pt"
        if not os.path.exists(voice_path):
            logger.info(f"Error: Voice file not found at {voice_path}")
            raise FileNotFoundError(f"Voice file not found at {voice_path}")

        try:
            self.default_voice = torch.load(voice_path).to(self.device)
            logger.info("Default voice loaded successfully")
        except Exception as e:
            logger.info(f"Error loading default voice: {str(e)}")
            raise

        # Dictionary of available voices
        self.voices = {
            "default": "af",
            "bella": "af_bella",
            "sarah": "af_sarah",
            "adam": "am_adam",
            "michael": "am_michael",
            "emma": "bf_emma",
            "isabella": "bf_isabella",
            "george": "bm_george",
            "lewis": "bm_lewis",
            "nicole": "af_nicole",
            "sky": "af_sky",
        }
        return
```

# Define the `predict` function

The `predict` function contains the actual inference logic. The steps here are:

* Process input text and handle voice selection
* Chunk text for long inputs
* Generate audio
* Convert resulting audio to base64 and return it

```python model/model.py theme={"system"}
    def predict(self, model_input):
        # Run model inference here
        start = time.time()
        text = str(model_input.get("text", "Hi, I'm kokoro"))
        voice = str(model_input.get("voice", "af"))
        speed = float(model_input.get("speed", 1.0))
        logger.info(
            f"Text has {len(text)} characters. Using voice {voice} and speed {speed}."
        )
        if voice != "af":
            voicepack = torch.load(f"/app/data/Kokoro-82M/voices/{voice}.pt").to(
                self.device
            )
        else:
            voicepack = self.default_voice

        if len(text) >= 400:
            logger.info("Text is longer than 400 characters, splitting into sentences.")
            wavs = []

            def group_sentences(text, max_length=400):
                sentences = sent_tokenize(text)

                # Split long sentences
                while max([len(sent) for sent in sentences]) > max_length:
                    max_sent = max(sentences, key=len)
                    sentences_before = sentences[: sentences.index(max_sent)]
                    sentences_after = sentences[sentences.index(max_sent) + 1 :]
                    new_sentences = [
                        s.strip() + "." for s in max_sent.split(".") if s.strip()
                    ]
                    sentences = sentences_before + new_sentences + sentences_after

                return sentences

            sentences = group_sentences(text)
            logger.info(f"Processing {len(sentences)} chunks. Starting generation...")

            for sent in sentences:
                if sent.strip():
                    audio, _ = generate(
                        self.model, sent.strip(), voicepack, lang=voice[0], speed=speed
                    )
                    # Remove potential artifacts at the end
                    audio = audio[:-2000] if len(audio) > 2000 else audio
                    wavs.append(audio)

            # Concatenate all audio chunks
            audio = np.concatenate(wavs)
        else:
            logger.info("No splitting needed. Generating audio...")
            audio, _ = generate(self.model, text, voicepack, lang=voice[0], speed=speed)

        # Write audio to in-memory buffer
        buffer = io.BytesIO()
        wav.write(buffer, 24000, audio)
        wav_bytes = buffer.getvalue()
        duration_seconds = len(audio) / 24000
        logger.info(
            f"Generation took {time.time()-start} seconds to generate {duration_seconds:.2f} seconds of audio"
        )
        return {"base64": base64.b64encode(wav_bytes).decode("utf-8")}
```

# Setting up the `config.yaml`

Running Kokoro requires a handful of Python libraries, including `torch`, `transformers`, and others.

```yaml config.yaml theme={"system"}
build_commands:
- python3 -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
environment_variables: {}
model_metadata:
  example_model_input: {"text": "Kokoro is a frontier TTS model for its size of 82 million parameters (text in/audio out). On 25 Dec 2024, Kokoro v0.19 weights were permissively released in full fp32 precision under an Apache 2.0 license. As of 2 Jan 2025, 10 unique Voicepacks have been released, and a .onnx version of v0.19 is available.In the weeks leading up to its release, Kokoro v0.19 was the #1🥇 ranked model in TTS Spaces Arena. Kokoro had achieved higher Elo in this single-voice Arena setting over other models, using fewer parameters and less data. Kokoro's ability to top this Elo ladder suggests that the scaling law (Elo vs compute/data/params) for traditional TTS models might have a steeper slope than previously expected.", "voice": "af", "speed": 1.0}
model_name: kokoro
python_version: py311
requirements:
- torch==2.5.1
- transformers==4.48.0
- scipy==1.15.1
- phonemizer==3.3.0
- nltk==3.9.1
- numpy
- huggingface_hub[hf_transfer]
- hf_transfer==0.1.9
- munch==4.0.0
resources:
  accelerator: T4
  use_gpu: true
runtime:
  predict_concurrency: 1
secrets: {}
system_packages:
- espeak-ng
```

## Configuring resources for Kokoro

Note that we need an T4 GPU to run this model.

```yaml config.yaml theme={"system"}
resources:
  accelerator: T4
  use_gpu: true
```

## System Packages

Running Kokoro requires `espeak-ng` to synthesize speech output.

```yaml config.yaml theme={"system"}
system_packages:
- espeak-ng
```

# Deploy the model

Deploy the model like you would other Trusses by running the following command:

```bash  theme={"system"}
truss push kokoro --publish
```

# Run an inference

Use a Python script to call the deployed model and parse its response. In this example, the script sends text input to the model and saves the returned audio (decoded from base64) as a WAV file: `output.wav`.

```python infer.py theme={"system"}
import httpx
import base64

# Replace the empty string with your model id below
model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

with httpx.Client() as client:
    # Make the API request
    resp = client.post(
        f"https://model-{model_id}.api.baseten.co/production/predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
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
