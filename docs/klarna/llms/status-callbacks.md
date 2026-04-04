# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/api-documentation/status-callbacks.md

# Status Callbacks

It is possible when integrating HPP to received status changes callbacks to a certain URL. This address that is unique to every session will be called by our systems whenever the status of the session is updated. This is really handy to create interaction whenever something happens and avoid to have a costly polling mechanism. It is advised to read our [guide on how to track the HPP Session status changes](https://docs.klarna.com/payments/other-products/hosted-payment-page/before-you-start/tracking-session-status/).

{{#mermaid:
sequenceDiagram
autonumber
participant A as Consumer
participant B as Browser
participant C as HPP
participant D as Merchant Backend
C -->> A: A link to the HPP is provided to the consumer by e-mail, SMS, QR code or<br/> simply browser redirection
B ->> C: Request url
note over A,D: The consumer arrives to the HPP and the distribution of the link was successful,<br/> the Merchant backend is notified to be able to act on it.<br/> On integration with multiple actors, it may allow to tell the other actor (a clerk) that the consumer is filling the application.
C -->>D: Notification IN_PROGRESS
alt Successful authorization
A ->>C: Presses pay button
note over A,D: The consumer has a successful authorization from Klarna and the payment can be satisfied. The HPP session is considered as COMPLETED<br/> but it is needed from the Merchant to place the order.
C -->>D: Notification COMPLETED
note over A,D: Depending on how the HPP session was created, the consumer will receive as a result a hosted confirmation page<br/> or a redirection to your website using merchant_urls.
C ->>B: Result
else Declined authorization
A ->>C: Presses pay button
note over A,D: Although the consumer wants to pay with Klarna, its application may be declined, which is known as a Failure.<br/> The HPP session is considered as FAILED, but the consumer can still try again until they cancel the HPP session<br/> or the merchant integration does it.
C -->>D: Notification FAILED
note over A,D: Depending on how the HPP session was created, the consumer will receive as a result a hosted confirmation page<br/> or a redirection to your website using merchant_urls.
C ->>B: Result
else Bank and error cases
note over A,D: The consumer chooses to cancel the order or to go back to the checkout progress.<br/> All cases can be interpreted the same way as there is just a notification that will send the new status of the HPP session.<br/> Depending if it is a back button or cancellation request,<br/> the consumer may or may not come back to the same HPP session.
A ->>C: Presses back button or cancellation button
C -->>D: Notification BACK or CANCELLED
note over A,D: Depending on how the HPP session was created, the consumer will receive as a result a hosted confirmation page<br/> or a redirection to your website using merchant_urls.
C -->>B: Result
else Timeout of the HPP session
note over A,D: The consumer may not use the back button or cancel button and just leave the page, or choose another payment method using the previous<br/> page feature of their browser. In these cases, the HPP system loses track of the consumer.<br/> A timer is set for every HPP session and will turn the status to TIMEOUT. This timer will depend on how the HPP session was created.
C -->>D: Notification TIMEOUT
end
}}

## Activating Callbacks

When [creating the HPP Session](https://docs-portal-eu.production.c2c.klarna.net/hosted-payment-page/api-documentation/create-session)*HPP Session*, you need to pass an URL in the status_update field of the merchant_urls. This URL will be called by HPP each time the status of the *HPP Session* is updated on Consumers actions, it contains the new status of the *HPP Session* the same way it would be gotten by reading the *HPP Session* from the [read session endpoint of the API](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/read-session/).

## Definition of callbacks calls

| **Description** | **POST the Status of the HPP Session to the integrator** |
|----|----|
| **URL** | HPP will use merchant_urls.status_updatereceived in the [create session call](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/create-session/) |
| **Operation** | POST |
| **Example** | curl -X POST \<merchant_urls.status_update\> --data “<content>” |

### Body of the callback

| **Field Key** | **Type** | **Description** |
|----|----|----|
| **event_id** | String | Identifier of the event, allowing the integrator to de-duplicate operations if needed. |
| **session** | JSON | And object representing the session status when the event occurred. Content is exactly the same as one could get from the [read session endpoint](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/read-session/). |

## Expected response and retry strategy

The calls made to the status_update URL will be made by *HPP* without waiting for any response from your server. It is expected from the the URL to send back a 2xx status code response. In case no response is gotten in less than 3 seconds, there will be a retry after a few seconds. This mechanism will happen up to three times, with 4 calls being made for the same events. If of these calls are unanswered, the callback mechanism will end.

## Securing the callbacks

The URL provided as status_update must be over HTTPS, but to be able to authenticate that the callback comes from Klarna, it is advised to generate a one time token that you will only use for this specific *HPP Session*. This lets you validate that the call made to you on an update of status is only made by us.

``` json
{
    "merchant_urls": {
        "status_update": "https://example.com/statsCallbackEndpoint?hppSessionId={{session_id}}&secretToken=7d1cbc3b-b30c-4be2-a8c4-dc76482d7bf6"
    }
}
```

The value passed here 7d1cbc3b-b30c-4be2-a8c4-dc76482d7bf6 could be something that is generated by the integrator for every new session.

## Happy flow examples

These are the callbacks that an integration layer will get when an HPP Session is completed.

### Consumer arrives on HPP

``` json
{
  "event_id": "270b2adc-35a4-4524-800a-a5d2b8a96a2c",
  "session": {
    "session_id": "35bde117-ce5f-774f-9bcb-ec514a0963ad",
    "status": "IN_PROGRESS",
    "updated_at": "2019-05-13T14:51:46.288Z",
    "expires_at": "2019-05-15T13:51:43.507Z"
  }
}
```

### Consumer completes Payment

#### Klarna Payments

To learn more about place_order_mode, read our [guide on how to integrate Klarna Payments with HPP](https://docs.klarna.com/payments/other-products/hosted-payment-page/before-you-start/accept-klarna-payments-using-hosted-payment-page/). Default value for place_order_mode

``` json
{
  "event_id": "27ba32b0-644b-4b22-94a9-dac503bcae18",
  "session": {
    "session_id": "39a1c773-bafd-754d-af1f-b30c592f1267",
    "status": "COMPLETED",
    "authorization_token": "a1a8f727-2756-6058-bd3c-40069be0994b",
    "updated_at": "2019-05-13T14:54:04.675Z",
    "expires_at": "2019-05-15T13:51:43.507Z"
  }
}
```

With place_order_mode as PLACE_ORDER or CAPTURE_ORDER

``` json
{
  "event_id": "27ba32b0-644b-4b22-94a9-dac503bcae18",
  "session": {
    "session_id": "39a1c773-bafd-754d-af1f-b30c592f1267",
    "status": "COMPLETED",
    "order_id": "a1a8f727-2756-6058-bd3c-40069be0994b",
    "klarna_reference": "X438HG0Q",
    "updated_at": "2019-05-13T14:54:04.675Z",
    "expires_at": "2019-05-15T13:51:43.507Z"
  }
}
```</content></merchant_urls.status_update\>