# Source: https://novita.ai/docs/api-reference/model-apis-hunyuan-image-3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan Image 3

Hunyuan Image 3.0 is a state-of-the-art text-to-image generation model. By simply providing a written prompt, you can create high-quality images that capture the essence of your story, resonate emotionally, and elevate your creative output.

<Tip>
  This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the generation results.
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
  The positive prompt for the generation.
</ParamField>

<ParamField body="size" type="string" required={false}>
  The size of the generated media in pixels (width\*height). Range \[256 \~ 1536 per dimension]. Default is `1024*1024`.
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  The random seed to use for the generation. -1 means a random seed will be used. Range \[-1 \~ 2147483647]. Default is `-1`.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).