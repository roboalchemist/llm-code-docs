# Source: https://novita.ai/docs/api-reference/model-apis-kling-v2.1-t2v-master.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.1 Master Text to Video

Kling V2.1 is the latest evolution of Kuaishou's AI-powered video‑generation model, designed to seamlessly create short, cinematic‑quality clips from a single image or a text prompt. It represents a major leap forward from Kling 2.0, emphasizing motion fidelity, visual coherence, and prompt accuracy.

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

<ParamField body="prompt" type="string" required={true}>
  Text prompt for generation; Positive text prompt; Cannot exceed 2500 characters.
</ParamField>

<ParamField body="duration" type="string" default="5">
  The duration of the generated media in seconds.

  Available options: `5`, `10`
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Generated video aspect ratio.

  Available options: `16:9`, `9:16`, `1:1`
</ParamField>

<ParamField body="guidance_scale" type="number" default={0.5}>
  The guidance scale to use for the generation.

  Range: 0 to 1
  Step: 0.1
</ParamField>

<ParamField body="negative_prompt" type="string">
  Negative text prompt; Cannot exceed 2500 characters.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).