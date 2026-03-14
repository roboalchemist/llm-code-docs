# Source: https://novita.ai/docs/api-reference/model-apis-vidu-q3-pro-t2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu Q3 Pro Text-to-Video

Vidu Q3 Pro Text-to-Video generates high-quality videos with synchronized audio from text descriptions, supporting resolutions up to 1080p and durations from 1-16 seconds.

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

<ParamField body="seed" type="integer">
  Random seed for reproducibility. Use 0 for random.

  Value range: \[0, 2147483647]
</ParamField>

<ParamField body="audio" type="boolean" default={true}>
  Enable synchronized audio generation (dialogue and sound effects). Only supported by Q3 model.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Text description for video generation. Max 2000 characters.

  Length limit: 0 - 2000
</ParamField>

<ParamField body="wm_url" type="string">
  URL of the watermark image.
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  Video length in seconds (1-16).

  Value range: \[1, 16]
</ParamField>

<ParamField body="off_peak" type="boolean" default={false}>
  Use off-peak pricing tier. Tasks will be processed within 48 hours at reduced cost.
</ParamField>

<ParamField body="watermark" type="boolean" default={false}>
  Whether to add watermark to the video.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output video quality.

  Optional values: `540p`, `720p`, `1080p`
</ParamField>

<ParamField body="wm_position" type="integer">
  Watermark position: 1=top-left, 2=top-right, 3=bottom-left, 4=bottom-right.

  Value range: \[1, 4]
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Output video aspect ratio.

  Optional values: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).