# Source: https://novita.ai/docs/api-reference/model-apis-wan-t2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Wan 2.1 Text to Video

Accelerated inference for Wan 2.1 14B Text-to-Video, a comprehensive and open suite of video foundation models that pushes the boundaries of video generation. By default, the API will generate a video with 5 seconds.

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

<ParamField body="extra" type="object" required={false}>
  Optional extra parameters for the request.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="webhook" type="object" required={false}>
      Webhook settings. More details can be found at [Webhook Documentation](/api-reference/model-apis-webhook).

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="url" type="string" required={true}>
          The URL of the webhook endpoint. Novita AI will send the task generated outputs to your specified webhook endpoint.
        </ParamField>

        <ParamField body="test_mode" type="object" required={false}>
          By specifying Test Mode, a mock event will be sent to the webhook endpoint.

          <Expandable title="properties" defaultOpen={false}>
            <ParamField body="enabled" type="boolean" required={true}>
              Set to true to enable Test Mode, or false to disable it.

              The default is `false`.
            </ParamField>

            <ParamField body="return_task_status" type="string" required={true}>
              Control the data content of the mock event. When set to TASK\_STATUS\_SUCCEED, you'll receive a normal response; when set to TASK\_STATUS\_FAILED, you'll receive an error response.

              Supports: `TASK_STATUS_SUCCEED`, `TASK_STATUS_FAILED`.
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Prompt text required to guide the generation.

  Range: `1 <= x <= 2000`.
</ParamField>

<ParamField body="negative_prompt" type="string" required={false}>
  Negative prompts instruct the model on what elements to avoid generating.

  Range: `0 <= x <= 2000`.
</ParamField>

<ParamField body="width" type="integer" required={false}>
  Width of the output video.

  Supports: `480`, `720`, `832`, `1280`.

  Default: `832`. If the width or height is not specified, the width and the height will be forced to `832` and `480` respectively.
</ParamField>

<ParamField body="height" type="integer" required={false}>
  Height of the output video.

  Supports:

  * (480p) `832` for `width` of `480`
  * (480p) `480` for `width` of `832`
  * (720p) `1280` for `width` of `720`
  * (720p) `720` for `width` of `1280`

  Default: `480`. If the width or height is not specified, the width and the height will be forced to `832` and `480` respectively.
</ParamField>

<ParamField body="loras" type="object[]" required={false}>
  LoRA models to be applied to the video generation.

  Currently supports up to **3 LoRAs**.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="path" type="string" required={true}>
      The path to the LoRA model. You can specify either a LoRA model name from Hugging Face, for example: `Remade-AI/Cyberpunk`; or a model download URL from Civitai, for example: `https://civitai.com/api/download/models/1572591?type=Model&format=SafeTensor`.

      <Warning>
        The LoRA model must be compatible with Wan2.1 14B T2V, otherwise it will not work. Please check compatibility before using it.
      </Warning>
    </ParamField>

    <ParamField body="scale" type="number" required={true}>
      The scale value of lora. The larger the value, the more biased the effect is towards lora.

      Range: `0 <= x <= 4.0`.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  A seed is a number generates noise, which, makes generation deterministic. Using the same seed and set of parameters will produce identical content each time.

  Range: `-1 <= x <= 9999999999`. Default: `-1`.
</ParamField>

<ParamField body="steps" type="integer" required={false}>
  The number of inference steps.

  Range: `1 <= x <= 40`. Default: `30`.
</ParamField>

<ParamField body="guidance_scale" type="float" required={false}>
  Guidance scale parameter controls how closely the generated content follows the prompt.

  Range: `0 <= x <= 10`. Default: `5.0`.
</ParamField>

<ParamField body="flow_shift" type="float" required={false}>
  The flow\_shift parameter primarily affects the speed and magnitude of object movement in the video. Higher values produce more pronounced and faster movement, while lower values make the motion slower and more subtle.

  Range: `1 <= x <= 10`. Default: `5.0`.
</ParamField>

<ParamField body="enable_safety_checker" type="boolean" required={false}>
  The enable\_safety\_checker parameter controls whether the safety filter is applied to the generated content. When enabled, it helps filter out potentially harmful or inappropriate content from the video output.

  Default: `true`.
</ParamField>

<ParamField body="fast_mode" type="boolean" required={false}>
  Whether to enable fast mode, which will generate videos more quickly but may reduce quality and lower the price.

  Default: `false`.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

Here is an example of how to use the Wan 2.1 Text to Video API.

1. Generate a task\_id by sending a POST request to the Wan 2.1 Text to Video API.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/wan-t2v' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "height": 1280,
    "width": 720,
    "seed": -1,
    "prompt": "3D animation of a small, round, fluffy creature with big, expressive eyes explores a vibrant, enchanted forest. The creature, a whimsical blend of a rabbit and a squirrel, has soft blue fur and a bushy, striped tail. It hops along a sparkling stream, its eyes wide with wonder. The forest is alive with magical elements: flowers that glow and change colors, trees with leaves in shades of purple and silver, and small floating lights that resemble fireflies. The creature stops to interact playfully with a group of tiny, fairy-like beings dancing around a mushroom ring. The creature looks up in awe at a large, glowing tree that seems to be the heart of the forest."
}'
```

`Response:`

```js  theme={"system"}
{
    "task_id": "{Returned Task ID}"
}
```

2. Use `task_id` to get output videos.

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get videos url in `videos` of response.

`Request:`

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/async/task-result?task_id={Returned Task ID}' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "task": {
        "task_id": "{Returned Task ID}",
        "task_type": "WAN_TXT_TO_VIDEO",
        "status": "TASK_STATUS_SUCCEED",
        "reason": "",
        "eta": 0,
        "progress_percent": 100
    },
    "images": [],
    "videos": [
        {
            "video_url": "{The URL of the generated video}",
            "video_url_ttl": "3600",
            "video_type": "mp4"
        }
    ]
}
```

`Video files:`

<video controls className="w-full aspect-video" src="https://pub-f964a1c641c04024bce400ad128c8cd6.r2.dev/wan-t2v-demo.mp4" />


Built with [Mintlify](https://mintlify.com).