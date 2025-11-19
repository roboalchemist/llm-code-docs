# Source: https://docs.baseten.co/reference/inference-api/status-endpoints/deployment-get-async-queue-status.md

# Async deployment

> Use this endpoint to get the status of a published deployment's async queue.

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

<ParamField path="deployment_id" type="string" required>
  The ID of the deployment.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Response

<ResponseField name="model_id" type="string" required>
  The ID of the model.
</ResponseField>

<ResponseField name="deployment_id" type="string" required>
  The ID of the deployment.
</ResponseField>

<ResponseField name="num_queued_requests" type="integer" required>
  The number of requests in the deployment's async queue with `QUEUED` status (i.e. awaiting processing by the model).
</ResponseField>

<ResponseField name="num_in_progress_requests" type="integer" required>
  The number of requests in the deployment's async queue with `IN_PROGRESS` status (i.e. currently being processed by the model).
</ResponseField>

<ResponseExample>
  ```json 200 theme={"system"}
  {
    "model_id": "<string>",
    "deployment_id": "<string>",
    "num_queued_requests": 12,
    "num_in_progress_requests": 3
  }
  ```
</ResponseExample>

### Rate limits

Calls to the `/async_queue_status` endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

To gracefully handle hitting this rate limit, we advise implementing a backpressure mechanism, such as calling `/async_queue_status` with exponential backoff in response to 429 errors.

<RequestExample>
  ```py Model theme={"system"}
  import requests
  import os

  model_id = ""
  deployment_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```py Chain theme={"system"}
  import requests
  import os

  chain_id = ""
  deployment_id = ""
  # Read secrets from environment variables
  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.get(
      f"https://chain-{chain_id}.api.baseten.co/deployment/{deployment_id}/async_queue_status",
      headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>
