# Source: https://docs.aimlapi.com/api-references/video-models/minimax/video-01.md

# video-01

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `video-01`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/video-01" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

An innovative AI model designed for generating high-quality videos from text prompts or image. Developed by Hailou AI, this model can produce visually striking content with cinematic qualities, allowing users to create engaging videos quickly and efficiently.

## Setup your API Key

If you don’t have an API key for the AI/ML API yet, feel free to use our [Quickstart guide](https://docs.aimlapi.com/quickstart/setting-up).

## How to Make a Call

<details>

<summary>Step-by-Step Instructions</summary>

Generating a video using this model involves sequentially calling two endpoints:

* The first one is for creating and sending a video generation task to the server (returns a generation ID).
* The second one is for requesting the generated video from the server using the generation ID received from the first endpoint.

Below, you can find both corresponding API schemas.

</details>

## API Schemas

{% hint style="success" %}
Now, all of our API schemas for video models use our new universal short URL — `https://api.aimlapi.com/v2/video/generations`.\
However, you can still call this model using the legacy URL that includes the vendor name.
{% endhint %}

### Create a video generation task and send it to the server

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["video-01"]},"prompt":{"type":"string","maxLength":2000,"description":"The text description of the scene, subject, or action to generate in the video."},"image_url":{"type":"string","format":"uri","description":"A direct link to an online image or a Base64-encoded local image that will serve as the first frame for the video.\nImage specifications: \n- format must be JPG, JPEG, or PNG; \n- aspect ratio should be greater than 2:5 and less than 5:2; \n- the shorter side must exceed 300 pixels; \n- file size must not exceed 20MB."},"enhance_prompt":{"type":"boolean","default":true,"description":"If True, the incoming prompt will be automatically optimized to improve generation quality when needed. For more precise control, set it to False — the model will then follow the instructions more strictly."}},"required":["model","prompt"],"title":"video-01"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Retrieve the generated video from the server

After sending a request for video generation, this task is added to the queue. This endpoint lets you check the status of a video generation task using its `id`, obtained from the endpoint described above.\
If the video generation task status is `completed`, the response will include the final result — with the generated video URL and additional metadata.

## GET /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AI/ML Gateway","version":"1.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"get":{"operationId":"VideoControllerV2_pollVideo_v2","parameters":[{"name":"generation_id","required":true,"in":"query","schema":{"type":"string"}}],"responses":{"200":{"description":"Successfully generated video","content":{"application/json":{"schema":{"$ref":"#/components/schemas/Video.v2.PollVideoResponseDTO"}}}}},"tags":["Video Models"]}}},"components":{"schemas":{"Video.v2.PollVideoResponseDTO":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."},"duration":{"type":"number","nullable":true,"description":"The duration of the video."}},"required":["url"]},"duration":{"type":"number","nullable":true,"description":"The duration of the video."},"error":{"nullable":true,"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"tokens_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["tokens_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}
```
