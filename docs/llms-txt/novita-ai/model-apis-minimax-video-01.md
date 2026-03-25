# Source: https://novita.ai/docs/api-reference/model-apis-minimax-video-01.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Minimax Video-01

Minimax Video-01 (also known as Hailuo) is an AI video generation model that creates 6-second videos at 720p resolution and 25fps. It supports both text-to-video and image-to-video generation.

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

<ParamField body="prompt" type="string" required={true}>
  Prompt text required to guide the generation.

  Range: `1 <= x <= 2000`.
</ParamField>

<ParamField body="image_url" type="string" required={false}>
  The URL of the first frame image to be used for video generation.
</ParamField>

<ParamField body="enable_prompt_expansion" type="boolean" required={false}>
  Whether to enable prompt optimization.

  Default: `true`.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

Here is an example of how to use the Minimax Video-01 API.

1. Generate a task\_id by sending a POST request to the Minimax Video-01 API.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/minimax-video-01' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "prompt": "A cute panda is walking in the grassland slowly",
    "image_url": "https://pub-f964a1c641c04024bce400ad128c8cd6.r2.dev/minimax-video-01-image.jpg",
    "enable_prompt_expansion": True,
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
        "task_type": "MINIMAX_VIDEO_01",
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

<video controls className="w-full aspect-video" src="https://pub-f964a1c641c04024bce400ad128c8cd6.r2.dev/minimax-video-01-result.mp4" />


Built with [Mintlify](https://mintlify.com).