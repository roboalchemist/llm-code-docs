# Source: https://novita.ai/docs/api-reference/model-apis-wan-2.2-t2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 Text to Video

Wan 2.2 Professional Text-to-Video model can generate high-quality video content based on text descriptions. Compared to previous models, it offers significant improvements in visual detail and motion stability, and can produce videos with durations of 5 seconds and 8 seconds.

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
  Basic input information, such as prompts.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="prompt" type="string" required={true}>
      Text prompt. Supports both English and Chinese, with a maximum length of 800 characters, and any excess will be automatically truncated.

      Example value: A small cat running under the moonlight.
    </ParamField>

    <ParamField body="negative_prompt" type="string" required={false}>
      Negative prompt, used to describe content that should be avoided in the video, allowing for restrictions on the video content.

      Supports both English and Chinese, with a maximum length of 500 characters. Any excess will be automatically truncated.

      Example value: Low resolution, errors, worst quality, low quality, incomplete, extra fingers, disproportionate, etc.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="parameters" type="object" required={true}>
  Video processing parameters.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="size" type="string" required={true}>
      Supports resolutions for 480P, 720P, and 1080P.
      Used to specify the video resolution in the format of width\*height. The supported resolutions for different models are as follows:

      **480P tier**: Available video resolutions and their corresponding aspect ratios are:

      * `832*480`: 16:9.
      * `480*832`: 9:16.
      * `624*624`: 1:1.

      **720P tier**: Available video resolutions and their corresponding aspect ratios are:

      * `1280*720`: 16:9.
      * `720*1280`: 9:16.

      **1080P tier**: Available video resolutions and their corresponding aspect ratios are:

      * `1920*1080`: 16:9.
      * `1080*1920`: 9:16.
      * `1440*1440`: 1:1.
      * `1632*1248`: 4:3.
      * `1248*1632`: 3:4.

      <Warning>
        **Common misconceptions about the size parameter**: The size must be set to the specific values of the target resolution (e.g., `1280*720`), not the aspect ratio (e.g., `1:1`) or resolution tier name (e.g., `480P` or `720P`).
      </Warning>
    </ParamField>

    <ParamField body="duration" type="integer" required={false}>
      The duration of the generated video.

      * `480P` and `720P` resolutions, the duration can be either `5` or `8` seconds.
      * `1080P` resolution, the duration is fixed at 5 seconds.

      Default value: `5`.
    </ParamField>

    <ParamField body="prompt_extend" type="bool" required={false}>
      Whether to enable intelligent prompt rewriting. When enabled, a large model is used to intelligently rewrite the input prompt. This significantly improves the generation effect for shorter prompts but increases processing time.

      * `true`: Default value, enable intelligent rewriting.
      * `false`: Do not enable intelligent rewriting.
    </ParamField>

    <ParamField body="seed" type="integer" required={false}>
      Random seed, used to control the randomness of the model's generated content. The value range is `[0, 2147483647]`.

      If not provided, the algorithm automatically generates a random number as the seed. To maintain relatively stable generated content, you can use the same seed parameter value.
    </ParamField>

    <ParamField body="loras" type="array" required={false}>
      1080P is not supported. List of LoRAs to apply (max 3).

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="path" type="string" required={true}>
          Path to the LoRA model. <br />
          Example: `Cseti/wan2.2-14B-Kinestasis_concept-lora-v1`.
        </ParamField>

        <ParamField body="scale" type="float" required={true}>
          Scale of the LoRA model

          Value range: 0.0 \~ 4.0
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).