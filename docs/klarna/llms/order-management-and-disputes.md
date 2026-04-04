# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/shopify-payments/order-management-and-disputes.md

# Source: https://docs.klarna.com/platform-solutions/acquiring-partners/adyen/payments/order-management-and-disputes.md

# Adyen order management and disputes

## In this section, you’ll find the best practices for Adyen and Klarna integration. We recommend you follow the steps below to get the most value from your new payment option.

## Order management

Adyen has integrated Klarna's order management API requests that you’re likely to use on a daily basis. Here are some of our best practices:

- When the order is ready to be shipped, make sure to include all relevant order line items in the [capture request](https://docs.adyen.com/payment-methods/klarna/web-drop-in#manual-captures). This is especially important for partial capture orders. If order lines are missing, Adyen adds a `CORRECTION` order line to each partial capture in the order. As a result, all items from the same order will be listed on every invoice issued for that order, as well as in the customer’s Klarna account. Even though the customer is billed correctly, this can be confusing and lead to avoidable customer support queries.
- When the order is captured, add the [shipping and tracking information](https://docs.adyen.com/payment-methods/klarna/web-drop-in#shipping-and-tracking-information). This lets the customer track the status of their order.
- When the order is fully refunded, make sure you send all order line items in the captured request. If the order is refunded partially, make sure to send all relevant order line items. If order lines are missing, Adyen adds a `CORRECTION` line in the refund request, which can be confusing for customers.
- If you haven’t opted for multiple partial captures, [Adyen will clear the remaining Klarna balance](https://docs.adyen.com/api-explorer/Checkout/70/post/payments/_paymentPspReference_/captures) in case of a partial capture.

## Data handling

### Address & phone validation

Make sure to validate all addresses and phone numbers before sharing them with Adyen. Rejections due to mismatched or incorrect addresses late in the process can have a negative impact on acceptance rates, so ensuring these are correct early on is critical.

### Tax handling with discounts

You need to declare the tax amounts and VAT for your Klarna orders. It’s crucial to declare discounts and taxes correctly. Make sure to follow the [invoice lines and discounts guidance in Adyen Docs](https://docs.adyen.com/payment-methods/klarna/invoice-lines) to avoid integration issues.

### Extra merchant data (EMD)

[Extra merchant data](https://docs.klarna.com/api/payments/#operation/createCreditSession!path=attachment&t=request) is a set of additional information typically unavailable during the checkout flow. This information may consist of data about the customer performing the transaction, the products or services associated with the transaction, or the seller and their affiliates. Depending on the business category or the type of goods you sell, sending EMD data may be a mandatory requirement.  Here are some examples of business categories where sending EMD is mandatory:

- Travel (flight, train, bus, car rental, hotel)
- Marketplaces
- Tickets and events 
- Subscriptions
- Vouchers and gift cards

### Product and image URLs

You can share the [imageUrl](https://docs.klarna.com/api/payments/#operation/createOrder!path=order_lines/image_url&t=request)`imageUrl` and the [productUrl](https://docs.klarna.com/api/payments/#operation/createOrder!path=order_lines/product_url&t=request)`productUrl` with Adyen. This lets Klarna use these resources in your communication with the customer to improve the post-purchase experience in the Klarna app. This helps the end customer to visualize the purchase they have made.

## Disputes

You can manage the [Klarna disputes](https://docs.adyen.com/risk-management/chargeback-guidelines/klarna-chargebacks) using the [Adyen customer area](https://docs.adyen.com/risk-management/chargeback-guidelines/klarna-chargebacks#klarna-dispute-ca) or by using the [Adyen dispute API](https://docs.adyen.com/risk-management/chargeback-guidelines/klarna-chargebacks#klarna-dispute-api). If you have any questions regarding disputes, please reach out to Adyen support who will be able to help you.