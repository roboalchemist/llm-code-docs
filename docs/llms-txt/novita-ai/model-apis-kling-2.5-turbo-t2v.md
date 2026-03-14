# Source: https://novita.ai/docs/api-reference/model-apis-kling-2.5-turbo-t2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.5 Turbo Text to Video

Kling 2.5 Turbo is an advanced text-to-video model capable of generating ultra-smooth motion, cinematic visuals, and outputs that closely adhere to the input prompt.

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
  Positive text prompt that guides the video generation. Maximum length: 2500 characters.
</ParamField>

<ParamField body="duration" type="string" default="5">
  Duration of the generated video in seconds.

  Available options: `5`, `10`
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Aspect ratio of the output video.

  Available options: `16:9`, `9:16`, `1:1`
</ParamField>

<ParamField body="cfg_scale" type="number" default={0.5}>
  Controls the adherence to the prompt. Higher values result in outputs that more strictly follow the prompt, while lower values allow for more creativity.

  Range: 0 to 1
</ParamField>

<ParamField body="mode" type="string" default="pro">
  Video generation mode. Supported values:

  * `pro`: Professional mode
</ParamField>

<ParamField body="negative_prompt" type="string">
  Negative text prompt to specify elements to avoid in the output. Maximum length: 2500 characters.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).