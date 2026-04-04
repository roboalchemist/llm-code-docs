# Source: https://novita.ai/docs/api-reference/model-apis-wan2.6-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.6 Image to Video

AI-based image-to-video service. Generate high-quality video content from input images and text prompts, providing professional video generation capabilities: ready-to-use REST inference API, best performance, zero cold start, and affordable pricing.

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
    <ParamField body="prompt" type="string">
      Text prompt that describes the expected elements and visual characteristics in the generated video. Supports both Chinese and English. Each Chinese character/letter counts as one character. The excess part will be automatically truncated.

      Length limit: 0 - 2000
    </ParamField>

    <ParamField body="img_url" type="string" required={true}>
      URL of the input image or Base64-encoded data. Supports HTTP or HTTPS protocol. For local files, you can upload to obtain a temporary URL. Image limitations: formats: JPEG, JPG, PNG (transparent channels not supported), BMP, WEBP; resolution: width and height range \[360, 2000] (pixels); file size: no more than 10MB. Input image notes: 1. Use a public URL - HTTP or HTTPS supported; for local files, upload to obtain a temporary URL, e.g. [https://cdn.translate.alibaba.com/r/wanx-demo-1.png](https://cdn.translate.alibaba.com/r/wanx-demo-1.png). 2. Provide the Base64-encoded image string - format: data:{MIME_type};base64,{base64_data}; e.g. data:image/png;base64,GDU7MtCZEbTbmRZ... (string truncated for display). See documentation for more.
    </ParamField>

    <ParamField body="template" type="string">
      Name of video effect template. If not filled, no effects are used. Different templates support different special effects. Please query the template list before calling to avoid failure.
    </ParamField>

    <ParamField body="audio_url" type="string">
      Audio file URL, which the model will use to generate the video. Supports HTTP or HTTPS protocol. Audio limitations: format wav/mp3; duration 3–30s; file size up to 15MB. If the audio is longer than duration (5s or 10s), only the first 5 or 10 seconds are used, the rest is discarded. If the audio is shorter than the video, the excess part of the video will be silent. For example, for a 3s audio and a 5s video, the first 3 seconds have sound, the last 2 seconds are silent.
    </ParamField>

    <ParamField body="negative_prompt" type="string">
      Negative prompt: describes what content should NOT appear in the video. Supports both Chinese and English, up to 500 characters. Excess content is truncated.

      Length limit: 0 - 500
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="parameters" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="seed" type="integer">
      Random seed. Range is \[0, 2147483647]. If not specified, the system generates a random seed. To improve reproducibility, it is recommended to set a fixed seed. Note: since generation is probabilistic, even with the same seed, results may differ.

      Value range: \[0, 2147483647]
    </ParamField>

    <ParamField body="audio" type="boolean" default={true}>
      Controls whether to add audio. Priority: audio\_url > audio. Only works when audio\_url is empty, see audio settings. true: (default) add audio automatically; false: no audio track in the video.
    </ParamField>

    <ParamField body="duration" type="integer" default={5}>
      Duration (in seconds) of the generated video. Duration affects cost; please check model pricing before use.

      Optional values: `5`, `10`, `15`
    </ParamField>

    <ParamField body="shot_type" type="string" default="multi">
      Video generation mode. single: single shot; multi: multi-shot.

      Optional values: `single`, `multi`
    </ParamField>

    <ParamField body="watermark" type="boolean" default={false}>
      Add watermark at lower-right corner of the video (text fixed as "AI Generated"). false: (default) no watermark; true: watermark added.
    </ParamField>

    <ParamField body="resolution" type="string" default="1080P">
      Target resolution for the generated video. Supports 720P and 1080P.

      Optional values: `720P`, `1080P`
    </ParamField>

    <ParamField body="prompt_extend" type="boolean" default={true}>
      Whether to enable intelligent prompt rewriting. If enabled, a large language model rewrites the prompt for improved results (especially effective for short prompts, at the cost of additional time). true: (default) enabled; false: not enabled.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).