# Source: https://novita.ai/docs/api-reference/model-apis-vidu-2.0-img2video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu 2.0 Image to Video

Vidu 2.0 Image to Video transforms static images into dynamic videos, incorporating creative storytelling and animations.

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
  An image to be used as the start frame of the generated video.

  For fields that accept images:

  * Only accepts 1 image
  * Accepts public URL or Base64 format
  * Supported formats: png, jpeg, jpg, webp
  * The aspect ratio of the images must be less than 1:4 or 4:1
  * All images are limited to 50MB
  * The length of the base64 decode must be under 10MB, and it must include an appropriate content type string. For instance:

  ```
  data:image/png;base64,{base64_encode}
  ```
</ParamField>

<ParamField body="prompt" type="string" required={false}>
  Text prompt for video generation, with a maximum length of 1500 characters.
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  Video duration in seconds. Default is 4 seconds, with options available for `4` or `8` seconds.
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  Random seed for video generation.

  * Defaults to a random seed number
  * Manually set values will override the default random seed
</ParamField>

<ParamField body="resolution" type="string" required={false}>
  Resolution based on duration:

  * 4s: default 360p, options: `360p`, `720p`, `1080p`
  * 8s: default 720p, options: `720p`
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