# Source: https://novita.ai/docs/api-reference/model-apis-vidu-q2-text2video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# VIDU Q2 Text to Video

VIDU Q2 Text to Video API, supports multiple resolution options. Generates video content based on text descriptions.

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

<ParamField body="bgm" type="boolean" default={false}>
  Whether to add background music
</ParamField>

<ParamField body="seed" type="integer">
  Random seed, used to control the randomness of the generation result. The same seed will produce similar results.
</ParamField>

<ParamField body="audio" type="boolean" default={false}>
  Whether to generate audio
</ParamField>

<ParamField body="style" type="string">
  Video style, e.g., cinematic, realistic, artistic, etc.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Text prompt, describing the desired video content in detail

  Length limit: 1 - unlimited
</ParamField>

<ParamField body="duration" type="integer" required={true} default={5}>
  Video duration in seconds, supports 1-10 seconds

  Optional values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`
</ParamField>

<ParamField body="subjects" type="array" default="[]">
  List of subjects, each containing id, images, and voice\_id (can be empty for text-to-video)

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="id" type="string" required={true}>
      Subject ID, referenced in the prompt using @id
    </ParamField>

    <ParamField body="images" type="array" required={true}>
      List of subject image URLs

      Array length: 1 - unlimited
    </ParamField>

    <ParamField body="voice_id" type="string" default="">
      Voice ID, optional
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="watermark" type="boolean" default={false}>
  Whether to add watermark
</ParamField>

<ParamField body="resolution" type="string" default="720p">
  Output video resolution. Default is 720p.

  Optional values: `540p`, `720p`, `1080p`
</ParamField>

<ParamField body="aspect_ratio" type="string">
  Video aspect ratio, e.g., 16:9, 9:16, 1:1, etc.
</ParamField>

<ParamField body="movement_amplitude" type="string">
  Movement amplitude, controls the intensity of object movement in the video

  Optional values: `auto`, `small`, `medium`, `high`
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).