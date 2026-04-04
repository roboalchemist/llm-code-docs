# Source: https://novita.ai/docs/api-reference/model-apis-glm-image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM Image Generation

GLM Image text-to-image generation tool creates high-quality images from text prompts, producing HD images with fine details and high consistency.

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

<ParamField body="size" type="string" default="1280x1280">
  Image size. Recommended values: 1280x1280 (default), 1568x1056, 1056x1568, 1472x1088, 1088x1472, 1728x960, 960x1728. Custom sizes: dimensions should be 1024-2048px, max total pixels 4194304, both must be multiples of 32.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Text description of desired image. Describe the scene, subject, style, and details you want in the generated image.
</ParamField>

<ParamField body="quality" type="string" default="hd">
  Image quality. HD produces finer details with higher consistency.

  Optional values: `hd`
</ParamField>

<ParamField body="watermark_enabled" type="boolean" default={true}>
  Control AI watermark on generated images. true: Enable watermark (default). false: Disable watermark
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).