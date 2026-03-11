# Source: https://novita.ai/docs/api-reference/model-apis-vidu-q3-pro-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu Q3 Pro Image-to-Video

Vidu Q3 Pro Image-to-Video transforms static images into dynamic videos with natural motion and smoother scene dynamics while maintaining subject consistency.

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
  Random seed for reproducibility; 0 or omit for random generation

  Value range: \[0, 2147483647]
</ParamField>

<ParamField body="audio" type="string">
  Custom audio URL for video background music; supports mp3, wav, m4a, flac; max 20MB
</ParamField>

<ParamField body="style" type="string" default="general">
  Visual style of output; general for realistic, anime for animated style

  Optional values: `general`, `anime`
</ParamField>

<ParamField body="images" type="array" required={true}>
  Reference image URLs for video generation; supports `.jpg`, `.jpeg`, `.png`, `.webp`.
  Max file size 50MB per image; aspect ratio must be between 1:4 and 4:1.
  only support one image input now.
</ParamField>

<ParamField body="is_rec" type="boolean" default={false}>
  Enable audio scene matching; when true, matches audio rhythm to video motion
</ParamField>

<ParamField body="prompt" type="string">
  Motion description for video generation; describes scene motion, actions, and dynamics.

  Length limit: 0 - 1500
</ParamField>

<ParamField body="wm_url" type="string">
  Custom watermark image URL; supports png, jpeg, jpg, webp; max 10MB
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  Video length in seconds

  Value range: \[1, 16]
</ParamField>

<ParamField body="off_peak" type="boolean" default={false}>
  Use off-peak pricing; when true, task is queued for off-peak processing at reduced cost
</ParamField>

<ParamField body="watermark" type="boolean" default={false}>
  Enable watermark on output video
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output video resolution

  Optional values: `540p`, `720p`, `1080p`
</ParamField>

<ParamField body="wm_position" type="string">
  Watermark position on video

  Optional values: `top-left`, `top-right`, `bottom-left`, `bottom-right`
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Output video aspect ratio

  Optional values: `16:9`, `9:16`, `4:3`, `3:4`, `1:1`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).