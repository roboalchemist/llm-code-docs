# Source: https://novita.ai/docs/api-reference/model-apis-kling-v2.6-pro-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.6 Pro Image-to-Video

The Kling v2.6 Pro Image-to-Video tool transforms static images into dynamic videos, generating natural motion and smoother scene dynamics while maintaining subject consistency.

<Tip>
  This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the video generation results.
</Tip>

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="image" type="string" required={true}>
  First frame image for the video; supported formats: `.jpg`, `.jpeg`, `.png`.
  Max file size: 10MB; width and height must be >= 300px; aspect ratio must be between 1:2.5 and 2.5:1.
</ParamField>

<ParamField body="sound" type="boolean" default={true}>
  Whether to generate audio along with the video.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Positive prompt text for video generation; max 2500 characters.
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  Duration of the generated media (in seconds).

  Optional values: `5`, `10`
</ParamField>

<ParamField body="cfg_scale" type="number" default={0.5}>
  Controls the flexibility of video generation; higher values make the generated content adhere more closely to the prompt.

  Value range: \[0, 1]
</ParamField>

<ParamField body="voice_list" type="array">
  List of voice IDs (max 2).

  Array length: 0 - 2
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Aspect ratio of the generated video.

  Optional values: `16:9`, `9:16`, `1:1`
</ParamField>

<ParamField body="negative_prompt" type="string">
  Negative prompt; max 2500 characters.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).