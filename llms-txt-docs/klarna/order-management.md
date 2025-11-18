# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/payments-for-shopify/order-management.md

# Shopify order management

## This article details the order operations you can manage in the Klarna payments app integration for Shopify.

The Klarna payments app integration for Shopify comes with an integrated order management feature. We recommend that you manage the Klarna orders as part of the standard order management within your Shopify admin.

- Orders marked as *Paid* or *Authorized* are guaranteed funds by Klarna and can be fulfilled when appropriate for the shop.
- Orders marked as *[Payment pending](https://help.shopify.com/en/manual/orders/manage-orders/alt_payments_pending)* should not be fulfilled until the payment is completed and therefore guaranteed by Klarna.

While order management can be done directly via the Klarna Merchant portal, this will cause Klarna data and Shopify order data to be out of sync and could result in unintended updates, for example, duplicated refunds. Unless there is a problem, you should manage all orders through the Shopify admin and not the Klarna Merchant portal.

## Capturing an order

The payment status of captured orders depends on the [Payment capture method configuration setting](https://help.shopify.com/en/manual/orders/get-paid) in the Shopify admin under Settings\> Payments. You can set the payment capture method to automatic or manual. This **Payment capture** setting applies to all orders in a Shopify store.

- For manually captured orders, the Shopify payment status is first set to **[Payment pending](https://shopify.dev/apps/payments/processing-a-payment#pend-a-payment)**. After a small time delay, after the Klarna order has been created, the Shopify order is set to **[Authorized](https://shopify.dev/apps/payments/capturing-an-authorized-payment)**. You can manually capture the Shopify order once, which will trigger the corresponding capture of the Klarna order. The Klarna capture doesn't contain order line data, as [capture order line data isn’t shared by Shopify](https://shopify.dev/apps/payments/capturing-an-authorized-payment#request-body-example). 
- For automatically captured orders, the Shopify payment status is first set to **[Payment pending](https://shopify.dev/apps/payments/processing-a-payment#pend-a-payment)**. After a small time delay, the status is set to **[Paid](https://shopify.dev/apps/payments/processing-a-payment)** and then after another time delay of up to 20 minutes, the corresponding Klarna order is automatically captured.

Usage of automatic capture is restricted to specific business rules and categories. Please refer to our [guidelines](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/automatic-capture.md) before enabling this functionality. Shopify currently adds the \[<https: en="" help.shopify.com="" manual="" order-status#order-payment-status-desc="" orders="">:~:text=Expiring%20isn%27t%20a%20payment%20status%2C%20but%20the%20Expiring%20badge%20is%20displayed%20two%20days%20before%20the%20deadline%20for%20capturing%20payment%20on%20orders%20that%20have%20the%20Authorized%20payment%20status. Expiring badge\]**to Shopify orders at a default time period of 7 days, which doesn't match the Klarna order expiration date, as set by Klarna in the [authorizationExpiresAt field when resolving the payment on Shopify](https://shopify.dev/api/payments-apps/latest/mutations/paymentSessionResolve). Even when a Shopify order has an**Expiring''' badge, Klarna payment can still be captured from the Shopify order, as long as the Klarna order hasn't expired or already been captured. By default, Klarna orders expire after 28 days. While Klarna orders can be captured directly in the [Klarna Merchant portal](https://portal.klarna.com/), we recommend keeping Shopify and Klarna order data in sync whenever possible. The [capture of Klarna orders](https://docs.klarna.com/platform-solutions/shopify/payments/klarna-payments/order-management) is not based upon the Shopify order being fulfilled and shipped, as was previously. If you'd like to have the Klarna order based on Shopify order fulfillment, you may be able to build that specific to your store using the [Shopify Flow](https://apps.shopify.com/flow) app. If you use Shopify Flow to capture the orders, please note [the recommended time delay settings](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/order-management). Based on your Klarna contract, Klarna charges merchant fees for captured orders. When Shopify orders are automatically captured, that is, immediately after the order is placed, Klarna fees will apply for each order, even if the order is canceled in the Shopify admin without being fulfilled.


![ The Payment capture method configuration setting will be supported with the new Klarna payment integration app; merchants can choose for all their Shopify orders to be automaticallycaptured or manuallycaptured. The following image shows the configuration.](811e19b4-fbce-480a-8b62-1a9bd9d6ae7d-payment-capture.jpeg)
*ThePayment capture methodconfiguration setting will be supported with the new Klarna payment integration app; merchants can choose for all their Shopify orders to beautomaticallycaptured ormanuallycaptured. The following image shows the configuration.*

![ Klarna orders are first given a Payment pending status.](c2cc2fcf-7d65-4fb1-bd8a-0ac71c9aca9f-Pending-Payment-Shopify-order-status.jpeg)
*Klarna orders are first given aPayment pendingstatus.*

### Shopify flow with manual payment method capture

If you’re using the [Shopify Flow app](https://apps.shopify.com/flow) to trigger the capture of a Shopify order when the **Payment capture method** is set to **Manually**, we recommend that you include a time delay of around 30 minutes after the check**,** if the payment method is Klarnastep to avoid the **Payment gateway** being set to null in some Shopify webhooks, for example for webhooks used by [Signifyd](https://apps.shopify.com/signifyd) and similar apps.


![ Order payment status examples with capture method set to Manualand Automatically.](a06f3313-6ef1-47a2-ab19-cfdf9609jjc98b.jpeg)
*Order payment status examples with capture method set toManualandAutomatically.*

## Partial capture

Partial capture (multi-capture) is supported for Klarna orders for Shopify Plus merchants. There is a UI bug in Shopify that currently occurs if trying to complete another capture while the first capture is pending. During this time it may appear to be possible to capture a much larger amount than the original order amount, however this is incorrect and will lead to an error if attempted.

## Refunding an order

[Refunds made in Shopify](https://help.shopify.com/en/manual/orders/refund-cancel-order) will update the Klarna order after a short time delay of less than 10 minutes. This applies for all types of Shopify refunds: before or after Shopify order fulfillment, full or partial refunds, order line based refunds, and amount-based refunds. The Klarna refund doesn’t include order line data as [refund order line data is not shared by Shopify](https://shopify.dev/apps/payments/processing-a-refund#initiate-the-refund-flow).

## Canceling an order

- If you cancel the order whose payment capture method was set to **Automatically capture**, the Klarna order would have already been captured and canceling the Shopify order will result in a refund for the Klarna order.
- If the order's payment capture method was set to **Manually capture**, [canceling the Shopify order](https://help.shopify.com/en/manual/orders/cancel-delete-order) before manually setting the order as **Paid** will result in the Klarna order also being canceled, if the payment was not yet captured. For orders already captured, you should use a refund instead, as a cancel call won't be accepted by Klarna.

## Editing order lines

You can remove and add items to a Klarna order that has been placed. Editing order lines is possible for both automatically and manually captured Klarna orders.

- When you remove an order line from an order, you need to capture the full order amount in Shopify. After you’ve captured the amount, you have to process a refund for the amount of the item you’ve removed from the order.
- When you add an order line to an order, Shopify will send an email to your customer with a link to your Shopify checkout. The customer can then use Klarna to pay for the additional item. Once the customer pays, a new order will be created in Klarna’s database. The newly created order line includes the number of the original order.

For more information about editing orders see the [article about Editing order items in Shopify documentation](https://help.shopify.com/en/manual/orders/edit-orders).

## Extending a Klarna order's authorization time

For orders that aren’tautomatically captured based on your store's [Payment capture method](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/order-management) setting, we recommend that you manually capture the order prior to the Klarna order expiration date. The expiration time frame depends on your Klarna contract. By default, orders expire after 28 days. The Klarna order's authorization time can’t be extended within the Shopify admin. You can extend the authorization time for Klarna orders in the Klarna Merchant portal, if applicable for the order.


![  If applicable for the order, you can extend the authorization time for Klarna orders in the Klarna Merchant portal by clicking the Extend expiration date link.](a06f3313-6ef1-47a2-ab19-cfdf9609c98b.jpeg)
*If applicable for the order, you can extend the authorization time for Klarna orders in the Klarna Merchant portal by clicking theExtend expiration datelink.*</https:>