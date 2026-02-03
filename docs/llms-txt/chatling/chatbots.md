# Source: https://docs.chatling.ai/api-reference/v2/usage/chatbots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chatbots

> Get the chatbots usage for the project.

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseField name="data" type="object">
  <Expandable title="properties">
    <ResponseField name="used" type="integer">
      The number of chatbots created.
    </ResponseField>

    <ResponseField name="max" type="integer">
      The maximum number of chatbots allowed for the project.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success",
      "data": {
          "used": 2,
          "max": 5
      }
  }
  ```
</ResponseExample>
