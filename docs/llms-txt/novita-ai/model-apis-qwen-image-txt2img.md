# Source: https://novita.ai/docs/api-reference/model-apis-qwen-image-txt2img.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen-Image Text to Image

Qwen-Image — a 20B MMDiT model for next-gen text-to-image generation. Especially strong at creating stunning graphic posters with native text.

<Tip>
  This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the image generation results.
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
  Text prompt for image generation.
</ParamField>

<ParamField body="size" type="string" required={false}>
  The size of the generated media in pixels (width\*height). Default is `1024*1024`. Range: 256 \~ 1536 per dimension.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={true}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

Here is an example of how to use the Qwen-Image Text to Image API.

1. Generate a task\_id by sending a POST request to the Qwen-Image Text to Image API.

`Request:`

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/qwen-image-txt2img' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
    "prompt": "A cinematic scene of a quiet girl with short brown hair sitting by a misty lake at dawn. She wears an oversized sweater, holding a warm mug. Soft morning light filters through the trees, cool tones, tranquil mood, light fog, 50mm photography style.",
    "size": "1024*1024"
}'
```

`Response:`

```js  theme={"system"}
{
    "task_id": "{Returned Task ID}"
}
```

2. Use `task_id` to get output images.

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get image url in `images` of response.

`Request:`

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/async/task-result?task_id={Returned Task ID}' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "extra": {
        "has_nsfw_contents": []
    },
    "task": {
        "task_id": "0cdee604-7168-4ff4-9b2a-9793c0cc6cdf",
        "task_type": "QWEN_IMAGE_TEXT_TO_IMAGE",
        "status": "TASK_STATUS_SUCCEED",
        "reason": "",
        "eta": 0,
        "progress_percent": 0
    },
    "images": [
        {
            "image_url": "https://d2p7pge43lyniu.cloudfront.net/output/9dc2f15a-0dd3-49a3-a121-a352f229c84b-u2_c61a700e-dfec-4c01-81c6-bf890ad68f6c.jpeg",
            "image_url_ttl": "0",
            "image_type": "jpeg",
            "nsfw_detection_result": null
        }
    ],
    "videos": [],
    "audios": []
}
```

`Image files:`

<Frame><img src="https://mintcdn.com/novitaai/OIO9nfACcX0vhcTI/images/qwen-txt2img-output.jpeg?fit=max&auto=format&n=OIO9nfACcX0vhcTI&q=85&s=a05d9896c7acab16e08f768a94be236e" alt="LLM API Providers" width="1024" height="1024" data-path="images/qwen-txt2img-output.jpeg" /></Frame>


Built with [Mintlify](https://mintlify.com).