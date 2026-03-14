# Source: https://novita.ai/docs/api-reference/model-apis-flux-2-pro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Flux 2 Pro Image Gen

FLUX.2 \[pro] from Black Forest Labs delivers production-grade text-to-image generation with enhanced realism, sharper text rendering, and native editing for reliable, repeatable results. Ready-to-use REST inference API, best performance, no coldstarts, affordable pricing.

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
  Random seed for generation. -1 means use a random seed. Range: -1 to 2147483647

  Value range: \[-1, 2147483647]
</ParamField>

<ParamField body="size" type="string">
  Pixel size (width\*height) of the output media. Each dimension ranges from 256 to 1536 pixels
</ParamField>

<ParamField body="images" type="array">
  A list of input image URLs for editing. Up to 3 images are supported

  Array length: 1 - 3
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  A text prompt describing the expected editing effect for the image
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).