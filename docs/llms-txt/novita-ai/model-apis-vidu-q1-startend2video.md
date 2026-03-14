# Source: https://novita.ai/docs/api-reference/model-apis-vidu-q1-startend2video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu Q1 Start End to Video

Vidu Q1 Start End to Video transforms static images into dynamic videos, incorporating creative storytelling and animations.

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

<ParamField body="images" type="string[]" required={true}>
  Two images: first is start frame, second is end frame.

  Notes:

  1. Public URL or Base64
  2. Aspect ratios must be close: ratio between start/end frame must be in 0.8\~1.25
  3. Format: png, jpeg, jpg, webp
  4. Max size: 50MB
  5. The length of the base64 decode must be under 10MB, and it must include an appropriate content type string. For instance:

  ```
  data:image/png;base64,{base64_encode}
  ```
</ParamField>

<ParamField body="prompt" type="string" required={false}>
  Prompt description, max 1500 characters.
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  Video duration in seconds. The default is 5 seconds, with `5` being the only available option.
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  Random seed for video generation.

  * Defaults to a random seed number
  * Manually set values will override the default random seed
</ParamField>

<ParamField body="resolution" type="string" required={false}>
  Output video resolution. Default is 1080p, with `1080p` as the only option available.
</ParamField>

<ParamField body="movement_amplitude" type="string" required={false}>
  The movement amplitude of objects in the frame. Default: `auto`<br />
  Accepted values: `auto`, `small`, `medium`, `large`
</ParamField>

<ParamField body="bgm" type="boolean" required={false}>
  Whether to add background music to the generated video. Default: `false`<br />
  Acceptable values: `true`, `false`

  When true, the system will automatically add a suitable BGM. BGM has no time limit and the system automatically adapts.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).