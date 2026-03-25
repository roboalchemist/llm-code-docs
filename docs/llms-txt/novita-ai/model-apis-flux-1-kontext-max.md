# Source: https://novita.ai/docs/api-reference/model-apis-flux-1-kontext-max.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# FLUX.1 Kontext Max

FLUX.1 Kontext \[max] is a model with greatly improved prompt adherence and typography generation meet premium consistency for editing without compromise on speed.

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

<ParamField body="seed" type="integer" required={false}>
  The random seed to use for the generation. Range \[-1 \~ 2147483647].
</ParamField>

<ParamField body="guidance_scale" type="number" required={false}>
  The guidance scale to use for the generation. Default is 3.5. Range \[1.0 \~ 20.0].
</ParamField>

<ParamField body="safety_tolerance" type="string" required={false}>
  The safety tolerance level for the generated image. 1 being the most strict and 5 being the most permissive. Default is 2.<br />
  Enum: `1`, `2`, `3`, `4`, `5`
</ParamField>

<ParamField body="aspect_ratio" type="string" required={false}>
  The aspect ratio of the generated image.<br />
  Enum: `21:9`, `16:9`, `4:3`, `3:2`, `1:1`, `2:3`, `3:4`, `9:16`, `9:21`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).