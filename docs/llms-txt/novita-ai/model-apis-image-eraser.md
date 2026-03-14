# Source: https://novita.ai/docs/api-reference/model-apis-image-eraser.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Eraser

AI-powered image erasing service. Supports object removal from images via mask and text prompts. Offers high-quality image processing: out-of-the-box REST inference API, top performance, no cold start, affordable pricing.

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

<ParamField body="mask" type="string">
  Mask image indicating the area to be erased. Areas to erase should be white; areas to keep should be black.
</ParamField>

<ParamField body="image" type="string" required={true}>
  The original image to be processed.
</ParamField>

<ParamField body="prompt" type="string">
  Text prompt specifying the object or region to remove from the image, e.g., 'dog' or 'hat'.
</ParamField>

<ParamField body="output_format" type="string" default="jpeg">
  Output image format.

  Optional values: `jpeg`, `png`, `webp`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).