# Source: https://docs.aimlapi.com/api-references/video-models/kling-ai/v1-standard-text-to-video.md

# v1-standard/text-to-video

{% columns %}
{% column width="66.66666666666666%" %}
{% hint style="info" %}
This documentation is valid for the following list of our models:

* `kling-video/v1/standard/text-to-video`
  {% endhint %}
  {% endcolumn %}

{% column width="33.33333333333334%" %} <a href="https://aimlapi.com/app/kling-video/v1/standard/text-to-video" class="button primary">Try in Playground</a>
{% endcolumn %}
{% endcolumns %}

This model converts textual descriptions into high-quality video content.

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
Now, all of our API schemas for video models use our new universal short URL — `https://api.aimlapi.com/v2/video/generations`. \
However, you can still call this model using the legacy URL that includes the vendor name.
{% endhint %}

### Create a video generation task and send it to the server

## POST /v2/video/generations

>

```json
{"openapi":"3.0.0","info":{"title":"AIML API","version":"1.0.0"},"servers":[{"url":"https://api.aimlapi.com"}],"paths":{"/v2/video/generations":{"post":{"operationId":"_v2_video_generations","requestBody":{"required":true,"content":{"application/json":{"schema":{"type":"object","properties":{"model":{"type":"string","enum":["kling-video/v1/standard/text-to-video"]},"prompt":{"type":"string","description":"The text description of the scene, subject, or action to generate in the video."},"aspect_ratio":{"type":"string","enum":["16:9","9:16","1:1"],"default":"16:9","description":"The aspect ratio of the generated video."},"duration":{"type":"integer","description":"The length of the output video in seconds.","enum":[5,10]},"negative_prompt":{"type":"string","description":"The description of elements to avoid in the generated video."},"cfg_scale":{"type":"number","minimum":0,"maximum":1,"description":"The CFG (Classifier Free Guidance) scale is a measure of how close you want the model to stick to your prompt."},"camera_control":{"type":"string","enum":["down_back","forward_up","right_turn_forward","left_turn_forward"],"description":"Camera control parameters."},"advanced_camera_control":{"type":"object","properties":{"movement_type":{"type":"string","enum":["horizontal","vertical","pan","tilt","roll","zoom"],"description":"The type of camera movement."},"movement_value":{"type":"integer","minimum":-10,"maximum":10,"description":"The value of the camera movement."}},"required":["movement_type","movement_value"],"description":"Advanced camera control parameters."}},"required":["model","prompt"],"title":"kling-video/v1/standard/text-to-video"}}}},"responses":{"200":{"content":{"application/json":{"schema":{"type":"object","properties":{"id":{"type":"string","description":"The ID of the generated video."},"status":{"type":"string","enum":["queued","generating","completed","error"],"description":"The current status of the generation task."},"video":{"type":"object","nullable":true,"properties":{"url":{"type":"string","format":"uri","description":"The URL where the file can be downloaded from."}},"required":["url"]},"error":{"type":"object","nullable":true,"properties":{"name":{"type":"string"},"message":{"type":"string"}},"required":["name","message"],"description":"Description of the error, if any."},"meta":{"type":"object","nullable":true,"properties":{"usage":{"type":"object","nullable":true,"properties":{"credits_used":{"type":"number","description":"The number of tokens consumed during generation."}},"required":["credits_used"]}},"description":"Additional details about the generation."}},"required":["id","status"]}}}}}}}}}
```

### Retrieve the generated video from the server

After sending a request for video generation, this task is added to the queue. Based on the service's load, the generation can be completed in seconds or take a bit more.

{% openapi src="<https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-6b5ccfe59555f1a8ec3892b3c05134ce122bf1a6%2Fv1.6-pro-effects-pair.json?alt=media>" path="/v2/generate/video/kling/generation" method="get" %}
[v1.6-pro-effects-pair.json](https://3927338786-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FROMd1X5PuqtikJ48n2N9%2Fuploads%2Fgit-blob-6b5ccfe59555f1a8ec3892b3c05134ce122bf1a6%2Fv1.6-pro-effects-pair.json?alt=media)
{% endopenapi %}
