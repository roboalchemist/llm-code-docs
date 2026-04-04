# Overcharge handling

In PSD2 rules, an overcharge is when a customer is charged an amount that is more than what they agreed to pay for a product or service. The payment service provider applies strong customer authentication (SCA) to the final amount of the transaction or declines the transaction if the final amount is higher than the amount the buyer agreed to when initiating the transaction. PayPal defines SCA as re-authorization in this case. For more information, see [New overcapture requirements](https://www.paypal.com/us/cshelp/article/new-overcapture-requirements-psd2-help954). If you charge more than the amount the buyer has approved to pay during checkout, the Capture Order API returns a `PAYER_ACTION_REQUIRED` error. The API provides a URL redirecting the buyer to re-approve the new amount.

## How it works

1. The payer checks out and approves the amount presented on PayPal pages.
2. A higher amount than the payer approved is authorized and captured.
3. A `PAYER_ACTION_REQUIRED` error is returned.
4. Optional: Use the [Confirm Payment Source API](/docs/api/orders/v2/#orders_confirm) to provide a `return_url` or `cancel_url`. The API can also block shipping address changes in which `"shipping_preferences=SET_PROVIDED_ADDRESS"`.
5. Redirect the buyer to the `payer-action` URL.
6. The buyer approves the higher amount and is redirected to the return URL.
7. The order is captured.

### Integration

The flow chart shows the following integration steps:

- Create an order with the [Orders V2 API](/docs/api/orders/v2/#orders_create/).
- The smart button redirects the buyer to PayPal.
- The buyer approves the order on the PayPal checkout pages.
- The PayPal checkout window closes. The buyer is returned to merchant’s checkout.
- The buyer selects a shipping method and confirms other details.
- Use the [Patch Order API](/docs/api/orders/v2/#orders_patch/) to update the shipping costs, shipping address, and other details.
- Capture the order. For more information on how to capture an order, see [Orders V2 API](/docs/api/orders/v2/#orders_create/).
- If capture fails with the error, `http422 PAYER_ACTION_REQUIRED`, redirect the buyer to PayPal using the `payer-action` URL.
- Buyer re-approves the order and is redirected to the return URL.
- Capture the order. For more information on how to capture an order, see [Orders V2 API](/docs/api/orders/v2/#orders_create/).

![swimlanes-749986c097b759ed856f4fdfa990cc0b.png](https://www.paypalobjects.com/devdoc/swimlanes-749986c097b759ed856f4fdfa990cc0b.png)

## Sample request - Patch Order

```curl
[
  {
    "op": "replace",
    "path": "/purchase_units/@reference_id=='default'/amount",
    "value": {
      "currency_code": "USD",
      "value": "101",
      "breakdown": {
        "item_total": {
          "currency_code": "USD",
          "value": 1.00
        },
        "shipping": {
          "currency_code": "USD",
          "value": 100.00
        }
      }
    }
  }
]
```

The request returns the `HTTP 204` status code.

## Sample response - successful capture

```curl
{
  "id": "5KM89009KL896372M",
  "intent": "CAPTURE",
  "status": "COMPLETED"
}
```

An overcapture error will give you an `HTTP 422` error code response, which means that payer action is needed.

## Sample response - overcapture error

```curl
{
  "name": "UNPROCESSABLE_ENTITY",
  "details": [
    {
      "issue": "PAYER_ACTION_REQUIRED",
      "description": "Payer needs to perform the following action before proceeding with payment."
    }
  ],
  "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
  "debug_id": "9495b4f46e3ff",
  "links": [
    {
      "href": "https://developer.paypal.com/docs/api/orders/v2/#error-PAYER_ACTION_REQUIRED",
      "rel": "information_link",
      "method": "GET"
    },
    {
      "href": "https://www.sandbox.paypal.com/checkoutnow?token=XYZ",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```

Set the `shipping_preference` to `SET_PROVIDED_ADDRESS` to confirm the payment source.

You need to pass `return_url` and `cancel_url` if you don't provide them in the Create Order API call.

## Sample request - confirm payment source

```curl
{
  "payment_source": {
    "paypal": {
      "experience_context": {
        "payment_method_preference": "IMMEDIATE_PAYMENT_REQUIRED",
        "shipping_preference": "SET_PROVIDED_ADDRESS",
        "user_action": "PAY_NOW",
        "return_url": "https://example.com/returnUrl",
        "cancel_url": "https://example.com/cancelUrl"
      }
    }
  }
}
```