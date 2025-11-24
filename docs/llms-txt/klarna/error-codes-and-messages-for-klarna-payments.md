# Source: https://docs.klarna.com/resources/developer-tools/error-handling/error-codes-and-messages-for-klarna-payments.md

# Error codes and messages for Klarna Payments

## Check out our usual error messages and what they mean

## Summary of possible errors

| **HTTPS status code** | **Error code**        |
|-----------------------|-----------------------|
| 400                   | BAD_REQUEST           |
| 400                   | BAD_VALUE             |
| 403                   | INVALID_OPERATION     |
| 403                   | MERCHANT_INACTIVE     |
| 403                   | REJECTED              |
| 404                   | NOT_FOUND             |
| 404                   | SESSION_COMPLETED     |
| 409                   | BAD_VALUE             |
| 500                   | INTERNAL_SERVER_ERROR |

## Details of possible errors

### 400 - BAD_REQUEST

`BAD_REQUEST` error could be precent in any type of request.

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[]` | The server cannot or will not process the request due to something that is perceived to be a client error. |  |

### 400 - BAD_VALUE

This is one of the most frequent errors, the**error message**will indicate which specific property needs to be reviewed and fixed. see the table below for some examples of error messages.

`BAD_VALUE` error could be present in multiple requests and depending in which operation the error occurs the customer will have a different impact during the purchase journey:

- `create_session`: Klarna's content can't be displayed, and customer is unable to use Klarna.
- `update_session`: The customer won’t be able to proceed until the session's details have been fixed.
- `create_order`: The customer proceeded with the payment or credit flow successfully, but order creation failed afterwards. Depending on the integration the customer might see the order incorrectly as completed, or the customer can be instructed to try again.
- `create_token`: The customer proceeded with the authorization flow successfully, but create_token call had invalid details, and the customer couldn't be tokenized for recurring purchases.

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[BAD_VALUE : order_lines[X].tax_rate]` | Error message on the validation criteria for the tax calculation. The tax rate indicated should be aligned with tax values shared in other properties since Klarna will perform validations on it. | See [how to handle tax in Klarna Payments](https://docs.klarna.com/payments/web-payments/additional-resources/error-handling-and-validations/tax-handling/) |
| `[BAD_VALUE : order_lines[X].total_tax_amount]` | There is an error in the tax amounts for an specific order line \[X\]. Tax amounts should add up over all order lines since Klarna will perform validations on it. | See [how to handle tax in Klarna Payments](https://docs.klarna.com/payments/web-payments/additional-resources/error-handling-and-validations/tax-handling/) |
| `[BAD_VALUE : order_tax_amount]` | There is an error in the tax amounts. total order tax amounts should add up over all order lines since Klarna will perform validations on it. | See [how to handle tax in Klarna Payments](https://docs.klarna.com/payments/web-payments/additional-resources/error-handling-and-validations/tax-handling/) |
| `[BAD_VALUE : order_lines]` | Order lines sent may be malformed, don't follow our guidelines, violate API field restrictions or completely missing. | Refer to the [Klarna payments API reference](https://docs.klarna.com/api/payments/) for details on expected formats. |
| `[BAD_VALUE : purchase_currency]` | The currency in your payment request not formatted correctly or doesn't apply for a certain locale. | locale and `currency` values in the request should be supported by Klarna. Refer to our [Klarna documentation](https://docs.klarna.com/klarna-payments/in-depth-knowledge/puchase-countries-currencies-locales/) for compatible combinations. |
| `[BAD_VALUE : billing_address.{fields}, shipping_address.{fields}]` | A field in the billing_address or shipping_address object in your payment request is not formatted correctly. | Read more about [customer data requirements](https://docs.klarna.com/klarna-payments/in-depth-knowledge/customer-data-requirements/). |
| `[BAD_VALUE : attachment.attachment]` | The attachment object is used for [EMD](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/extra-merchant-data/) (extra merchant data). This error means that the data sent in the attachment object does not follow Klarna's requirements. | See [Attachment Schema](https://docs.klarna.com/api/attachment-schema/) doc for detail documentation on formats expected for EMD. |
| `[BAD_VALUE: locale]` | The locale in your payment request is not compatible. | `locale` parameter sent in the request should follow expected format and values. Read more about [locale and language](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales/). |

If the error message indicates an issue in order amount or order lines, compare the latest successfully sent details with the details in create_order call to see what changes caused the error.

Discounts, coupons, shipping fees and taxes applied on the checkout page can sometimes cause incorrect calculations.

### 401 - UNAUTHORIZED

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[]` | Typically indicates that the credentials used for the authentication are invalid. | Review the credentials being used. If multiple credentials were created ensure you are using the latest one. See more information about [authentication](https://docs.klarna.com/api/authentication/). |

### 403 - INVALID_OPERATION

| **Error message** | **Description** | **Error Handling** |
|----|----|----|
| `[Authorization token already consumed]` | The operation is not allowed or configured for the MID. |  |
| `[Not allowed to create customer token for intent buy]` | The operation is not allowed or configured for the MID. Not all payments methods allow the creation of customer tokens. | Read more about recurring payments. |
| `[]` | The operation is not allowed or configured for the MID. |  |

### 403 - MERCHANT_INACTIVE

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[]` | The MID has not been activated. | Contact your Delivery manager or [Merchant support](https://www.klarna.com/uk/business/contact-merchant-support/) to get it active. |

### 403 - REJECTED

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Rejected]` | Authorization has not been approved by Klarna. |  |

### 404 - NOT_FOUND

`NOT_FOUND` error could be present in multiple requests and depending in which operation the error occurs the customer will have a different impact during the purchase journey:

- `update_session`: Often invisible for the customer if the merchant creates a new session for the customer directly after failed session update attempt.
- `authorize`: The customer sees an error message, and is prompted to start over.

| **Error message** | **Description** | **Error Handling** |
|----|----|----|
| `[Invalid session id]` | The session id used in the operation is not valid. Typically occurs when the session has expired, but the merchant still tries to update the session. The merchant often creates a new session for the customer automatically. | This could be due to multiple reasons as [expired sessions](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/) or IP mismatches. |
| `[Invalid authorization token]` | Typically occurs when the authorization token has expired or a new one has been created. | To fix the error, [request a new authorization token](https://docs.klarna.com/klarna-payments/integrate-with-klarna-payments/step-2-check-out/22-get-authorization/#authorize-call) or make sure you are using the most recent token. |
| `[Authorization cannot be deleted]` |  |  |

### 404 - SESSION_COMPLETED

`SESSION_COMPLETED` error could be present in `autorize` request and it is invisible to the customer.

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Session has already been completed]` | The session already has a successful order created, no pre-purchase operations allowed (such as *update_session*, *authorize() and create_order*). The error is often triggered when authorization callback is in use, but it's invisible to the customer, as redirection to order confirmation page occurs quickly after successful authorization callback. |  |

### 409 - BAD_VALUE

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Not matching fields...]` | The data shared with Klarna in a previous step (such as *create_session*, *load()*, or *authorize()*) have been modified causing the validation to fail. |  |
| `[The order has been already completed with different request body]` |  |  |

### 500 - INTERNAL_SERVER_ERROR

| **Error message** | **Description** | **Handling error** |
|----|----|----|
| `[Internal error]` Something went wrong internally. |  |  |