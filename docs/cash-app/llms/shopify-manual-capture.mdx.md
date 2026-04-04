# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/shopify/shopify-manual-capture.mdx

***

## stoplight-id: iveqkl0oknpsp

# Shopify Manual Capture

CashApp Afterpay’s integration enables you to leverage Shopify’s manual capture setting.

<Info>
  This is a Shopify store-wide setting, so if you have it enabled for another payment method it is enabled for the new payment gateway.
</Info>

If you enable *Manually capture payment for orders* within your Shopify payment settings, this means the following:

**Cash App Afterpay will not automatically capture orders when the customer completes checkout**

* Instead, Cash App Afterpay will place an authorization hold on the customer’s account like other payment methods

* Unlike other payment methods, the customer’s installment plan begins as soon as the authorization is made

* Most customers are charged for their first installment at this time, unless they qualify for Cash App Afterpay’s *No payment Up-Front* program. This is where the first installment is collected two weeks after the authorization is made

* Cash App Afterpay’s authorization hold is **valid for a period of 13 days from the time of authorization**. If the order has not been captured before this time, any uncaptured amount is automatically voided. This voided amount is subtracted from the Cash App Afterpay customer’s outstanding balance of the order. Sometimes the voided amount is more than the customer’s outstanding balance of the order. In this case the customer is refunded the remainder of the voided amount, up to the authorized amount. For more information on refunds, see the [Cash App Afterpay help](https://help.afterpay.com/hc/en-us/articles/360031623571-How-do-refunds-and-returns-work-at-Afterpay)

**Capture orders through the Shopify order tab, integrations, or direct through Shopify’s API**

* You can use all the available options on Shopify to capture Cash App Afterpay orders as any other payment method supporting manual capture

* **If you capture orders through a third-party integration or through Shopify’s API, you may need to extend your configurations to capture Cash App Afterpay orders**.

* If you capture orders through Shopify’s order tab, you will now need to capture Cash App Afterpay orders. See the [Shopify help on how to manually capture payments](https://help.shopify.com/en/manual/orders/get-paid#capture-payments-manually)

* **Shopify will continue to restrict orders to a single capture**. This means that any uncaptured amounts will expire and are voided on the 14th day after the original authorization

**To cancel an authorised order, you can use all the methods that Shopify allows (orders tab, integrations or Shopify’s API)**

* See the [Shopify help on how to manually capture payments](https://help.shopify.com/en/manual/orders/get-paid#capture-payments-manually)

* Shopify will continue to restrict cancellations to only apply to the full order amount - Shopify does not support partial cancellations

**Refunds will continue as normal**

* For partially captured orders, only the captured amount is available to be refunded

**You will only be settled for funds that you have captured**
