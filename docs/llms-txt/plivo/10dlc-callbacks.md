# Source: https://plivo.com/docs/messaging/concepts/callbacks/10dlc-callbacks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# 10DLC Callbacks

> Receive status updates for brand, campaign, and number registrations

Registering your number with 10DLC requires you to interact with different Plivo APIs.

For every Brand, Campaign, Number Linking, and Number Unlinking request you send, Plivo sends a status update to a URL you configure as a callback. You can store this information on your server for delivery status analysis.

<Frame>
    <img src="https://mintcdn.com/plivo/sqGJ0ONkT5kTuesy/images/sms-callbacks.png?fit=max&auto=format&n=sqGJ0ONkT5kTuesy&q=85&s=64a94312c5c0ea3237779f8384a3eb8a" alt="SMS callbacks" width="813" height="232" data-path="images/sms-callbacks.png" />
</Frame>

The webhooks you integrate with Plivo are triggered by changes in the status of Brand, Campaign, or Number requests (e.g. successful registration of your brand with TCR). Upon one of these events, Plivo makes an HTTP request (POST or GET) to the endpoint URL you’ve configured for the webhook. To handle a webhook, you must create a listener (web app) that can accept these HTTP requests from Plivo.

## Create Brand

* [Node.js](/messaging/concepts/callbacks/10dlc-callbacks#register-brand-standard-node)

* [PHP](/messaging/concepts/callbacks/10dlc-callbacks#register-brand-standard-node)

* [.NET](/messaging/concepts/callbacks/10dlc-callbacks#register-brand-standard-net)

* [Curl](/messaging/concepts/callbacks/10dlc-callbacks#register-brand-standard-curl)

## Create Campaign

* [Node.js](/messaging/concepts/callbacks/10dlc-callbacks#register-brand-standard-node)

* [PHP](/messaging/concepts/callbacks/10dlc-callbacks#register-brand-standard-php)

* [.NET](/messaging/concepts/callbacks/10dlc-callbacks#register-brand-standard-net)

* [Curl](/messaging/concepts/callbacks/10dlc-callbacks#register-brand-standard-curl)

## Link Number

* [Node.js](/messaging/concepts/callbacks/10dlc-callbacks#register-campaign-node)

* [PHP](/messaging/concepts/callbacks/10dlc-callbacks#register-campaign-php)

* [.NET](/messaging/concepts/callbacks/10dlc-callbacks#register-campaign-net)

* [Curl](/messaging/concepts/callbacks/10dlc-callbacks#register-campaign-curl)

## Unlink Number

* [Node.js](/messaging/concepts/callbacks/10dlc-callbacks#unlink-number-node)

* [PHP](/messaging/concepts/callbacks/10dlc-callbacks#unlink-number-php)

* [.NET](/messaging/concepts/callbacks/10dlc-callbacks#unlink-number-net)

* [Curl](/messaging/concepts/callbacks/10dlc-callbacks#unlink-number-curl)

## Handle callbacks in your web app

To handle callbacks in your application, your endpoint should capture HTTP requests and respond to them. When Plivo sends the HTTP request callbacks to the webhook during an event, you should capture the request (POST or GET based on the method you’ve defined for the URL) and respond with a 200 OK response. You can store the callback data in your database.

<Note>
  <strong>Note:</strong> Plivo automatically retries webhooks three times if an HTTP 200 status code is not returned:
  \*First at 60 seconds after the original attempt.
  \*Second at 120 seconds after the first retry attempt.
  \*Third at 240 seconds after the second retry attempt.
</Note>

## Possible  status values

| **Endpoint**      | **Status** | **Explanation**                                                                                                                                                    |
| ----------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| brand             | created    | Brand creation request was submitted to TCR for processing.                                                                                                        |
|                   | rejected   | Brand creation was rejected by TCR. Reach out to our support team to learn why.                                                                                    |
|                   | registered | Brand was registered with TCR. You can now create campaigns using this brand.                                                                                      |
| campaign          | created    | Campaign creation request was submitted to TCR for processing.                                                                                                     |
|                   | rejected   | Campaign creation request was rejected by TCR. Reach out to our support team to learn why.                                                                         |
|                   | registered | Campaign was registered with TCR. You can now link your Plivo long codes with this campaign.                                                                       |
| number\_linking   | created    | Request to link your Plivo long code with the campaign was submitted to operators.                                                                                 |
|                   | failed     | Request to link your Plivo long code with the campaign was rejected by operators. Retry the request; if the            issue persists, contact our support team.   |
|                   | success    | Request to link your Plivo long code with the campaign was processed by operators.                                                                                 |
| number\_unlinking | created    | Request to unlink your Plivo long code with the campaign was submitted to operators.                                                                               |
|                   | failed     | Request to unlink your Plivo long code with the campaign was rejected by operators. Retry the request; if            the issue persists, contact our support team. |
|                   | success    | Request to unlink your Plivo long code with the campaign was processed by operators. This number can now be            linked to other campaigns.                  |

## Test and Validate

Let’s take a look at an example. Typically, you would include a URL that points to your web app, but we’ll use a URL from [RequestBin](https://requestbin.com/), a service that lets you collect, analyze, and debug HTTP requests, so we can check the callbacks.

* Create a new bin in RequestBin.
* Replace the “url” placeholder with the URL of the new bin.
* Run the code that appear above. You should see callback requests in RequestBin similar to the screenshots below for various callback events.

### Brand created callback

<Frame>
    <img src="https://mintcdn.com/plivo/2OFvQXVNT3srKLUy/images/created-pending-1.png?fit=max&auto=format&n=2OFvQXVNT3srKLUy&q=85&s=ceb4744e1aa22f2e0558280c3ecbf8bf" alt="" width="1980" height="496" data-path="images/created-pending-1.png" />
</Frame>

### Brand registered callback

<Frame>
    <img src="https://mintcdn.com/plivo/NFI9_HRHTMInDf93/images/active-1.png?fit=max&auto=format&n=NFI9_HRHTMInDf93&q=85&s=18605d2437f269f811c06bc7729cd32a" alt="" width="1952" height="528" data-path="images/active-1.png" />
</Frame>

### Campaign created callback

<Frame>
    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/campaign-created.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=dc078a0c9220437b92d8e4253ca43fb3" alt="" width="1408" height="350" data-path="images/campaign-created.png" />
</Frame>

### Campaign registered callback

<Frame>
    <img src="https://mintcdn.com/plivo/EvRfP72Bjs4tuRt5/images/campaign-registered.png?fit=max&auto=format&n=EvRfP72Bjs4tuRt5&q=85&s=5b9e70fff5f7fd28714f42c78fb45047" alt="" width="1369" height="346" data-path="images/campaign-registered.png" />
</Frame>

### Number linking created callback

<Frame>
    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-linked.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=4602abb181fda49cd6957f15a57cc6a2" alt="" width="2040" height="480" data-path="images/number-linked.png" />
</Frame>

### Number unlinking created callback

<Frame>
    <img src="https://mintcdn.com/plivo/M2NzHE_bNZbCm0gd/images/number-unlinked.png?fit=max&auto=format&n=M2NzHE_bNZbCm0gd&q=85&s=13e40bb9756ac18f74c51e3cbc073b31" alt="" width="2005" height="507" data-path="images/number-unlinked.png" />
</Frame>

## Validating callbacks

To avoid spoof attacks, you can validate the callbacks that your server URL receives. All requests made by Plivo to your server URLs include X-Plivo-Signature-V2, X-Plivo-Signature-Ma-V2, and X-Plivo-Signature-V2-Nonce HTTP headers. You can use them to validate that a request is from Plivo, as we discuss in our [signature validation guide](/messaging/concepts/signature-validation/).
