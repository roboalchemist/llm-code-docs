# Source: https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-orders-and-manage-authorizations.md

# Refund orders and manage authorizations

## Learn how to refund and manage orders efficiently using the Klarna Order Management API.

## Refund an order

Use the Order management API to refund the items on a captured order.

When your customers return the items they bought and you need to refund that order, use this API call to credit the amount back to your customers.

The following diagram depicts how this API call works:

{{#mermaid:
sequenceDiagram
   autonumber
participant A as MERCHANT
participant B as KLARNA
A ->> B: POST /ordermanagement/v1/orders/{order_id}/refunds
note over A, B: Provide the refund amount (full or partial)
alt SUCCESSFUL
B -->> A: 201: Created includes refund_id, location
else ERROR
B -->> A: 403: correlation_id, error_code, error_message
end
}}

If you want to learn how to correctly allocate refunds when you deliver in multiple shipments, see the [Refund allocation section.](https://docs.klarna.com/payments/after-payments/order-management/more-actions/refund-allocation/)

## Refund a captured order amount

To refund the amount of an order, send a POST request to the [{apiUrl}/ordermanagement/v1/orders/{order_id}/refunds](https://docs.klarna.com/api/ordermanagement/#operation/refundOrder) endpoint.

Include the following in your request:

**Header**

- Klarna-Idempotency-Key : This header will guarantee the idempotency of the operation. The key should be unique and is recommended to be a UUID version 4. Retries of requests are safe to be applied in case of errors such as network errors, socket errors and timeouts.

**Body**

- refunded_amount (required): the total order amount to be refunded. It must be less or equal to the captured_amount from the [order capture](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders/)
- reference (optional): Internal reference to the refund. This will be included in the settlement files.
- description (optional): text to add details of the refunds. Your customers can see this description
- order_lines (optional): list of details associated with this refund. We highly recommend you send order lines as they allow us to locate the refund to the right capture (consumer invoice). Order lines are also helpful for your customers to visualize the refunded amount in the Klarna app

``` json
{
"refunded_amount": 100000000",
"reference": "9dfcd4b6-9428-4835-ad93-3720ea808608",
"description": "Description of the refund shown to the customer",
"order_lines": [
{
"image_url": "https://yourstore.example/product/headphones.png",
"merchant_data": "Some metadata",
"name": "string",
"product_identifiers": {
"brand": "Intel",
"category_path": "Electronics Store> Computers & Tablets> Desktops",
"color": "Denim blue",
"global_trade_item_number": "735858293167",
"manufacturer_part_number": "BOXNUC5CPYH",
"size": "4"
},
"product_url": "https://yourstore.example/product/headphones",
"quantity": 1,
"quantity_unit": "pcs.",
"reference": "75001",
"subscription": {
"interval": "MONTH",
"interval_count": 1,
"name": "string"
},
"tax_rate": 0,
"total_amount": 100000000,
"total_discount_amount": 0,
"total_tax_amount": 100000000,
"type": "physical",
"unit_price": 100000000
}
]
}
```

Sample of a request to refund an order.

### Success response

If the request is successful, you'll receive a `201 Created` response, including `refund_id` and `location` as HTTP response headers.

### Error response

If your request contains errors, you'll receive an error response. Make sure the order is already captured and the `order_id` is correct.

You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section.

``` json
{
"error_code": "REFUND_NOT_ALLOWED",
"error_messages": [
"Over refund is not allowed. Refund not possible."
],
"correlation_id": "7863c755-eb1b-4b24-a884-06c2368389d7"
}
```

Sample of an error response *to refund an order.*

Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/refundOrder)

## Refund with return fees

Use the Order management API to make a refund with fees when your customers want to return items.

When your customers ask for a refund and want to return the items they bought, you can charge a return fee using this API call.

Your customers are charged with this return fee at the moment of refund, meaning that we take the return fee from the refunded amount they receive.

### Conditions for charging fees

Charging the return fee is only possible if the orders meet the required conditions:

- The order is fully captured in one single capture and not in partial captures.
- The sum of the order lines is exactly equal to the refunded amount.
- The order corresponds to one of these markets:
  - Austria 🇦🇹
  - Germany **🇩🇪**
  - Denmark 🇩🇰
  - Finland 🇫🇮
  - France 🇫🇷
  - Netherlands 🇳🇱
  - Norway 🇳🇴
  - Sweden 🇸🇪
  - Italy 🇮🇹
  - Spain 🇪🇸
  - Ireland 🇮🇪
  - Portugal 🇵🇹
  - Czech Republic 🇨🇿
  - Australia 🇦🇺
  - Greece 🇬🇷

### Charge return fees

To charge return fees, you have to call the same endpoint you use for [refunding an order,](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-and-extend-orders/) but with type: `return_fee` as an additional parameter in `order_lines`.

Send a `POST` request to the [`{apiUrl}`](https://docs.klarna.com/api/ordermanagement/#operation/refundOrder)`/ordermanagement/v1/orders/{order_id}/refunds` endpoint.

Include the following in your request:

**Header**

- `Klarna-Idempotency-Key`: This header will guarantee the idempotency of the operation. The key should be unique and is recommended to be a UUID version 4. Retries of requests are safe to be applied in case of errors such as network errors, socket errors and timeouts.

**Body**

- `refunded_amount` (required): the total order amount to be refunded. It must be less or equal to the captured_amount from the [order capture](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders/)
- `reference` (optional): Internal reference to the refund. This will be included in the settlement files.
- `description` (optional): text to add details of the refunds. Your customers can see this description
- `order_lines` (required): list of details associated with this capture. You have to add an extra order line representing the return fee and set its type to return_fee

``` json
{
"refunded_amount": 9500,
"reference": "1786c73b-a2be-4d42-a9f7-ff1c4bca5ccc",
"description": "Description of the refund shown to the customer",
"order_lines": [
{
"name": "T-Shirt",
"type": "physical",
"quantity": 1,
"unit_price": 10000,
"total_amount": 10000
},
{
"name": "Return fee",
"type": "return_fee",
"quantity": 1,
"unit_price": -500,
"total_amount": -500
}
]
}
```

Sample request to refund with return fees.

You must add the parameter `type: return_fee` in the order lines to charge the return fee successfully. Adding this parameter lets your customer visualize the fee in the Klarna app.

### Success response

If the request is successful, you'll receive a `201 Created` response, including `refund_id` and `location` as HTTP response headers.

### Error response

If your request contains errors, you'll receive an error response. Make sure the order is already captured and the `order_id` in the request is correct.

You can use the `correlation_id`, and the `order_id` values to troubleshoot the call in the Merchant portal logs section.

``` json
{
"error_code": "REFUND_NOT_ALLOWED",
"error_messages": [
"Over refund is not allowed. Refund not possible."
],
"correlation_id": "7863c755-eb1b-4b24-a884-06c2368389d7"
}
```

Sample of an error response to refund with return fees.

### Remove return fees

You can also remove the charged fees added in the request explained above. For this action, you have to send a new request to [refund an order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-and-extend-orders/), including the amount previously charged as a return fee.

Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/refundOrder)

## Release order authorization

Use the Order management API to release the authorization of an order.

When you have an order that isn't fully captured and you don't plan to perform more captures on it, you should cancel it by releasing the order's authorization.

With this action, your customers won't be debited for the remaining authorized order amount. If your customers paid by card, we'll refund the remaining amount to their account.

To release the authorization of an order, send a POST request to the [`{apiUrl}`](https://docs.klarna.com/api/ordermanagement/#operation/releaseRemainingAuthorization)`/ordermanagement/v1/orders/{order_id}/release-remaining-authorization` endpoint.

Provide the `order_id` as path parameters. The `order_id` is the identifier you get in a successful response when \[ placing a new order\].

You don't need a request body for this `POST` method.

### Success response

If the request is successful, you'll receive a `204 No content` response.

### Error response

If your request contains errors, you'll receive an error response. Make sure the order is not captured or canceled and the `order_id` is correct.

You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section.

``` json
{
"error_code": "NOT_ALLOWED",
"error_messages": [
"Order is fully captured. Remaining authorization cannot be released."
],
"correlation_id": "fefd0ea8-6899-41f9-93a7-ccd125c1af86"
}
```

Sample of an error response to release an order authorization.

Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/releaseRemainingAuthorization)

## Extend payment date

Use the Order management API to extend the order’s payment due date.

When you want to give your customers more time to pay for their purchase, you have to extend the order's payment due date.

To get an extension for the payment date, follow these steps:

1.  [Get the available options](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-and-extend-orders/#step-1-get-the-available-extension-options) for extending the due date of a specific order.
2.  [Extend the due date](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-orders-and-manage-authorizations/#extend-payment-date-step-2-extend-the-payment-due-date) using one of the available options from the previous call.

As we relate every capture with an individual invoice for the customer, you can extend the payment due date per capture.

This is a paid feature. Given that the order extension increases the credit costs, we charge a fee. For more information, see the [pricing section](https://docs.klarna.com/payments/after-payments/order-management/more-actions/extend-customer-due-date-pricing/).

### Conditions

Extending the payment date is only possible for orders associated with a pay-later method, such as Pay in 30 days or Pay in 4 installments.

### Step 1: Get the available extension options

To get the available options for extending an order's payment due date, send a GET request to the [`{apiUrl}`](https://docs.klarna.com/api/ordermanagement/#operation/getOptionsForExtendDueDate)`/ordermanagement/v1/orders/{order_id}/captures/{capture_id}/extend-due-date-options` endpoint.

Provide `order_id` and `capture_id` as path parameters. The `order_id` is the identifier you get in a successful response when placing a new order, and the `capture_id` is the identifier you get when successfully capturing an order.

You don't need a request body for this `POST` method.

### Success response

If your request is successful, you'll receive a response body including `number_of_days` for the amount of days this order can be extended.

``` json
{
"currency": "usd",
"options": [
{
"amount": 0,
"number_of_days": 0
}
]
}
```

Sample of a successful response to get the extension options.

### Error response

If your request contains errors, you'll receive an error response. Ensure the `order_id` and the `capture_id` values you provided are valid and correctly formatted.

``` json
{
"correlation_id": "string",
"error_code": "string",
"error_messages": [
"string"
]
}
```

Sample of an error response to get the extension options.

You can use the `correlation_id` and the `order_id` value to troubleshoot the call in the Merchant portal logs section.

### Step 2: Extend the payment due date

To extend the payment due date for a specific order, send a `PATCH` request to the [`{apiUrl}`](https://docs.klarna.com/api/ordermanagement/#operation/extendDueDate)`/ordermanagement/v1/orders/{order_id}/captures/{capture_id}/extend-due-date-options` endpoint.

``` json
{
"number_of_days": 0
}
```

Sample of a request to extend the payment due date.

Provide one of the extension options you got as `number_of_days` from Step 1.

### Success response

If the request is successful, you'll receive a 204 No content response.

### Error response

​If your request contains errors, you'll receive an error response. Ensure the `order_id` and the `capture_id` values you provided are valid and correctly formatted.

``` json
{
"correlation_id": "string",
"error_code": "string",
"error_messages": [
"string"
]
}
```

Sample of an error response to extend the payment due date.

​You can use the `correlation_id` and the `order_id` value to troubleshoot the call in the Merchant portal logs section.

Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/extendDueDate)