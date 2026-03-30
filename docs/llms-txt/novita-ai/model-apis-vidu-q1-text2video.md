# Source: https://novita.ai/docs/api-reference/model-apis-vidu-q1-text2video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Vidu Q1 Text to Video

Vidu Q1 Text to Video generates smooth and seamless videos by utilizing keyframes to maintain consistent themes.

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
  Text prompt for video generation, with a maximum length of 1500 characters.
</ParamField>

<ParamField body="style" type="string" required={false}>
  The style of output video. Default: `general`<br />
  Accepted values: `general`, `anime`

  * `general`: General style. Allows style control through prompts
  * `anime`: Anime style. Optimized for anime aesthetics, with better performance for anime-related prompts
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  Video duration in seconds. Default is 5 seconds, with `5` being the only available option.
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