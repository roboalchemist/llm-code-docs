# Source: https://novita.ai/docs/api-reference/model-apis-z-image-turbo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Z Image Turbo

Z-Image Turbo is a high-speed image generation model that supports rapid generation of high-quality images based on text prompts.

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

<ParamField body="seed" type="integer" default={-1}>
  Random seed for generation. -1 means using a random seed. Range: -1 to 2147483647

  Value range: \[-1, 2147483647]
</ParamField>

<ParamField body="size" type="string" default="1024*1024">
  Pixel dimensions of the generated image (width\*height). Each dimension ranges from 256 to 1536 pixels
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Positive prompt for generation
</ParamField>

<ParamField body="enable_base64_output" type="boolean" default={false}>
  If enabled, the output will be encoded as a BASE64 string instead of a URL. This property is only available via API
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).