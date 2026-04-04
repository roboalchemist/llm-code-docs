# Source: https://docs.klarna.com/payments/in-store-payments/integrate-klarna-in-store/api-integration/cancel-a-payment.md

# Cancel a payment

## You can cancel an ongoing payment session before the customer completes the payment.

You can cancel the payment session if the customer decides not to finalize the purchase. We recommend that you cancel such sessions as soon as possible to ensure the session duration in your system and in Klarna’s match. While an In-store payment session expires in 46 hours, the session in your system may have a shorter expiration time.

## Canceling a payment

To cancel a payment, send a `DELETE` request to the [`{apiURL}`](https://docs.klarna.com/api/api-urls/)`/payments/v1/sessions/{session_id}` endpoint. Provide the Klarna payments session ID as the `session_id` path parameter. When you cancel a session, a canceled status view will be displayed on the terminal.


![ The cancelation message is displayed after you cancel an in-store payment session.](d55f8323-c2d8-4166-b8dc-1f1ae82cac4c_In-store_payment_canceled_2023-05_01.jpeg)
*The cancelation message is displayed after you cancel an in-store payment session.*