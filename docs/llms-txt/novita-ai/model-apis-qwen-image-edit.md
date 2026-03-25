# Source: https://novita.ai/docs/api-reference/model-apis-qwen-image-edit.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image Edit

Qwen-Image Edit — a 20B MMDiT model for next-gen image edit generation. Built on 20B Qwen-Image, it brings precise bilingual text editing (Chinese & English) while preserving style, and supports both semantic and appearance-level editing.

<Tip>
  This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the image generation results.
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
  The prompt to generate an image from.
</ParamField>

<ParamField body="image" type="string" required={true}>
  The image to generate an image from.
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  The random seed to use for the generation. -1 means a random seed will be used. Range: -1 \~ 2147483647. Default is -1.
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