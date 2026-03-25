# Source: https://novita.ai/docs/api-reference/model-apis-vidu-q2-pro-fast-img2video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 Pro Fast Image to Video

VIDU Q2 Pro Fast image to video API, supports 720P and 1080P resolutions. Fast mode significantly reduces generation time.

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

<ParamField body="bgm" type="boolean" default={false}>
  Whether to add background music
</ParamField>

<ParamField body="seed" type="integer">
  Random seed for controlling randomness. Same seed produces similar results.
</ParamField>

<ParamField body="audio" type="boolean" default={false}>
  Whether to generate audio
</ParamField>

<ParamField body="images" type="array" required={true}>
  Input image URL list

  Array length: 1 - unlimited
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Text prompt describing the desired video content
</ParamField>

<ParamField body="duration" type="integer" required={true} default={5}>
  Video duration in seconds, supports 1-10 seconds

  Optional values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
</ParamField>

<ParamField body="off_peak" type="boolean" default={false}>
  Whether to enable off-peak mode
</ParamField>

<ParamField body="voice_id" type="string">
  Voice ID, optional
</ParamField>

<ParamField body="watermark" type="boolean" default={false}>
  Whether to add watermark
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output video resolution. Supports 720p and 1080p. Default is 720p.

  Optional values: `720p`, `1080p`
</ParamField>

<ParamField body="movement_amplitude" type="string" default="auto">
  Movement amplitude, controls the intensity of object movement

  Optional values: `auto`, `small`, `medium`, `high`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).