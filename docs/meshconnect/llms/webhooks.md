# Source: https://docs.meshconnect.com/testing/webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.meshconnect.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer Webhooks

If your business relies on transfer status updates to make business decisions (releasing inventory, dispersing funds, etc.), then polling Mesh’s managed transfers endpoint is an inefficient and ineffective solution. Mesh offers webhooks to solve this problem. A webhook is a callback function that allows lightweight, event-driven communication between 2 systems. The events that trigger communications from Mesh’s webhooks are updates to transfer statuses. Instead of polling a Mesh endpoint, you can provide Mesh (via the Dashboard) with a unique callback URL which will automatically receive transfer status updates as Mesh learns about them.

## Secure Data Transmission

* Mesh uses HMAC (Hash-based Message Authentication Code)
* When clients register their Webhook URI, they receive a Secret from Mesh which will be used in signing the request.
* Mesh signs each webhook request using a secret key. The receiver can verify the signature using the same secret key to ensure the data has not been tampered with.
* Mesh will include a signature header (e.g., **`X-Mesh-Signature-256`**) that the receiver can use to validate the integrity and authenticity of the payload.

This is the function we use for creating HMAC signature that is used in the request header:

```csharp  theme={null}
 public string GenerateHmacSignature(string payload, string webhookSecret)
    {
        using var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(webhookSecret));
        byte[] hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(payload));
        return Convert.ToBase64String(hash);
    }
```

# Whitelist IP

All the webhook calls from Mesh side will come from this static IP:

```bash  theme={null}
20.22.113.37
```

## Webhook Event Model

The webhook payload contains the core information related to a transfer update, and also includes additional fields specific to the webhook event.

### Transfer data

* **`TransferId`** (`Guid`): The unique identifier of the transfer related to this event.
* **`Timestamp`** (`long`): The timestamp indicating when the event occurred.
* **`TransferStatus`** (`string`): The status of the transfer at the time of the event. This is an enumeration representing various possible states of the transfer.
* **`TransactionId`** (`string`): The unique identifier for the transaction associated with the transfer.
* **`TxHash`** (`string`): The unique identifier for the blockchain transaction associated with the transfer.
* **`UserId`** (`string`): The unique identifier of the user associated with the transfer.
* **`Token`** (`string`): The token associated with the transfer.
* **`Chain`** (`string`): The chain associated with the transfer.
* **`SourceAmount`** (`decimal?`): The amount of token that has left the source account.
* **`SourceAccountProvider`** (`string`): The account provider that has been used to send the token.
* **`DestinationAmount`** (`decimal?`): The amount of token that has received by the destination account.
* **`DestinationAddress`** (`string`): The destination account address.
* **`RefundAddress`** (`string`): The refund address (optional).

### Webhook call data

* **`EventId`** (`Guid`): A unique identifier for the event. This event identifies each message sent to clients. This ID will remain same even in case of retries.
* **`Id`** (`Guid`): A unique identifier for the webhook event. This is considered as SentID, there maybe multiple retries for any event pushed into the queue. For each try for sending a specific event there is a different Id.
* **`SentTimestamp`** (`long`): The timestamp indicating when the webhook event was sent.

### Payload

The payload format is JSON. Here is an example of payload.

```json  theme={null}
{
  "Id": "358c6ab7-4518-416b-9266-c680fda3a8dd",
  "EventId": "56713e70-be74-4a37-0036-08da97f5941a",
  "SentTimestamp": 1720532648,
  "UserId": "user_id_provided_by_client",
  "TransactionId": "transaction_id_provided_by_client",
  "TransferId": "dd4063e5-f317-441c-3f07-08dc7353b6f8",
  "TransferStatus": "Pending",
  "TxHash": "0x7d4ec1ce50952a377452c95fdf5a787ff551f08c0343093f866c84f57c473495",
  "Chain":"Ethereum",
  "Token":"ETH",
  "DestinationAddress":"0x0Ff0000f0A0f0000F0F000000000ffFf00f0F0f0",
  "SourceAccountProvider" :"Binance",
  "SourceAmount":0.004786046226555188,
  "DestinationAmount":0.004786046226555188,
  "RefundAddress": "0x0Ff0000f0A0f0000F0F000000000ffFf00f0F0f0",
  "Timestamp": 1715175519038
}
```

### Transfer Status Values

* **`pending`**: The transfer has been initiated via Mesh, but has not yet reached a final state. Mesh does not yet have a Transfer Hash for this transfer.
* **`succeeded`**: A final state that indicates the transfer was successfully delivered to the destination address. Mesh has a Transfer Hash for this transfer.
* **`failed`**: A final state that indicates the transfer has failed. No transfer hash available.

### Create and register your callback URI

* Create an endpoint that can receive a POST request with application/json content.
* Go to [Account —> API Keys](https://dashboard.meshconnect.com/company/keys) in your Mesh Dashboard.
* Scroll down to “Production Transfer Webhook URI” and “Sandbox Transfer Webhook URI”

<img src="https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerWebhookURI.png?fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=fe05ae7e40b11ba72bf76224a79a87f8" alt="Register Webhook" data-og-width="5760" width="5760" data-og-height="4096" height="4096" data-path="images/registerWebhookURI.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerWebhookURI.png?w=280&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=5de51ea2ac7a95ebb29c909cfb3e9629 280w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerWebhookURI.png?w=560&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=bd6a73ee76a4c9ce611b2699965ad7a5 560w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerWebhookURI.png?w=840&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=7615e658aa3835e4d8e26821a49c8d9c 840w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerWebhookURI.png?w=1100&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=60865389f000fe01df15e0b5a1ed761b 1100w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerWebhookURI.png?w=1650&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=e0da5324c1b9ecc3461130e4224a5d4f 1650w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerWebhookURI.png?w=2500&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=864adc132bcaea03c101e61f94dc4b94 2500w" />

* When registering an endpoint, you’ll be prompted to store your secret key, as you won’t be able to view it again.

<img src="https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerModal.png?fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=535d6074015a8a816a4446e161135903" alt="Register Webhook" data-og-width="5760" width="5760" data-og-height="4096" height="4096" data-path="images/registerModal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerModal.png?w=280&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=6b230327d5e5057eb8506bd916ff969c 280w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerModal.png?w=560&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=935a1440123de1cb79f1d106995bf731 560w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerModal.png?w=840&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=182d2a94417f1da8820cf34966bbd6d6 840w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerModal.png?w=1100&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=b5d44371c22f2ed002e94642aedb0611 1100w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerModal.png?w=1650&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=42507bb4903de9dcf1e9117b2e45a28a 1650w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registerModal.png?w=2500&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=3e3d66f7d6a1d37a5bd0478f4ee7bcd8 2500w" />

* You can only save one production URI and one Sandbox URI, but you can deactivate one and save a new one at any time.

<img src="https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registeredWebhookURI.png?fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=ca6d4f633383e94b7a80d32bc6941686" alt="Register Webhook" data-og-width="5760" width="5760" data-og-height="4096" height="4096" data-path="images/registeredWebhookURI.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registeredWebhookURI.png?w=280&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=e95ece6bd3b8817f3a6e604f7db22e94 280w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registeredWebhookURI.png?w=560&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=55c57bd627957a0ad96406d7f6d8bd34 560w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registeredWebhookURI.png?w=840&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=d92b50688b93456c67be223a15a2c769 840w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registeredWebhookURI.png?w=1100&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=5b270df1ce0468a15b25762961024b40 1100w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registeredWebhookURI.png?w=1650&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=ea53f2fa12ac78c3dc67f344997aaf05 1650w, https://mintcdn.com/mesh-40/wbkTiMTetR6YzaN-/images/registeredWebhookURI.png?w=2500&fit=max&auto=format&n=wbkTiMTetR6YzaN-&q=85&s=a2e5d756e1c6e4a1e4ca59c5e121ec01 2500w" />

### How to respond to a Mesh webhook event

* Please respond with a **`200`** response in \< 200ms to confirm receipt of the event.
* If Mesh does not receive a **`200`** response in \< 200ms, the webhook will retry (you will receive the event again with all duplicate information except for a different **`Id`**).
