# Source: https://novita.ai/docs/api-reference/model-apis-progress-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Progress

## GET Progress

This API provides a query for the result of image generation, which can be in progress, failed, or successful. If successful, it will return the S3 URL of the generated image.

## Request Headers

<ParamField header="Authorization" type="string" required={true} />

## Query Parameters

<ParamField query="task_id" type="arraystring[]" required={true}>
  The ID of the task being queried.
</ParamField>

## Response

<ResponseField name="code" type="integer" required={false}>
  CodeNormal=0, CodeInternalError=-1, CodeInvalidJSON=1, CodeModelNotExist=2, CodeTaskIdNotExist=3, CodeInvalidAuth=4, CodeHostUnavailable=5, CodeParamRangeOutOfLimit=6, CodeCostBalanceFailure=7, CodeSamplerNotExist=8, CodeTimeout=9, CodeNotSupport=10
</ResponseField>

<ResponseField name="msg" type="string" required={false} />

<ResponseField name="data" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="status" type="integer" required={false} />

    <ResponseField name="progress" type="number" required={false} />

    <ResponseField name="eta_relative" type="number" required={false} />

    <ResponseField name="imgs" type="string[]¦null" required={false} />

    <ResponseField name="failed_reason" type="string" required={false} />

    <ResponseField name="current_images" type="string[]" required={false} />

    <ResponseField name="submit_time" type="string" required={false} />

    <ResponseField name="execution_time" type="string" required={false} />

    <ResponseField name="txt2img_time" type="string" required={false} />

    <ResponseField name="finish_time" type="string" required={false} />

    <ResponseField name="info" type="string" required={false} />

    <ResponseField name="enable_nsfw_detection" type="boolean" required={false} />

    <ResponseField name="nsfw_detection_result" type="object[]" required={false}>
      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="valid" type="boolean" required={false} />

        <ResponseField name="confidence" type="number" required={false} />
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

## Example

request

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v2/progress?task_id=' \
--header 'Authorization: Bearer {{API Key}}'
```

response

```json  theme={"system"}
{
  "code": 0,
  "msg": "",
  "data": {
    "status": 2,
    "progress": 1,
    "eta_relative": 0,
    "imgs": [
      "https://stars-test.s3.amazonaws.com/free/859d452b-f682-45fc-b0e7-5bd7b61a107d-0.png",
      "https://stars-test.s3.amazonaws.com/free/859d452b-f682-45fc-b0e7-5bd7b61a107d-1.png",
      "https://stars-test.s3.amazonaws.com/free/859d452b-f682-45fc-b0e7-5bd7b61a107d-2.png",
      "https://stars-test.s3.amazonaws.com/free/859d452b-f682-45fc-b0e7-5bd7b61a107d-3.png"
    ],
    "failed_reason": "",
    "current_images": [""],
    "submit_time": "2024-01-24 15:08:17",
    "execution_time": "2024-01-24 15:08:17",
    "txt2img_time": "2024-01-24 15:08:22",
    "finish_time": "2024-01-24 15:08:22",
    "info": "",
    "enable_nsfw_detection": true,
    "nsfw_detection_result": [
      {
        "valid": true,
        "confidence": 57.62467
      },
      {
        "valid": true,
        "confidence": 3.908125
      },
      {
        "valid": true,
        "confidence": 99.84468
      },
      {
        "valid": true,
        "confidence": 2.440833
      }
    ],
    "debug_info": {
      "submit_time_ms": 1706080097101,
      "execution_time_ms": 1706080097369,
      "txt2img_time_ms": 1706080102333,
      "finish_time_ms": 1706080102479
    }
  }
}
```


Built with [Mintlify](https://mintlify.com).