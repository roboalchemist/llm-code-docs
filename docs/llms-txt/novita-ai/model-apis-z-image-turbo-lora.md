# Source: https://novita.ai/docs/api-reference/model-apis-z-image-turbo-lora.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Z Image Turbo LoRA

Z-Image Turbo LoRA is a high-speed image generation model that supports rapid generation of high-quality images based on text prompts, with support for applying custom LoRA weights.

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
  Random seed for generation. -1 means using a random seed

  Value range: \[-1, 2147483647]
</ParamField>

<ParamField body="size" type="string" default="1024*1024">
  Pixel dimensions of the generated image (width\*height)
</ParamField>

<ParamField body="loras" type="array" default="[]">
  List of LoRAs to apply (maximum 3)

  Array length: 0 - 3

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="path" type="string" required={true}>
      URL or path to the LoRA weights
    </ParamField>

    <ParamField body="scale" type="number" default={1}>
      Scale factor for the LoRA weights. Used to scale the LoRA weights before merging with the base model

      Value range: \[0, 4]
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Positive prompt for generation
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).