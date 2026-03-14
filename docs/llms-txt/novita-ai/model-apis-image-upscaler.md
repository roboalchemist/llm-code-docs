# Source: https://novita.ai/docs/api-reference/model-apis-image-upscaler.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Upscaling

AI-powered image upscaling service that enhances low-resolution images to higher resolutions, providing high-quality image processing: out-of-the-box REST inference API, best performance, no cold start, and affordable pricing.

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
  The URL of the original image to be upscaled.
</ParamField>

<ParamField body="resolution" type="string" default="4k">
  Target resolution after upscaling.

  Optional values: `2k`, `4k`, `8k`
</ParamField>

<ParamField body="output_format" type="string" default="jpeg">
  The output image format.

  Optional values: `jpeg`, `png`, `webp`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).