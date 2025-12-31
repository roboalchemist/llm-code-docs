# Source: https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/view-and-change-orders.md

# View and change orders

## Learn about the details of the calls that let you view and edit your orders. For each call, you can find a description, technical details, and sample requests and responses.

## Check the details of an order

Use the Order management API to check the details of an order. When you want to check the details of an order, this API call provides you with order information like address, date, amount, purchase country, and status.

### Retrieve order details

To check the order details, send a `GET` request to the `{apiUrl}/ordermanagement/v1/orders/{order_id}` endpoint. Provide the order id you want to revise as an `{order_id}` path parameter. The `order_id` is the identifier you get in a successful response when placing a new order. You can check these details for up to three years after an order is created.

### Success response

In response to your call, you receive a data object containing the order details.

``` json
{
  "order_id": "7849fd84-47dc-4919-a7ce-xxxxxxxxxx",
  "status": "CAPTURED",
  "fraud_status": "ACCEPTED",
  "order_amount": 200,
  "original_order_amount": 200,
  "captured_amount": 200,
  "refunded_amount": 0,
  "remaining_authorized_amount": 0,
  "purchase_currency": "PLN",
  "locale": "pl-PL",
  "order_lines": [
    {
      "reference": "",
      "type": "physical",
      "quantity": 1,
      "quantity_unit": "",
      "name": "dress",
      "total_amount": 200,
      "unit_price": 200,
      "total_discount_amount": 0,
      "tax_rate": 0,
      "total_tax_amount": 0
    }
  ],
  "klarna_reference": "20S0XXXX",
  "billing_address": {
    "given_name": "Test",
    "family_name": "Person-pl",
    "title": "",
    "street_address": "Ul. Górczewska 124",
    "street_address2": "",
    "postal_code": "01-460",
    "city": "Warszawa",
    "region": "",
    "country": "PL",
    "email": "customer@email.pl",
    "phone": "+48795222223"
  },
  "created_at": "2022-07-08T09:48:16.680Z",
  "purchase_country": "PL",
  "expires_at": "2022-08-05T00:00:00.000Z",
  "captures": [
    {
      "capture_id": "32904e4c-61d2-400e-9b77-XXXXXX",
      "klarna_reference": "20S0XXXX-1",
      "captured_amount": 200,
      "captured_at": "2022-07-08T09:48:17.738Z",
      "description": "",
      "order_lines": [],
      "refunded_amount": 0,
      "billing_address": {
        "given_name": "Test",
        "family_name": "Person-pl",
        "title": "",
        "street_address": "Ul. Górczewska 124",
        "street_address2": "",
        "postal_code": "01-460",
        "city": "Warszawa",
        "region": "",
        "country": "PL",
        "email": "customer@email.pl",
        "phone": "+48795222223"
      }
  ],
  "refunds": [],
  "initial_payment_method": {
    "type": "INVOICE",
    "description": "Pay later"
  }
}
```

Sample of a successful response to check order details.

### Error response

If the order id in your request is invalid, you get an error response. Ensure the `order_id` value you provided is correctly formatted. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs app section.

``` json
{
  "error_code": "INVALID_ORDER_ID",
  "error_messages": [
    "Order ID must be a valid UUID."
  ],
  "correlation_id": "dd482985-2e0f-415d-9f30-74ce93e7e68e"
}
```

Sample of an error response to check order details. Ready to send this request? See the [API reference of this call](https://docs.klarna.com/api/ordermanagement/#operation/getOrder).

## Update order amount

Use the Order management API to update the total amount of an order before it is captured, canceled, or expired. When your customer contacts you to change, add, or remove a product from the order and you need to update the total order amount, this API call enables you to make the required changes. The updated amount replaces the original order amount, including the order lines if you sent them when creating an order. The following diagram depicts how this API call works:

{{#mermaid:
sequenceDiagram
autonumber
participant A as MERCHANT
participant B as KLARNA
A ->> B: PATCH /ordermanagement/v1/orders/{order_id}/authorization
note over A, B:  order_amount (required) <br> description (optional) <br> order_lines (optional)
alt SUCCESSFUL
B -->> A: 204: No content
else ERROR
B -->> A: 403: correlation_id, error_code, error_message
end
}}

### Conditions for updating

You can only update the amount if the order meets the following conditions:

- The order isn’t fully captured, canceled, or expired.
- For increasing an authorized amount, we run a second risk assessment or credit lookup on the customer. If the update is rejected following the assessment, your customer has to place a new order in your online store for the new items.
- Only certain payment methods support increasing the authorized amount, as shown in the table below:

| Supported payment method | Identifier   | Available markets               |
|--------------------------|--------------|---------------------------------|
| Pay later                | INVOICE      | All (excluding CH)              |
| Pay later                | B2B_INVOICE  | All (excluding CH)              |
| Base account             | BASE_ACCOUNT | All (excluding CH)              |
| Pay now                  | DIRECT_DEBIT | All (excluding CH)              |
| Fixed amount             | FIXED_AMOUNT | AT, DE, DK, FI, FR, NL, NO & SE |

To update the order amount, send the updated order details in a PATCH request to the {apiUrl}/ordermanagement/v1/orders/{order_id}/authorization endpoint. The `order_id` is the identifier you get in a successful response when placing a new order. Include the following in your request:

- order_amount (required): the new amount for the order. If you’re decreasing the order amount, this has to be less than the current authorized amount. If you’re increasing the order amount, this has to be more than the current authorized amount
- description (optional): text to add details
- order_lines (optional): the new order lines that will replace the existing ones

``` json
{
  "order_amount": 6000,
  "description": "",
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
  ]
}
```

Sample request to update the order amount. We recommend you always send updated order lines to improve the customer experience. The order lines can later help your customer visualize their purchase in the Klarna app and in the invoice. The original order lines will be deleted if you don't send order lines in this call.

### Success response

If the request is successful, the order amount is updated, and you'll receive a `204 No content` response.

### Error response

If your request contains errors, you'll receive an error response. Make sure your request meets the [conditions for updating the order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/view-and-change-orders/#update-order-amount-conditions-for-updating) and the parameters are correct. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal Logs section.

``` json
{
  "error_code": "NOT_ALLOWED",
  "error_messages": [
    "Update not allowed."
  ],
  "correlation_id": "a3183112-74bc-44ac-9453-51af2577d717"
}
```

Sample of an error response to update order amount. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/updateAuthorization)

## Update merchant references

Use the Order management API to update the order ID (merchant references). When you want to use your own order ID or make any change to the order ID we provide, you have to send an API call to update the merchant references. A merchant reference is the order number you assign to the order in your system, different from the default one we provide when creating the order. Your customers can use the merchant reference identifier to inquire about the purchase they made in your store. When you update the merchant reference, we don't create a new Klarna `order_id.` The merchant reference is the `order_id` from your system. To update the merchant references, send the updated references in a `PATCH` request to the `apiUrl}/ordermanagement/v1/orders/{order_id}/merchant-references`. The `order_id` is the identifier you get in a successful response when placing a new order.

``` json
{
    "merchant_reference1": "15632423",
    "merchant_reference2": "special order"
}
```

Sample request to update merchant references. You can update one or both references (`merchant_reference1` and `merchant_reference2`). You can also clear a reference by setting its value to "" (empty string). You can use either one or both merchant references. The parameter `merchant_reference1` is the order id from your system.

### Success response

If the request is successful, the merchant reference is updated, and you'll receive a 204 No content response.

### Error response

If your request contains errors, you'll receive an error response. Make sure the `order_id` is correct. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the [Merchant portal Logs](https://docs.klarna.com/resources/business-tools/merchant-portal-guide/payments/) section.

``` json
{
  "error_code": "NO_SUCH_ORDER",
  "error_messages": [
    "Order cannot be found. Merchant references cannot be updated."
  ],
  "correlation_id": "17c50e6c-c79d-4174-9369-4b58bca2d2ab"
}
```

Sample of an error response to update merchant references. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/updateMerchantReferences)

## Update customer address

Use the Klarna order management API to update your customer's shipping address. When your customer wants to change their shipping address, you have to send an API request to change the address associated with that order. After you update this information, the customer undergoes another credit check. You can’t update the billing address anymore due to changes in our risk assessment. To update the customer's shipping address, send the updated addresses in a `PATCH` request to the `{apiUrl}/ordermanagement/v1/orders/{order_id}/customer-details`. The `order_id` is the identifier you get in a successful response when placing a new order. To clear a field, set its value to “” (empty string). However, you can't clear mandatory fields.  Refer to the [Order management API](https://docs.klarna.com/api/ordermanagement/#operation/updateConsumerDetails) reference to learn which fields are mandatory.

``` json
{
  "shipping_address": {
    "street_address": "123 Fake St",
    "postal_code": "12345",
    "city": "New York",
    "region": "NY",
    "country": "US"
  }
}
```

Sample request to update the customer's shipping address.

### Success response

If the request is successful, the order is updated, and you'll receive a `204 No content` response.

### Error response

If your request contains errors, you'll receive an error response. It can be due to our risk assessment. Also, make sure the `order_id` is correct. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal Logs section.

``` json
{
  "error_code": "NOT_ALLOWED",
  "error_messages": [
    "Billing address cannot be updated for user account order. Customer details cannot be updated."
  ],
  "correlation_id": "b1fbf280-ea6e-4aee-a6ea-58b4b458ef47"
}
```

Sample of an error response to update customer address. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/updateConsumerDetails)

## Add shipping information to order

Use the Order management API to add shipping information to an order and enable delivery tracking. When you want to add shipping details to an order, you can send the shipping details after creating the order, as explained in this API call. This call can be used for a better customer experience when shipping information is available before capturing the order. By adding the shipping details on order level, you make this information available to your customers so that they can keep [track of the delivery](https://docs.klarna.com/payments/after-payments/order-management/more-actions/delivery-tracking/). To add the shipping information to an order, send a `POST` request to the `{apiUrl}/ordermanagement/v1/orders/{order_id}/shipping-info` endpoint. Provide `order_id` as path parameter. The `order_id` is the identifier you get in a successful response when placing a new order. Include the following required body parameters in your request:

- `return_shipping_company`: name of the shipping company for the return shipment
- `return_tracking_number`: tracking number that identifies the return shipment
- `return_tracking_uri`: URL where the customer can track the return shipment
- `shipping_company`: logistics company (carrier) managing the delivery. For more information, see the [carrier list.](https://docs.klarna.com/payments/after-payments/order-management/more-actions/klarna-carrier-partner-list/)
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

Sample request to add shipping information. You can add different shipping information for different items in the same call. For example, suppose a single order includes two packages associated with two different shipments and tracking numbers; in that case, you have to send the `shipping_info` details for each item. You can learn more about shipping companies in the [Carrier partner section](https://docs.klarna.com/payments/after-payments/order-management/more-actions/klarna-carrier-partner-list/).

### Success response

If your request is successful, you'll receive a `204 No content` response.

### Error response

If your request contains errors, you'll receive an error response. Ensure the `order_id` value you provided is valid and correctly formatted. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant Portal logs section.

``` json
{
  "error_code": "NO_SUCH_ORDER",
  "error_messages": [
    "Order 7849fd84-47dc-4919-a7ce-47b9f46156f cannot be found. Shipping info cannot be added to order 7849fd84-47dc-4919-a7ce-47b9f46156f."
  ],
  "correlation_id": "f072554f-ef99-4b21-85da-633355aab998"
}
```

Sample of an error response to add shipping information. Ready to send this request? See the [API reference of this call](https://docs.klarna.com/api/ordermanagement/#operation/appendOrderShippingInfo).

## Cancel an order

Use the Order management API to cancel uncaptured orders. When your customers don't want to proceed with the purchase and need to cancel their order before you capture it, send an API call to cancel the authorization. When you cancel the order, we release the authorized amount and you can't make further updates to the order. To successfully cancel the order, don’t capture any items listed in it. The following diagram depicts how this API call works:

{{#mermaid:
sequenceDiagram
    autonumber
    
    participant A as KLARNA
    participant B as MERCHANT
    
    B ->> A: POST orders/{order_id}/cancel
alt SUCCESSFUL
    A -->> B: 204: No content
else ERROR
    A -->> B: 403: correlation_id, error_code, error_message
end
}} To cancel an authorized order, send a `POST` request to the `{apiUrl}/ordermanagement/v1/orders/{order_id}/cancel`. The order_id is the identifier you get in a successful response when placing a new order. You don't need a request body for this `POST`method.

### Success response

If the request is successful, the order is canceled, and you'll receive a 204 No content response.

### Error response

If your request contains errors, you'll receive an error response. It can be because the order has captures or is closed.

``` json
{
  "error_code": "CANCEL_NOT_ALLOWED",
  "error_messages": [
    "Order has previous captures. Cancel not possible."
  ],
  "correlation_id": "95ccbcb1-8963-4569-b721-1a354"
}
```

Sample of an error response to cancel an order. Make sure the `order_id` is correct. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal Logs section. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/cancelOrder)

## Acknowledge your Klarna Payment orders

Use the Order management API to acknowledge your Klarna Payment orders. When you integrate our \[ Klarna Payment solution\], you’ll receive a push notification anytime your customers use Klarna in your store. Upon receiving this notification, you let us know that you're aware of the order by calling our order acknowledgment endpoint. This step is required if you're integrating Klarna Payment into your online business. To verify that the notification you receive is authentic, we recommend \[ checking the order details\] before taking further action. To acknowledge an order, send a `POST` request to the `{apiUrl}/ordermanagement/v1/orders/{order_id}/acknowledge endpoint`. The `order_id` is the identifier you get in a successful response when placing a new order. You don't need a request body for this `POST` method. In case of same-day shipping, you can acknowledge your Klarna Payment orders by capturing them.

### Success response

If the request is successful, you'll receive a 204 No content response.

### Error response

If your request contains errors, you'll receive an error response. Make sure the `order_id` is correct. You can use the `correlation_id` and the `order_id` values to troubleshoot the call in the Merchant portal logs section.

``` json
{
  "error_code": "NO_SUCH_ORDER",
  "error_messages": [
    "Order 7849fd85-47dc-4919-a7ce-47b9f461562f cannot be found. Acknowledgement not possible."
  ],
  "correlation_id": "c56002ca-81ee-436a-b213-093e5afe75d3"
}
```

Sample of an error response to acknowledge your Klarna Payment orders. Ready to send this request? See the [API reference of this call.](https://docs.klarna.com/api/ordermanagement/#operation/acknowledgeOrder)