# Source: https://docs.baseten.co/inference/async.md

# Async inference

> Run asynchronous inference on deployed models

Async requests are a "fire and forget" way of executing model inference requests. Instead of waiting for a response from a model, making an async request queues the request, and immediately returns with a request identifier. Optionally, async request results are sent via a `POST` request to a user-defined webhook upon completion.

Use async requests for:

* Long-running inference tasks that may otherwise hit request timeouts.
* Batched inference jobs.
* Prioritizing certain inference requests.

<Note>
  Async fast facts:

  * Async requests can be made to any model—**no model code changes necessary**.
  * Async requests can remain queued for up to 72 hours and run for up to 1 hour.
  * Async requests are **not** compatible with streaming model output.
  * Async request inputs and model outputs are **not** stored after an async request has been completed. Instead, model outputs will be sent to your webhook via a `POST` request.
</Note>

## Quick start

There are two ways to use async inference:

1. Provide a webhook endpoint where model outputs will be sent via a `POST` request. If providing a webhook, you can **use async inference on any model, without making any changes to your model code**.
2. Inside your Truss' `model.py`, save prediction results to cloud storage. If a webhook endpoint is provided, your model outputs will also be sent to your webhook.

Note that Baseten **does not** store model outputs. If you do not wish to use a webhook, your `model.py` must write model outputs to a cloud storage bucket or database as part of its implementation.

<Tabs>
  <Tab title="Quick start with webhook">
    <Steps>
      <Step title="Setup webhook endpoint">
        Set up a webhook endpoint for handling completed async requests. Since Baseten doesn't store model outputs, model outputs from async requests will be sent to your webhook endpoint.

        Before creating your first async request, try running a sample request against your webhook endpoint to ensure that it can consume async predict results properly. Check out [this example webhook test](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code#test_webhook.py).

        We recommend using [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code) as a starting point.

        <iframe src="https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code?embed=true" width="100%" height="400" />
      </Step>

      <Step title="Schedule an async predict request">
        Call `/async_predict` on your model. The body of an `/async_predict` request includes the model input in `model_input` field, with the addition of a webhook endpoint (from the previous step) in the `webhook_endpoint` field.

        {" "}

        ```py Python theme={"system"}
        import requests
        import os

        model_id = ""  # Replace this with your model ID
        webhook_endpoint = ""  # Replace this with your webhook endpoint URL
        # Read secrets from environment variables
        baseten_api_key = os.environ["BASETEN_API_KEY"]

        # Call the async_predict endpoint of the production deployment
        resp = requests.post(
            f"https://model-{model_id}.api.baseten.co/production/async_predict",
            headers={"Authorization": f"Api-Key {baseten_api_key}"},
            json={
                "model_input": {"prompt": "hello world!"},
                "webhook_endpoint": webhook_endpoint
                # Optional fields for priority, max_time_in_queue_seconds, etc
            },
        )

        print(resp.json())
        ```

        Save the `request_id` from the `/async_predict` response to check its status or cancel it.

        ```json 201 theme={"system"}
        {
          "request_id": "9876543210abcdef1234567890fedcba"
        }
        ```

        See the [async inference API reference](/reference/inference-api/predict-endpoints/environments-async-predict) for more endpoint details.
      </Step>

      <Step title="Check async predict results">
        Using the `request_id` saved from the previous step, check the status of your async predict request:

        {" "}

        ```py Python theme={"system"}
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

        Once your model has finished executing the request, the async predict result will be sent to your webhook in a `POST` request.

        ```json  theme={"system"}
        {
          "request_id": "9876543210abcdef1234567890fedcba",
          "model_id": "my_model_id",
          "deployment_id": "my_deployment_id",
          "type": "async_request_completed",
          "time": "2024-04-30T01:01:08.883423Z",
          "data": {
            "my_model_output": "hello world!"
          },
          "errors": []
        }
        ```
      </Step>

      <Step title="Secure your webhook">
        We strongly recommend securing the requests sent to your webhooks to validate that they are from Baseten.

        For instructions, see our [guide to securing async requests](/inference/async#securing-async-inference).
      </Step>
    </Steps>
  </Tab>

  <Tab title="Quick start with saving model outputs">
    <Steps>
      <Step title="Update your model to save prediction results">
        Update your Truss's `model.py` to save prediction results to cloud storage, such as S3 or GCS. We recommend implementing this in your model's `postprocess()` method, which will run on CPU after the prediction has completed.
      </Step>

      <Step title="Setup webhook endpoint">
        Optionally, set up a webhook endpoint so Baseten can notify you when your async request completes.

        Before creating your first async request, try running a sample request against your webhook endpoint to ensure that it can consume async predict results properly. Check out [this example webhook test](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code#test_webhook.py).

        We recommend using [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code) as a starting point.

        <iframe src="https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code?embed=true" width="100%" height="400" />
      </Step>

      <Step title="Schedule an async predict request">
        Call `/async_predict` on your model. The body of an `/async_predict` request includes the model input in `model_input` field, with the addition of a webhook endpoint (from the previous step) in the `webhook_endpoint` field.

        {" "}

        ```py Python theme={"system"}
        import requests
        import os

        model_id = ""  # Replace this with your model ID
        webhook_endpoint = ""  # Replace this with your webhook endpoint URL
        # Read secrets from environment variables
        baseten_api_key = os.environ["BASETEN_API_KEY"]

        # Call the async_predict endpoint of the production deployment
        resp = requests.post(
            f"https://model-{model_id}.api.baseten.co/production/async_predict",
            headers={"Authorization": f"Api-Key {baseten_api_key}"},
            json={
                "model_input": {"prompt": "hello world!"},
                "webhook_endpoint": webhook_endpoint
                # Optional fields for priority, max_time_in_queue_seconds, etc
            },
        )

        print(resp.json())
        ```

        Save the `request_id` from the `/async_predict` response to check its status or cancel it.

        ```json 201 theme={"system"}
        {
          "request_id": "9876543210abcdef1234567890fedcba"
        }
        ```

        See the [async inference API reference](/reference/inference-api/predict-endpoints/environments-async-predict) for more endpoint details.
      </Step>

      <Step title="Check async predict results">
        Using the `request_id` saved from the previous step, check the status of your async predict request:

        {" "}

        ```py Python theme={"system"}
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

        Once your model has finished executing the request, the async predict result will be sent to your webhook in a `POST` request.

        ```json  theme={"system"}
        {
          "request_id": "9876543210abcdef1234567890fedcba",
          "model_id": "my_model_id",
          "deployment_id": "my_deployment_id",
          "type": "async_request_completed",
          "time": "2024-04-30T01:01:08.883423Z",
          "data": {
            "my_model_output": "hello world!"
          },
          "errors": []
        }
        ```
      </Step>

      <Step title="Secure your webhook">
        We strongly recommend securing the requests sent to your webhooks to validate that they are from Baseten.

        For instructions, see our [guide to securing async requests](/inference/async#securing-async-inference).
      </Step>
    </Steps>
  </Tab>
</Tabs>

<Tip>
  **Chains**: this guide is written for Truss models, but
  [Chains](/development/chain/overview) support async inference likewise. An
  Chain entrypoint can be invoked via its `async_run_remote` endpoint, e.g.
  `https://chain-{chain_id}.api.baseten.co/production/async_run_remote`. The
  internal Chainlet-Chainlet call will still run synchronously.
</Tip>

## User guide

### Configuring the webhook endpoint

Configure your webhook endpoint to handle `POST` requests with [async predict results](/inference/async#processing-async-predict-results). We require that webhook endpoints use HTTPS.

We recommend running a sample request against your webhook endpoint to ensure that it can consume async predict results properly. Try running [this webhook test](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code#test_webhook.py).

For local development, we recommend using [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code) as a starting point. This code validates the webhook request and logs the payload.

<iframe src="https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code?embed=true" width="100%" height="400" />

### Making async requests

<Tabs>
  <Tab title="Production deployment">
    ```py Python theme={"system"}
    import requests
    import os

    model_id = ""  # Replace this with your model ID
    webhook_endpoint = ""  # Replace this with your webhook endpoint URL
    # Read secrets from environment variables
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    # Call the async_predict endpoint of the production deployment
    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/production/async_predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model_input": {"prompt": "hello world!"},
            "webhook_endpoint": webhook_endpoint
            # Optional fields for priority, max_time_in_queue_seconds, etc
        },
    )

    print(resp.json())
    ```
  </Tab>

  <Tab title="Development deployment">
    ```py Python theme={"system"}
    import requests
    import os

    model_id = ""  # Replace this with your model ID
    webhook_endpoint = ""  # Replace this with your webhook endpoint URL
    # Read secrets from environment variables
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    # Call the async_predict endpoint of the development deployment
    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/development/async_predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model_input": {"prompt": "hello world!"},
            "webhook_endpoint": webhook_endpoint
            # Optional fields for priority, max_time_in_queue_seconds, etc
        },
    )

    print(resp.json())
    ```
  </Tab>

  <Tab title="Other published deployments">
    ```py Python theme={"system"}
    import requests
    import os

    model_id = ""  # Replace this with your model ID
    deployment_id = "" # Replace this with your deployment ID
    webhook_endpoint = ""  # Replace this with your webhook endpoint URL
    # Read secrets from environment variables
    baseten_api_key = os.environ["BASETEN_API_KEY"]

    # Call the async_predict endpoint of the given deployment
    resp = requests.post(
        f"https://model-{model_id}.api.baseten.co/deployment/{deployment_id}/async_predict",
        headers={"Authorization": f"Api-Key {baseten_api_key}"},
        json={
            "model_input": {"prompt": "hello world!"},
            "webhook_endpoint": webhook_endpoint
            # Optional fields for priority, max_time_in_queue_seconds, etc
        },
    )

    print(resp.json())
    ```
  </Tab>
</Tabs>

Create an async request by calling a model's `/async_predict` endpoint. See the [async inference API reference](/reference/inference-api/predict-endpoints/environments-async-predict) for more endpoint details.

### Getting and canceling async requests

<Tabs>
  <Tab title="Get async request details">
    <Info> You may get the status of an async request for up to 1 hour after the request has been completed. </Info>

    ```py Python theme={"system"}
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
  </Tab>

  <Tab title="Cancel async request">
    ```py Python theme={"system"}
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
  </Tab>
</Tabs>

Manage async requests using the [get async request API endpoint](/reference/inference-api/status-endpoints/get-async-request-status) and the [cancel async request API endpoint](/reference/inference-api/predict-endpoints/cancel-async-request).

### Processing async predict results

Baseten does not store async predict results. Ensure that prediction outputs are either processed by your webhook, or saved to cloud storage in your model code (for example, in your model's `postprocess` method).

If a webhook endpoint was provided in the `/async_predict` request, the async predict results will be sent in a `POST` request to the webhook endpoint. Errors in executing the async prediction will be included in the `errors` field of the async predict result.

Async predict result schema:

* `request_id` (string): the ID of the completed async request. This matches the `request_id` field of the `/async_predict` response.
* `model_id` (string): the ID of the model that executed the request
* `deployment_id` (string): the ID of the deployment that executed the request
* `type` (string): the type of the async predict result. This will always be `"async_request_completed"`, even in error cases.
* `time` (datetime): the time in UTC at which the request was sent to the webhook
* `data` (dict or string): the prediction output
* `errors` (list): any errors that occurred in processing the async request

Example async predict result:

```json  theme={"system"}
{
  "request_id": "9876543210abcdef1234567890fedcba",
  "model_id": "my_model_id",
  "deployment_id": "my_deployment_id",
  "type": "async_request_completed",
  "time": "2024-04-30T01:01:08.883423Z",
  "data": {
    "my_model_output": "hello world!"
  },
  "errors": []
}
```

## Observability

Metrics for async request execution are available on the [Metrics tab](/observability/metrics#async-queue-metrics) of your model dashboard.

* Async requests are included in inference latency and volume metrics.
* A time in async queue chart displays the time an async predict request spent in the `QUEUED` state before getting processed by the model.
* A async queue size chart displays the current number of queued async predict requests.

<Frame caption="The time in async queue chart.">
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=1dad9805fe14469dcec6d4a34de6177d" data-og-width="1183" width="1183" data-og-height="674" height="674" data-path="images/async-metrics.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=45f877ef07f77b697b8c32b29fd89ace 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=0eff92e843c7801b7fe1c708ae424df9 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=bac3852551a0194b12cdd376a3221a1d 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5c44d8f82786d4fd3511f9cbca34d1ea 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=47e9439cda73a7709776ad4a8c802562 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/images/async-metrics.png?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=c4400b8e7eec5caaacd4dd23ba2f922f 2500w" />
</Frame>

# Securing async inference

Since async predict results are sent to a webhook available to anyone over the internet with the endpoint, you'll want to have some verification that these results sent to the webhook are actually coming from Baseten.

We recommend leveraging webhook signatures to secure webhook payloads and ensure they are from Baseten.

This is a two-step process:

1. Create a webhook secret.
2. Validate a webhook signature sent as a header along with the webhook request payload.

## Creating webhook secrets

Webhook secrets can be generated via the [Secrets tab](https://app.baseten.co/settings/secrets).

<Frame caption="Generate a webhook secret with the &#x22;Add webhook secret&#x22; button.">
  <img src="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=21bbb82f4d935acb8d2bef093976ee5c" data-og-width="1276" width="1276" data-og-height="387" height="387" data-path="images/webhook-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=280&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=6363c0d708393aae40a2dea2552fef05 280w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=560&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=9d8e6ca890928b6b17c06fc964c8d07d 560w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=840&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=35f91f3f4cf3ab3c91a23be8e65c20ac 840w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=1100&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=1eddd1a9b52b0d959bb7108772933973 1100w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=1650&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=42d2b29476c3e1e3ef2ac11b5f7eb73a 1650w, https://mintcdn.com/baseten-preview/QSTsjlPJ_dU4jrB6/images/webhook-secret.png?w=2500&fit=max&auto=format&n=QSTsjlPJ_dU4jrB6&q=85&s=19a19ea3aec8c1d8854bf61f23c7893e 2500w" />
</Frame>

A webhook secret looks like:

```
whsec_AbCdEf123456GhIjKlMnOpQrStUvWxYz12345678
```

Ensure this webhook secret is saved securely. It can be viewed at any time and [rotated if necessary](/inference/async#creating-webhook-secrets) in the Secrets tab.

## Validating webhook signatures

If a webhook secret exists, Baseten will include a webhook signature in the `"X-BASETEN-SIGNATURE"` header of the webhook request so you can verify that it is coming from Baseten.

A Baseten signature header looks like:

`"X-BASETEN-SIGNATURE": "v1=signature"`

Where `signature` is an [HMAC](https://docs.python.org/3.12/library/hmac.html#module-hmac) generated using a [SHA-256](https://en.wikipedia.org/wiki/SHA-2) hash function calculated over the whole async predict result and signed using a webhook secret.

If multiple webhook secrets are active, a signature will be generated using each webhook secret. In the example below, the newer webhook secret was used to create `newsignature` and the older (soon to expire) webhook secret was used to create `oldsignature`.

`"X-BASETEN-SIGNATURE": "v1=newsignature,v1=oldsignature"`

To validate a Baseten signature, we recommend the following. A full Baseten signature validation example can be found in [this Repl](https://replit.com/@baseten-team/Baseten-Async-Inference-Starter-Code#validation.py).

<Steps>
  <Step title="Compare timestamps">
    Compare the async predict result timestamp with the current time and decide if it was received within an acceptable tolerance window.

    ```python  theme={"system"}
    TIMESTAMP_TOLERANCE_SECONDS = 300

    # Check timestamp in async predict result against current time to ensure its within our tolerance
    if (datetime.now(timezone.utc) -
        async_predict_result.time).total_seconds() > TIMESTAMP_TOLERANCE_SECONDS:
      logging.error(
          f"Async predict result was received after {TIMESTAMP_TOLERANCE_SECONDS} seconds and is considered stale, Baseten signature was not validated."
      )
    ```
  </Step>

  <Step title="Recompute Baseten signature">
    Recreate the Baseten signature using webhook secret(s) and the async predict result.

    ```python  theme={"system"}
    WEBHOOK_SECRETS = [] # Add your webhook secrets here

    async_predict_result_json = async_predict_result.model_dump_json()

    # We recompute expected Baseten signatures with each webhook secret
    for webhook_secret in WEBHOOK_SECRETS:
      for actual_signature in baseten_signature.replace("v1=", "").split(","):
        expected_signature = hmac.digest(
            webhook_secret.encode("utf-8"),
            async_predict_result_json.encode("utf-8"),
            hashlib.sha256,
        ).hex()
    ```
  </Step>

  <Step title="Compare signatures">
    Compare the expected Baseten signature with the actual computed signature using [`compare_digest`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest), which will return a boolean representing whether the signatures are indeed the same.

    ```python  theme={"system"}
    hmac.compare_digest(expected_signature, actual_signature)
    ```
  </Step>
</Steps>

## Keeping webhook secrets secure

<Tip> We recommend periodically rotating webhook secrets. </Tip>

In the event that a webhook secret is exposed, you're able to rotate or remove it.

Rotating a secret in the UI will set the existing webhook secret to expire in 24 hours, and generate a new webhook secret. During this period, Baseten will include multiple signatures in the signature headers.

Removing webhook secrets could cause your signature validation to fail. Recreate a webhook secret after deleting and ensure your signature validation code is up to date with the new webhook secret.

## FAQs

### Can I run sync and async requests on the same model?

Yes, you can run both sync and async requests on the same model. Sync requests always take priority over async requests. Keep the following in mind:

* **Rate Limits**: Ensure you adhere to rate limits, as they apply to async requests. [Learn more](/reference/inference-api/predict-endpoints/environments-async-predict#rate-limits)
* **Concurrency**: Both sync and async requests count toward the total number of concurrent requests. [Learn more](/development/model/performance/concurrency)
