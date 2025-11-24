# Source: https://docs.klarna.com/payments/in-store-payments/integrate-klarna-in-store/api-integration/initiate-an-in-store-payment.md

# Initiate an in-store payment

## This guide walks you through initiating a payment and letting your customers pay with Klarna in your physical store.

## Start a payment session

If you're an existing e-commerce partner, you may already be familiar with the [Klarna payments API](https://docs.klarna.com/api/payments/#operation/createCreditSession). The request and actions described in this guide use the same API, modified for the in-store scenario. To let your customer pay with Klarna in a physical store, start a new Klarna payments session by sending a `POST` request to the [`{apiURL}`](https://docs.klarna.com/api/api-urls/)`/payments/v1/sessions endpoint`.

### Sample request

To start an in-store payment session, include the following in your request:

- the `acquiring_channel` parameter set to `in_store` to indicate the payment will happen in a physical store
- the `distribution` object, including the distribution method set to `one_qr` and the URL that will receive status updates

A sample request to initiate an in-store payment session. 

### With Short Code


``` json
{
    "acquiring_channel": "in_store",
    "purchase_country": "SE",
    "purchase_currency": "SEK",
    "locale": "en-SE",
    "merchant_reference1": "ON4711",
    "order_amount": 18000,
    "order_tax_amount": 3000,
    "order_lines": [
        {
            "image_url": "https://www.exampleobjects.com/logo.png",
            "type": "physical",
            "reference": "Could be a Product Id or SKU #",
            "name": "Cool Bike",
            "quantity": 1,
            "unit_price": 20000,
            "tax_rate": 2000,
            "total_amount": 18000,
            "total_discount_amount": 2000,
            "total_tax_amount": 3000
        }
    ],
    "attachment": {
    "content_type": "application/vnd.klarna.internal.emd-v2+json",
    "body": "{\"in_store_payment\": [{\"store_info\": {\"merchant_store_id\":\"Example Shop\",\"store_terminal_id\":\"POS1232\",\"store_address\": {\"street_address\":\"drottninggatan\",\"street_number\":\"12\",\"postal_code\": \"23451\",\"city\": \"Stockholm\",\"country\": \"SE\"}}}]}"
    },
    "distribution": {
       "method": "one_qr",
       "short_code": "2005",
       "callback_urls": {
         "status_update": "https://example.com/callback"
        }
   }
}
```



### Without short code


``` json
{
    "acquiring_channel": "in_store",
    "purchase_country": "SE",
    "purchase_currency": "SEK",
    "locale": "en-SE",
    "merchant_reference1": "ON4711",
    "order_amount": 18000,
    "order_tax_amount": 3000,
    "order_lines": [
        {
            "image_url": "https://www.exampleobjects.com/logo.png",
            "type": "physical",
            "reference": "Could be a Product Id or SKU #",
            "name": "Cool Bike",
            "quantity": 1,
            "unit_price": 20000,
            "tax_rate": 2000,
            "total_amount": 18000,
            "total_discount_amount": 2000,
            "total_tax_amount": 3000
        }
    ],
    "attachment": {
    "content_type": "application/vnd.klarna.internal.emd-v2+json",
    "body": "{\"in_store_payment\": [{\"store_info\": {\"merchant_store_id\":\"Example Shop\",\"store_terminal_id\":\"POS1232\",\"store_address\": {\"street_address\":\"drottninggatan\",\"street_number\":\"12\",\"postal_code\": \"23451\",\"city\": \"Stockholm\",\"country\": \"SE\"}}}]}"
    },
    "distribution": {
       "method": "one_qr",
       "callback_urls": {
         "status_update": "https://example.com/callback"
        }
   }
}
```

## Extra merchant data

When initiating a payment session, it is required to send EMD as part of the request similar to the sample request. [This guide](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/extra-merchant-data.md) describes how to send all \[<https: #="" api="" docs.klarna.com="" extra-merchant-data="">:~:text=Array-,store_info,-object required EMD\] data in the request.

### Sending customer data

In some cases, you might want to send billing address when creating a payment session in order to improve the payment experience at the point of sale, for example by pre-filling the checkout form with information that is already know and reducing the need for the customer to manually fill in all fields.

``` json
{
    "acquiring_channel": "in_store",
    "purchase_country": "SE",
    "purchase_currency": "SEK",
    "locale": "en-SE",
    "merchant_reference1": "ON4711",
    "order_amount": 18000,
    "order_tax_amount": 3000,
    "order_lines": [
        {
            "image_url": "https://www.exampleobjects.com/logo.png",
            "type": "physical",
            "reference": "Could be a Product Id or SKU #",
            "name": "Cool Bike",
            "quantity": 1,
            "unit_price": 20000,
            "tax_rate": 2000,
            "total_amount": 18000,
            "total_discount_amount": 2000,
            "total_tax_amount": 3000
        }
    ],
    "attachment": {
    "content_type": "application/vnd.klarna.internal.emd-v2+json",
    "body": "{\"in_store_payment\": [{\"store_info\": {\"merchant_store_id\":\"Example Shop\",\"store_terminal_id\":\"POS1232\",\"store_address\": {\"street_address\":\"drottninggatan\",\"street_number\":\"12\",\"postal_code\": \"23451\",\"city\": \"Stockholm\",\"country\": \"SE\"}}}]}"
    },
    "distribution": {
       "method": "one_qr",
       "short_code": "2005",
       "callback_urls": {
         "status_update": "https://example.com/callback"
        }
   },
   "billing_address": {
       "attention": "Attn",
       "city": "Stockholm",
       "country": "SE",
       "email": "test.sam@test.com",
       "family_name": "Andersson",
       "given_name": "Sven",
       "organization_name": "string",
       "phone": "+46705465131",
       "postal_code": "12865",
       "region": "",
       "street_address": "Kungsgatan 45",
       "street_address2": "Floor 22 / Flat 2",
       "title": "Mr."
   }
}
```

In this case, please include the following to send billing address. You can refer to [create a session](https://docs.klarna.com/api/payments/#operation/createCreditSession) for a full list of supported request information.

- The billing_address object to send billing address information

## Distribution object

| Parameter | Type | Required or optional | Description |
|----|----|----|----|
| `method` | string |  |  |
| `short_code` | string | optional, populate only when short code is available | A numerical code consisting of 2–20 digits that links a payment session with the customer. The code is displayed on the customer’s device when they scan a static QR code. The cashier enters the code into the device at the till. Then, the short code is included in a POST request to the Klarna payments API. |
| `callback_urls` | object | optional | Include this object if you want to use a webhook instead of polling to get the distribution result. |
| `status_update` | string | optional | The URL to which the status updates will be sent. |

### Success response

In response to your request, you receive:

- `session_id`, a payment session identifier.
- `payment_method_categories`, an array that lists the available payment methods. This information is returned by the API, but you don’t need to take any actions related to it.
- the `distribution` object, containing `result_url` which needs to be called to receive the QR (link to Monitor the status page)

``` json
{
    "session_id" : "{session_id}",
    "payment_method_categories": [
        {
            "identifier": "klarna",
            "name": "Pay with Klarna",
            "asset_urls": {
                "descriptive": "https://x.klarnacdn.net/payment-method/…",
                "standard": "https://x.klarnacdn.net/payment-method/…"
            }
        }
    ],
    "distribution": {
        "result_url":"https://api.klarna.com/iss/v1/distributions/{session_id}"
   }
}
```

*A sample success response to initiate an in-store payment session request.*

## Error handling

The errors listed below can occur when you initialize a payment session, learn more in [Error handling guide](https://docs.klarna.com/resources/developer-tools/error-handling/error-codes-and-messages-for-klarna-payments.md). You can retrieve the error from the distribution result endpoint or by subscribing to a webhook.

| Error code | Description | Action to take |
|----|----|----|
| `BAD_REQUEST` | The shortcode should be within the limits and integers only. Otherwise any of the fields needs to be in appropriate format. | Create request with an appropriate input |
| `PERMISSION_DENIED` | API credentials are incorrect and permission is not available | Don’t retry the session and contact Klarna’s merchant support. |
| `UNKNOWN` | System error | Don’t retry the session and contact Klarna’s merchant support. |</https:>