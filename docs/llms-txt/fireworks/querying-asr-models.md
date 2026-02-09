# Source: https://docs.fireworks.ai/guides/querying-asr-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Speech to Text

> Convert audio to text with streaming and pre-recorded transcription

Fireworks AI provides three ASR (Automatic Speech Recognition) features: **Streaming Transcription**, **Pre-recorded Transcription**, and **Pre-recorded Translation**. This guide shows you how to get started with each feature.

## Streaming Transcription

Convert audio to text in real-time using WebSocket connections. Perfect for voice agents and live applications.

### Quick Start

**Available Models:**

* [`fireworks-asr-large`](https://app.fireworks.ai/models/fireworks/fireworks-asr-large): Cost efficient model for real-time transcription over web-sockets
* [`fireworks-asr-v2`](https://app.fireworks.ai/models/fireworks/fireworks-asr-v2): Next generation and ultra-low latency audio streaming for real-time transcription over web-sockets

For a working example of streaming transcription see the following resources:

1. [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb)
2. [Python cookbook](https://github.com/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/python)

For more detailed information, see the [full streaming API documentation](/api-reference/audio-streaming-transcriptions) and the [source code](https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text)

## Pre-recorded Transcription

Convert audio files to text. Supports files up to 1GB in formats like MP3, FLAC, and WAV. Transcribe multiple hours of audio in minutes.

### Quick Start

For a working example of pre-recorded transcription see the [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_prerecorded_speech_to_text/audio_prerecorded_speech_to_text.ipynb)

**Available Models:**

* [`whisper-v3`](https://app.fireworks.ai/models/fireworks/whisper-v3): Highest accuracy
  * model=`whisper-v3`
  * base\_url=`https://audio-prod.api.fireworks.ai`
* [`whisper-v3-turbo`](https://app.fireworks.ai/models/fireworks/whisper-v3-turbo): Faster processing
  * model=`whisper-v3-turbo`
  * base\_url=`https://audio-turbo.api.fireworks.ai`

For more detailed information, see the [full transcription API documentation](/api-reference/audio-transcriptions)

## Pre-recorded Translation

Translate audio from any of our supported languages to English. Supports files up to 1GB in formats like MP3, FLAC, and WAV.

### Quick Start

<CodeGroup>
  ```python Python (fireworks sdk) theme={null}
  !pip install fireworks-ai requests

  from fireworks.client.audio import AudioInference
  import requests
  import time
  from dotenv import load_dotenv
  import os

  load_dotenv()

  # Prepare client
  audio = requests.get("https://tinyurl.com/3cy7x44v").content
  client = AudioInference(
      model="whisper-v3",
      base_url="https://audio-prod.api.fireworks.ai",
      #
      # Or for the turbo version
      # model="whisper-v3-turbo",
      # base_url="https://audio-turbo.api.fireworks.ai",
      api_key=os.getenv("FIREWORKS_API_KEY")
  )

  # Make request
  start = time.time()
  r = await client.translate_async(audio=audio)
  print(f"Took: {(time.time() - start):.3f}s. Text: '{r.text}'")
  ```

  ```python Python (openai sdk) theme={null}
  !pip install openai requests
  from openai import OpenAI
  import requests
  from dotenv import load_dotenv
  import os

  load_dotenv()

  client = OpenAI(
              base_url="https://audio-prod.api.fireworks.ai/v1",
              api_key=os.getenv("FIREWORKS_API_KEY"),
          )
  audio_file= requests.get("https://tinyurl.com/3cy7x44v").content

  translation = client.audio.translations.create(
      model="whisper-v3",
      file=audio_file,
  )

  print(translation.text)
  ```

  ```bash curl theme={null}

  # Download audio file
  curl -L -o "audio.flac" "https://tinyurl.com/4997djsh"

  # Make request
  curl -X POST "https://audio-prod.api.fireworks.ai/v1/audio/translations" \
  -H "Authorization: <FIREWORKS_API_KEY>" \
  -F "file=@audio.flac"
  ```
</CodeGroup>

For more detailed information, see the [full translation API documentation](/api-reference/audio-translations)

## Supported Languages

We support 95+ languages including English, Spanish, French, German, Chinese, Japanese, Russian, Portuguese, and many more. See the [complete language list](/api-reference/audio-transcriptions#supported-languages).

## Common Use Cases

* **Call Center / Customer Service**: Transcribe or translate customer calls
* **Note Taking**: Transcribe audio for automated note taking

## Next Steps

1. Explore [advanced features](/api-reference/audio-transcriptions) like speaker diarization and custom prompts
2. Contact us at [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) for dedicated endpoints and enterprise features
