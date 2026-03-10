# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/shopify/faq.mdx

***

## stoplight-id: au4sjhr2yd4kh

# Shopify FAQ

Frequently Asked Questions:

## Configuration and Setup

### Can’t verify your merchant account in the Business Hub?

You need **User** or **Hub Admin** permissions in the Business Hub to verify your merchant account. Make sure you have the right permissions before trying to connect your Business Hub account.

### Can't log in to the Business Hub?

If you've already installed the [Afterpay US payment app](/cash-app-afterpay/guides/platforms/shopify/add-cash-app-afterpay-at-checkout#download-the-afterpay-us-payment-app), you'll be redirected to the Business Hub to verify your merchant account.

If you're having trouble signing in:

* Use the [Forgot my password](https://hub.us.afterpay.com/forgot-password) link to reset your Business Hub password.
* Contact your team's main internal onboarding contact if you need general user account access created for the Business Hub

If you are still unable access the Business Hub, contact our Merchant Admin team by using the contact information below:

Email: [na-afterpay-merchant-admin@squareup.com](mailto:na-afterpay-merchant-admin@squareup.com)

Phone: +1 (484) 772-2736 | We are available Monday–Friday, 7:00am–4:00pm (PST).

Please make sure to provide the following information so that we can promptly help you:

* Your full name
* Merchant ID
* Trading/Business name
* Email address

***

### Why am I seeing "Your payment can't be processed for technical reasons. Please try a different payment method" at checkout?

This can occur when a customer checks out with Cash App Afterpay without entering an email address.

To prevent this from happening you can go to your [Shopify settings](https://www.shopify.com/admin/settings/checkout) and select **Customers can only check out using email**.

***

### Why are Cash App Afterpay orders not captured?

See the [Shopify Manual Capture](/cash-app-afterpay/guides/platforms/shopify/shopify-manual-capture) topic.

***

### Why can't I see Cash App Afterpay in my Express Checkout?

Cash App Afterpay is currently unavailable on Shopify Express Checkout.
If you navigate to the *Payment Methods* you should be able to view Cash App Afterpay.

If Cash App Afterpay is not visible on the Payment Methods, please contact your Cash App Afterpay Delivery Manager.

***

## Shopify Themes

### How do I add Cash App Afterpay to my theme?

See the instructions on the [Manually Add Cash App Afterpay Site Messaging to Theme](/cash-app-afterpay/guides/platforms/shopify/manually-add-cash-app-afterpay-site-messaging-to-theme) page.

***

### Why did Cash App Afterpay disappear from the Shopify product page after changing themes?

To display the Cash App Afterpay installment detail on the Shopify product pages, the active store theme is modified. When you change the Shopify theme, a new set of theme/template files is installed, which will not include the Cash App Afterpay product page display.

Although the product page display will require re-integration, Cash App Afterpay will remain active as a payment method on the Shopify checkout page.

To re-integrate the Cash App Afterpay product page display for the newly installed Shopify theme, please complete the steps outlined in the [Cash App Afterpay site messaging](/cash-app-afterpay/guides/platforms/shopify/manually-add-cash-app-afterpay-site-messaging-to-theme) topic.

***

### How do I add Cash App Afterpay to my payment icons?

To place a payment icon on the footer (bottom) of the payment page, first ensure that you have [enabled payment icons in your footer](https://help.shopify.com/en/manual/online-store/themes/themes-by-shopify/vintage-themes/customizing-vintage-themes/add-credit-card-icons#enable-payment-icons-in-your-footer).

Then do the following:

1. From your [Shopify admin](https://admin.shopify.com/), go to Online Store and select **Themes**.

   ![footer-payment-1.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/footer-payment-1.png)

2. Find the theme you want to edit, then click the **...** button to open the *Actions* menu. Click **Edit Code**.

   ![footer-payment-2.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/footer-payment-2.png)

3. In the *Sections* directory, click **footer.liquid**.

   ![footer-payment-3.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/footer-payment-3.png)

   If your theme doesn't include this file, click **theme.liquid** in the Layout folder.

   ![footer-payment-4.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/footer-payment-4.png)

4. Find the following code in the file:

   ```
   {% for type in shop.enabled_payment_types %}
   ```

5. Replace that line with the following two lines of code:

   ```liquid
   {% assign enabled_payment_types = "cashappafterpay" | concat: shop.enabled_payment_types %}
   {% for type in enabled_payment_types %}
   ```

6. Click **Save**

## <Note title="Code language">The code examples above are in [Liquid](https://shopify.github.io/liquid/basics/introduction) which is Shopify's own code language.</Note>

## Cash App Afterpay Banner

### How do I add a Cash App Afterpay banner myself?

If Cash App Afterpay messaging is already on your store and you would like to add a customizable Cash App Afterpay Banner, follow the instructions on the [Add an Cash App Afterpay Banner to Shopify page](/cash-app-afterpay/guides/platforms/shopify/add-a-cash-app-afterpay-banner-to-shopify).

***

## Orders

### Why was the customer returned to the Shopify checkout after trying to place an order with Cash App Afterpay?

A common cause for a customer being returned to the Shopify checkout page after trying to place an order with Cash App Afterpay is invalid order amount.

A customer's Cash App Afterpay transaction will not be approved should the order total be:

* Below the merchant minimum order value
* Above the merchant maximum order value
* In a non-supported currency

In any of these cases the customer is returned to the Shopify checkout page.

***

### How can I process a refund?

Cash App Afterpay orders can be refunded from Shopify and are automatically sent to Cash App Afterpay.

You can learn how to do refunds [here](https://help.shopify.com/en/manual/orders/refund-cancel-order).

***

### How do I update my store's minimum or maximum order value?

Please send an email with your request to [merchantAdminUS@afterpay.com](mailto:merchantAdminUS@afterpay.com)

***

### Why is the amount different between a Shopify order and Cash App Afterpay after capture?

This occurs if the cart is modified after the customer is redirected to Cash App Afterpay to complete the order.

<Note>This issue has been resolved by Shopify's Checkout Extensibility. If you are affected by this issue, it is likely that you still use Shopify's older checkout platform, called *checkout.liquid*. According to Shopify, they will have contacted you about migration to the latest Checkout Extensibility platform. As the *checkout.liquid* platform deprecated on August 13th 2024, we urge you to use Shopify's latest checkout platform to avoid posssible problems.</Note>
Adding or subtracting units of any item to the cart, or even new items, changes the amount. The transaction on the Cash App Afterpay side now has a different amount than the amount in the merchant's Shopify shop.

According to Shopify, payments apps must not do any of the following:

* Use any [Shopify APIs](https://shopify.dev/api) other than the Payment Apps API and [mandatory webhooks](https://shopify.dev/docs/apps/webhooks/configuration/mandatory-webhooks) for General Data Protection Regulation (GDPR)

* For more details, see the [Prohibited actions](https://shopify.dev/docs/apps/payments#prohibited-actions) section

If the amount is different and the customer has paid less than the order at the Shopify shop, the order status automatically becomes **Partially Paid**.

![faq-9.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/faq-9.png)

#### Fix the problem

You, the merchant, must make a manual action to fix the problem. Here are some ideas:

* If the amount paid is less than the final order value, you can ask the customer to submit an extra payment. Ask the customer to use a different payment method to make this payment

* If the amount paid is more than the final order value, you can make a partial refund to resolve the discrepancy

* You can cancel the entire order, and refund the customer. Then ask the customer to place their order again, this time with the correct number of items in the cart

## <Note>If this problem occurs regularly, please inform Shopify.</Note>

## Messaging

### Selectively hide Cash App Afterpay Messaging

Shopify sellers manually placing the [Onsite Messaging](/cash-app-afterpay/guides/afterpay-messaging/getting-started) widget on their **Product Detail** and **Cart** pages can selectively hide the **Onsite Messaging Widget** for certain items.

Tag products you want to exclude (for example, `no-cash-app-afterpay`) and insert a brief code snippet into your theme files where the `<square-placement>` tags are located.

<Note>This option is ideal for Shopify merchants who prefer to restrict the usage of Cash App Afterpay for specific products, including gift cards.</Note>
**Product Detail page**

```js
{% unless product.tags contains 'no-cash-app-afterpay' %}
<square-placement>
</square-placement>
{% endunless %}
```

**Cart page**

```js
{% assign cash_app_afterpay_eligible = true %}
{% for item in cart.items %}
{% if item.product.tags contains 'no-cash-app-afterpay' %}
{% assign cash_app_afterpay_eligible = false %}
{% break %}
{% endif %}
{% endfor %}
{% if cash_app_afterpay_eligible %}
<square-placement>
</square-placement>
{% endif %}
```

***

## Onsite Messaging App

### How do I get started with Cash App Afterpay On-Site Messaging for Shopify?

To use the Cash App Afterpay On-Site Messaging app, you must install the app from the [Shopify app store](https://apps.shopify.com/afterpay-messaging). Configure this app according to your preferences. This setup includes customizing the appearance of on-site messages and ensuring the messages integrate with your store's theme.

***

### How can I manually add Cash App Afterpay messaging to my Shopify theme?

You can manually integrate Cash App Afterpay messaging into your Shopify theme. This process involves adjusting your theme's HTML/Liquid files to include Cash App Afterpay's messaging scripts at the desired locations on your product and cart pages. For details see the [Manually Add Cash App Afterpay Site Messaging to Theme](/cash-app-afterpay/guides/platforms/shopify/manually-add-cash-app-afterpay-site-messaging-to-theme) page.

***

### What are the implementation steps for Cash App Afterpay On-Site Messaging on Shopify?

There are several key steps to implement:

* Ensure your store meets the technical requirements

* Configure the app's settings in your Shopify admin

* Test the messaging display on your store to confirm that it functions correctly and reflects the intended customer experience.

For details on all the above steps, see the [Cash App Afterpay On Site Messaging App](/cash-app-afterpay/guides/platforms/shopify/cash-app-afterpay-on-site-messaging-app) page.

***

## Cash App Pay

### Generate Cash App Pay Logo URL on Shopify

As part of the Cash App Pay checkout setup process, you need to provide Cash App Afterpay with a logo URL. This is for a Cash App Pay logo that appears on the checkout page.

Sometimes it's hard to figure out what this logo URL will be, so here's a method:

1. Go to [Shopify admin](https://accounts.shopify.com/lookup?) and log in as normal.

2. Go to the *Files* page.

   ![cash-app-logo-workaround.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/cash-app-logo-workaround.png)

3. Upload a square shaped logo that is at least 256 x 256 pixels in size and under 2MB file size. For the full Cash App logo specification, see the [Adding Cash App Pay to Your Site](/cash-app-afterpay/guides/api-development/add-cash-app-pay-to-your-site/overview#add-your-logo-to-the-qr-code-scanner) page. Any square shaped logo that meets the size criteria will do, the logo does not have to be the Cash App logo.

4. Give Caash App Afterpay the URL to the logo.
