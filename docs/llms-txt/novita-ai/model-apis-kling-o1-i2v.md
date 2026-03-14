# Source: https://novita.ai/docs/api-reference/model-apis-kling-o1-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling-o1 Image to Video

Kling Omni Video O1 image-to-video tool leverages MVL (Multimodal Vision Language) technology to convert static images into dynamic cinematic videos. It maintains subject consistency while adding natural motion, physical simulation, and smooth scene dynamics.

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
  first\_frame is the first frame
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  The positive prompt for the generation.
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  The duration of the generated media in seconds.

  Optional values: `5`, `10`
</ParamField>

<ParamField body="last_image" type="string">
  last\_frame is the last frame.
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  The aspect ratio of the generated video.

  Optional values: `16:9`, `9:16`, `1:1`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).