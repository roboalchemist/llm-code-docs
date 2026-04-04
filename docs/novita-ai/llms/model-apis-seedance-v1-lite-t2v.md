# Source: https://novita.ai/docs/api-reference/model-apis-seedance-v1-lite-t2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance V1 Lite Text to Video

Seedance V1 Lite is an AI video model designed for coherent multi-shot video generation, offering smooth motion and precise adherence to detailed prompts. It supports resolutions of 480p, 720p, and 1080p.

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

<ParamField body="prompt" type="string" required={true}>
  Text prompt for video generation; Positive text prompt; Cannot exceed 2000 characters.
</ParamField>

<ParamField body="resolution" type="string" required={true}>
  Video quality. Accepted values: `480p`, `720p`, `1080p`
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  The aspect ratio of the generated video.
  Accepted values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
</ParamField>

<ParamField body="duration" type="integer" required={true} default={5}>
  Specifies the length of the generated video in seconds. Available options: `5`, `10`
</ParamField>

<ParamField body="camera_fixed" type="boolean" default={false}>
  Determines if the camera position should remain fixed.
</ParamField>

<ParamField body="seed" type="integer" default={-1} minimum={-1} maximum={2147483647}>
  The random seed to use for the generation. -1 means a random seed will be used.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).