# Source: https://novita.ai/docs/api-reference/model-apis-kling-v3.0-std-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling v3.0 Standard Image-to-Video

Kling v3.0 Standard Image-to-Video transforms static images into dynamic videos with natural motion, smooth scene dynamics, optional audio co-generation, and multi-prompt composition support.

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
  First frame image for video; supports `.jpg`, `.jpeg`, `.png`.
  Image file size must not exceed 10MB; width and height must be >= 300px; aspect ratio must be between 1:2.5 and 2.5:1.
</ParamField>

<ParamField body="sound" type="boolean" default={false}>
  Whether to generate audio simultaneously when generating video.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Positive prompt text for video generation, describing scene motion, camera moves, actions, voice style, ambience, and sound effects; must not exceed 2500 characters.
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  Duration of generated video in seconds (3-15).

  Optional values: `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`
</ParamField>

<ParamField body="cfg_scale" type="number" default={0.5}>
  Controls the flexibility of video generation. Lower values produce more natural motion; higher values result in generated content more closely following the prompt.

  Value range: \[0, 1]
</ParamField>

<ParamField body="end_image" type="string">
  Ending frame image URL for guided transitions between start and end frames. Same format constraints as image. Cannot be used together with multi\_prompt.
</ParamField>

<ParamField body="multi_prompt" type="array">
  Array of prompts for multi-shot video composition. Each item contains a prompt and duration for one segment. Cannot be used together with end\_image.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="prompt" type="string" required={true}>
      Motion description for this video segment.
    </ParamField>

    <ParamField body="duration" type="integer" default={5}>
      Duration of this segment in seconds (3-15).

      Value range: \[3, 15]
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="negative_prompt" type="string">
  Negative prompt specifying elements to avoid in visuals and audio; must not exceed 2500 characters.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).