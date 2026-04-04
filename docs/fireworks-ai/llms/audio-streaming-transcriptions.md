# Source: https://docs.fireworks.ai/api-reference/audio-streaming-transcriptions.md

# Streaming Transcription

<Steps>
  <Step title="Open a WebSocket">
    Streaming transcription is performed over a WebSocket. Provide the transcription parameters and establish a WebSocket connection to the endpoint.
  </Step>

  <Step title="Stream audio and receive transcriptions">
    Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono). In parallel, receive transcription from the WebSocket.
  </Step>
</Steps>

<CardGroup cols={2}>
  <Card title="Try Python notebook" icon="notebook" href="https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb">
    Stream audio to get transcription continuously in real-time.
  </Card>
</CardGroup>

<CardGroup cols={2}>
  <Card title="Explore Python sources" icon="code" href="https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/python">
    Stream audio to get transcription continuously in real-time.
  </Card>

  <Card title="Explore Node.js sources" icon="code" href="https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/nodejs">
    Stream audio to get transcription continuously in real-time.
  </Card>
</CardGroup>

### URLs

Fireworks provides serverless, real-time ASR via WebSocket endpoints. Please select the appropriate version:

#### Streaming ASR v1 (default)

Production-ready and generally recommended for all use cases.

```
wss://audio-streaming.api.fireworks.ai/v1/audio/transcriptions/streaming
```

#### Streaming ASR v2 (preview)

An early-access version of our next-generation streaming transcription service. V2 is good for use cases that require lower latency and higher accuracy in noisy situations.

```
wss://audio-streaming-v2.api.fireworks.ai/v1/audio/transcriptions/streaming
```

### Headers

<ParamField header="Authorization" type="string" required>
  Your Fireworks API key, e.g. `Authorization=API_KEY`. Alternatively, can be provided as a query param.
</ParamField>

### Query Parameters

<ParamField query="Authorization" type="string" optional>
  Your Fireworks API key. Required when headers cannot be set (e.g., browser WebSocket connections). Can alternatively be provided via the Authorization header.
</ParamField>

<ParamField query="response_format" type="string" default="verbose_json" optional>
  The format in which to return the response. Currently only `verbose_json` is recommended for streaming.
</ParamField>

<ParamField query="language" type="string | null" optional>
  The target language for transcription. See the [Supported Languages](#supported-languages) section below for a complete list of available languages.
</ParamField>

<ParamField query="prompt" type="string | null" optional>
  The input prompt that the model will use when generating the transcription. Can be used to specify custom words or specify the style of the transcription. E.g. `Um, here's, uh, what was recorded.` will make the model to include the filler words into the transcription.
</ParamField>

<ParamField query="temperature" type="float" default="0">
  Sampling temperature to use when decoding text tokens during transcription.
</ParamField>

<ParamField query="timestamp_granularities" type="string | list[string] | null" optional>
  The timestamp granularities to populate for this streaming transcription. Defaults to null. Set to `word,segment` to enable timestamp granularities. Use a list for timestamp\_granularities in all client libraries. A comma-separated string like `word,segment` only works when manually included in the URL (e.g. in curl).
</ParamField>

### Client messages

<Tabs>
  <Tab title="binary">
    This field is for client to send audio chunks over to server. Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono).
  </Tab>

  <Tab title="SttStateClear">
    This field is for client event initiating the context clean up.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.state.clear">
      A constant string that identifies the type of event as "stt.state.clear".
    </ResponseField>

    <ResponseField name="reset_id" type="string">
      The ID of the context or session to be cleared.
    </ResponseField>
  </Tab>

  <Tab title="SttInputTrace">
    This field is for client event initiating tracing.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.input.trace">
      A constant string indicating the event type is "stt.input.trace".
    </ResponseField>

    <ResponseField name="trace_id" type="string">
      The ID used to correlate this trace event across systems.
    </ResponseField>
  </Tab>
</Tabs>

### Server messages

<Tabs>
  <Tab title="json">
    <ResponseField name="task" type="string" default="transcribe" required>
      The task that was performed — either `transcribe` or `translate`.
    </ResponseField>

    <ResponseField name="language" type="string" required>
      The language of the transcribed/translated text.
    </ResponseField>

    <ResponseField name="text" type="string" required>
      The transcribed/translated text.
    </ResponseField>

    <ResponseField name="words" type="object[] | null" optional>
      Extracted words and their corresponding timestamps.

      <Expandable title="Word properties">
        <ResponseField name="word" type="string" required>
          The text content of the word.
        </ResponseField>

        <ResponseField name="language" type="string" required>
          The language of the word.
        </ResponseField>

        <ResponseField name="probability" type="number" required>
          The probability of the word.
        </ResponseField>

        <ResponseField name="hallucination_score" type="number" required>
          The hallucination score of the word.
        </ResponseField>

        <ResponseField name="start" type="number" optional>
          Start time of the word in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="end" type="number" optional>
          End time of the word in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="is_final" type="bool" required>
          Indicates whether this word has been finalized.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="segments" type="object[] | null" optional>
      Segments of the transcribed/translated text and their corresponding details.

      <Expandable title="Segment properties (partial)">
        <ResponseField name="id" type="number" required>
          The ID of the segment.
        </ResponseField>

        <ResponseField name="text" type="string" required>
          The text content of the segment.
        </ResponseField>

        <ResponseField name="words" type="object[] | null" optional>
          Extracted words in the segment.
        </ResponseField>

        <ResponseField name="start" type="number" optional>
          Start time of the segment in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>

        <ResponseField name="end" type="number" optional>
          End time of the segment in seconds. Appears only when timestamp\_granularities is set to `word,segment`.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>

  <Tab title="SttStateCleared">
    This field is for server to communicate it successfully cleared the context.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.state.cleared">
      A constant string indicating the event type is "stt.state.cleared"
    </ResponseField>

    <ResponseField name="reset_id" type="string">
      The ID of the context or session that has been successfully cleared.
    </ResponseField>
  </Tab>

  <Tab title="SttOutputTrace">
    This field is for server to complete tracing.

    <ResponseField name="event_id" type="string">
      A unique identifier for the event.
    </ResponseField>

    <ResponseField name="object" type="string" fixed="stt.output.trace">
      A constant string indicating the event type is "stt.output.trace".
    </ResponseField>

    <ResponseField name="trace_id" type="string">
      The ID used to correlate this output trace with the corresponding input trace.
    </ResponseField>
  </Tab>
</Tabs>

### Streaming Audio

Stream short audio chunks (50-400ms) in binary frames of PCM 16-bit little-endian at 16kHz sample rate and single channel (mono).  Typically, you will:

1. Resample your audio to 16 kHz if it is not already.
2. Convert it to mono.
3. Send 50ms chunks (16,000 Hz \* 0.05s = 800 samples) of audio in 16-bit PCM (signed, little-endian) format.

### Handling Responses

The client maintains a state dictionary, starting with an empty dictionary `{}`. When the server sends the first transcription message, it contains a list of segments. Each segment has an `id` and `text`:

```python  theme={null}
# Server initial message:
{
    "segments": [
        {"id": "0", "text": "This is the first sentence"},
        {"id": "1", "text": "This is the second sentence"}
    ]
}

# Client initial state:
{
    "0": "This is the first sentence",
    "1": "This is the second sentence",
}
```

When the server sends the next updates to the transcription, the client updates the state dictionary based on the segment `id`:

```python  theme={null}
# Server continuous message:
{
    "segments": [
        {"id": "1", "text": "This is the second sentence modified"},
        {"id": "2", "text": "This is the third sentence"}
    ]
}

# Client updated state:
{
    "0": "This is the first sentence",
    "1": "This is the second sentence modified",   # overwritten
    "2": "This is the third sentence",             # new
}
```

### Handling Connection Interruptions & Timeouts

Real-time streaming transcription over WebSockets can run for a long time. The longer a WebSocket session runs, the more likely it is to experience interruptions from network glitches to service hiccups.
It is important to be aware of this and build your client to recover gracefully so the stream keeps going without user impact.

In the following section, we’ll outline recommended practices for handling connection interruptions and timeouts effectively.

#### When a connection drops

Although Fireworks is designed to keep streams running smoothly, occasional interruptions can still occur. If the WebSocket is disrupted (e.g., bandwidth limitation or network failures),
your application must initialize a new WebSocket connection, start a fresh streaming session and begin sending audio as soon as the server confirms the connection is open.

#### Avoid losing audio during reconnects

While you’re reconnecting, audio could be still being produced and you could lose that audio segment if it is not transferred to our API during this period.
To minimize the risk of dropping audio during a reconnect, one effective approach is to store the audio data in a buffer until it can re-establish the connection to our API and then sends the data for transcription.

### Keep timestamps continuous across sessions

When timestamps are enabled, the result will include the start and end time of the segment in seconds. And each new WebSocket session will reset the timestamps to start from 00:00:00.

To keep a continuous timeline, we recommend to maintain a running “stream start offset” in your app and add that offset to timestamps from each new session so they align with the overall audio timeline.

### Example Usage

Check out a brief Python example below or example sources:

* [Python notebook](https://colab.research.google.com/github/fw-ai/cookbook/blob/main/learn/audio/audio_streaming_speech_to_text/audio_streaming_speech_to_text.ipynb)
* [Python sources](https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/python)
* [Node.js sources](https://github.com/fw-ai/cookbook/tree/main/learn/audio/audio_streaming_speech_to_text/nodejs)

<CodeGroup>
  ```python  theme={null}
  !pip3 install requests torch torchaudio websocket-client

  import io
  import time
  import json
  import torch
  import requests
  import torchaudio
  import threading
  import websocket
  import urllib.parse

  lock = threading.Lock()
  state = {}

  def on_open(ws):
      def send_audio_chunks():
          for chunk in audio_chunk_bytes:
              ws.send(chunk, opcode=websocket.ABNF.OPCODE_BINARY)
              time.sleep(chunk_size_ms / 1000)

          final_checkpoint = json.dumps({"checkpoint_id": "final"})
          ws.send(final_checkpoint, opcode=websocket.ABNF.OPCODE_TEXT)

      threading.Thread(target=send_audio_chunks).start()

  def on_message(ws, message):
      message = json.loads(message)
      if message.get("checkpoint_id") == "final":
          ws.close()
          return

      update = {s["id"]: s["text"] for s in message["segments"]}
      with lock:
          state.update(update)
          print("\n".join(f" - {k}: {v}" for k, v in state.items()))

  def on_error(ws, error):
      print(f"WebSocket error: {error}")

  # Open a connection URL with query params
  url = "wss://audio-streaming.api.fireworks.ai/v1/audio/transcriptions/streaming"
  params = urllib.parse.urlencode({
      "language": "en",
  })
  ws = websocket.WebSocketApp(
      f"{url}?{params}",
      header={"Authorization": "<FIREWORKS_API_KEY>"},
      on_open=on_open,
      on_message=on_message,
      on_error=on_error,
  )
  ws.run_forever()
  ```
</CodeGroup>

### Dedicated endpoint

For fixed throughput and predictable SLAs, you may request a dedicated endpoint for streaming transcription at [inquiries@fireworks.ai](mailto:inquiries@fireworks.ai) or [discord](https://www.google.com/url?q=https%3A%2F%2Fdiscord.gg%2Ffireworks-ai).

### Supported Languages

The following languages are supported for transcription:

| Language Code | Language Name       |
| ------------- | ------------------- |
| en            | English             |
| zh            | Chinese             |
| de            | German              |
| es            | Spanish             |
| ru            | Russian             |
| ko            | Korean              |
| fr            | French              |
| ja            | Japanese            |
| pt            | Portuguese          |
| tr            | Turkish             |
| pl            | Polish              |
| ca            | Catalan             |
| nl            | Dutch               |
| ar            | Arabic              |
| sv            | Swedish             |
| it            | Italian             |
| id            | Indonesian          |
| hi            | Hindi               |
| fi            | Finnish             |
| vi            | Vietnamese          |
| he            | Hebrew              |
| uk            | Ukrainian           |
| el            | Greek               |
| ms            | Malay               |
| cs            | Czech               |
| ro            | Romanian            |
| da            | Danish              |
| hu            | Hungarian           |
| ta            | Tamil               |
| no            | Norwegian           |
| th            | Thai                |
| ur            | Urdu                |
| hr            | Croatian            |
| bg            | Bulgarian           |
| lt            | Lithuanian          |
| la            | Latin               |
| mi            | Maori               |
| ml            | Malayalam           |
| cy            | Welsh               |
| sk            | Slovak              |
| te            | Telugu              |
| fa            | Persian             |
| lv            | Latvian             |
| bn            | Bengali             |
| sr            | Serbian             |
| az            | Azerbaijani         |
| sl            | Slovenian           |
| kn            | Kannada             |
| et            | Estonian            |
| mk            | Macedonian          |
| br            | Breton              |
| eu            | Basque              |
| is            | Icelandic           |
| hy            | Armenian            |
| ne            | Nepali              |
| mn            | Mongolian           |
| bs            | Bosnian             |
| kk            | Kazakh              |
| sq            | Albanian            |
| sw            | Swahili             |
| gl            | Galician            |
| mr            | Marathi             |
| pa            | Punjabi             |
| si            | Sinhala             |
| km            | Khmer               |
| sn            | Shona               |
| yo            | Yoruba              |
| so            | Somali              |
| af            | Afrikaans           |
| oc            | Occitan             |
| ka            | Georgian            |
| be            | Belarusian          |
| tg            | Tajik               |
| sd            | Sindhi              |
| gu            | Gujarati            |
| am            | Amharic             |
| yi            | Yiddish             |
| lo            | Lao                 |
| uz            | Uzbek               |
| fo            | Faroese             |
| ht            | Haitian Creole      |
| ps            | Pashto              |
| tk            | Turkmen             |
| nn            | Nynorsk             |
| mt            | Maltese             |
| sa            | Sanskrit            |
| lb            | Luxembourgish       |
| my            | Myanmar             |
| bo            | Tibetan             |
| tl            | Tagalog             |
| mg            | Malagasy            |
| as            | Assamese            |
| tt            | Tatar               |
| haw           | Hawaiian            |
| ln            | Lingala             |
| ha            | Hausa               |
| ba            | Bashkir             |
| jw            | Javanese            |
| su            | Sundanese           |
| yue           | Cantonese           |
| zh-hant       | Traditional Chinese |
| zh-hans       | Simplified Chinese  |
