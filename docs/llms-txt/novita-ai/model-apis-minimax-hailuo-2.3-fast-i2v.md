# Source: https://novita.ai/docs/api-reference/model-apis-minimax-hailuo-2.3-fast-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Minimax Hailuo 2.3 Fast Image to Video

Minimax Hailuo 2.3 Fast offers significantly accelerated video generation, effectively balancing quality and performance at a more cost-effective rate.

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
  Prompt text required to guide the generation.

  Range: `1 <= x <= 2000`.
</ParamField>

<ParamField body="image" type="string" required={true}>
  The image to be used for video generation. Supports public URL or Base64 encoding(`data:image/jpeg;base64,...`).
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  The length of the generated video in seconds. Default: `6`<br />
  Optional values: `6`, `10`
</ParamField>

<ParamField body="resolution" type="string" required={false}>
  The resolution of the generated video. Default: `768P`

  * For 6-second videos: supports `768P`, `1080P`
  * For 10-second videos: supports `768P` only
</ParamField>

<ParamField body="enable_prompt_expansion" type="boolean" required={false}>
  Whether to enable prompt optimization.

  Default: `true`.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).