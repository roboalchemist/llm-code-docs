# Source: https://novita.ai/docs/api-reference/model-apis-wan2.6-t2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Text to Video

AI-powered text-to-video service. Generate high-quality video content from text prompts, offering professional video generation capabilities: ready-to-use REST inference API, best-in-class performance, no cold start, and affordable pricing.

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
      Text prompt describing the desired elements and visual features in the generated video. Supported in both Chinese and English, each Chinese character/letter counts as one character; excess will be automatically truncated.

      Length limit: 0 - 2000
    </ParamField>

    <ParamField body="audio_url" type="string">
      Audio file URL to be used by the model to generate video. Supports HTTP or HTTPS. Audio limits: wav/mp3 format; duration 3\~30s; file size ≤ 15MB. Exceeding duration: if audio length exceeds duration value (5s or 10s), only the first 5s or 10s are kept, rest is discarded. If audio is shorter than video duration, the excess part of the video is silent. For example, if audio is 3s and video duration is 5s, the first 3s of the output video has sound, the last 2s is silent.
    </ParamField>

    <ParamField body="negative_prompt" type="string">
      Negative prompt, describing content that should not appear in the video. Allows limiting the video content. Supported in Chinese and English, no more than 500 characters; excess will be automatically truncated.

      Length limit: 0 - 500
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="parameters" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="seed" type="integer">
      Random seed. Range: \[0, 2147483647]. If not specified, the system generates a random seed. For better reproducibility, it is recommended to specify a seed value. Note: Due to probabilistic nature of the model, results might not be exactly identical even with the same seed.

      Value range: \[0, 2147483647]
    </ParamField>

    <ParamField body="size" type="string" default="1920*1080">
      Specify the resolution of the generated video in format width*height. Supports 720P options (1280*720/720*1280/960*960/1088*832/832*1088) and 1080P options (1920*1080/1080*1920/1440*1440/1632*1248/1248\*1632).

      Optional values: `1280*720`, `720*1280`, `960*960`, `1088*832`, `832*1088`, `1920*1080`, `1080*1920`, `1440*1440`, `1632*1248`, `1248*1632`
    </ParamField>

    <ParamField body="audio" type="boolean" default={true}>
      Whether to add audio. Parameter priority: audio\_url > audio. This parameter only works when audio\_url is empty. true: (default) automatically add audio to video; false: no audio, resulting in a silent video.
    </ParamField>

    <ParamField body="duration" type="integer" default={5}>
      Duration of the generated video in seconds. Options: 5, 10, 15; default is 5. Duration directly influences cost: cost = unit price (based on resolution) x duration (seconds). Please confirm model pricing before calling.

      Optional values: `5`, `10`, `15`
    </ParamField>

    <ParamField body="shot_type" type="string" default="multi">
      Video generation mode. 'single' for single-shot generation; 'multi' for multi-shot generation.

      Optional values: `single`, `multi`
    </ParamField>

    <ParamField body="watermark" type="boolean" default={false}>
      Whether to add a watermark. The watermark will be at the bottom right of the video, labeled as "AI Generated". false: (default) no watermark; true: add watermark.
    </ParamField>

    <ParamField body="prompt_extend" type="boolean" default={true}>
      Whether to enable prompt intelligent rewriting. If enabled, a large model is used to smartly rewrite the input prompt, which can significantly improve results for short prompts but may increase processing time. true: (default) enable smart rewriting; false: do not enable.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).