# Source: https://novita.ai/docs/api-reference/model-apis-txt2speech.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Text to Speech

**This Text-To-Speech API converts written text into natural-sounding speech across multiple languages. Utilizing advanced voice synthesis technology, it delivers clear and lifelike vocal output, suitable for a wide range of applications, including e-learning platforms, accessibility tools, virtual assistants, and multimedia presentations.**

> This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the speech generation results.

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
    <ParamField body="response_audio_type" type="string" required={false}>
      The returned audio type. Default is wav.<br />
      Enum: `wav`, `mp3`
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
              Control the data content of the mock event. When set to TASK\_STATUS\_SUCCEED, you'll receive a normal response; when set to TASK\_STATUS\_FAILED, you'll receive an error response.<br />
              Enum: `TASK_STATUS_SUCCEED`, `TASK_STATUS_FAILED`
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

<ParamField body="request" type="object" required={true}>
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="voice_id" type="string" required={true}>
      Voice ID<br />
      Enum: `Emily`, `James`, `Olivia`, `Michael`, `Sarah`, `John`
    </ParamField>

    <ParamField body="language" type="string" required={true}>
      Identify the languages spoken in the generated audio<br />
      Enum: `en-US`, `zh-CN`, `ja-JP`
    </ParamField>

    <ParamField body="texts" type="string[]" required={true}>
      Source text for synthetic speech, UTF-8 encoded, supporting a maximum of 512 characters.
    </ParamField>

    <ParamField body="volume" type="number" required={false}>
      Control the volume of the generated audio; select a value between 1.0 and 2.0. The default value is 1.0.
    </ParamField>

    <ParamField body="speed" type="number" required={false}>
      Control the speed of the generated audio; select a value between 0.8 and 3.0. The default value is 1.0.
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>

## Example

request

```bash  theme={"system"}
curl --location 'https://api.novita.ai/v3/async/txt2speech' \
--header 'Authorization: Bearer {{API Key}}' \
--header 'Content-Type: application/json' \
--data '{
  "request": {
    "voice_id": "Emily",
    "language": "en-US",
    "texts": [
      "To be or not to be, that is a question."
    ],
    "volume": 1.2,
    "speed": 1.0
  }
}'
```

response

```json  theme={"system"}
{
  "task_id": "b49df8dc-4a72-474b-a863-xxx"
}
```


Built with [Mintlify](https://mintlify.com).