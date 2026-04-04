# Source: https://docs.together.ai/docs/speech-to-text.md

> Learn how to transcribe and translate audio into text!

# Speech-to-Text

Together AI provides comprehensive audio transcription and translation capabilities powered by state-of-the-art speech recognition models including OpenAI's Whisper and Voxtral. This guide covers everything from batch transcription to real-time streaming for low-latency applications.

## Quick Start

Here's how to get started with basic transcription and translation:

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  ## Basic transcription

  response = client.audio.transcriptions.create(
      file="path/to/audio.mp3",
      model="openai/whisper-large-v3",
      language="en",
  )
  print(response.text)

  ## Basic translation

  response = client.audio.translations.create(
      file="path/to/foreign_audio.mp3",
      model="openai/whisper-large-v3",
  )
  print(response.text)
  ```

  ```python Python v2 theme={null}
  from together import Together

  client = Together()

  with open("audio.wav", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          language="en",
      )
      print(response.text)

  ## Basic translation

  with open("audio.wav", "rb") as audio_file:
      response = client.audio.translations.create(
          file=audio_file,
          model="openai/whisper-large-v3",
      )
      print(response.text)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  // Basic transcription
  const transcription = await together.audio.transcriptions.create({
    file: 'path/to/audio.mp3',
    model: 'openai/whisper-large-v3',
    language: 'en',
  });
  console.log(transcription.text);

  // Basic translation
  const translation = await together.audio.translations.create({
    file: 'path/to/foreign_audio.mp3',
    model: 'openai/whisper-large-v3',
  });
  console.log(translation.text);
  ```

  ```curl cURL theme={null}
  ## Transcription
  curl -X POST "https://api.together.xyz/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@audio.mp3" \
       -F "model=openai/whisper-large-v3" \
       -F "language=en"

  ## Translation
  curl -X POST "https://api.together.xyz/v1/audio/translations" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@foreign_audio.mp3" \
       -F "model=openai/whisper-large-v3"
  ```

  ```shell Shell theme={null}
  ## Transcription
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --language en

  ## Translation
  together audio translate foreign_audio.mp3 \
    --model openai/whisper-large-v3
  ```
</CodeGroup>

## Available Models

Together AI supports multiple speech-to-text models:

| Organization | Model Name       | Model String for API           | Capabilities                        |
| :----------- | :--------------- | :----------------------------- | :---------------------------------- |
| OpenAI       | Whisper Large v3 | openai/whisper-large-v3        | Real-time, Translation, Diarization |
| Mistral AI   | Voxtral Mini 3B  | mistralai/Voxtral-Mini-3B-2507 |                                     |

## Audio Transcription

Audio transcription converts speech to text in the same language as the source audio.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.audio.transcriptions.create(
      file="meeting_recording.mp3",
      model="openai/whisper-large-v3",
      language="en",
      response_format="json",
  )

  print(f"Transcription: {response.text}")
  ```

  ```python Python v2 theme={null}
  from together import Together

  client = Together()

  with open("meeting_recording.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          language="en",
          response_format="json",
      )

  print(f"Transcription: {response.text}")
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  const response = await together.audio.transcriptions.create({
    file: 'meeting_recording.mp3',
    model: 'openai/whisper-large-v3',
    language: 'en',
    response_format: 'json',
  });

  console.log(`Transcription: ${response.text}`);
  ```

  ```shell Shell theme={null}
  together audio transcribe meeting_recording.mp3 \
    --model openai/whisper-large-v3 \
    --language en \
    --response-format json
  ```
</CodeGroup>

The API supports the following audio formats:

* `.wav` (audio/wav)
* `.mp3` (audio/mpeg)
* `.m4a` (audio/mp4)
* `.webm` (audio/webm)
* `.flac` (audio/flac)

**Input Methods**

**Local File Path**

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="/path/to/audio.mp3",
      model="openai/whisper-large-v3",
  )
  ```

  ```python Python v2 theme={null}
  with open("/path/to/audio.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
      )
  ```
</CodeGroup>

**Path Object**

<CodeGroup>
  ```python Python theme={null}
  from pathlib import Path

  audio_file = Path("recordings/interview.wav")
  response = client.audio.transcriptions.create(
      file=audio_file,
      model="openai/whisper-large-v3",
  )
  ```

  ```python Python v2 theme={null}
  from pathlib import Path

  audio_path = Path("recordings/interview.wav")
  with open(audio_path, "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
      )
  ```
</CodeGroup>

**URL**

```python Python theme={null}
response = client.audio.transcriptions.create(
    file="https://example.com/audio.mp3", model="openai/whisper-large-v3"
)
```

**File-like Object**

```python Python theme={null}
with open("audio.mp3", "rb") as audio_file:
    response = client.audio.transcriptions.create(
        file=audio_file,
        model="openai/whisper-large-v3",
    )
```

**Language Support**

Specify the audio language using ISO 639-1 language codes:

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="spanish_audio.mp3",
      model="openai/whisper-large-v3",
      language="es",  # Spanish
  )
  ```

  ```python Python v2 theme={null}
  with open("spanish_audio.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          language="es",  # Spanish
      )
  ```
</CodeGroup>

Common specifiable language codes:

* "en" - English
* "es" - Spanish
* "fr" - French
* "de" - German
* "ja" - Japanese
* "zh" - Chinese
* "auto" - Auto-detect (default)

**Custom Prompts**

Use prompts to improve transcription accuracy for specific contexts:

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="medical_consultation.mp3",
      model="openai/whisper-large-v3",
      language="en",
      prompt="This is a medical consultation discussing patient symptoms, diagnosis, and treatment options.",
  )
  ```

  ```python Python v2 theme={null}
  with open("medical_consultation.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          language="en",
          prompt="This is a medical consultation discussing patient symptoms, diagnosis, and treatment options.",
      )
  ```

  ```shell Shell theme={null}
  together audio transcribe medical_consultation.mp3 \
    --model openai/whisper-large-v3 \
    --language en \
    --prompt "This is a medical consultation discussing patient symptoms, diagnosis, and treatment options."
  ```
</CodeGroup>

## Real-time Streaming Transcription

For applications requiring the lowest latency, use the real-time WebSocket API. This provides streaming transcription with incremental results.

<Warning>
  The WebSocket API is currently only available via raw WebSocket connections. SDK support coming soon.
</Warning>

**Establishing a Connection**

Connect to: `wss://api.together.ai/v1/realtime?model={model}&input_audio_format=pcm_s16le_16000`

**Headers:**

```javascript  theme={null}
{
  'Authorization': 'Bearer YOUR_API_KEY',
  'OpenAI-Beta': 'realtime=v1'
}
```

**Query Parameters**

| Parameter            | Type   | Required | Description                                    |
| :------------------- | :----- | :------- | :--------------------------------------------- |
| model                | string | Yes      | Model to use (e.g., `openai/whisper-large-v3`) |
| input\_audio\_format | string | Yes      | Audio format: `pcm_s16le_16000`                |

**Client → Server Messages**

**1. Append Audio to Buffer**

```json  theme={null}
{
  "type": "input_audio_buffer.append",
  "audio": "base64-encoded-audio-chunk"
}
```

Send audio data in base64-encoded PCM format.

**2. Commit Audio Buffer**

```json  theme={null}
{
  "type": "input_audio_buffer.commit"
}
```

Forces transcription of any remaining audio in the server-side buffer.

**Server → Client Messages**

**Delta Events (Intermediate Results)**

```json  theme={null}
{
  "type": "conversation.item.input_audio_transcription.delta",
  "delta": "The quick brown fox jumps"
}
```

Delta events are intermediate transcriptions. The model is still processing and may revise the output. Each delta message overrides the previous delta.

**Completed Events (Final Results)**

```json  theme={null}
{
  "type": "conversation.item.input_audio_transcription.completed",
  "transcript": "The quick brown fox jumps over the lazy dog"
}
```

Completed events are final transcriptions. The model is confident about this text. The next delta event will continue from where this completed.

**Real-time Example**

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  import base64
  import json
  import os
  import sys

  import numpy as np
  import sounddevice as sd
  import websockets

  # Configuration
  API_KEY = os.getenv("TOGETHER_API_KEY")
  MODEL = "openai/whisper-large-v3"
  SAMPLE_RATE = 16000
  BATCH_SIZE = 4096  # 256ms batches for optimal performance

  if not API_KEY:
      print("Error: Set TOGETHER_API_KEY environment variable")
      sys.exit(1)


  class RealtimeTranscriber:
      """Realtime transcription client for Together AI."""

      def __init__(self):
          self.ws = None
          self.stream = None
          self.is_ready = False
          self.audio_buffer = np.array([], dtype=np.float32)
          self.audio_queue = asyncio.Queue()

      async def connect(self):
          """Connect to Together AI API."""
          url = (
              f"wss://api.together.xyz/v1/realtime"
              f"?intent=transcription"
              f"&model={MODEL}"
              f"&input_audio_format=pcm_s16le_16000"
              f"&authorization=Bearer {API_KEY}"
          )

          self.ws = await websockets.connect(
              url,
              subprotocols=[
                  "realtime",
                  f"openai-insecure-api-key.{API_KEY}",
                  "openai-beta.realtime-v1",
              ],
          )

      async def send_audio(self):
          """Capture and send audio to API."""

          def audio_callback(indata, frames, time, status):
              self.audio_queue.put_nowait(indata.copy().flatten())

          # Start microphone stream
          self.stream = sd.InputStream(
              samplerate=SAMPLE_RATE,
              channels=1,
              dtype="float32",
              blocksize=1024,
              callback=audio_callback,
          )
          self.stream.start()

          # Process and send audio
          while True:
              try:
                  audio = await asyncio.wait_for(
                      self.audio_queue.get(), timeout=0.1
                  )

                  if self.ws and self.is_ready:
                      # Add to buffer
                      self.audio_buffer = np.concatenate(
                          [self.audio_buffer, audio]
                      )

                      # Send when buffer is full
                      while len(self.audio_buffer) >= BATCH_SIZE:
                          batch = self.audio_buffer[:BATCH_SIZE]
                          self.audio_buffer = self.audio_buffer[BATCH_SIZE:]

                          # Convert float32 to int16 PCM
                          audio_int16 = (
                              np.clip(batch, -1.0, 1.0) * 32767
                          ).astype(np.int16)
                          audio_base64 = base64.b64encode(
                              audio_int16.tobytes()
                          ).decode()

                          # Send to API
                          await self.ws.send(
                              json.dumps(
                                  {
                                      "type": "input_audio_buffer.append",
                                      "audio": audio_base64,
                                  }
                              )
                          )

              except asyncio.TimeoutError:
                  continue
              except Exception as e:
                  print(f"Error: {e}", file=sys.stderr)
                  break

      async def receive_transcriptions(self):
          """Receive and display transcription results."""
          current_interim = ""

          try:
              async for message in self.ws:
                  data = json.loads(message)

                  if data["type"] == "session.created":
                      self.is_ready = True

                  elif (
                      data["type"]
                      == "conversation.item.input_audio_transcription.delta"
                  ):
                      # Interim result
                      print(
                          f"\r\033[90m{data['delta']}\033[0m", end="", flush=True
                      )
                      current_interim = data["delta"]

                  elif (
                      data["type"]
                      == "conversation.item.input_audio_transcription.completed"
                  ):
                      # Final result
                      if current_interim:
                          print("\r\033[K", end="")
                      print(f"\033[92m{data['transcript']}\033[0m")
                      current_interim = ""

                  elif data["type"] == "error":
                      print(f"\nError: {data.get('message', 'Unknown error')}")

          except websockets.exceptions.ConnectionClosed:
              pass

      async def close(self):
          """Close connections and cleanup."""
          if self.stream:
              self.stream.stop()
              self.stream.close()

          # Flush remaining audio
          if len(self.audio_buffer) > 0 and self.ws and self.is_ready:
              try:
                  audio_int16 = (
                      np.clip(self.audio_buffer, -1.0, 1.0) * 32767
                  ).astype(np.int16)
                  audio_base64 = base64.b64encode(audio_int16.tobytes()).decode()
                  await self.ws.send(
                      json.dumps(
                          {
                              "type": "input_audio_buffer.append",
                              "audio": audio_base64,
                          }
                      )
                  )
              except Exception:
                  pass

          if self.ws:
              await self.ws.close()

      async def run(self):
          """Main execution loop."""
          try:
              print("🎤 Together AI Realtime Transcription")
              print("=" * 40)
              print("Connecting...")

              await self.connect()

              print("✓ Connected")
              print("✓ Recording started - speak now\n")

              # Run audio capture and transcription concurrently
              await asyncio.gather(
                  self.send_audio(), self.receive_transcriptions()
              )

          except KeyboardInterrupt:
              print("\n\nStopped")
          except Exception as e:
              print(f"Error: {e}", file=sys.stderr)
          finally:
              await self.close()


  async def main():
      transcriber = RealtimeTranscriber()
      await transcriber.run()


  if __name__ == "__main__":
      asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import WebSocket from 'ws';
  import recorder from 'node-record-lpcm16';

  // Configuration
  const API_KEY = process.env.TOGETHER_API_KEY;
  const MODEL = 'openai/whisper-large-v3';
  const SAMPLE_RATE = 16000;

  if (!API_KEY) {
    console.error('Error: Set TOGETHER_API_KEY environment variable');
    process.exit(1);
  }

  class RealtimeTranscriber {
    /** Realtime transcription client for Together AI. */
    private ws: WebSocket | null = null;
    private isReady = false;
    private currentInterim = '';

    async connect() {
      /** Connect to Together AI API. */
      const url =
        `wss://api.together.xyz/v1/realtime` +
        `?intent=transcription` +
        `&model=${MODEL}` +
        `&input_audio_format=pcm_s16le_16000` +
        `&authorization=Bearer ${API_KEY}`;

      this.ws = new WebSocket(url, [
        'realtime',
        `openai-insecure-api-key.${API_KEY}`,
        'openai-beta.realtime-v1',
      ]);

      this.ws.on('message', (data) => this.receiveTranscriptions(data));
      this.ws.on('error', (err) => console.error(`Error: ${err}`));

      return new Promise((resolve) => {
        this.ws?.on('open', () => {
          resolve(null);
        });
      });
    }

    sendAudio() {
      /** Capture and send audio to API. */
      const mic = recorder.record({
        sampleRate: SAMPLE_RATE,
        threshold: 0,
        verbose: false,
      });

      mic.stream().on('data', (chunk: Buffer) => {
        if (this.ws && this.isReady && this.ws.readyState === WebSocket.OPEN) {
          this.ws.send(
            JSON.stringify({
              type: 'input_audio_buffer.append',
              audio: chunk.toString('base64'),
            })
          );
        }
      });

      mic.stream().on('error', (err) => {
        console.error('Microphone Error:', err);
      });
    }

    receiveTranscriptions(data: WebSocket.Data) {
      /** Receive and display transcription results. */
      const message = JSON.parse(data.toString());

      if (message.type === 'session.created') {
        this.isReady = true;
      } else if (
        message.type === 'conversation.item.input_audio_transcription.delta'
      ) {
        // Interim result
        process.stdout.write(`\r\x1b[90m${message.delta}\x1b[0m`);
        this.currentInterim = message.delta;
      } else if (
        message.type === 'conversation.item.input_audio_transcription.completed'
      ) {
        // Final result
        if (this.currentInterim) {
          process.stdout.write('\r\x1b[K');
        }
        console.log(`\x1b[92m${message.transcript}\x1b[0m`);
        this.currentInterim = '';
      } else if (message.type === 'error') {
        console.error(`\nError: ${message.message || 'Unknown error'}`);
      }
    }

    async run() {
      /** Main execution loop. */
      try {
        console.log('🎤 Together AI Realtime Transcription');
        console.log('='.repeat(40));
        console.log('Connecting...');

        await this.connect();

        console.log('✓ Connected');
        console.log('✓ Recording started - speak now\n');

        this.sendAudio();
      } catch (e) {
        console.error(`Error: ${e}`);
      }
    }
  }

  async function main() {
    const transcriber = new RealtimeTranscriber();
    await transcriber.run();
  }

  main();
  ```
</CodeGroup>

## Audio Translation

Audio translation converts speech from any language to English text.

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.translations.create(
      file="french_audio.mp3",
      model="openai/whisper-large-v3",
  )
  print(f"English translation: {response.text}")
  ```

  ```python Python v2 theme={null}
  with open("french_audio.mp3", "rb") as audio_file:
      response = client.audio.translations.create(
          file=audio_file,
          model="openai/whisper-large-v3",
      )
  print(f"English translation: {response.text}")
  ```

  ```typescript TypeScript theme={null}
  const response = await together.audio.translations.create({
    file: 'french_audio.mp3',
    model: 'openai/whisper-large-v3',
  });
  console.log(`English translation: ${response.text}`);
  ```

  ```shell Shell theme={null}
  together audio translate french_audio.mp3 \
    --model openai/whisper-large-v3
  ```
</CodeGroup>

**Translation with Context**

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.translations.create(
      file="business_meeting_spanish.mp3",
      model="openai/whisper-large-v3",
      prompt="This is a business meeting discussing quarterly sales results.",
  )
  ```

  ```python Python v2 theme={null}
  with open("business_meeting_spanish.mp3", "rb") as audio_file:
      response = client.audio.translations.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          prompt="This is a business meeting discussing quarterly sales results.",
      )
  ```

  ```shell Shell theme={null}
  together audio translate business_meeting_spanish.mp3 \
    --model openai/whisper-large-v3 \
    --prompt "This is a business meeting discussing quarterly sales results."
  ```
</CodeGroup>

## Speaker Diarization

Enable diarization to identify who is speaking when. If known you can also add `min_speakers` and `max_speakers` expected in the audio to improve the diarization accuracy.

<CodeGroup>
  ```python Python theme={null}
  from together import Together

  client = Together()

  response = client.audio.transcriptions.create(
      file="meeting.mp3",
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      diarize="true",  # Enable speaker diarization
      min_speakers=1,
      max_speakers=5,
  )

  # Access speaker segments
  print(response.speaker_segments)
  ```

  ```python Python v2 theme={null}
  from together import Together

  client = Together()

  with open("meeting.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          response_format="verbose_json",
          diarize="true",  # Enable speaker diarization
      )

  # Access speaker segments
  print(response.speaker_segments)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';

  const together = new Together();

  async function transcribeWithDiarization() {
    const response = await together.audio.transcriptions.create({
      file: 'meeting.mp3',
      model: 'openai/whisper-large-v3',
      diarize: true  // Enable speaker diarization
    });

    // Access the speaker segments
    console.log(`Speaker Segments: ${response.speaker_segments}\n`);
  }

  transcribeWithDiarization();
  ```

  ```curl cURL theme={null}
  curl -X POST "https://api.together.xyz/v1/audio/transcriptions" \
       -H "Authorization: Bearer $TOGETHER_API_KEY" \
       -F "file=@meeting.mp3" \
       -F "model=openai/whisper-large-v3" \
       -F "diarize=true"
  ```
</CodeGroup>

**Example Response with Diarization:**

```json  theme={null}
AudioSpeakerSegment(
    id=1,
    speaker_id='SPEAKER_01',
    start=6.268,
    end=30.776,
    text=(
        "Hello. Oh, hey, Justin. How are you doing? ..."
    ),
    words=[
        AudioTranscriptionWord(
            word='Hello.',
            start=6.268,
            end=11.314,
            id=0,
            speaker_id='SPEAKER_01'
        ),
        AudioTranscriptionWord(
            word='Oh,',
            start=11.834,
            end=11.894,
            id=1,
            speaker_id='SPEAKER_01'
        ),
        AudioTranscriptionWord(
            word='hey,',
            start=11.914,
            end=11.995,
            id=2,
            speaker_id='SPEAKER_01'
        ),
        ...
    ]
)
```

## Word-level Timestamps

Get word-level timing information:

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      timestamp_granularities="word",
  )

  print(f"Text: {response.text}")
  print(f"Language: {response.language}")
  print(f"Duration: {response.duration}s")

  ## Access individual words with timestamps
  if response.words:
      for word in response.words:
          print(f"'{word.word}' [{word.start:.2f}s - {word.end:.2f}s]")
  ```

  ```python Python v2 theme={null}
  with open("audio.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          response_format="verbose_json",
          timestamp_granularities="word",
      )

  print(f"Text: {response.text}")
  print(f"Language: {response.language}")
  print(f"Duration: {response.duration}s")

  ## Access individual words with timestamps
  if response.words:
      for word in response.words:
          print(f"'{word['word']}' [{word['start']:.2f}s - {word['end']:.2f}s]")
  ```

  ```shell Shell theme={null}
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --response-format verbose_json \
    --timestamp-granularities word \
    --pretty
  ```
</CodeGroup>

**Example Output:**

```text Text theme={null}
Text: It is certain that Jack Pumpkinhead might have had a much finer house to live in.
Language: en
Duration: 7.2562358276643995s
Task: None

'It' [0.00s - 0.36s]
'is' [0.42s - 0.47s]
'certain' [0.51s - 0.74s]
'that' [0.79s - 0.86s]
'Jack' [0.90s - 1.11s]
'Pumpkinhead' [1.15s - 1.66s]
'might' [1.81s - 2.00s]
'have' [2.04s - 2.13s]
'had' [2.16s - 2.26s]
'a' [2.30s - 2.32s]
'much' [2.36s - 2.48s]
'finer' [2.54s - 2.74s]
'house' [2.78s - 2.93s]
'to' [2.96s - 3.03s]
'live' [3.07s - 3.21s]
'in.' [3.26s - 7.27s]
```

## Response Formats

**JSON Format (Default)**

Returns only the transcribed/translated text:

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      response_format="json",
  )

  print(response.text)  # "Hello, this is a test recording."
  ```

  ```python Python v2 theme={null}
  with open("audio.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          response_format="json",
      )

  print(response.text)  # "Hello, this is a test recording."
  ```
</CodeGroup>

**Verbose JSON Format**

Returns detailed information including timestamps:

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      response_format="verbose_json",
      timestamp_granularities="segment",
  )

  ## Access segments with timestamps
  for segment in response.segments:
      print(f"[{segment.start:.2f}s - {segment.end:.2f}s]: {segment.text}")
  ```

  ```python Python v2 theme={null}
  with open("audio.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          response_format="verbose_json",
          timestamp_granularities="segment",
      )

  ## Access segments with timestamps
  for segment in response.segments:
      print(
          f"[{segment['start']:.2f}s - {segment['end']:.2f}s]: {segment['text']}"
      )
  ```

  ```shell Shell theme={null}
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --response-format verbose_json \
    --timestamp-granularities segment \
    --pretty
  ```
</CodeGroup>

**Example Output:**

```text Text theme={null}
[0.11s - 10.85s]: Call is now being recorded. Parker Scarves, how may I help you? Online for my wife, and it turns out they shipped the wrong... Oh, I am so sorry, sir. I got it for her birthday, which is tonight, and now I'm not 100% sure what I need to do. Okay, let me see if I can help. Do you have the item number of the Parker Scarves? I don't think so. Call the New Yorker, I... Excellent. What color do...

[10.88s - 21.73s]: Blue. The one they shipped was light blue. I wanted the darker one. What's the difference? The royal blue is a bit brighter. What zip code are you located in? One nine.

[22.04s - 32.62s]: Karen's Boutique, Termall. Is that close? I'm in my office. Okay, um, what is your name, sir? Charlie. Charlie Johnson. Is that J-O-H-N-S-O-N? And Mr. Johnson, do you have the Parker scarf in light blue with you now? I do. They shipped it to my office. It came in not that long ago. What I will do is make arrangements with Karen's Boutique for...

[32.62s - 41.03s]: you to Parker Scarf at no additional cost. And in addition, I was able to look up your order in our system, and I'm going to send out a special gift to you to make up for the inconvenience. Thank you. You're welcome. And thank you for calling Parker Scarf, and I hope your wife enjoys her birthday gift. Thank you. You're very welcome. Goodbye.

[43.50s - 44.20s]: you
```

## Advanced Features

**Temperature Control**

Adjust randomness in the output (0.0 = deterministic, 1.0 = creative):

<CodeGroup>
  ```python Python theme={null}
  response = client.audio.transcriptions.create(
      file="audio.mp3",
      model="openai/whisper-large-v3",
      temperature=0.0,  # Most deterministic
  )

  print(f"Text: {response.text}")
  ```

  ```python Python v2 theme={null}
  with open("audio.mp3", "rb") as audio_file:
      response = client.audio.transcriptions.create(
          file=audio_file,
          model="openai/whisper-large-v3",
          temperature=0.0,  # Most deterministic
      )

  print(f"Text: {response.text}")
  ```

  ```shell Shell theme={null}
  together audio transcribe audio.mp3 \
    --model openai/whisper-large-v3 \
    --temperature 0.0
  ```
</CodeGroup>

## Async Support

All transcription and translation operations support async/await:

**Async Transcription**

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from together import AsyncTogether


  async def transcribe_audio():
      client = AsyncTogether()

      response = await client.audio.transcriptions.create(
          file="audio.mp3",
          model="openai/whisper-large-v3",
          language="en",
      )

      return response.text


  ## Run async function
  result = asyncio.run(transcribe_audio())
  print(result)
  ```

  ```python Python v2 theme={null}
  import asyncio
  from together import AsyncTogether


  async def transcribe_audio():
      client = AsyncTogether()

      with open("audio.mp3", "rb") as audio_file:
          response = await client.audio.transcriptions.create(
              file=audio_file,
              model="openai/whisper-large-v3",
              language="en",
          )

      return response.text


  ## Run async function
  result = asyncio.run(transcribe_audio())
  print(result)
  ```
</CodeGroup>

**Async Translation**

<CodeGroup>
  ```python Python theme={null}
  async def translate_audio():
      client = AsyncTogether()

      response = await client.audio.translations.create(
          file="foreign_audio.mp3",
          model="openai/whisper-large-v3",
      )

      return response.text


  result = asyncio.run(translate_audio())
  print(result)
  ```

  ```python Python v2 theme={null}
  async def translate_audio():
      client = AsyncTogether()

      with open("foreign_audio.mp3", "rb") as audio_file:
          response = await client.audio.translations.create(
              file=audio_file,
              model="openai/whisper-large-v3",
          )

      return response.text


  result = asyncio.run(translate_audio())
  print(result)
  ```
</CodeGroup>

**Concurrent Processing**

Process multiple audio files concurrently:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from together import AsyncTogether


  async def process_multiple_files():
      client = AsyncTogether()

      files = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]

      tasks = [
          client.audio.transcriptions.create(
              file=file,
              model="openai/whisper-large-v3",
          )
          for file in files
      ]

      responses = await asyncio.gather(*tasks)

      for i, response in enumerate(responses):
          print(f"File {files[i]}: {response.text}")


  asyncio.run(process_multiple_files())
  ```

  ```python Python v2 theme={null}
  import asyncio
  from together import AsyncTogether


  async def process_multiple_files():
      client = AsyncTogether()

      files = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]

      async def transcribe_file(file_path):
          with open(file_path, "rb") as audio_file:
              return await client.audio.transcriptions.create(
                  file=audio_file,
                  model="openai/whisper-large-v3",
              )

      tasks = [transcribe_file(file) for file in files]
      responses = await asyncio.gather(*tasks)

      for i, response in enumerate(responses):
          print(f"File {files[i]}: {response.text}")


  asyncio.run(process_multiple_files())
  ```
</CodeGroup>

## Best Practices

**Choosing the Right Method**

* **Batch Transcription:** Best for pre-recorded audio files, podcasts, or any non-real-time use case
* **Real-time Streaming:** Best for live conversations, voice assistants, or applications requiring immediate feedback

**Audio Quality Tips**

* Use high-quality audio files for better transcription accuracy
* Minimize background noise
* Ensure clear speech with good volume levels
* Use appropriate sample rates (16kHz or higher recommended)
* For WebSocket streaming, use PCM format: `pcm_s16le_16000`
* Consider file size limits for uploads
* For long audio files, consider splitting into smaller chunks
* Use streaming for real-time applications when available

**Diarization Best Practices**

* Works best with clear audio and distinct speakers
* Speakers are labeled as SPEAKER\_00, SPEAKER\_01, etc.
* Use with `verbose_json` format to get segment-level speaker information

**Next Steps**

* Explore our [API Reference](/reference/audio-transcriptions) for detailed parameter documentation
* Learn about [Text-to-Speech](/docs/text-to-speech) for the reverse operation
* Check out our [Real-time Audio Transcription App guide](/docs/how-to-build-real-time-audio-transcription-app)


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt