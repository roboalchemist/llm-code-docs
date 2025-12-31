# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/payments-for-shopify/testing-the-integration.md

# Testing Klarna Payments for Shopify

## Test Klarna Payments safely on your Shopify store using Test mode to validate integration without real transactions, and remember to disable it before going live.

## Activate Test mode in Shopify’s store admin

When you activate **Test mode** on the Klarna payment method in your store’s Shopify admin, you can place test orders. Klarna doesn’t collect or settle any money for these test orders. You can test a Klarna integration with Shopify in two ways:

1.  Integrating your Klarna production Merchant ID to a staging version of your website and enabling **Test mode** via **Shopify Settings**\> **Payments**\> **Klarna**\> **Manage**\> **Test mode**.

This allows you to test that Klarna works with your website without the risk of customers placing an order on your live site. This also has the additional benefit of the test orders being separate from your live store. Once you have finished your testing, you will then need to disconnect and uninstall the Klarna app from your staging store. Once uninstalled it takes 48 hours for Shopify to remove the integration record from your staging store. To avoid the wait, contact your regional [Merchant Support](https://www.klarna.com/pay-now/business/merchant-support/) team and ask them to manually remove the integration record. A Klarna Playground Merchant ID can't be used to test the Shopify integration. You must have a Production Merchant ID that has been approved by Klarna before testing your integration with Shopify. 2. Integrating your Klarna Production Merchant ID with your live Shopify store and enabling **Test mode** within the Klarna settings found in **Shopify Settings**\> **Payments**\> **Klarna**\> **Manage**\> **Test mode**. When you enable **Test mode** in your live store, customers will still be able to place Klarna orders in your store. However these orders won’t be placed in our live system, and, as such **these orders shouldn’t be shipped and won’t be paid out.** These orders will still be visible on your Shopify orders page. If you activate **Test mode**, make sure to uncheck **Enable test mode** as soon you complete the testing. Klarna doesn’t pay out for test orders, even if a customer places a real order while **Test mode** was checked.


![ Activating Test mode in Shopify store admin.](757b6bd6-178c-4b23-b3ea-53a6c8645a62-shopify-ppp-test-mode.jpeg)
*Activating Test mode in Shopify store admin.*

**Good to know**

- Test orders will be visible in the Shopify admin if the order was completed. These shouldn’t be shipped as they aren’t live Klarna orders.
- When **Test mode** is disabled, live orders will be visible in both the Klarna production Merchant portal and the Shopify admin.
- The Klarna payment methods offered with test mode active may not match your production account's configured Klarna payment offerings.
- The Klarna Shopify direct integration is agnostic of specific Klarna payment methods though, so testing is still applicable with differing payment methods.
- To test specific payment methods, you can use [Klarna’s Demo Store](https://www.klarna.com/demo/) with applicable payment methods by region.

**In summary:**

- Activating Test mode in Shopify's admin allows you to place test orders without collecting or settling money. Test mode uses the production account.
- It's crucial to disable Test mode after testing, as Klarna doesn't pay for test orders, even if real orders were placed during testing. 
- The Klarna payment methods in Test mode may differ from the payment methods in production.