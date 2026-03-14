# Source: https://novita.ai/docs/api-reference/model-apis-vidu-q1-reference2video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu Q1 Reference to Video

Vidu Q1 Reference to Videos generates videos using a reference image and text description. It supports various subjects, such as characters and objects. By uploading multiple perspectives of a subject, you can create videos that maintain visual consistency.

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
  The model will use the provided images as references to generate a video with consistent subjects.

  For fields that accept images:

  * Accepts 1 to 7 images
  * Images Assets can be provided via URLs or Base64 encode
  * You must use one of the following codecs: PNG, JPEG, JPG, WebP
  * The dimensions of the images must be at least 128x128 pixels
  * The aspect ratio of the images must be less than 1:4 or 4:1
  * All images are limited to 50MB
  * The length of the base64 decode must be under 10MB, and it must include an appropriate content type string. For instance:

  ```
  data:image/png;base64,{base64_encode}
  ```
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Text prompt for video generation, with a maximum length of 1500 characters.
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  Video duration in seconds. The default is 5 seconds, with `5` being the only available option.
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  Random seed for video generation.

  * Defaults to a random seed number
  * Manually set values will override the default random seed
</ParamField>

<ParamField body="aspect_ratio" type="string" required={false}>
  The aspect ratio of the output video. Default: `16:9`<br />
  Accepted values: `16:9`, `9:16`, `1:1`
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