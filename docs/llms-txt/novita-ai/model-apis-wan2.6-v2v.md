# Source: https://novita.ai/docs/api-reference/model-apis-wan2.6-v2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Reference Video

AI-based reference video service that supports generation of high-quality videos from text prompts, providing professional video generation capabilities: plug-and-play REST inference API, optimal performance, no cold start, and affordable pricing.

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

<ParamField body="input" type="object" required={true}>
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="prompt" type="string" required={true}>
      Text prompt describing the elements and visual features expected in the generated video. Supports both Chinese and English; each Chinese character/letter counts as one character; any excess will be automatically truncated.

      Length limit: 0 - 2000
    </ParamField>

    <ParamField body="audio_url" type="string">
      URL of the audio file to be used for video generation by the model. Supports HTTP or HTTPS. Audio requirements: wav or mp3 format; duration 3 to 30 seconds; file size not exceeding 15MB. If the audio length exceeds the duration value (5s or 10s), only the first 5 or 10 seconds will be used, and the rest will be discarded. If the audio length is less than the video duration, the overflow part will be silent. For example, if the audio is 3 seconds and the video duration is 5 seconds, the first 3 seconds of the video will have sound and the last 2 seconds will be silent.
    </ParamField>

    <ParamField body="reference_urls" type="array" required={true}>
      Reference videos are indexed as characterx according to their order. For example, if there are two reference videos, the prompt should specify 'character1 sings by the road, character2 dances nearby.' For a single reference video, still use character1.

      Array length: 1 - 3
    </ParamField>

    <ParamField body="negative_prompt" type="string">
      Negative prompt describing unwanted content in the video scene, which can restrict video visuals. Supports both Chinese and English, up to 500 characters; excess will be automatically truncated.

      Length limit: 0 - 500
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="parameters" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="seed" type="integer">
      Random seed. The range is \[0, 2147483647]. If not specified, the system generates a random seed automatically. To improve reproducibility, it is recommended to fix the seed value. Note that results may not be completely deterministic even with the same seed.

      Value range: \[0, 2147483647]
    </ParamField>

    <ParamField body="size" type="string" default="1920*1080">
      Specify the resolution of the generated video in the format width*height. Supported 720P levels: 1280*720/720*1280/960*960/1088*832/832*1088; 1080P levels: 1920*1080/1080*1920/1440*1440/1632*1248/1248\*1632.

      Optional values: `1280*720`, `720*1280`, `960*960`, `1088*832`, `832*1088`, `1920*1080`, `1080*1920`, `1440*1440`, `1632*1248`, `1248*1632`
    </ParamField>

    <ParamField body="audio" type="boolean" default={true}>
      Whether to add audio. Parameter priority: audio\_url > audio; only effective when audio\_url is empty. true (default): the video will be generated with audio; false: the video will be silent.
    </ParamField>

    <ParamField body="duration" type="integer" default={5}>
      Duration of the generated video in seconds. Acceptable values are 5 or 10, default is 5. Duration directly affects cost: cost = unit price (based on resolution) × duration (seconds). Please check model pricing before using.

      Optional values: `5`, `10`
    </ParamField>

    <ParamField body="shot_type" type="string" default="multi">
      Video generation mode. 'single': single-shot generation; 'multi': multi-shot generation.

      Optional values: `single`, `multi`
    </ParamField>

    <ParamField body="watermark" type="boolean" default={false}>
      Whether to add a watermark at the bottom right corner of the video. The watermark text is fixed as 'AI Generated.' false (default): no watermark; true: add watermark.
    </ParamField>

    <ParamField body="prompt_extend" type="boolean" default={true}>
      Enable prompt smart rewriting. If enabled, the input prompt will be intelligently rewritten by a large model. This can significantly improve the effect for shorter prompts, but will increase latency. true (default): enable smart rewriting; false: do not enable.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).