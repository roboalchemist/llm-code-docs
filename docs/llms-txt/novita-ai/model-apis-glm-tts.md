# Source: https://novita.ai/docs/api-reference/model-apis-glm-tts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM Text to Speech

Convert text to natural speech using GLM-TTS, supporting multiple voices, emotion control, and tone adjustment.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="input" type="string" required={true}>
  The text to convert to speech

  Length limit: 0 - 1024
</ParamField>

<ParamField body="speed" type="number" default={1}>
  Speech speed, default is 1.0, range \[0.5, 2]

  Value range: \[0.5, 2]
</ParamField>

<ParamField body="voice" type="string" required={true} default="tongtong">
  The voice to use for audio generation, supporting both system voices and cloned voices. System voices include: tongtong (Tongtong, default voice), chuichui (Chuichui), xiaochen (Xiaochen), jam (Dongdong Zoo jam voice), kazi (Dongdong Zoo kazi voice), douji (Dongdong Zoo douji voice), luodo (Dongdong Zoo luodo voice)
</ParamField>

<ParamField body="volume" type="number" default={1}>
  Volume, default is 1.0, range (0, 10]

  Value range: \[0, 10]
</ParamField>

<ParamField body="response_format" type="string" default="pcm">
  Audio output format, defaults to pcm format

  Optional values: `wav`, `pcm`
</ParamField>

<ParamField body="watermark_enabled" type="boolean">
  Controls whether to add watermark when generating AI audio. true: Enables explicit watermark and implicit digital watermark for AI-generated content by default, complying with policy requirements. false: Disables all watermarks, only effective for users who have completed watermark removal action.
</ParamField>

## Response

Request processed successfully, recommended sample rate is 24000

Format: `binary`


Built with [Mintlify](https://mintlify.com).