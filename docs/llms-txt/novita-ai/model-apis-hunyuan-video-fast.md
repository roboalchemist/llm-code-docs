# Source: https://novita.ai/docs/api-reference/model-apis-hunyuan-video-fast.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hunyuan Video Fast

Accelerated inference for HunyuanVideo with high resolution, a state-of-the-art text-to-video generation model capable of creating high-quality videos with realistic motion from text descriptions.

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

<ParamField body="model_name" type="string" required={true}>
  Name of the model checkpoint.

  Supports: `hunyuan-video-fast`.
</ParamField>

<ParamField body="width" type="integer" required={true}>
  Width of the output video.

  Supports: `720`, `1280`.
</ParamField>

<ParamField body="height" type="integer" required={true}>
  Height of the output video.

  Supports:

  * `720` for `width` of `1280`
  * `1280` for `width` of `720`
</ParamField>

<ParamField body="seed" type="integer" required={true}>
  A seed is a number generates noise, which, makes generation deterministic. Using the same seed and set of parameters will produce identical content each time.

  Range: `-1 <= x <= 9999999999`.
</ParamField>

<ParamField body="steps" type="integer" required={true}>
  The number of denoising steps. More steps usually produce higher quality content but take more time to generate.

  Range: `2 <= x <= 30`.
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Prompt text required to guide the generation.

  Range: `1 <= x <= 2000`.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

Here is an example of how to use the Hunyuan Video Fast API.

1. Generate a task\_id by sending a POST request to the Hunyuan Video Fast API.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/hunyuan-video-fast' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "model_name": "hunyuan-video-fast",
    "height": 720,
    "width": 1280,
    "seed": -1,
    "steps": 30,
    "prompt": "A close up view of a glass sphere that has a zen garden within it. There is a small dwarf in the sphere who is raking the zen garden and creating patterns in the sand.",
    "frames": 85
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
        "task_type": "HUNYUAN_VIDEO_FAST",
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

<video controls className="w-full aspect-video" src="https://pub-f964a1c641c04024bce400ad128c8cd6.r2.dev/hunyuan-video-fast-demo.mp4" />


Built with [Mintlify](https://mintlify.com).