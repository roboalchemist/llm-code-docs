# Source: https://www.apollographql.com/docs/graphos/platform/insights/notifications/schema-proposals.md

# Schema Proposals Notifications

Configure GraphOS to send notifications to a webhook whenever schema proposals are created or revised or if their status changes.
These webhooks are useful for automating workflows. For example, your organization may want to open a draft pull request in your codebase whenever a proposal's status changes to **Approved**.

## Setup

1. Go to your graph's **Settings** page in [GraphOS Studio](https://studio.apollographql.com/?referrer=docs-content).

2. Open the **Reporting** tab.

3. Click **Add notification** in the upper right.

4. Select **Schema proposal** and click **Next**.

5. Select the schema proposal event(s) you want to receive notifications for:

   * **Proposal creation**
   * **Proposal revision**
   * **Proposal status change**

6. Select either an existing webhook notification channel or to create a new one. If creating a new one, configure the webhook as described in the next section.

## Configure webhook

Custom webhooks require you to set up an HTTPS endpoint accessible via the public internet. GraphOS sends webhook notifications to this endpoint as `POST` requests. Notification details are provided as JSON in the request body, as described in the next section.

1. Specify a name for this notification channel in the **Channel Name** field. This name must be unique among all your graph's notification channels, including Slack channels.

2. In the **Webhook URL** input, provide the URL of your HTTP(S) endpoint.

3. Optionally, enter a **Secret Token**.

   If you enter a token, each notification HTTP request includes an `x-apollo-signature` header whose value is a [Hash Message Authentication Code (HMAC)](https://en.wikipedia.org/wiki/HMAC) generated using the token, the request body as the message, and the SHA256 hash function. The `x-apollo-signature` header has the format `sha256=<hmac-value>`.

   Given the following inputs:

   **Secret token** (key): `your_secret_token`

   **Request body** (message):

   ```json
   {
     "eventType": "APOLLO_PROPOSAL_STATUS_CHANGE",
     "eventId": "00000000-0000-0000-0000-00000000",
     "graphId": "graphId",
     "variantId": "p-1",
     "proposalId": "00000000-0000-0000-0000-00000000",
     "change": {
       "status": "OPEN",
       "previousStatus": "DRAFT"
     },
     "timestamp": "1970-01-01T00:00:00+0000"
   }
   ```

   **Hash function**: SHA256

   The `x-apollo-header` value would be `sha256=0400670a3ea155eb9f602a60e7897e72515e1a4b04fe06a786e631cc32a1307e`.

   Refer to this [guide from Okta](https://www.okta.com/identity-101/hmac/) to learn more about implementation and see additional resources.

4. Click **Next** and complete any remaining steps in the dialog.

5. When a webhook is received at your configured channel, please respond with status code 200 to acknowledge that the notification was received; otherwise GraphOS will attempt to resend the notification three times."

### Webhook format

Custom webhook notification details are provided as a JSON object in the request body.
To avoid including sensitive information, payloads contain IDs—for example, proposal ID and revision ID—rather than objects containing details about the proposal or revision.
You can use the [Platform API](https://www.apollographql.com/docs/graphos/reference/platform-api/) to fetch full objects using the IDs in the webhook payload.

The JSON object conforms to the structure of the `ResponseShape` interface:

```javascript
enum ProposalStatus {
  OPEN
  DRAFT
  IMPLEMENTED
  APPROVED
}

interface ResponseShape {
  "eventType": string;
  "eventId": string;
  "graphId": string;
  "variantId": string;
  "proposalId": string;
  "change": {
    "status": ProposalStatus | undefined
    "previousStatus": ProposalStatus | undefined
    "revisionId": string | undefined
  },
  "timestamp": string;
}
```

#### Field descriptions

Field
Description

##### `eventType`

The schema proposal event, either `APOLLO_PROPOSAL_CREATED`, `APOLLO_PROPOSAL_REVISION_SAVED`, or `APOLLO_PROPOSAL_STATUS_CHANGE`

##### `eventId`

A unique event ID

##### `proposalId`

A unique proposal ID

##### `change`

* This field isn't present for `APOLLO_PROPOSAL_CREATED` events.

* For `PROPOSAL_REVISION_SAVED` events, the unique `revisionId` of the saved revision.

* For `APOLLO_PROPOSAL_STATUS_CHANGE` events, the current `status` and `previousStatus` of the proposal.
  See [proposal statuses](https://www.apollographql.com/docs/graphos/platform/schema-management/proposals/#proposal-statuses) for more information.

##### `graphId`

A unique graph ID

##### `variantId`

An unique ID in the graph ref format, for example, `graphId@variantName`

##### `timestamp`

An ISO 8601 Date string indicating when the event occurred
