# Source: https://novita.ai/docs/api-reference/model-apis-vidu-q2-pro-multiframe.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 Pro Multi-frame to Video

VIDU Q2 Pro multi-frame to video API, generates high-quality coherent video content from multiple keyframe images.

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

<ParamField body="wm_url" type="string">
  Watermark image URL. Uses default watermark if enabled but not provided. Ignored if watermark is false.
</ParamField>

<ParamField body="payload" type="string">
  Pass-through parameter. No processing, only data transmission. Maximum 1048576 characters.
</ParamField>

<ParamField body="meta_data" type="string">
  Metadata identifier in JSON format string. Transparent field.
</ParamField>

<ParamField body="watermark" type="boolean" default={false}>
  Whether to add watermark. true: add watermark; false: no watermark. Default is no watermark.
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Video resolution. Default is 720p.

  Optional values: `540p`, `720p`, `1080p`
</ParamField>

<ParamField body="start_image" type="string" required={true}>
  First frame image. Supports Base64 encoding or image URL. Only 1 image supported. Supports png, jpeg, jpg, webp formats. Image ratio should be less than 1:4 or 4:1. Maximum size 50 MB.
</ParamField>

<ParamField body="wm_position" type="string" default="bottom_left">
  Watermark position. Default is bottom\_left. Ignored if watermark is false.

  Optional values: `top_left`, `top_right`, `bottom_right`, `bottom_left`
</ParamField>

<ParamField body="image_settings" type="array" required={true}>
  Keyframe configuration array, minimum 2 keyframes, maximum 9 keyframes

  Array length: 2 - 9

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="prompt" type="string">
      Prompt for continuing from the previous image, used to control the generated video content.
    </ParamField>

    <ParamField body="duration" type="integer" default={5}>
      Duration between keyframes in seconds. Default is 5s. Valid range: 2-7 seconds.

      Value range: \[2, 7]
    </ParamField>

    <ParamField body="key_image" type="string" required={true}>
      Intermediate frame reference image. Model uses this as the end frame to generate video. Supports Base64 encoding or image URL. Only 1 image supported. Input order is timeline order (from start to end). Supports png, jpeg, jpg, webp formats. Image ratio should be less than 1:4 or 4:1. Maximum size 50 MB.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).