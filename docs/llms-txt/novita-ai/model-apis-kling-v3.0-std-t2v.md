# Source: https://novita.ai/docs/api-reference/model-apis-kling-v3.0-std-t2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling v3.0 Standard Text-to-Video

Kling v3.0 Standard Text-to-Video generates high-quality videos from text prompts with smooth motion, cinematic visuals, accurate prompt adherence, and optional native audio co-generation. Supports 3-15 second duration with multiple aspect ratios.

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

<ParamField body="sound" type="boolean" default={false}>
  Whether to generate audio simultaneously when generating video. Supports Chinese and English voice output.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Positive prompt text for video generation; must not exceed 2500 characters.

  Length limit: 0 - 2500
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  Duration of generated video in seconds.

  Optional values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
</ParamField>

<ParamField body="cfg_scale" type="number" default={0.5}>
  Controls the flexibility of video generation. Use 0 for maximum creativity, 0.5 (default) for balanced results, or 1 for strict adherence to the prompt.

  Value range: \[0, 1]
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Aspect ratio of the generated video.

  Optional values: `16:9`, `9:16`, `1:1`
</ParamField>

<ParamField body="negative_prompt" type="string">
  Negative prompt describing elements to avoid in the generated video; must not exceed 2500 characters.

  Length limit: 0 - 2500
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).