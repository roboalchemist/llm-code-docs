# Source: https://novita.ai/docs/api-reference/model-apis-img2video.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Image to Video

**This API seamlessly transforms an image into a cohesive video. It is designed to create smooth transitions and animations from static images, making it ideal for producing dynamic visual content for presentations, social media, and marketing campaigns.**

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
      The returned video type. Default is mp4.Enum: `mp4, gif`
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
              Control the data content of the mock event. When set to TASK\_STATUS\_SUCCEED, you'll receive a normal response; when set to TASK\_STATUS\_FAILED, you'll receive an error response.Enum: `TASK_STATUS_SUCCEED, TASK_STATUS_FAILED`
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
  Specifies the model to be used for processing. SVD (Singular Value Decomposition): Ideal for applications involving matrix factorization and dimensionality reduction. This model is well-suited for tasks such as signal processing, recommendation systems, and data compression, offering robust feature extraction and data simplification capabilities. SVD-XT: This model is an extended version of the standard SVD, optimized for handling larger datasets and more complex computations. It provides enhanced performance and accuracy in environments requiring intensive data processing.Enum: `SVD-XT, SVD`
</ParamField>

<ParamField body="image_file" type="string" required={true}>
  The base64 of input image, with a maximum resolution of 2048 x 2048 and a maximum file size of 30 Mb.
</ParamField>

<ParamField body="frames_num" type="integer" required={true}>
  Total number of video frames. When the parameter model\_name=SVD\_XT, then frames\_num = 25; when the parameter model\_name=SVD, then frames\_num = 14.
</ParamField>

<ParamField body="frames_per_second" type="integer" required={true}>
  Frames per second; the larger the frame rate, the smoother the video. Currently, only the number 6 is supported.
</ParamField>

<ParamField body="image_file_resize_mode" type="string" required={true}>
  The image file resize mode has two settings: When set to ORIGINAL\_RESOLUTION, it retains the original image size but ensures the resolution is below 576 x 1024. When set to CROP\_TO\_ASPECT\_RATIO, it maintains the original proportions of the image and crops it to fit within a 576 x 1024 resolution.Enum: `ORIGINAL_RESOLUTION, CROP_TO_ASPECT_RATIO`
</ParamField>

<ParamField body="steps" type="integer" required={true}>
  The number of denoising steps. More steps usually produce higher quality content, but take more time to generate. Range \[1, 50].
</ParamField>

<ParamField body="seed" type="integer" required={false}>
  A seed is a number from which Stable Diffusion generates noise, which, makes generation deterministic. Using the same seed and set of parameters will produce identical content each time, minimum -1. Defaults to -1.
</ParamField>

<ParamField body="motion_bucket_id" type="integer" required={false}>
  Identifies the specific motion bucket to be utilized during the img2video process. This parameter selects a predefined set of motion profiles, each corresponding to a unique identifier ranging from 1 to 255. Selecting an appropriate motion bucket can tailor the animation effects to better suit the specific characteristics or themes of the input images. Range \[1, 255].
</ParamField>

<ParamField body="cond_aug" type="number" required={false}>
  The amount of noise added to the conditioning image. The higher the value, the less the video resembles the conditioning image. Increasing this value also enhances the motion in the generated video. Range \[0, 1].
</ParamField>

<ParamField body="enable_frame_interpolation" type="boolean" required={false}>
  Enables frame interpolation to standardize video output to 24 frames per second (fps). This feature smooths out motion by generating intermediate frames, enhancing the fluidity and continuity of the video sequence. This is particularly useful for converting lower frame rate footage to a more cinematic frame rate.
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

This API helps generate a video from an image. The returned video can be accessed via the API `/v3/async/task-result` using the `task_id`.

**Try it in [playground](https://novita.ai/playground#img2video).**

`Request:`

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/async/img2video' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "model_name": "SVD-XT",
    "image_file": "{{Base64 encoded image}}",
    "frames_num": 25,
    "frames_per_second": 6,
    "seed": 20231127,
    "image_file_resize_mode": "CROP_TO_ASPECT_RATIO",
    "steps": 20
}'
```

`Response:`

```js  theme={"system"}
{
    "task_id": "fa20dff3-18cb-4417-a7f8-269456a35154"
}
```

**Use `task_id` to get videos**

HTTP status codes in the 2xx range indicate that the request has been successfully accepted, while status codes in the 5xx range indicate internal server errors.

You can get the video URLs from the `videos` field in the response.

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
        "task_type": "IMG_TO_VIDEO",
        "status": "TASK_STATUS_SUCCEED",
        "reason": ""
    },
    "images": [],
    "videos": [
        {
            "video_url": "https://faas-output-video.s3.ap-southeast-1.amazonaws.com/test/fa20dff3-18cb-4417-a7f8-269456a35154/e40de30e115947a0be2dfc78925e587d.mp4?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIASVPYCN6LRCW3SOUV%2F20231127%2Fap-southeast-1%2Fs3%2Faws4_request&X-Amz-Date=20231127T151757Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&x-id=GetObject&X-Amz-Signature=14faf7df34c2c2ff68fed102095af593844db7c5c5cd2d80e80beec0613192c7",
            "video_url_ttl": "3600",
            "video_type": "mp4"
        }
    ]
}
```


Built with [Mintlify](https://mintlify.com).