# Source: https://novita.ai/docs/api-reference/model-apis-flux-1-kontext-dev.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# FLUX.1 Kontext Dev

FLUX.1 Kontext dev is a model with greatly improved prompt adherence and typography generation meet premium consistency for editing without compromise on speed.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="prompt" type="string" required={true}>
  The prompt to generate an image from.
</ParamField>

<ParamField body="images" type="string[]" required={false}>
  The images to generate an image from. Limit to a maximum of 4 images.
</ParamField>

<ParamField body="fast_mode" type="boolean" required={false}>
  Whether to enable fast mode, which will generate videos more quickly but may reduce quality and lower the price.

  Default: `false`.
</ParamField>

<ParamField body="size" type="string" required={false}>
  The size of the generated media in pixels (width\*height). Range \[256 \~ 1536 per dimension].
</ParamField>

<ParamField body="num_inference_steps" type="integer" required={false}>
  The number of inference steps to perform. Default is 28. Range \[1 \~ 50].
</ParamField>

<ParamField body="guidance_scale" type="number" required={false}>
  The guidance scale to use for the generation. Default is 2.5. Range \[1.0 \~ 20.0].
</ParamField>

<ParamField body="num_images" type="integer" required={false}>
  The number of images to generate. Default is 1. Range \[1 \~ 4].
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  The random seed to use for the generation. Default is -1. -1 means a random seed will be used. Range \[-1 \~ 2147483647].
</ParamField>

<ParamField body="output_format" type="string" required={false}>
  The format of the output image. Default is jpeg.<br />
  Enum: `jpeg`, `png`, `webp`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).