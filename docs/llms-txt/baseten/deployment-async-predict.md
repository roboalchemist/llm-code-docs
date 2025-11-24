# Source: https://docs.baseten.co/reference/inference-api/predict-endpoints/deployment-async-predict.md

# Async deployment

> Use this endpoint to call any [published deployment](/deploy/lifecycle) of your model.

### Parameters

<ParamField path="model_id" type="string" required>
  The ID of the model you want to call.
</ParamField>

<ParamField path="deployment_id" type="string" required>
  The ID of the specific deployment you want to call.
</ParamField>

### Headers

<ParamField header="Authorization" type="string" required>
  Your Baseten API key, formatted with prefix `Api-Key` (e.g. `{"Authorization": "Api-Key abcd1234.abcd1234"}`).
</ParamField>

### Body

There is a 256 KiB size limit to `/async_predict` request payloads.

<ParamField body="model_input" type="json" required>
  JSON-serializable model input.
</ParamField>

<ParamField body="webhook_endpoint" type="string" default="null">
  <Note> Baseten **does not** store model outputs. If `webhook_endpoint` is empty, your model must save prediction outputs so they can be accessed later. </Note>

  URL of the webhook endpoint. We require that webhook endpoints use HTTPS. Both HTTP/2 and HTTP/1.1 protocols are supported.
</ParamField>

<ParamField body="priority" type="integer" default={0}>
  Priority of the request. A lower value corresponds to a higher priority (e.g. requests with priority 0 are scheduled before requests of priority 1).

  `priority` is between 0 and 2, inclusive.
</ParamField>

<ParamField body="max_time_in_queue_seconds" type="integer" default={600}>
  Maximum time a request will spend in the queue before expiring.

  `max_time_in_queue_seconds` must be between 10 seconds and 72 hours, inclusive.
</ParamField>

<ParamField body="inference_retry_config" type="json">
  Exponential backoff parameters used to retry the model predict request.

  <Expandable>
    <ParamField body="max_attempts" type="integer" default={3}>
      Number of predict request attempts.

      `max_attempts` must be between 1 and 10, inclusive.
    </ParamField>

    <ParamField body="initial_delay_ms" type="integer" default={1000}>
      Minimum time between retries in milliseconds.

      `initial_delay_ms` must be between 0 and 10,000 milliseconds, inclusive.
    </ParamField>

    <ParamField body="max_delay_ms" type="integer" default={5000}>
      Maximum time between retries in milliseconds.

      `max_delay_ms` must be between 0 and 60,000 milliseconds, inclusive.
    </ParamField>
  </Expandable>
</ParamField>

### Response

<ResponseField name="request_id" type="string" required>
  The ID of the async request.
</ResponseField>

### Rate limits

Two types of rate limits apply when making async requests:

* Calls to the `/async_predict` endpoint are limited to **200 requests per second**.

* Each organization is limited to **5,000 `QUEUED` or `IN_PROGRESS` async requests**, summed across all deployments.

If either limit is exceeded, subsequent `/async_predict` requests will receive a 429 status code.

To avoid hitting these rate limits, we advise:

* Implementing a backpressure mechanism, such as calling `/async_predict` with exponential backoff in response to 429 errors.
* Monitoring the [async queue size metric](/observability/metrics#async-queue-metrics). If your model is accumulating a backlog of requests, consider increasing the number of requests your model can process at once by increasing the number of max replicas or the concurrency target in your autoscaling settings.

<RequestExample>
  ```py Python theme={"system"}
  import requests
  import os

  model_id = ""
  deployment_id = ""
  webhook_endpoint = ""

  # Read secrets from environment variables

  baseten_api_key = os.environ["BASETEN_API_KEY"]

  resp = requests.post(
  f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict",
  headers={"Authorization": f"Api-Key {baseten_api_key}"},
  json={
  "model_input": {"prompt": "hello world!"},
  "webhook_endpoint": webhook_endpoint # Optional fields for priority, max_time_in_queue_seconds, etc
  },
  )

  print(resp.json())

  ```

  ```sh cURL theme={"system"}
  curl --request POST \
    --url https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict \
    --header "Authorization: Api-Key $BASETEN_API_KEY" \
    --data '{
    "model_input": {"prompt": "hello world!"},
    "webhook_endpoint": "https://my_webhook.com/webhook",
    "priority": 1,
    "max_time_in_queue_seconds": 100,
    "inference_retry_config": {
      "max_attempts": 3,
      "initial_delay_ms": 1000,
      "max_delay_ms": 5000
    }
  }'
  ```

  ```js Node.js theme={"system"}
  const fetch = require("node-fetch");

  const resp = await fetch(
    "https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict",
    {
      method: "POST",
      headers: { Authorization: "Api-Key YOUR_API_KEY" },
      body: JSON.stringify({
        model_input: { prompt: "hello world!" },
        webhook_endpoint: "https://my_webhook.com/webhook",
        priority: 1,
        max_time_in_queue_seconds: 100,
        inference_retry_config: {
          max_attempts: 3,
          initial_delay_ms: 1000,
          max_delay_ms: 5000,
        },
      }),
    }
  );

  const data = await resp.json();

  console.log(data);
  ```
</RequestExample>

<ResponseExample>
  ```json 201 theme={"system"}
  {
    "request_id": "<string>"
  }
  ```
</ResponseExample>
