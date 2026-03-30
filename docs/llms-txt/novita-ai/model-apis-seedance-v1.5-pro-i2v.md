# Source: https://novita.ai/docs/api-reference/model-apis-seedance-v1.5-pro-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance 1.5 Pro Image To Video

Seedance 1.5 pro Image to Video API.

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

<ParamField body="fps" type="integer" default={24}>
  Frame rate (frames per second). Only 24 fps is supported.

  Optional values: `24`
</ParamField>

<ParamField body="seed" type="integer" default={-1}>
  Seed integer for controlling randomness. Range: \[-1, 2^32-1]. -1 means using a random seed. The same seed with the same request produces similar (but not identical) results.

  Value range: \[-1, 4294967295]
</ParamField>

<ParamField body="image" type="string" required={true}>
  The first frame image for image-to-video generation. Can be an image URL or Base64-encoded image. URL must be accessible. Base64 format: `data:image/<image format>;base64,<Base64 encoding>`. Supported formats: jpeg, png, webp, bmp, tiff, gif. Aspect ratio: (0.4, 2.5), dimensions: (300, 6000) pixels, size: \< 30 MB.
</ParamField>

<ParamField body="ratio" type="string" default="adaptive">
  Aspect ratio of the generated video. 'adaptive': For text-to-video, the model intelligently selects the best ratio based on the prompt; for image-to-video, it automatically selects based on the uploaded first frame image ratio.

  Optional values: `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `21:9`, `adaptive`
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Text prompt describing the expected video content. Supports both Chinese and English. Recommended not to exceed 500 characters. To generate audio with dialogue, place the spoken content within double quotes for better audio generation results.
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  Video duration in seconds. Supports specified duration within the range \[4, 12]. Note: Duration affects billing.

  Value range: \[4, 12]
</ParamField>

<ParamField body="watermark" type="boolean" default={false}>
  Whether the generated video includes a watermark. true: with watermark. false: without watermark.
</ParamField>

<ParamField body="last_image" type="string">
  The last frame image for first-and-last-frame image-to-video generation. Can be an image URL or Base64-encoded image. Requirements are the same as the image field. When aspect ratios differ, the last frame will be automatically cropped to match the first frame.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Video resolution. Seedance 1.5 pro supports 480p and 720p (1080p is not currently supported).

  Optional values: `480p`, `720p`
</ParamField>

<ParamField body="camera_fixed" type="boolean" default={false}>
  Whether to fix the camera position. true: The platform appends a fixed camera instruction to the prompt (effect not guaranteed). false: Camera is not fixed.
</ParamField>

<ParamField body="service_tier" type="string" default="default">
  Service tier for processing the request. 'default': Online inference mode with lower RPM and concurrency quota, suitable for time-sensitive scenarios. 'flex': Offline inference mode with higher TPD quota at 50% of the online mode price, suitable for latency-insensitive scenarios.

  Optional values: `default`, `flex`
</ParamField>

<ParamField body="generate_audio" type="boolean" default={true}>
  Whether the generated video includes synchronized audio. true: Video includes automatically generated speech, sound effects, and background music based on the prompt and visual content. false: Output silent video.
</ParamField>

<ParamField body="execution_expires_after" type="integer" default={172800}>
  Task timeout threshold in seconds, calculated from the created\_at timestamp. Default: 172800 (48 hours). Range: \[3600, 259200]. Tasks exceeding this time will be automatically terminated and marked as 'expired'.

  Value range: \[3600, 259200]
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).