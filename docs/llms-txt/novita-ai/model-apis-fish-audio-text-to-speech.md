# Source: https://novita.ai/docs/api-reference/model-apis-fish-audio-text-to-speech.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Fish Audio Text to Speech

<Note>
  For best results, upload reference audio using the [create model](/api-reference/model-apis-fish-audio-voice-cloning) before using this one. This improves speech quality and reduces latency.
</Note>

Fish Audio converts text into speech.

Audio formats supported:

* WAV / PCM
  * Sample Rate: 8kHz, 16kHz, 24kHz, 32kHz, 44.1kHz
  * Default Sample Rate: 44.1kHz
  * 16-bit, mono

* MP3
  * Sample Rate: 32kHz, 44.1kHz
  * Default Sample Rate: 44.1kHz
  * mono
  * Bitrate: 64kbps, 128kbps (default), 192kbps

* Opus
  * Sample Rate: 48kHz
  * Default Sample Rate: 48kHz
  * mono
  * Bitrate: -1000 (auto), 24kbps, 32kbps (default), 48kbps, 64kbps

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

<ParamField header="model" type="enum<string>" default="s1" required={false}>
  Specify which TTS model to use. Only supports model: `s1`.
</ParamField>

## Request Body

<ParamField body="text" type="string" required={true}>
  Text to be converted to speech.
</ParamField>

<ParamField body="temperature" type="number" default={0.9}>
  Controls randomness in the speech generation. Higher values (e.g., 1.0) make the output more random, while lower values (e.g., 0.1) make it more deterministic. We recommend `0.9` for `s1` model.

  Required range: `0 <= x <= 1`
</ParamField>

<ParamField body="top_p" type="number" default={0.9}>
  Controls diversity via nucleus sampling. Lower values (e.g., 0.1) make the output more focused, while higher values (e.g., 1.0) allow more diversity. We recommend `0.9` for `s1` model.

  Required range: `0 <= x <= 1`
</ParamField>

<ParamField body="references" type="ReferenceAudio · object[] | null">
  References to be used for the speech, this requires MessagePack serialization, this will override reference\_voices and reference\_texts.

  <Expandable title="properties">
    <ParamField body="audio" type="file" required={true}>
      Reference audio file.
    </ParamField>

    <ParamField body="text" type="string" required={true}>
      Reference text corresponding to the audio.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="reference_id" type="string | null">
  ID of the reference model to be used for the speech.
</ParamField>

<ParamField body="prosody" type="ProsodyControl · object">
  Prosody to be used for the speech.

  <Expandable title="properties">
    <ParamField body="speed" type="number" default={1}>
      Speech speed control.
    </ParamField>

    <ParamField body="volume" type="number" default={0}>
      Speech volume control.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="chunk_length" type="integer" default={200}>
  Chunk length to be used for the speech.

  Required range: `100 <= x <= 300`
</ParamField>

<ParamField body="normalize" type="boolean" default={true}>
  Whether to normalize the speech, this will reduce the latency but may reduce performance on numbers and dates.
</ParamField>

<ParamField body="format" type="enum<string>" default="mp3">
  Format to be used for the speech.

  Available options: `wav`, `pcm`, `mp3`, `opus`
</ParamField>

<ParamField body="sample_rate" type="integer | null">
  Sample rate to be used for the speech.
</ParamField>

<ParamField body="mp3_bitrate" type="enum<integer>" default={128}>
  MP3 Bitrate to be used for the speech.

  Available options: `64`, `128`, `192`
</ParamField>

<ParamField body="opus_bitrate" type="enum<integer>" default={32}>
  Opus Bitrate to be used for the speech.

  Available options: `-1000`, `24`, `32`, `48`, `64`
</ParamField>

<ParamField body="latency" type="enum<string>" default="normal">
  Latency to be used for the speech, balanced will reduce the latency but may lead to performance degradation.

  Available options: `normal`, `balanced`
</ParamField>

## Response

The API will directly return the audio stream in the format specified by the `format` parameter (default: mp3).


Built with [Mintlify](https://mintlify.com).