# Source: https://docs.klarna.com/resources/developer-tools/testing-payments/test-cases.md

# Test cases

## In this section, you can find different scenarios for testing Klarna’s payment and checkout flows.

## End-to-end test cases

Test your Klarna integration by following the steps for each of the cases below. If a test case or a step doesn't apply to your store, for example, you don't offer partial refunds, skip the test case.

The cases cover 4 main stages of the order lifecycle:

1.  In the purchase stage, the customer adds items to the cart, proceeds to checkout, and places an order, either in the full amount or with a discount. While testing, you perform the steps in this stage. In real-life scenarios, your customer does so.
2.  In the pre-shipment stage, you cancel orders that can't be fulfilled.
3.  In the shipment stage, you ship the items to the customer, as well as capture the items in your system and in Klarna.
4.  In the post-shipment stage, the customer returns the items and you refund the full order amount or a part of it.

Here are some things to keep in mind when you test:

- You can verify the results in **Orders**in the Merchant portal.
- The manual order management steps in the Merchant portal are available only if your Klarna integration isn't linked to any external systems, as the order status in the Merchant portal isn't synchronized with the external systems.
- Test cases 1–8 walk you through checking the basic order details in the Merchant portal's **Orders**.
- You can also [test your integration's richness](https://docs.klarna.com/resources/developer-tools/testing-payments/test-cases/#test-the-integration-richness) and validate some optional order details using **Logs** in the playground Merchant portal. Keep the API reference open as it will help you to understand the details in the logs.
- In all test cases, use Klarna’s [sample customer data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/) for the market you are testing.
- Make sure to use your test (playground) environment API credentials. Your production keys won't work in playground.

Happy testing!

Don't use any real-life data when testing. Instead, use the [sample customer data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/) and [sample payment data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-payment-data/).

## Test case 1: Place, fully capture, and fully refund an order

This test case lets you test placing an order that contains 1 item, capturing the order in full, and processing a refund for the order returned by your customer.

### Purchase stage

In the first stage, you place an order.

1.  Add a product to the cart and go to checkout.
2.  Place the order, choosing Klarna as the payment method. Verify that you're redirected to the order confirmation page. The order is now created in your system and in Klarna.
3.  Verify the order was correctly created. Log into the Merchant portal and go to **Orders**.
4.  Search for your order using the search bar, then click the link in the Klarna reference column to view the order details.
5.  On the **Order lines** tab, check that the **Product name**, **Unit price**, **Tax**, and **Amount** are correct.

### Shipment stage

In the second stage, the goods are shipped to the customer and you capture the order to receive a payout for the items sold.

1.  In your system, capture all order items. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [capture the order in the Merchant portal](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/capture-and-track-orders/).
2.  Verify the capture in the Merchant portal. Go to **Orders** and check if the order's status is *Fully Captured*.

### Post-shipment stage

In the final stage, the customer returns the order and you refund the order amount back to the customer.

1.  In your system, refund all the order items. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [refund the items in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/refund-an-order/).
2.  Verify the refund in the Merchant portal. Go to **Orders** and check if the order's status contains two labels: *Fully Captured* and *Fully Refunded*. Also, verify that the refunded amount and the remaining amount to be paid are correct.

## Test case 2: Place, fully capture, and partially refund an order

This test case lets you test placing an order that contains 2 items, capturing the order in full, and processing a refund for 1 out of 2 items.

In the process, you'll verify that the cart is being updated correctly when you navigate between the checkout and the product pages.

### Purchase stage

In the first stage, you place an order.

1.  Add a product to the cart and go to checkout.
2.  Return to the store and add another product to the cart.
3.  Go to checkout again.
4.  Place the order, choosing Klarna as the payment method. The order is now created in your system and in Klarna.
5.  Verify the order was correctly created. Log into the Merchant portal and go to **Orders**.
6.  Search for your order using the search bar, then click the link in the Klarna reference column to view the order details.
7.  On the **Order lines** tab, check that the **Product name**, **Unit price**, **Tax**, and **Amount** are correct.

### Shipment stage

In the second stage, the goods are shipped to the customer and you capture the order to receive a payout for the items sold.

1.  In your system, capture all order items. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [capture the order in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/capture-an-order/).
2.  Verify the capture in the Merchant portal. Go to **Orders** and check if the order's status is *Fully Captured*.

### Post-shipment stage

In the final stage, the customer returns 1 out of 2 items from the order and you refund the item amount back to the customer.

1.  In your system, refund 1 of the order items. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [refund the item in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/refund-an-order/).
2.  Verify the refund in the Merchant portal. Go to **Orders** and check if the order's status contains two labels: *Fully Captured* and *Partially Refunded*. Also, verify that the refunded amount and the remaining open amount to be paid are correct.

## Test case 3: Place, partially capture an order, and release the remaining authorization

This test case lets you test placing an order that contains 2 items, capturing 1 out of 2 order items, and releasing the authorized amount for the other item that can't be shipped.

### Purchase stage

In the first stage, you place an order.

1.  Add a product to the cart and go to checkout.
2.  Return to the store and add another product to the cart.
3.  Go to checkout again.
4.  Place the order, choosing Klarna as the payment method. The order is now created in your system and in Klarna.
5.  Verify the order was correctly created. Log into the Merchant portal and go to **Orders**.
6.  Search for your order using the search bar, then click the link in the Klarna reference column to view the order details.
7.  On the **Order lines** tab, check that the **Product name**, **Unit price**, **Tax**, and **Amount** are correct.

### Shipment stage

In the second stage, 1 item is shipped to the customer and you capture the order to receive a payout for that item.

1.  In your system, capture 1 item only. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [capture the order item in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/capture-an-order/).
2.  Verify the capture in the Merchant portal. Go to **Orders** and check if the order's status is *Partially Captured*.

### Post-shipment stage

In the final stage, you release the previously authorized amount for the item that wasn't captured back to the customer.

1.  In your system, [release the remaining amount](http://docs.klarna.com/payments/after-payments/order-management/manage-orders-with-the-api/refund-orders-and-manage-authorizations/#release-order-authorization) back to the customer. If you're not integrating directly with the Order management API and don't have an integration with other systems [cancel the order in the Merchant portal](https://docs.klarna.com/payments/after-payments/order-management/manage-orders-in-the-merchant-portal/cancel-an-order/).
2.  Verify the released amount in the Merchant portal. Go to **Orders** and check if the order's status is *Fully Captured*.

## Test case 4: Place, fully capture, and fully refund an order with a discount code

This test case lets you test placing an order that contains 1 item, applying a discount, capturing the order in full, and processing a refund.

### Purchase stage

In the first stage, you place an order.

1.  Add a product to the cart and go to checkout.
2.  Enter a discount code to reduce the order amount.
3.  Place the order, choosing Klarna as the payment method. The order is now created in your system and in Klarna.
4.  Verify the order was correctly created. Log into the Merchant portal and go to **Orders**.
5.  Search for your order using the search bar, then click the link in the Klarna reference column to view the order details.
6.  On the **Order lines** tab, check that the **Product name**, **Unit price**, **Tax**, and **Amount** are correct. Also, verify that the discount code was applied and the discounted amount is correct.

### Shipment stage

In the second stage, the goods are shipped to the customer and you capture the order to receive a payout for the items sold.

1.  In your system, capture all order items. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [capture the order in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/capture-an-order/).
2.  Verify the capture in the Merchant portal. Go to **Orders** and check if the order's status is *Fully Captured*.

### Post-shipment stage

In the final stage, the customer returns the order and you refund the order amount back to the customer.

1.  In your system, refund all the order items. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [refund the order in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/refund-an-order/).
2.  Verify the refund in the Merchant portal. Go to **Orders** and check if the order's status is *Fully Refunded*.

## Test case 5: Place, fully capture, and partially refund an order with a gift card

This test case lets you test placing an order that contains 2 items, applying a gift card, capturing the order in full, and processing a refund for 1 out of 2 items.

### Purchase stage

In the first stage, you place an order.

1.  Add a product to the cart and go to checkout.
2.  Return to the store and add another product to the cart.
3.  Go to checkout again.
4.  Enter a gift card to reduce the order amount.
5.  Place the order, choosing Klarna as the payment method. The order is now created in your system and in Klarna.
6.  Verify the order was correctly created. Log into the Merchant portal and go to **Orders**.
7.  Search for your order using the search bar, then click the link in the Klarna reference column to view the order details.
8.  On the **Order lines** tab, check that the **Product name**, **Unit price**, **Tax**, and **Amount** are correct.

### Shipment stage

In the second stage, the goods are shipped to the customer and you capture the order to receive a payout for the items sold.

1.  In your system, capture all order items. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [capture the order in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/capture-an-order/).
2.  Verify the capture in the Merchant portal. Go to **Orders** and check if the order's status is *Fully Captured*.

### Post-shipment stage

In the final stage, the customer returns 1 out of 2 items from the order and you refund the item amount back to the customer.

1.  In your system, refund 1 of the order items. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [refund the item in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/refund-an-order/).
2.  Verify the refund in the Merchant portal. Go to **Orders** and check if the order's status contains two labels: *Fully Captured* and *Partially Refunded*. Also, verify that the refunded amount and the remaining open amount to be paid are correct.

## Test case 6: Place and cancel an order before the capture

This test case lets you test placing an order that contains 1 item, and canceling the order before it's captured.

### Purchase stage

In the first stage, you place an order.

1.  Add a product to the cart and go to checkout.
2.  Place the order, choosing Klarna as the payment method. The order is now created in your system and in Klarna.
3.  Verify the order was correctly created. Log into the Merchant portal and go to **Orders**.
4.  Search for your order using the search bar, then click the link in the Klarna reference column to view the order details.
5.  On the **Order lines** tab, check that the **Product name**, **Unit price**, **Tax**, and **Amount** are correct.

### Pre-shipment stage

In this stage, you cancel the order that can't be fulfilled.

1.  In your system, cancel the order. If you're not integrating directly with the Order management API and don't have an integration with other systems, you can [capture the order in the Merchant portal](https://docs.klarna.com/order-management/manage-orders-in-the-merchant-portal/capture-an-order/).
2.  Verify the cancellation in the Merchant portal. Go to **Orders** and check if the order's status is *Cancelled*.

## Test case 7: Place an order with different billing and shipping addresses

This test case lets you test placing an order that contains 1 item while providing different billing and shipping addresses.

### Purchase stage

In the first stage, you place an order.

1.  Add a product to the cart and go to checkout.
2.  Enter different billing and shipping addresses.
3.  Place the order, choosing Klarna as the payment method. The order is now created in your system and in Klarna.
4.  Verify the order was correctly created. Log into the Merchant portal and go to **Orders**.
5.  Search for your order using the search bar, then click the link in the Klarna reference column to view the order details.
6.  On the **Order lines** tab, check that the **Product name**, **Unit price**, **Tax**, and **Amount** are correct. In the **Customer** panel, verify that **Shipping address** is different than **Billing address**.

## Test case 8: Place an order with a shipping fee

This test case lets you test placing an order that contains 1 item while applying a shipping fee to the order.

### Purchase stage

In the first stage, you place an order.

1.  Add a product to the cart and go to checkout.
2.  Select a shipping option that has a shipping fee.
3.  Place the order, choosing Klarna as the payment method. The order is now created in your system and in Klarna.
4.  Verify the order was correctly created. Log into the Merchant portal and go to **Orders**.
5.  Search for your order using the search bar, then click the link in the Klarna reference column to view the order details.
6.  On the **Order lines** tab, check that the **Product name**, **Unit price**, **Tax**, and **Amount** are correct.

## Test the integration richness

If you want to check if the test orders contain the correct details, review the logs in the Merchant portal. Refer to [Klarna's API reference](https://docs.klarna.com/api) to learn about specific parameters and values in each request.

1.  In the Merchant portal, go to Orders. Click the value in **Klarna reference** to view the order details.
2.  Go to the **Summary** tab and copy the **Klarna order ID**.
3.  Go to **Logs** and enter the copied order ID as the search term. The result is a list of requests related to the order.
4.  Depending on the actions covered by the test case you followed to create an order, look for the following details in the logs.

| Order characteristics | Applicable test cases | Expected results in Logs |
|---------------------|---------------------|------------------------|
| All placed orders | 1–8 | The `order_lines` object contains the `product_url` and `image_url` values. |
| Refund an order | 1, 2, 4, 5 | The response header includes the refund's URI and ID. |
| Order placed with a discount code | 4 | The `order_lines` object contains either: <ul><li>a separateorder_linewith type equal todiscountand a negative amount value</li><li>the discount added per order line in thetotal_discount_amountfield</li></ul> |
| Order placed with a gift card | 5 | The `order_lines` object contains a separate order line with type equal to `gift_card` and a negative amount value. |
| Order placed with different billing and shipping addresses | 7 | The `billing_address` object and the `shipping_address` object have different values, corresponding to the values entered in the widget. |
| An order with a shipping fee | 8 | A separate `order_line` with type equal to `shipping_fee` includes the correct shipping fee amount. |