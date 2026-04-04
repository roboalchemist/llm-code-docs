# Source: https://novita.ai/docs/api-reference/model-apis-wan-2.2-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.2 Image to Video

Wan 2.2 Professional Image-to-Video model generates a silent video based on the initial frame image and text. It offers significant improvements in visual detail and motion stability.

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

      Example value: A small cat running on the grass.
    </ParamField>

    <ParamField body="negative_prompt" type="string" required={false}>
      Negative prompt, used to describe content that should be avoided in the video, allowing for restrictions on the video content.

      Supports both English and Chinese, with a maximum length of 500 characters. Any excess will be automatically truncated.

      Example value: Low resolution, errors, worst quality, low quality, incomplete, extra fingers, disproportionate, etc.
    </ParamField>

    <ParamField body="img_url" type="string" required={true}>
      The URL of the initial frame image used for video generation.

      The URL must be publicly accessible and support HTTP or HTTPS protocols.

      Image restrictions:

      * Image formats: JPEG, JPG, PNG (no support for transparency), BMP, WEBP.
      * Image resolution: The width and height of the image should be within the range of \[360, 2000] pixels.
      * File size: No more than 10MB.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="parameters" type="object" required={true}>
  Video processing parameters, such as specifying the output video resolution and duration.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="resolution" type="string" required={true}>
      The resolution tier of the generated video. <br />
      Options: `480P`, `720P`, `1080P`
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

      Example value: true.
    </ParamField>

    <ParamField body="seed" type="integer" required={false}>
      Random seed, used to control the randomness of the model's generated content. The value range is `[0, 2147483647]`.

      If not provided, the algorithm automatically generates a random number as the seed. To maintain relatively stable generated content, you can use the same seed parameter value.

      Example value: 12345.
    </ParamField>

    <ParamField body="loras" type="array" required={false}>
      1080P is not supported. List of LoRAs to apply (max 3).

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="path" type="string" required={true}>
          Path to the LoRA model. <br />
          Example: `ostris/wan22_i2v_14b_orbit_shot_lora`.
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