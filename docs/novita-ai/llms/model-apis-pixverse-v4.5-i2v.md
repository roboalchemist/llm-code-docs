# Source: https://novita.ai/docs/api-reference/model-apis-pixverse-v4.5-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# PixVerse V4.5 Image to Video

Generate high-quality videos from text descriptions and image using PixVerse's latest v4.5 model. Supports multiple resolutions, aspect ratios, and motion modes for versatile video creation.

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
  Text prompt for video generation.

  * Maximum length: 2048 characters
  * Clear description of desired scene and motion
</ParamField>

<ParamField body="image" type="string" required={true}>
  First frame of the video.

  * Supported image formats include .jpg/.jpeg/.png
  * The image file size cannot exceed 10MB
  * The image resolution should not be less than 300\*300px
  * The aspect ratio of the image should be between 1:2.5 \~ 2.5:1
</ParamField>

<ParamField body="resolution" type="string" required={false}>
  Video quality. Default: `540p`<br />
  Accepted values:

  * fast\_mode is false: `360p`, `540p`, `720p`, `1080p`
  * fast\_mode is true: `360p`, `540p`, `720p`
</ParamField>

<ParamField body="negative_prompt" type="string" required={false}>
  Negative prompt for generation.

  * Maximum length: 2048 characters
</ParamField>

<ParamField body="fast_mode" type="boolean" required={false}>
  Whether to enable fast mode, which will generate videos more quickly but may reduce quality and lower the price.

  Default: `false`.
</ParamField>

<ParamField body="style" type="string" required={false}>
  Style preset (v3.5 only).<br />
  Accepted values: `anime`, `3d_animation`, `clay`, `comic`, `cyberpunk`
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  The random seed to use for the generation.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).