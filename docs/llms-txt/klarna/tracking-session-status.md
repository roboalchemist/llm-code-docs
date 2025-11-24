# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/before-you-start/tracking-session-status.md

# Tracking session status

Each *HPP Session* is following a state machine to map the Consumer’s action to a certain state, which allows any integrator to act depending on the current state. Integrators have two ways to get the current state, either by reading the *HPP Session* using an API endpoint or by using the callback mechanism. Both systems can be used at the same time and it is advised to have a batch running in case there was a loss in communication between systems while the callbacks were sent. As described in the callbacks reference, the callback mechanism will try to reach the integrator system with a retry mechanism, but will stop doing so if your system is not answering after a few times. When integrating with Klarna Payments, as soon as the Consumer gets an authorization, you will be able to extract the **Authorization Token** of the *KP Session* from the server response, which will let you place the order.

## HPP Session Lifecycle


![ HPP Session lifecycle](95f61a59-bad5-47c4-bed2-e44a9c5b100b_HPP+session+lifecycle.jpeg)
*HPP Session lifecycle*

| Status name | Final | Status description |
|----|----|----|
| WAITING | No | Session is created and Consumer has not entered the Payment Page yet. |
| IN_PROGRESS | No | Consumer has entered the Payment Page on updated_at. |
| COMPLETED | Yes | Consumer has successfully gotten an Authorization from the Payment system onupdated_at. The*Authorization Token*is contained in theauthorization_tokenfield in a Klarna Payments integration. |
| FAILED | No | Consumer has been declined for the Payment onupdated_at. Session is still open for them to retry. |
| CANCELLED | Yes | Consumer has cancelled the HPP Session onupdated_at. This cancellation is definitive. |
| BACK | No | Consumer has pressed the Back button onupdated_at. Session is still open for them to retry. |
| ERROR | No | Consumer has encountered an error while paying onupdated_at. Session is still open for them to retry. |
| DISABLED | Yes | Session was disabled by an API call, on the merchant’s initiative, onupdated_at. |

## Reading the HPP Session updates by polling an endpoint

The *HPP Session* can be read by the integrator using a [specific endpoint of the API](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/read-session/). You will get the URL of the read session endpoint back from the [create session call](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/create-session/), it is the session_url parameter. You can for example use a polling mechanism to check the status of the session and update your data depending on the payload. Although we suggest that you use the callbacks mechanism. See our [reference of the Read Session endpoint](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/read-session/).

## Getting the HPP Session updates by using the callback mechanism

When [creating the HPP Session](https://docs-portal-eu.production.c2c.klarna.net/hosted-payment-page/api-documentation/create-session)*HPP Session* an integrator can pass an URL that will be called by our systems whenever the status of the session is updated. This is really handy to create interaction whenever something happens and avoid to have a costly polling mechanism. See our [reference of the callbacks mechanism](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/status-callbacks/).