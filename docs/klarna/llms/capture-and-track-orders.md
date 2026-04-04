# Source: https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders.md

# Capture and track orders

## Here you find details of the calls that enable you to capture your orders and add shipping information to track them. For each call, you can find a description, technical details, and sample requests and responses.

## Capture the full order amount

Use the Order management API to fully capture an order. When you fulfill the order (for example, you have sent the products to your customer), you need to capture the total amount for the items through this API call. Capturing the full order amount triggers the payments we send to your bank account based on your contract. The following diagram depicts how this API call works:

{{#mermaid:
sequenceDiagram
    autonumber
participant A as MERCHANT
participant B as KLARNA
A ->> B: POST /ordermanagement/v1/orders/{order_id}/captures
note over A, B: Provide the capture amount (full or partial)
alt SUCCESSFUL
B -->> A: 201: Created includes capture_id, location
else ERROR
B -->> A: 403: correlation_id, error_code, error_message
end
}} You can use the same endpoint for making full and partial captures. For a full capture, you send the total order amount. For a partial capture, you only send the order amount corresponding to the items you shipped. To capture the full order amount, send a POST request to the [{apiUrl}](https://docs.klarna.com/api/ordermanagement/#operation/captureOrder)/ordermanagement/v1/orders/{order_id}/captures endpoint. Include the following in your request: **Header**

- Klarna-Idempotency-Key : This header will guarantee the idempotency of the operation. The key should be unique and is recommended to be a UUID version 4. Retries of requests are safe to be applied in case of errors such as network errors, socket errors and timeouts.

**Body**

- captured_amount (required): the total order amount to be captured. It must be equal to the order_amount from the \[ order creation\]
- reference (optional): Internal reference to the capture. This will be included in the settlement files.
- description (optional): Description of the capture shown to the customer.
- order_lines (optional): list of details associated with this capture. This is recommended if you want to show capture details in the Klarna's app
- shipping_info (optional): shipping details such as company and tracking number. If you're shipping physical goods, you need to have shipping information available at this point. For more information, see the \[ Add shipping information section\].

``` json
{
  "captured_amount": 6000,
  "reference": "c9a94cf1-7126-4f55-92fa-4d34f416ed7f",
  "description": "Shipped the full order",
  "order_lines": [
    {
      "type": "physical",
      "reference": "123050",
      "name": "Tomatoes",
      "quantity": 10,
      "quantity_unit": "kg",
      "unit_price": 600,
      "tax_rate": 2500,
      "total_amount": 6000,
      "total_tax_amount": 1200
    }
  ],
  "shipping_info": [
    {
      "shipping_company": "DHL US",
      "tracking_number": "1234567890",
      "return_shipping_company": "UPS",
      "return_tracking_number": "112233445566778899"
    }
  ]
}
```

Sample request to capture an order.

### Success response

If the request is successful, you'll receive a `201 Created` response including `capture_id` and `location` as HTTP response headers.

### Error response

If your request contains errors, you'll receive an error response. Make sure the `order_id` is correct. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section.

``` json
{
  "correlation_id": "66782175-ae05-44fc-9eb3-eeceadbad271",
  "error_code": "NO_SUCH_ORDER",
  "error_messages": [
    "string"
  ]
}
```

Sample of an error response to capture an order. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/captureOrder)

## Capture part of the order amount

Use the Order management API to partially capture an order. When you partially fulfill the order (for example, you have sent some of the products to the customer but not all of them), you need to capture the amount for the sent items through this API call. You can use the same endpoint for making full and partial captures. For a full capture, you send the total order amount. For a partial capture, you only send the order amount corresponding to the items you sent. To capture a part of the order amount, send a POST request to the [{apiUrl}](https://docs.klarna.com/api/ordermanagement/#operation/captureOrder)`{apiUrl}/ordermanagement/v1/orders/{order_id}/captures` endpoint. Include the following in your request: **Header**

- `Klarna-Idempotency-Key` : This header will guarantee the idempotency of the operation. The key should be unique and is recommended to be a UUID version 4. Retries of requests are safe to be applied in case of errors such as network errors, socket errors and timeouts.

**Body**

- `captured_amount` (required): the partial order amount to be captured. It must be less than the total order_amount
- `reference` (optional): Internal reference to the capture. This will be included in the settlement files.
- `description` (optional): Description of the capture shown to the customer.
- `order_lines` (optional): list of details associated with this capture
- `shipping_info` (optional): shipping details such as company and tracking number. If you're shipping physical goods, you need to have shipping information available at this point. For more information, see the \[ Add shipping information section\].

``` json
{
  "captured_amount": 6000,
  "reference": "2027d87e-c394-4b22-9cfd-f51f79482793",
  "description": "Shipped the full order",
  "order_lines": [
    {
      "type": "physical",
      "reference": "123050",
      "name": "Tomatoes",
      "quantity": 10,
      "quantity_unit": "kg",
      "unit_price": 600,
      "tax_rate": 2500,
      "total_amount": 6000,
      "total_tax_amount": 1200
    }
  ],
  "shipping_info": [
    {
      "shipping_company": "DHL US",
      "tracking_number": "1234567890",
      "return_shipping_company": "UPS",
      "return_tracking_number": "112233445566778899"
    }
  ]
}
```

Sample of a request to partially capture an order.

### Success response

If the request is successful, you'll receive a `201 Created` response including `capture_id` and `location` as HTTP response headers.

### Error response

If your request contains errors, you'll receive an error response. Make sure the `order_id` is correct. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section.

``` json
{
  "correlation_id": "66782175-ae05-44fc-9eb3-eeceadbad271",
  "error_code": "NO_SUCH_ORDER",
  "error_messages": [
    "string"
  ]
}
```

Sample of an error response to partially capture an order. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/captureOrder)

## Check the details of a capture

Use the Order management API to check the details of a capture. When you want to check the details of a capture, this API call provides you with capture information like shipping info, order lines, capture id, amount, and date.

### Retrieve capture details

To check the capture details, send a `GET` request to the [{apiUrl}](https://docs.klarna.com/api/ordermanagement/#operation/getCapture)`{apiUrl}/ordermanagement/v1/orders/{order_id}/captures/{capture_id}` endpoint. Provide the `order_id` and the specific `capture_id` you want to know about. The `order_id` is the identifier you get in a successful response when placing a new order, and the `capture_id` is the identifier you get when successfully capturing an order.

### Success response

In response to your call, you receive a data object containing the capture details.

``` json
{
  "capture_id": "5b33ed47-79d0-4d76-99ea-4afaa7c8e552",
  "klarna_reference": "4K7Q6QF6-1",
  "captured_amount": 6000,
  "captured_at": "2017-01-10T10:31:17.973Z",
  "description": "Shipped the full order",
  "order_lines": [
    {
      "reference": "123050",
      "type": "physical",
      "quantity": 10,
      "quantity_unit": "kg",
      "name": "Tomatoes",
      "total_amount": 6000,
      "unit_price": 600,
      "total_discount_amount": 0,
      "tax_rate": 2500,
      "total_tax_amount": 1200
    }
  ],
  "refunded_amount": 0,
  "billing_address": {
    "given_name": "John",
    "family_name": "Doe",
    "title": "Mr",
    "street_address": "123 Fake St",
    "postal_code": "12345",
    "city": "New York",
    "region": "NY",
    "country": "US",
    "email": "john@doe.com",
    "phone": "123456"
  },
  "shipping_address": {
    "given_name": "John",
    "family_name": "Doe",
    "title": "Mr",
    "street_address": "123 Fake St",
    "postal_code": "12345",
    "city": "New York",
    "region": "NY",
    "country": "US",
    "email": "john@doe.com",
    "phone": "123456"
  },
  "shipping_info": [
    {
      "shipping_company": "DHL US",
      "tracking_number": "1234567890",
      "return_shipping_company": "UPS",
      "return_tracking_number": "112233445566778899"
    }
  ]
}
```

Sample of a success response to check capture details.

### Error response

If your request contains errors, you'll receive an error response. Ensure the `order_id` and the `capture_id` values you provided are valid and correctly formatted.

``` json
{
  "error_code": "NO_SUCH_ORDER",
  "error_messages": [
    "Order 7849fd84-47dc-4919-a7ce-47b9f46156f cannot be found"
  ],
  "correlation_id": "f072554f-ef99-4b21-85da-633355aab998"
}
```

Sample of an error response to check capture details. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/getCapture)

## Add shipping information to capture

Use the Order management API to add shipping information to an order and enable delivery tracking. When you want to add shipping details to an order, you have two ways to attach this information. One option is to send the shipping details in the request body when [capturing an order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders.md). Another option is to send the shipping details after capturing the order, as explained in this API call. By adding the shipping details to an order, you make this information available to your customers so that they can keep [track of the delivery](https://docs.klarna.com/payments/after-payments/order-management/more-actions/delivery-tracking.md). To add the shipping information to a captured order, send a `POST` request to the [{apiUrl}](https://docs.klarna.com/api/ordermanagement/#operation/appendShippingInfo)`{apiUrl}/ordermanagement/v1/orders/{order_id}/captures/{capture_id}/shipping-info` endpoint. Provide `order_id` and `capture_id` as path parameters. The `order_id` is the identifier you get in a successful response when placing a new order, and the `capture_id` is the identifier you get when successfully capturing an order. Include the following required body parameters in your request:

- `return_shipping_company`: name of the shipping company for the return shipment
- `return_tracking_number`: tracking number that identifies the return shipment
- `return_tracking_uri`: URL where the customer can track the return shipment
- `shipping_company`: logistics company (carrier) managing the delivery. For more information, see the [carrier list.](https://docs.klarna.com/payments/after-payments/order-management/more-actions/klarna-carrier-partner-list.md)
- `shipping_method`: method for delivering the goods
- `tracking_number`: tracking number that identifies the shipment
- `tracking_uri`: URI where the customer can track their shipment

``` json
{
  "shipping_info": [
    {
      "return_shipping_company": "DHL US",
      "return_tracking_number": "93456415674545679888",
      "return_tracking_uri": "http://shipping.example/findmypackage?93456415674545679888",
      "shipping_company": "DHL US",
      "shipping_method": "Home",
      "tracking_number": "63456415674545679874",
      "tracking_uri": "http://shipping.example/findmypackage?63456415674545679874"
    }
  ]
}
```

Sample request to add shipping information. You can add shipping information for two different items in the same call. For example, suppose a single order includes two packages associated with two different shipments and tracking numbers; in that case, you have to send the `shipping_info` details for each item. You can learn more about shipping companies in the [Carrier partner section](https://docs.klarna.com/payments/after-payments/order-management/more-actions/klarna-carrier-partner-list.md).

### Success response

If your request is successful, you'll receive a `204 No content` response.

### Error response

If your request contains errors, you'll receive an error response. Ensure the `order_id` and the `capture_id` values you provided are valid and correctly formatted. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section.

``` json
{
  "error_code": "NO_SUCH_ORDER",
  "error_messages": [
    "Order 7849fd84-47dc-4919-a7ce-47b9f46156f cannot be found. Shipping info cannot be added to capture 32904e4c-61d2-400e-9b77-b4a45d612."
  ],
  "correlation_id": "f072554f-ef99-4b21-85da-633355aab998"
}
```

Sample of an error response to add shipping information. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/appendShippingInfo)

## Send customer communications

Use the Order management API to trigger a new send out of customer communication. When you want to inform your customers about changes in their orders, use this API call to trigger an email to the customer with the latest details. This is also useful when your customer didn't receive the payment instructions or invoice as expected, and you want to send the information.

### Trigger customer communications

To trigger the send out of customer communications, send a `POST` request to the [{apiUrl}](https://docs.klarna.com/api/ordermanagement/#operation/triggerSendOut)`{apiUrl}/ordermanagement/v1/orders/{order_id}/captures/{capture_id}/trigger-send-out` endpoint. Provide `order_id` and `capture_id` as path parameters. The `order_id` is the identifier you get in a successful response when placing a new order, and the `capture_id` is the identifier you get when successfully capturing an order. You don't need a request body for this `POST` method.

### Success response

If the request is successful, you'll receive a `204 No content` response.

### Error response

If your request contains errors, you'll receive an error response. Ensure the `order_id` and the `capture_id` values you provided are valid and correctly formatted.

``` json
{
  "error_code": "NO_SUCH_ORDER",
  "error_messages": [
    "Order 7849fd84-47dc-4919-a7ce-47b9f46156f cannot be found."
  ],
  "correlation_id": "f072554f-ef99-4b21-85da-633355aab998"
}
```

Sample of an error response to send customer communications. ​You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/triggerSendOut)