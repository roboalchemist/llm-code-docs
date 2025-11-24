# Source: https://docs.klarna.com/payments/after-payments/order-management/more-actions/refund-allocation.md

# Refund allocation

## Read this article to learn how to correctly allocate refunds when you deliver in multiple shipments.

When you send the goods in multiple shipments or from multiple locations, you're capturing the order in parts. In these cases, we create separate invoices (payment instructions) for each shipment. For example, instead of receiving one invoice for all ordered goods at once, your customer gets individual invoices for each partial delivery. We have to pay special attention when your customer asks for a refund and returns only some of the goods. Here, we need to correctly allocate the refund amount to the specific invoice that corresponds to the shipment (capture) of the returned goods.

## The challenge

When your customers return some goods from a partially delivered order, they can expect the refund amount to be allocated to the specific invoice corresponding to that partial delivery. However, the refund is allocated to the general order and not to the specific invoice that corresponds to the shipment (capture) of the goods, causing confusion for your customers.

## The solution

We know that correct refund allocation ensures clarity for your customers, but we don't want you to bother with keeping track of capture IDs to correctly allocate refunds. Instead, you can ensure the correct refund allocation through the use of order lines. By keeping the order lines consistent between the specific capture and the refund you're making, you help us understand where to allocate the refund. Specifically, in the request body for capturing an order and in the one for [refunding an order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-and-extend-orders), you have to keep exactly the same value in the `reference` attribute of the `order_lines` parameter. This is how we can correctly allocate the refund to the right payment instruction. To help us correctly allocate the refund, you have to:

1.  [Identify the capture corresponding with the refunds.](https://docs.klarna.com/payments/after-payments/order-management/more-actions/refund-allocation.md)
2.  [Ensure the API request contains consistent order lines.](https://docs.klarna.com/payments/after-payments/order-management/more-actions/refund-allocation.md)
3.  [Request a refund through the Order management API.](https://docs.klarna.com/payments/after-payments/order-management/more-actions/refund-allocation.md)

### Identifying the capture.

The first step is to identify the specific capture that corresponds to the refunds your customer is requesting. Let’s say you have received a customer’s order for a T-shirt, a pair of jeans, and a pair of sneakers. You delivered this order in two separate shipments and [captured the order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders.md) in two separate parts:

| Capture A | Capture B |
|---------|---------|
| * Includes the T-shirt and the pair of jeans * Two order lines: a T-shirt (reference A12345) and a pair of jeans (reference A98765) | * Includes the pair of sneakers * One order line: a pair of sneakers (reference B24680) |

This is an example of Capture A, including two order lines, one per product:

``` json
{
  "captured_amount": 10000,
  "description": "Capture A, shipping part of the order",
  "order_lines": [
  {
    "reference": "A12345",
    "name": "T-shirt",
    "type": "physical",
    "quantity": 1,
    "total_amount": 3000,
    "unit_price": 3000
  },
  {
    "reference": "A98765",
    "name": "Jeans",
    "type": "physical",
    "quantity": 1,
    "total_amount": 7000,
    "unit_price": 7000
  }
  ]
}
```

Sample of a capture with two order lines. This is an example of Capture B, including one order line for a single product:

``` json
{
  "captured_amount": 10000,
  "description": "Capture B, shipping the rest of the order",
  "order_lines": [
  {
    "reference": "B24680",
    "name": "Sneakers",
    "type": "physical",
    "quantity": 1,
    "total_amount": 10000,
    "unit_price": 10000
  },
  ]
}
```

Sample of a capture with one order line. In this scenario, your customer wants to return the sneakers, so you have to pay attention to Capture B.

### Ensuring consistent order lines

Once you identified the correct capture, you have to prepare the refund and ensure you send consistent order lines in your request. Before you make an API call to refund the order, check that the request body for the refund contains order lines with exactly the same `reference` attribute as the request body for the capture (in this example, Capture B).

### Request a refund

Once you ensured you're sending consistent order lines, you're ready to go with the refund. You have to use our Order management API. Send a `POST` request to the `{apiUrl}/ordermanagement/v1/orders/{order_id}/refunds`[{apiUrl}](https://docs.klarna.com/api/ordermanagement/#operation/refundOrder)/ordermanagement/v1/orders/{order_id}/refunds endpoint and use the refund request matching the capture. This is an example of the refund request matching Capture B:

``` json
{
  "refunded_amount": 10000,
  "description": "Returning the sneakers",
  "order_lines": [
  {
    "reference": "B24680",
    "name": "Sneakers",
    "type": "physical",
    "quantity": 1,
    "total_amount": 10000,
    "unit_price": 10000
  },
  ]
}
```

Sample of a request to refund an order. For more information on the API call, see the [Refund an order](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-and-extend-orders) section.

## Conditions

Allocating refunds correctly is only possible if the orders meet the following conditions:

- The order you're refunding doesn't have any previous refunds with failed allocation.
- The sum of the order lines is exactly equal to the refunded amount.
- The refunded amount is equal to or less than the captured amount in the partial capture you're refunding. In the example above, the refunded amount corresponding to the sneakers cannot be more than the `captured_amount` in Capture B.

If your refund request doesn't meet these conditions, we'll accept the refund but we won't be able to allocate it to the right invoice.