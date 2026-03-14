# Source: https://novita.ai/docs/api-reference/model-apis-glm-asr.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM Audio to Text

Use the GLM-ASR-2512 model to transcribe audio files into text, supporting multi-language transcription.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="file" type="string" required={true}>
  The audio file URL or Base64 encoded string to be transcribed. Supported audio formats: .wav / .mp3. Limitations: file size ≤ 25 MB, audio duration ≤ 30 seconds
</ParamField>

<ParamField body="prompt" type="string">
  For long text scenarios, you can provide previous transcription results as context. Recommended to be less than 8000 characters.
</ParamField>

<ParamField body="hotwords" type="array">
  Hotword list to improve recognition accuracy for domain-specific vocabulary. Format example: \["person name", "place name"]. Recommended not to exceed 100 items.

  Array length: 0 - 100
</ParamField>

## Response

<ResponseField name="text" type="string" required={false}>
  The complete transcribed content of the audio
</ResponseField>


Built with [Mintlify](https://mintlify.com).