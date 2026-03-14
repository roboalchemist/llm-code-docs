# Source: https://novita.ai/docs/api-reference/model-apis-glm-tts-voice-clone.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM Voice Clone

Using voice cloning technology to generate speech synthesis with specified voice timbre and text content based on sample audio.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="text" type="string">
  Text content of the sample audio, optional
</ParamField>

<ParamField body="input" type="string" required={true}>
  Target text content for generating preview audio
</ParamField>

<ParamField body="audio_url" type="string" required={true}>
  URL of the sample audio. Size limit is 10MB, recommended audio duration is between 3 to 30 seconds.
</ParamField>

<ParamField body="voice_name" type="string" required={true}>
  Specify a unique voice name
</ParamField>

## Response

<ResponseField name="voice" type="string" required={false}>
  Voice timbre
</ResponseField>

<ResponseField name="audio_url" type="string" required={false}>
  URL of the generated preview audio file
</ResponseField>


Built with [Mintlify](https://mintlify.com).