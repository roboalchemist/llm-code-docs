# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/disputes/integrate-with-the-disputes-api.mdx

***

## stoplight-id: 87e81rujlq80x

# Integrate with the Disputes API

Merchants can integrate directly with the Disputes API to scale their disputes process and integrate with other order management and customer service tools. This is helpful for merchants who handle a high volume of transactions.

| **Action**                                                                                   | **Endpoint**                       | **Purpose**                               |
| -------------------------------------------------------------------------------------------- | ---------------------------------- | ----------------------------------------- |
| [Receive dispute](/cash-app-afterpay/api-reference/reference/disputes/receive-dispute)       | GET `/v2/disputes/{dispute_id}`    | Get detailed information about a dispute. |
| [List disputes](/cash-app-afterpay/api-reference/reference/disputes/retrieve-dispute)        | `/v2/disputes`                     | List disputes based on a set of criteria. |
| [Accept dispute](/cash-app-afterpay/api-reference/reference/disputes/accept-dispute)         | `/v2/disputes/{dispute_id}/accept` | Accept a dispute case.                    |
| [Respond to dispute](/cash-app-afterpay/api-reference/reference/disputes/respond-to-dispute) | POST `/v2/disputes/{dispute_id}`   | Submit evidence to respond to a dispute.  |
| [Upload file](/cash-app-afterpay/api-reference/reference/disputes/upload-file)               | `/v2/disputes/files`               | Upload a file for a dispute.              |
| [Retrieve file](/cash-app-afterpay/api-reference/reference/disputes/retrieve-file)           | `/v2/disputes/files/{id}`          | Retrieve a file for a dispute.            |

<div>
  ```mermaid
  ---
  config:
    sequence:
      mirrorActors: true
      width: 300
  ---
  %%{
    init: {
      'theme': 'base',
      'themeVariables': {
        'primaryColor': '#FFF',
        'primaryTextColor': '#000',
        'primaryBorderColor': '#000',
        'lineColor': '#000',
        'secondaryColor': '#fff',
        'tertiaryColor': '#fff',
        'noteBkgColor': '#fff',
        'noteBorderColor': '#000'
      }
    }
  }%%
  sequenceDiagram
      participant AP as $Afterpay Dispute API
      participant M as Merchant
      rect rgb(250,250,250)
        note over AP: Event: Dispute created
        AP -->> M: Webhook Notification
        M ->> AP: Fetch Dispute API
        AP ->> M: Latest Dispute Object
        M ->> M: Create Dispute
      end
      rect rgb(250,250,250)
        note over AP: Event: Dispute updated
        AP -->> M: Webhook Notification
        M ->> AP: Fetch Dispute API
        AP ->> M: Latest Dispute Object
        M ->> M: Update Dispute Status
      end
      rect rgb(250,250,250)
        note over AP: Action: Merchant Challenge Dispute
        M ->> AP: Upload File Api
        AP ->> M: Return file token
        M ->> AP: Challenge Dispute API
        AP ->> M: Latest Dispute Object
        M ->> M: Update Dispute Status
      end
      rect rgb(250,250,250)
        note over AP: Action: Merchant Accept Dispute
        M ->> AP: Accept Dispute API
        AP ->> M: Latest Dispute Object
        M ->> M: Update Dispute Status
      end
  ```
</div>

## Dispute notifications

Cash App Afterpay notifies merchants using webhooks when a dispute is created and any time it is updated. Cash App Afterpay expects the ACK (acknowledgement) with a 200 response. If the acknowledgement fails, Cash App Afterpay will reattempt sending the webhook a few times with exponential backoff.

The following table outlines the content for the webhook call:

| Field name           | Data type | Description                                                                                                        |
| -------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ |
| `webhook_event_id`   | String    | The `event_id` of the webhook.                                                                                     |
| `webhook_event_type` | String    | An enum variable that indicates if the dispute was created or updated. Possible values are `created` and `updated` |
| `dispute_id`         | String    | Dispute Identifier.                                                                                                |
| `merchant_reference` | String    | Merchant identifier.                                                                                               |

A `dispute_id` is passed in the webhook call. Merchants can use the Get Dispute endpoint to get the details for the dispute.

### Notification setup

Merchants must provide a webhook URL and merchant IDs to the Cash App Afterpay merchant service/dispute team to get the HMAC key and enable the notification.

The webhook endpoint should be maintained by merchants or partners, it should allow POST requests with `content-type` = `application/json`.

<Note>
  The payload format is defined in the previous table.
</Note>

### Notification authentication

* (option 1) Key Exchange Wiki: [Diffie-Hellman Key Exchange via Openssl: Quick Guide](/cash-app-afterpay/guides/api-development/disputes/integrate-with-the-disputes-api#key-exchange)
* (option 2) Securely get HMAC key from [https://squareup.sendsafely.com/](https://squareup.sendsafely.com/)

### HMAC signature

Cash App Afterpay recommends that you use HMAC for the authentication of the webhook notification.
Consider the following structure of the raw HTTP message.

```javascript
POST ${notification_uri} HTTP/1.1
Host: ${notification_base_url}
X-Afterpay-Request-Date: 1664239810
X-Afterpay-Request-Signature: ${signature}
Content-Type: application/json
{
    "webhook_event_id": "b4df2187-4090-4845-be15-a73546107cbe",
    "webhook_event_type": "created",
    "dispute_id": "dp_KvGaECApCMdsH8earUSa2V",
    "merchant_reference": "08CF65ZSFNHVM"
}
```

There will be two extra fields for authentication.

* `X-Afterpay-Request-Date` records the send time for the webhook request. We recommned aborting the stale notification after a fixed time (if you receive the webhook and current timestamp - `${X-Afterpay-Request-Date}` is greater than 5 minutes).
* `X-Afterpay-Request-Signature` records the signature of the HMAC key. Typically we generate the signature using the following steps:

  ```javascript
  PAYLOAD={"webhook_event_id": "b4df2187-4090-4845-be15-a73546107cbe", "webhook_event_type":       "created", "dispute_id": "dp_KvGaECApCMdsH8earUSa2V", "merchant_reference": "08CF65ZSFNHVM"}
  URL= "${partner_notification_uri}"
  SECRET=<hmac secret key here>
  TIME=1664239810
  MESSAGE="$URL\n$TIME\n$PAYLOAD"
  X-Afterpay-Request-Signature=$(printf "${MESSAGE}" | openssl dgst -hmac ${SECRET} -sha256   -binary | base64)
  ```

When a merchant or merchant agency receives a webhook notification, we recommend generating verification signatures in following steps.

<Info>
  If `HMAC == X-Afterpay-Request-Signature`, then continue to process the notification, or the merchant should abort the request.
</Info>

```javascript
PAYLOAD={"webhook_event_id": "b4df2187-4090-4845-be15-a73546107cbe", "webhook_event_type": "created", "dispute_id": "dp_KvGaECApCMdsH8earUSa2V", "merchant_reference": "08CF65ZSFNHVM"}
URL= "${Notification_uri}"
SECRET=<hmac secret key here>
TIME=${X-Afterpay-Request-Date}
MESSAGE="$URL\n$TIME\n$PAYLOAD"
HMAC=$(printf "${MESSAGE}" | openssl dgst -hmac ${SECRET} -sha256 -binary | base64)
```

## Series of events

| Trigger                                        | API event                                                                                                                                                                                                                                     | Outcome                                                                                                              |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| The customer creates a dispute in the app      | Webhook notifies the merchant (incl. webhook\_event\_type = created and a dispute\_id)                                                                                                                                                        | The dispute is created and the merchant is notified. The dispute status is updated to `needs_response`.              |
| The merchant retrieves the dispute information | The Get Dispute endpoint is called to fetch status of the dispute (based on Dispute ID), and returns the updated Dispute object. If images or attachments were supplied; these are retrieved with the Retrieve File api endpoint.             | The merchant can challenge or accept the dispute.                                                                    |
| The merchant challenges the dispute            | The merchant collates their response collateral internally. If there are files to upload, the Upload File endpoint is called for the relevant files. The Respond to Dispute endpoint is called which references the file IDs for those files. | The merchant has submitted evidence to challenge the dispute. The dispute status is updated to `under_review`.       |
| The merchant accepts the dispute               | The Accept Dispute endpoint is called, returns the Dispute object to the merchant.                                                                                                                                                            | The dispute status is updated to `lost` and the dispute is closed. The closing reason is set to `merchant_accepted`. |
| The customer accepts the merchant’s evidence   | If webhook is enabled, this will come through as a notification                                                                                                                                                                               | The dispute status is updated to ‘won’ and the dispute is closed. The closing reason is set to `evidence_accepted`.  |
| The customer rejects the merchant’s evidence   |                                                                                                                                                                                                                                               | The dispute is sent to Afterpay for adjudication                                                                     |
| Afterpay adjudicates in the merchant’s favor   | If webhook is enabled, this will come through as a notification                                                                                                                                                                               | The dispute status is updated to ‘won’ and the dispute is closed. The closing reason is set to `evidence_accepted`.  |
| Afterpay adjudicates in the customer’s favor   | If webhook is enabled, this will come through as a notification                                                                                                                                                                               | The dispute status is updated to `lost` and the dispute is closed. The closing reason is set to `evidence_rejected`. |
| The customer cancels the dispute               | If webhook is enabled, this will come through as a notification                                                                                                                                                                               | The dispute status is updated to `won` and the dispute is closed. The closing reason is set to `customer_cancelled`. |
| The customer updates the dispute.              | Webhook notifies merchant (incl. webhook\_event\_type = updated and a dispute\_id) Get Dispute endpoint is called to fetch status of the dispute (based on Dispute ID), returns the updated Dispute object.                                   | The dispute status is updated. The dispute status is updated to `needs_response`.                                    |
