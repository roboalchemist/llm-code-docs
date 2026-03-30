# Source: https://novita.ai/docs/api-reference/model-apis-video-merge-face.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Video Merge Face

**This API endpoint seamlessly integrates a face image into a target video, allowing you to replace the face in the video with the face from the image.**

> **Pricing:** \$0.0005 / Video Frame

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
  </Expandable>
</ParamField>

<ParamField body="request" type="object" required={true}>
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="video_assets_id" type="string" required={true}>
      Upload your input video to our temporary secure storage following the instructions in the guide <a href="#_1-get-video-assets-id">Get video assets id</a>, and the video\_assets\_id is the identifier for your input video. Supported video formats: MP4, with a maximum resolution of 3840 x 2160 and a maximum file size of 100 Mb.
    </ParamField>

    <ParamField body="enable_restore" type="boolean" required={true}>
      Whether to restore the output face image. If enabled, the output face video will be more detailed, but the API latency will be longer.
    </ParamField>

    <ParamField body="face_image_base64" type="string" required={true}>
      The base64-encoded face image, with a maximum resolution of 2048 x 2048 and a maximum file size of 30 MB.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

### 1. Get Video Assets ID

`Request:`

```bash  theme={"system"}
curl -X PUT -T "{{video file path}}" 'https://assets.novitai.com/video'
```

`Response:`

```js  theme={"system"}
{
    "assets_id": "cjIvbm92aXRhLWFpLWFzc2V0L3ZpZGVvL0NLd0N3aHJwS0ZyYVduNWVoejVFV0tleGlzN0toNmRq"
}
```


Built with [Mintlify](https://mintlify.com).