# Source: https://docs.baseten.co/reference/inference-api/status-endpoints/get-async-request-status.md

# Async request

> Use this endpoint to get the status of an async request.

### Parameters

<Tabs>
  <Tab title="Model">
    <ParamField path="model_id" type="string" required>
      The ID of the model.
    </ParamField>
  </Tab>

  <Tab title="Chain">
    <ParamField path="chain_id" type="string" required>
      The ID of the chain.
    </ParamField>
  </Tab>
</Tabs>

<ParamField path="request_id" type="string" required>
  The ID of the async request.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<Tabs>
  <Tab title="Model">
    <ResponseField name="request_id" type="string" required>
      The ID of the async request.
    </ResponseField>

    <ResponseField name="model_id" type="string" required>
      The ID of the model that executed the request.
    </ResponseField>

    <ResponseField name="deployment_id" type="string" required>
      The ID of the deployment that executed the request.
    </ResponseField>

    <ResponseField name="status" type="string" required>
      An enum representing the status of the request.

      Available options: `QUEUED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `EXPIRED`, `CANCELED`, `WEBHOOK_FAILED`
    </ResponseField>

    <ResponseField name="webhook_status" type="string" required>
      An enum representing the status of sending the predict result to the provided webhook.

      Available options: `PENDING`, `SUCCEEDED`, `FAILED`, `CANCELED`, `NO_WEBHOOK_PROVIDED`
    </ResponseField>

    <ResponseField name="created_at" type="string" required>
      The time in UTC at which the async request was created.
    </ResponseField>

    <ResponseField name="status_at" type="string" required>
      The time in UTC at which the async request's status was updated.
    </ResponseField>

    <ResponseField name="errors" type="object[]" required default={[]}>
      Any errors that occurred in processing the async request. Empty if no errors occurred.

      <Expandable>
        <ResponseField name="code" type="string" required>
          An enum representing the type of error that occurred.

          Available options: `MODEL_PREDICT_ERROR`, `MODEL_PREDICT_TIMEOUT`, `MODEL_NOT_READY`, `MODEL_DOES_NOT_EXIST`, `MODEL_UNAVAILABLE`, `MODEL_INVALID_INPUT`, `ASYNC_REQUEST_NOT_SUPPORTED`, `INTERNAL_SERVER_ERROR`
        </ResponseField>

        <ResponseField name="message" type="string" required>
          A message containing details of the error that occurred.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>

  <Tab title="Chain">
    <ResponseField name="request_id" type="string" required>
      The ID of the async request.
    </ResponseField>

    <ResponseField name="chain_id" type="string" required>
      The ID of the chain that executed the request.
    </ResponseField>

    <ResponseField name="deployment_id" type="string" required>
      The ID of the deployment that executed the request.
    </ResponseField>

    <ResponseField name="status" type="string" required>
      An enum representing the status of the request.

      Available options: `QUEUED`, `IN_PROGRESS`, `SUCCEEDED`, `FAILED`, `EXPIRED`, `CANCELED`, `WEBHOOK_FAILED`
    </ResponseField>

    <ResponseField name="webhook_status" type="string" required>
      An enum representing the status of sending the predict result to the provided webhook.

      Available options: `PENDING`, `SUCCEEDED`, `FAILED`, `CANCELED`, `NO_WEBHOOK_PROVIDED`
    </ResponseField>

    <ResponseField name="created_at" type="string" required>
      The time in UTC at which the async request was created.
    </ResponseField>

    <ResponseField name="status_at" type="string" required>
      The time in UTC at which the async request's status was updated.
    </ResponseField>

    <ResponseField name="errors" type="object[]" required default={[]}>
      Any errors that occurred in processing the async request. Empty if no errors occurred.

      <Expandable>
        <ResponseField name="code" type="string" required>
          An enum representing the type of error that occurred.

          Available options: `MODEL_PREDICT_ERROR`, `MODEL_PREDICT_TIMEOUT`, `MODEL_NOT_READY`, `MODEL_DOES_NOT_EXIST`, `MODEL_UNAVAILABLE`, `MODEL_INVALID_INPUT`, `ASYNC_REQUEST_NOT_SUPPORTED`, `INTERNAL_SERVER_ERROR`
        </ResponseField>

        <ResponseField name="message" type="string" required>
          A message containing details of the error that occurred.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Tab>
</Tabs>

<ResponseExample>
  ```json 200 (Model) theme={"system"}
  {
    "request_id": "<string>",
    "model_id": "<string>",
    "deployment_id": "<string>",
    "status": "<string>",
    "webhook_status": "<string>",
    "created_at": "<string>",
    "status_at": "<string>",
    "errors": [
      {
        "code": "<string>",
        "message": "<string>"
      }
    ]
  }
  ```

  ```json 200 (Chain) theme={"system"}
  {
    "request_id": "<string>",
    "chain_id": "<string>",
    "deployment_id": "<string>",
    "status": "<string>",
    "webhook_status": "<string>",
    "created_at": "<string>",
    "status_at": "<string>",
    "errors": [
      {
        "code": "<string>",
        "message": "<string>"
      }
    ]
  }
  ```
</ResponseExample>

### Rate limits

Calls to the get async request status endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To avoid hitting this rate limit, we recommend [configuring a webhook endpoint](/inference/async#configuring-the-webhook-endpoint) to receive async predict results instead of frequently polling this endpoint for async request statuses.

<RequestExample>
  ```py Python (Model) theme={"system"}
  import requests
  import os

  model_id = ""
  request_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Python (Chain) theme={"system"}
  import requests
  import os

  chain_id = ""
  request_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/async_request/{request_id}",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>
