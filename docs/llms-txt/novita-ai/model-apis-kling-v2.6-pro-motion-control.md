# Source: https://novita.ai/docs/api-reference/model-apis-kling-v2.6-pro-motion-control.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling V2.6 Pro Motion Control

The Kling v2.6 Pro Motion Control model generates animations by applying motion from a reference video to a reference image. It extracts motion paths from 3-30 second video clips to produce smooth, realistic video animations while maintaining subject identity consistency.

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

<ParamField body="image" type="string" required={true}>
  Reference image to animate (URL or base64 encoded); supported formats: `.jpg`, `.jpeg`, `.png`.
  Max file size: 10MB; width and height must be >= 300px; aspect ratio must be between 1:2.5 and 2.5:1.
</ParamField>

<ParamField body="video" type="string" required={true}>
  Reference motion video URL; contains the motion sequence to transfer; supported formats: `.mp4`, `.mov`.
  Max file size: 10MB; width and height must be >= 300px; aspect ratio must be between 1:2.5 and 2.5:1.
  Duration must be between 3 and 30 seconds.
</ParamField>

<ParamField body="prompt" type="string">
  Positive prompt for scene description, style, lighting, etc.
</ParamField>

<ParamField body="negative_prompt" type="string">
  Negative prompt; max 2500 characters.
</ParamField>

<ParamField body="keep_original_sound" type="boolean" default={true}>
  Whether to keep the original audio from the reference video.
</ParamField>

<ParamField body="character_orientation" type="string" required={true}>
  Character orientation in the generated video, can match either the image or video orientation.

  * `image`: Matches the character orientation in the image; reference video duration limited to 10 seconds.
  * `video`: Matches the character orientation in the video; reference video duration limited to 30 seconds.

  Optional values: `image`, `video`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).