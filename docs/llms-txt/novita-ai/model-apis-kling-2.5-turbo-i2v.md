# Source: https://novita.ai/docs/api-reference/model-apis-kling-2.5-turbo-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.5 Turbo Image to Video

Kling 2.5 Turbo Image-to-Video can generate cinematic, high-quality videos from a single image and text prompt. It features a new text-temporal engine, enhanced motion rendering, and faster inference speed, resulting in smooth action and content that closely matches the given prompt.

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
  The initial frame image for the video. Supported formats: `.jpg`, `.jpeg`, `.png`. Image size must not exceed 10MB. Minimum resolution: 300x300 pixels.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Positive prompt text for video generation. Maximum length: 2500 characters.
</ParamField>

<ParamField body="duration" type="string" default="5">
  Duration of the generated video (in seconds).

  Allowed values: `5`, `10`
</ParamField>

<ParamField body="cfg_scale" type="number" default={0.5}>
  Controls generation flexibility. Higher values increase adherence to the prompt but reduce creative freedom.

  Value range: 0 to 1
</ParamField>

<ParamField body="mode" type="string" default="pro">
  Video generation mode. Allowed value:

  * `pro`: professional mode
</ParamField>

<ParamField body="negative_prompt" type="string">
  Negative prompt to avoid undesired content in the video. Maximum length: 2500 characters.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).