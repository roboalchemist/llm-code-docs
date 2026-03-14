# Source: https://novita.ai/docs/api-reference/model-apis-kling-v3.0-pro-t2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling v3.0 Pro Text-to-Video

Kling v3.0 Pro Text-to-Video generates high-quality videos from text prompts with natural motion and smooth scene dynamics. Supports flexible duration from 3 to 15 seconds, audio-video co-generation, and multi-shot video generation.

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

<ParamField body="sound" type="boolean" default={false}>
  Whether to generate audio simultaneously when generating video.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Text prompt for video generation describing scene motion, camera moves, actions, voice style, ambience, and sound effects; must not exceed 2500 characters. Mutually exclusive with multi\_prompt.

  Length limit: 0 - 2500
</ParamField>

<ParamField body="duration" type="integer" default={5}>
  Duration of generated video in seconds. Supports flexible duration from 3 to 15 seconds.

  Value range: \[3, 15]
</ParamField>

<ParamField body="cfg_scale" type="number" default={0.5}>
  Controls the flexibility of video generation. Higher values result in generated content more closely following the prompt; lower values produce more natural motion.

  Value range: \[0, 1]
</ParamField>

<ParamField body="aspect_ratio" type="string" default="16:9">
  Aspect ratio of the generated video.

  Optional values: `16:9`, `9:16`, `1:1`
</ParamField>

<ParamField body="multi_prompt" type="array">
  List of prompts for multi-shot video generation. Divides video into multiple shots. Mutually exclusive with prompt.
</ParamField>

<ParamField body="negative_prompt" type="string">
  Negative prompt specifying elements to avoid in visuals and audio; must not exceed 2500 characters.

  Length limit: 0 - 2500
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).