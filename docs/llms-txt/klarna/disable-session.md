# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/api-documentation/disable-session.md

# Disable Session with Hosted Payment Page - API Details

If for any reason the payment session has to be canceled (expiration of an offer, order was paid using another payment method, etc), the HPP API gives to the Merchant the possibility to disable an **HPP Session**. To do that, it is required to send a delete request on the HPP Session resource. The URL of this resource is the session_url that you got back in the [create session response](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/create-session.md). When an HPP Session has been disabled by the Merchant, the Consumer will get an explicit error message when using a previous link that has been distributed. If the Consumer was still on the payment page while the session was disabled, they will get a *Page Not Found* error as soon as they do an action. The value of the status of the *HPP Session* will now be *DISABLED* and this status is definitive. [Read our guide on HPP Session statuses →](https://docs.klarna.com/payments/other-products/hosted-payment-page/before-you-start/tracking-session-status.md)

| **Description** | **Disable an HPP Session** |
|----|----|
| Reference | For a full list of returned values, please read API Reference. |
| Url structure | <https: %7bendpoint%7d="" %7bsession_id%7d="" hpp="" sessions="" v1=""> |
| Operation | DELETE |
| Example | curl -X "DELETE" <https: api.klarna.com="" hpp="" sessions="" v1=""></https:><session_id> --header "Authorization: Basic <token> " |

## Examples

This operation doesn’t require any body as a request and won’t send any body as response.</token></session_id></https:>