# Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/cancel-async-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Async cancel request

> Use this endpoint to cancel a queued async request.

Only `QUEUED` requests may be canceled.

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

<ResponseField name="request_id" type="string" required>
  The ID of the async request.
</ResponseField>

<ResponseField name="canceled" type="boolean" required>
  Whether the request was canceled.
</ResponseField>

<ResponseField name="message" type="string" required>
  Additional details about whether the request was canceled.
</ResponseField>

### Rate limits

Calls to the cancel async request status endpoint are limited to **20 requests per second**. If this limit is exceeded, subsequent requests will receive a 429 status code.

<RequestExample>
  ```python Python (Model) theme={"system"}
  import requests
  import os

  model_id = ""
  request_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.delete(
  f"https://model-{model_id}.api.baseten.co/async_request/{request_id}",
  headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```

  ```python Python (Chain) theme={"system"}
  import requests
  import os

  chain_id = ""
  request_id = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.delete(
  f"https://chain-{chain_id}.api.baseten.co/async_request/{request_id}",
  headers={"Authorization": f"Api-Key {baseten_api_key}"}
  )

  print(resp.json())
  ```
</RequestExample>
