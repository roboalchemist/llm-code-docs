# Source: https://docs.chatling.ai/api-reference/v2/knowledge-base/resync-source.md

# Resync data source

> Resync a data source.

**The following limitations apply:**

* The supported sources are links and Zoho articles.
* You can have up to 50 data sources queued for resync. If you exceed this limit, you will receive an error and must wait until some of the queued resyncs are complete.
* You can only resync data sources that are in the `processed` state.

## Request parameters

### Path

<ParamField path="chatbotId" type="string" required>
  The chatbot ID.
</ParamField>

<ParamField path="dataSourceId" type="string" required>
  The data source ID.
</ParamField>

## Response

<ResponseField name="status" type="string">
  The status of the request. Will be `success` if the request was successful, otherwise `error`.
</ResponseField>

<ResponseExample>
  ```json Response theme={null}
  {
      "status": "success"
  }
  ```
</ResponseExample>
