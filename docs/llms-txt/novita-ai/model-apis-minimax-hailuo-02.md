# Source: https://novita.ai/docs/api-reference/model-apis-minimax-hailuo-02.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Minimax Hailuo-02

Minimax Hailuo-02 (also known as Hailuo) is an AI video generation model that supports both text-to-video and image-to-video generation. It can generate 6-second videos at 768p or 1080p resolution, and 10-second videos at 768p resolution.

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

<ParamField body="image" type="string" required={false}>
  The first frame image to be used for video generation. Supports public URL or Base64 encoding(`data:image/jpeg;base64,...`).
</ParamField>

<ParamField body="end_image" type="string" required={false}>
  The end frame image to be used for video generation. Supports public URL or Base64 encoding(`data:image/jpeg;base64,...`).
</ParamField>

<ParamField body="duration" type="integer" required={false}>
  The length of the generated video in seconds. Default: `6`<br />
  Optional values: `6`, `10`
</ParamField>

<ParamField body="resolution" type="string" required={false}>
  The resolution of the generated video. Default: `768P`

  * For 6-second videos: supports `768P`, `1080P`
  * For 10-second videos: supports `768P` only
</ParamField>

<ParamField body="enable_prompt_expansion" type="boolean" required={false}>
  Whether to enable prompt optimization.

  Default: `true`.
</ParamField>

<ParamField body="fast_pretreatment" type="boolean" required={false} default={false}>
  Whether to shorten the prompt optimization time.

  Default: `false`.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

Here is an example of how to use the Minimax Hailuo-02 API.

1. Generate a task\_id by sending a POST request to the Minimax Hailuo-02 API.

`Request:`

```bash  theme={"system"}
curl \
-X POST https://api.novita.ai/v3/async/minimax-hailuo-02 \
-H "Authorization: Bearer $your_api_key" \
-H "Content-Type: application/json" \
-d '{
  "image": "https://doc-assets.novitai.com/minimax-hailuo-video-02-input-image.jpg",
  "prompt": "A gentleman leans on a retro-futuristic car under a streetlight, zooming out revealing classic design elements in a timeless, nostalgic style.",
  "duration": 6,
  "resolution": "768P",
  "enable_prompt_expansion": true
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
        "task_type": "MINIMAX_HAILUO_02",
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

<video controls className="w-full aspect-video" src="https://doc-assets.novitai.com/minimax-hailuo-video-02-result.mp4" />


Built with [Mintlify](https://mintlify.com).