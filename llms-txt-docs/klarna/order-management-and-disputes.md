# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/shopify-payments/order-management-and-disputes.md

# Order Management and Disputes

## Manage Klarna orders on Shopify effectively by configuring payment capture, handling refunds within set timelines, and responding promptly to chargebacks through Klarna’s dispute process.

## **Captures**

In your payment settings, you can choose to capture payments automatically when an order is placed, or to capture them manually within 28 days of an order. By default, your payments are captured automatically. When you capture a payment, the funds are provided to you immediately by Klarna. You can change the way that you capture payments in the Payments section of your Shopify admin. The manual capture option applies to all payments, not just those from Klarna. From the time the order is placed, you have until midnight Coordinated Universal Time (UTC) on the 28th calendar day from when the order was placed to capture the payment. If you don't capture the payment within that time, then the payment expires and becomes void. For manually captured orders, the Shopify payment status is initially set to "Payment pending." After a short delay, once the Klarna order is created, the status changes to "Authorized." You can then manually capture the Shopify order, which triggers the corresponding capture of the Klarna order. Note that Klarna capture does not include order line data as Shopify does not share this data. For automatically captured orders, the payment status starts as "Payment pending" and changes to "Paid" after a delay. The corresponding Klarna order is automatically captured after another delay of up to 20 minutes.

## **Refunds**

If you refund a transaction processed by Klarna, then the processing fee charged to you by Shopify Payments isn't refunded. Processing fees are determined by the subscription plan on your Shopify account. For more information about Shopify Payment fees, refer to the [Shopify Pricing](https://www.shopify.com/pricing) page for your location. Klarna allows refunds to be processed within 180 days of the initial charge of an order. If 180 days have passed from the date of the initial charge, then it's no longer possible to refund through a Klarna payment option. If you want to refund an order after 180 days, then work with the customer to return the funds to them using an external service.

## **Chargebacks**

If a chargeback is opened against a Klarna order, then the customer is encouraged to contact you directly.

- Klarna contacts the customer if the dispute isn't resolved after 21 days.
- Klarna then contacts you by email about the dispute and provides you with the Klarna order number.
- You can use the Klarna order number in your Shopify admin to find your order.
- You have 7 days to respond to the dispute notification from Klarna.