# Source: https://novita.ai/docs/api-reference/model-apis-kling-o1-video-edit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling-o1 Video Editing

Kling Omni Video O1 video editor supports conversational video editing through natural language commands. With simple text instructions such as "remove pedestrians" or "change day to dusk", you can remove objects, replace backgrounds, modify styles, adjust weather/lighting, and transform scenes.

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

<ParamField body="video" type="string" required={true}>
  The video URL.
</ParamField>

<ParamField body="images" type="array" default="[]">
  Including reference images of the element, scene, style, etc. Max 4.

  Array length: 0 - 4
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  The positive prompt for the generation.
</ParamField>

<ParamField body="fast_mode" type="boolean" default={false}>
  Whether to use fast mode
</ParamField>

<ParamField body="aspect_ratio" type="string">
  The aspect ratio of the generated video.

  Optional values: `16:9`, `9:16`, `1:1`
</ParamField>

<ParamField body="keep_original_sound" type="boolean" default={true}>
  Select whether to keep the video original sound through the parameter.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).