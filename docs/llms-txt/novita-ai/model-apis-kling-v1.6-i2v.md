# Source: https://novita.ai/docs/api-reference/model-apis-kling-v1.6-i2v.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# KLING V1.6 Image to Video

KLING V1.6 Image to Video is an AI image-to-video generation model developed by the Kuaishou AI Team. It transforms images into dynamic 5-second videos at 720p / 1080p resolution, offering high-quality visual outputs with enhanced motion and semantic understanding.

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

<ParamField body="mode" type="string" required={false}>
  The mode of the video generation.

  Supports:

  * `Standard`: fast creation, lower cost, and generate 720p video.
  * `Professional`: high quality, higher cost, generate 1080p video, and allow set an end frame.

  Default: `Standard`.
</ParamField>

<ParamField body="image_url" type="string" required={true}>
  The URL of the start frame image to be used for video generation.
</ParamField>

<ParamField body="end_image_url" type="string" required={false}>
  The URL of the end frame image to be used for video generation.

  <Warning>Only available when `mode` is `Professional`.</Warning>
</ParamField>

<ParamField body="prompt" type="string" required={true}>
  Prompt text required to guide the generation.

  Range: `1 <= x <= 2000`.
</ParamField>

<ParamField body="negative_prompt" type="string" required={false}>
  Negative prompts instruct the model on what elements to avoid generating.

  Range: `0 <= x <= 2000`.
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  The length of the generated video in seconds. Default: `5`.<br />
  Optional values: `5`, `10`
</ParamField>

<ParamField body="guidance_scale" type="float" required={false}>
  Guidance scale parameter controls how closely the generated content follows the prompt.

  Range: `0 <= x <= 1`. Default: `0.5`.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

Here is an example of how to use the KLING V1.6 Image to Video API.

1. Generate a task\_id by sending a POST request to the KLING V1.6 Image to Video API.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/kling-v1.6-i2v' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "mode": "Standard", 
    "image_url": "https://pub-f964a1c641c04024bce400ad128c8cd6.r2.dev/kling-v1.6-i2v-image",
    "prompt": "A cute dog standing up from a sitting position while wearing sunglasses",
    "negative_prompt": "low quality",
    "guidance_scale": 0.65
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
        "task_type": "KLING_V16_I2V_STANDARD",
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

<video controls className="w-full aspect-video" src="https://pub-f964a1c641c04024bce400ad128c8cd6.r2.dev/kling-v1.6-i2v-result.mp4" />


Built with [Mintlify](https://mintlify.com).