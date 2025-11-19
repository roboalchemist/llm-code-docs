# Source: https://docs.frigade.com/api-reference/webhooks.md

# Webhooks

Webhooks allow you to receive notifications from Frigade when certain events occur.
You can use webhooks to receive notifications about your users when they start a Flow and as they progress through it.

## Creating a webhook

To add a new webhook, open the **Developer** page from the left sidebar, pick the **Webhooks** tab and click the "New webhook" button.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/platform/webhooks.png" />
</Frame>

## Supported events

The following events are currently supported:

<ParamField body="flowResponse.startedFlow">When a user starts a Flow</ParamField>
<ParamField body="flowResponse.completedFlow">When a user completes a Flow</ParamField>
<ParamField body="flowResponse.skippedFlow">When a user dismisses/skips a Flow</ParamField>
<ParamField body="flowResponse.startedStep">When a user starts a Step in a Flow</ParamField>
<ParamField body="flowResponse.completedStep">When a user completes a Step in a Flow</ParamField>

## Webhook payload

The payload of the message includes the type of the event in the `type` property.

The data property contains the actual payload sent by Frigade.
The payload can be a different object depending on the event type.

### Schema

```typescript
{
  // Event type identifier
  type: string;  // e.g. "flowResponse.completedFlow"
  
  // Timestamp when the event occurred (ISO 8601)
  time: string;  // e.g. "2024-08-21T16:31:36.207Z"
  
  // Request timeout in milliseconds
  timeout: number;

  // User information
  user: {
    // The user id in your system. This will match the `foreignUserId` field in the data object.
    id: string;
    // The name of the user
    name: string;
    // The email of the user
    email: string | null;
  };

  // Flow information
  flow: {
    // Flow ID, for example: flow_8Lq7hAqA
    id: string;

    // Flow name, for example: "NPS Survey"
    name: string;
  };

  // Detailed response data
  data: {
    // Step-specific data, keyed by stepId
    [stepId: string]: {
      [fieldName: string]: any;
    };

    // Response ID
    id: string;

    // Flow ID
    flowId: string;

    // Flow slug
    flowSlug: string;

    // Numeric Frigade user ID
    userId: number;

    // Frigade user slug
    userSlug: string;

    // Action type: COMPLETED_FLOW, SKIPPED_FLOW, COMPLETED_STEP, SKIPPED_STEP
    actionType: string;

    // Step ID
    stepId: string;

    // ISO 8601 timestamp
    createdAt: string;

    // Foreign user ID. This will match your own internal user ID provided to Frigade.
    foreignUserId: string;

    // Whether the flow is blocked
    blocked: boolean;

    // Whether the flow is hidden
    hidden: boolean;

    // Additional data collected, such as form data in a stringified JSON object.
    data: string;
  };
}
```

The below example shows the payload for a `flowResponse.completedFlow` event for the [NPS Survey](/component/survey/nps) component with flattened data fields:

```json
{
  "timeout": 1000,
  "data__nps-feedback-page__nps-feedback-text": "I love the service!",
  "data__nps-score-page__nps-score": 10,
  "data__id": "flowResponse_uPzbTOayngU00Vzc",
  "data__flowId": "flow_8Lq7hAqA",
  "data__flowSlug": "flow_8Lq7hAqA",
  "data__userId": 53526,
  "data__userSlug": "user_qnsDyTeZxP2sl12Q",
  "data__actionType": "COMPLETED_FLOW",
  "data__data": "{}",
  "data__stepId": "nps-feedback-page",
  "data__blocked": false,
  "data__hidden": false,
  "user__name": "",
  "user__email": null,
  "user__id": "abcdefgh",
  "flow__id": "flow_8Lq7hAqA",
  "flow__name": "NPS Survey",
  "type": "flowResponse.completedFlow",
  "data": {
    "nps-feedback-page": {
      "nps-feedback-text": "I love the service!"
    },
    "nps-score-page": {
      "nps-score": 10
    },
    "id": "flowResponse_uPzbTOayngU00Vzc",
    "flowId": "flow_8Lq7hAqA",
    "flowSlug": "flow_8Lq7hAqA",
    "userId": 53526,
    "userSlug": "user_qnsDyTeZxP2sl12Q",
    "actionType": "COMPLETED_FLOW",
    "data": "{}",
    "stepId": "nps-feedback-page",
    "createdAt": "2024-08-21T16:31:36.187Z",
    "foreignUserId": "abcdefgh",
    "blocked": false,
    "hidden": false
  },
  "time": "2024-08-21T16:31:36.207Z",
  "user": {
    "name": "",
    "email": null,
    "id": "abcdefgh"
  },
  "flow": {
    "id": "flow_8Lq7hAqA",
    "name": "NPS Survey"
  }
}
```

## Verifying webhooks

When you create a webhook, Frigade will generate a secret key for you. You can use this key to verify that the webhook is coming from Frigade.

<Note>
  If you don't verify the request, your app will be susceptible to a number of attacks since your webhook endpoint is open to the public.
</Note>

To verify the request, you need to calculate the HMAC SHA256 digest of the JSON-encoded `data` field using the secret key as the key and compare it to the value in the `X-Webhook-Signature` header. The signature is base64 encoded.
Note that when JSON-encoding the `data` field it needs to match the order of the keys in the payload and not contain any whitespace between the keys and values.

For example, in Node.js, you can do it like this:

```ts
const crypto = require('crypto');

const payload = '{"type":"flowResponse.completedStep",....}}'
const secret = 'my-secret' // Find this in the webhook settings in the Frigade dashboard
function verifySignature(secret, payload) {
  const hmac = crypto.createHmac('sha256', secret);
  hmac.update(Buffer.from(payload, 'utf-8'));
  const digest = hmac.digest('base64');
  return digest;
}

const signature = verifySignature(secret, payload);

if (signature !== payload.signature) {
  throw new Error('Invalid signature');
}
```

## Verifying timestamps

The `time` field in the payload is the time when the event occurred. You can use this field to verify that the request is not a [replay attack](https://en.wikipedia.org/wiki/Replay_attack) by ignoring older events.

## Retrying failed requests

Frigade will retry failed requests up to 5 times with an exponential backoff strategy.

## Common fields

The following fields are available in all Frigade webhooks (shown in flattened format):

* `flow__id`: The ID of the Flow that triggered the webhook
* `flow__name`: The name of the Flow that triggered the webhook
* `user__id`: The ID of the user that triggered the webhook
* `user__name`: The name of the user that triggered the webhook (if available)
* `user__email`: The email of the user that triggered the webhook (if available)
