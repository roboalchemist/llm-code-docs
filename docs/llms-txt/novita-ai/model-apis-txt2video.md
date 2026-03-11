# Source: https://novita.ai/docs/api-reference/model-apis-txt2video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text to Video

**This API transforms textual descriptions into dynamic videos. By interpreting and visualizing the input text, it creates engaging video content that corresponds to the described scenarios, events, or narratives. This capability is ideal for content creation where the visual representation of text-based information enhances understanding or entertainment value.**

> This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the video generation results.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="extra" type="object" required={false}>
  Optional extra parameters for the request.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="response_video_type" type="string" required={false}>
      The returned video type. Default is mp4.<br />
      Enum: `mp4`, `gif`
    </ParamField>

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
              Set to true to enable Test Mode, or false to disable it. The default is false.
            </ParamField>

            <ParamField body="return_task_status" type="string" required={true}>
              Control the data content of the mock event. When set to TASK\_STATUS\_SUCCEED, you'll receive a normal response; when set to TASK\_STATUS\_FAILED, you'll receive an error response.<br />
              Enum: `TASK_STATUS_SUCCEED`, `TASK_STATUS_FAILED`
            </ParamField>
          </Expandable>
        </ParamField>
      </Expandable>
    </ParamField>

    <ParamField body="enterprise_plan" type="object" required={false}>
      Dedicated Endpoints settings, which only take effect for users who have already subscribed to the [Dedicated Endpoints Documentation](/guides/model-apis-dedicated-endpoints).

      <Expandable title="properties" defaultOpen={false}>
        <ParamField body="enabled" type="boolean" required={false}>
          Set to true to schedule this task to use your Dedicated Endpoints's dedicated resources. Default is false.
        </ParamField>
      </Expandable>
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="model_name" type="string" required={true}>
  Name of SD1.x checkpoints; this parameter specifies the name of the model checkpoint. Retrieve the corresponding sd\_name value by invoking the <a href="/api-reference/model-apis-get-model" target="_blank">Query Model</a> API with filter.types=checkpoint as the query parameter.
</ParamField>

<ParamField body="height" type="integer" required={true}>
  Height of the video, range \[256, 1024]
</ParamField>

<ParamField body="width" type="integer" required={true}>
  Width of the video, range \[256, 1024]
</ParamField>

<ParamField body="steps" type="integer" required={true}>
  The number of denoising steps. More steps usually produce higher quality content but take more time to generate. Range \[1, 50]
</ParamField>

<ParamField body="prompts" type="object[]" required={true}>
  The total number of frames in prompts must be less than or equal to 128, where the total number of frames is the cumulative sum of all prompt frames.

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="frames" type="integer" required={true}>
      Frames of this video clip, Range \[8, 64]
    </ParamField>

    <ParamField body="prompt" type="string" required={true}>
      Text input required to guide the generation, separated by `,`, Range \[1, 1024].
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="negative_prompt" type="string" required={false}>
  Text input that will not guide the generation, separated by `,`, Range \[1, 1024].
</ParamField>

<ParamField body="guidance_scale" type="number" required={false}>
  This setting determines how closely Stable Diffusion will adhere to your prompt. Higher guidance forces the model to better follow the prompt but may result in lower quality output. Range \[1, 30].
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  A seed is a number from which Stable Diffusion generates noise, which, makes generation deterministic. Using the same seed and set of parameters will produce identical content each time, minimum -1. Defaults to -1.
</ParamField>

<ParamField body="loras" type="object[]" required={false}>
  LoRA is a fast and lightweight training method that inserts and trains a significantly smaller number of parameters instead of all the model parameters. Currently supports up to 5 LoRAs.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="model_name" type="string" required={true}>
      Name of lora, retrieve the corresponding sd\_name\_in\_api value by invoking the <a href="/api-reference/model-apis-get-model">Get Model API</a> endpoint with filter.types=lora as the query parameter.
    </ParamField>

    <ParamField body="strength" type="number" required={true}>
      The strength value of lora. The larger the value, the more biased the effect is towards lora, Range \[0, 1]
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="embeddings" type="object[]" required={false}>
  Textual Inversion is a training method for personalizing models by learning new text embeddings from a few example images, currently supports up to 5 embeddings.

  <Expandable title="properties" defaultOpen={false}>
    <ParamField body="model_name" type="string" required={true}>
      Name of textual Inversion model, you can call the <a href="/api-reference/model-apis-get-model">Get Model API</a> endpoint with parameter filter.types=textualinversion to retrieve the sd\_name\_in\_api field as the model\_name.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="closed_loop" type="boolean" required={false}>
  The closed\_loop parameter controls the behavior of an animation when it loops. Specifically, it determines whether the last frame of the animation will transition smoothly back to the first frame.
</ParamField>

<ParamField body="clip_skip" type="integer" required={false}>
  This parameter indicates the number of layers to stop from the bottom during optimization, so clip\_skip on 2 would mean, that in SD1.x model where the CLIP has 12 layers, you would stop at 10th layer, Range \[1, 12], get reference at [A brief introduction to Clip Skip](/guides/model-apis-clip-skip).
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

This API helps generate videos from text. The returned video can be accessed via the API `/v3/async/task-result` using the `task_id`.

**Try it in [playground](https://novita.ai/playground#txt2video).**

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/txt2video' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "model_name": "darkSushiMixMix_225D_64380.safetensors",
    "height": 512,
    "width": 512,
    "steps": 20,
    "seed": -1,
    "prompts": [
        {
            "frames": 32,
            "prompt": "In the wintry dusk, a little girl holds matches tightly."
        },
        {
            "frames": 32,
            "prompt": "A little girl, barefoot on the frosty pavement, seeks solace."
        },
        {
            "frames": 32,
            "prompt": "A little girl with each match experiences a fleeting dance of warmth and hope."
        },
        {
            "frames": 32,
            "prompt": "In the quiet night, a little girl's silent story unfolds."
        }
    ],
    "negative_prompt": "nsfw, ng_deepnegative_v1_75t, badhandv4, (worst quality:2), (low quality:2), (normal quality:2), lowres, ((monochrome)), ((grayscale)), watermark"
}'
```

`Response:`

```js  theme={"system"}
{
    "task_id": "fa20dff3-18cb-4417-a7f8-269456a35154"
}
```

**Use `task_id` to get images**

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get videos url in `videos` of response.

`Request:`

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/async/task-result?task_id=fa20dff3-18cb-4417-a7f8-269456a35154' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "task": {
        "task_id": "fa20dff3-18cb-4417-a7f8-269456a35154",
        "task_type": "TXT_TO_VIDEO",
        "status": "TASK_STATUS_SUCCEED",
        "reason": "",
        "eta": 0,
        "progress_percent": 100
    },
    "images": [],
    "videos": [
        {
            "video_url": "https://faas-output-video.s3.ap-southeast-1.amazonaws.com/test/61bc0452-03a5-4e5b-ba78-2dbd3db6cc7d/99a87dec55c6431189aff4bad39fb4a0.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20231219%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20231219T143829Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=3b828cd8e72d9e83eb625e5e175defbfbcfc97acf4a605dc83588ae949b698b4",
            "video_url_ttl": "3600",
            "video_type": "mp4"
        }
    ]
}
```

`Video files:`

<video controls className="w-full aspect-video" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/txt2video.mp4" />


Built with [Mintlify](https://mintlify.com).