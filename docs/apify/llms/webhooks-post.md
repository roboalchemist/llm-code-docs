# Source: https://docs.apify.com/api/v2/webhooks-post.md

# Create webhook


```
POST 
https://api.apify.com/v2/webhooks
```


Creates a new webhook with settings provided by the webhook object passed as JSON in the payload. The response is the created webhook object.

To avoid duplicating a webhook, use the `idempotencyKey` parameter in the request body. Multiple calls to create a webhook with the same `idempotencyKey` will only create the webhook with the first call and return the existing webhook on subsequent calls. Idempotency keys must be unique, so use a UUID or another random string with enough entropy.

To assign the new webhook to an Actor or task, the request body must contain `requestUrl`, `eventTypes`, and `condition` properties.

* `requestUrl` is the webhook's target URL, to which data is sent as a POST request with a JSON payload.
* `eventTypes` is a list of events that will trigger the webhook, e.g. when the Actor run succeeds.
* `condition` should be an object containing the ID of the Actor or task to which the webhook will be assigned.
* `payloadTemplate` is a JSON-like string, whose syntax is extended with the use of variables.
* `headersTemplate` is a JSON-like string, whose syntax is extended with the use of variables. Following values will be re-written to defaults: "host", "Content-Type", "X-Apify-Webhook", "X-Apify-Webhook-Dispatch-Id", "X-Apify-Request-Origin"
* `description` is an optional string.
* `shouldInterpolateStrings` is a boolean indicating whether to interpolate variables contained inside strings in the `payloadTemplate`


```
"isAdHoc" : false,
    "requestUrl" : "https://example.com",
    "eventTypes" : [
        "ACTOR.RUN.SUCCEEDED",
        "ACTOR.RUN.ABORTED"
    ],
    "condition" : {
        "actorId": "janedoe~my-actor",
        "actorTaskId" : "W9bs9JE9v7wprjAnJ"
    },
    "payloadTemplate": "",
    "headersTemplate": "",
    "description": "my awesome webhook",
    "shouldInterpolateStrings": false,
```


**Important**: The request must specify the `Content-Type: application/json` HTTP header.

## Request

## Responses

* 201
* 400

**Response Headers**

* **Location**

Bad request - invalid input parameters or request body.
