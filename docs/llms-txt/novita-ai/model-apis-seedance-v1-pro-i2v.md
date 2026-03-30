# Source: https://novita.ai/docs/api-reference/model-apis-seedance-v1-pro-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance V1 Pro Image to Video

Seedance V1 Pro is an AI video model designed for coherent multi-shot video generation, offering smooth motion and precise adherence to detailed prompts. It supports resolutions of 480p, 720p, and 1080p.

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

<ParamField body="prompt" type="string">
  Text prompt for video generation; Positive text prompt; Cannot exceed 2000 characters.
</ParamField>

<ParamField body="image" type="string" required={true}>
  Input image supports both URL and Base64 format.

  * Supported image formats include `jpeg`, `png`, `webp`, `bmp`, `tiff`, `gif`.
  * The image file size cannot exceed 30MB.
  * Its shorter side must be greater than 300 pixels, and its longer side must be less than 6,000 pixels.
  * Its aspect ratio must be in the range of 0.4 to 2.5.
</ParamField>

<ParamField body="last_image" type="string">
  End image, supports both URL and Base64 format.

  * Supported image formats include `jpeg`, `png`, `webp`, `bmp`, `tiff`, `gif`.
  * The image file size cannot exceed 30MB.
  * Its shorter side must be greater than 300 pixels, and its longer side must be less than 6,000 pixels.
  * Its aspect ratio must be in the range of 0.4 to 2.5.

  The first and last frame images provided can be the same. If the aspect ratios of the first and last frame images differ, the first frame image will be used as the reference, and the last frame image will be automatically cropped to match.
</ParamField>

<ParamField body="resolution" type="string" required={true}>
  Video quality. Accepted values: `480p`, `720p`, `1080p`
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  The aspect ratio of the generated video.
  Accepted values: `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16`
</ParamField>

<ParamField body="camera_fixed" type="boolean" default={false}>
  Determines if the camera position should remain fixed.
</ParamField>

<ParamField body="seed" type="integer" default={-1} minimum={-1} maximum={2147483647}>
  The random seed to use for the generation. -1 means a random seed will be used.
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  Specifies the length of the generated video in seconds. Available options: `5`, `10`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).