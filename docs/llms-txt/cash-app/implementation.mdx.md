# Source: https://developers.cash.app/cash-app-afterpay/guides/afterpay-messaging/implementation.mdx

***

## stoplight-id: pxipyhmn76pw0

# Implementation

## Messaging installation

On-Site Messaging adds pay-over-time messaging to your store's website. For example, in the picture below the messaging is:

*4 payments of \$25.00 with Cash App Afterpay*
*Learn more*

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Product page messaging-2.png" alt="Product page messaging.png" noZoom />

Updates to the messaging are automatic, and a specific set of messaging logic is designed for your products (Pay in 4, Pay Monthly, etc). Use our On-Site Messaging Editor in the Business Hub to customize, preview, and manage your messaging.

## Requirements

To use this On-site Messaging feature you must:

* Be an existing Cash App Afterpay merchant
* Have a direct integration with Cash App Afterpay
* Have at least one retail website live and ready for use; a Sandbox environment is also available for testing

<Note>
  If you already have Cash App Afterpay Messaging through the JavaScript library, we recommend you replace these with On-Site Messaging instead. See the 

  [Migration page](/cash-app-afterpay/guides/afterpay-messaging/migration)

   for details.
</Note>

## Business hub environments

On-site Messaging configurations are environment-specific and tied to your production and sandbox merchant accounts. See our page on [Business Hub Access](/cash-app-afterpay/guides/welcome/business-hub) or speak to your dedicated account manager if you need assistance getting user access to the Business Hub links below.

| Environment | Link                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------------------------------ |
| Sandbox     | [https://hub.us-sandbox.afterpay.com/onsite-messaging](https://hub.us-sandbox.afterpay.com/onsite-messaging) |
| Production  | [https://hub.us.afterpay.com/onsite-messaging](https://hub.us.afterpay.com/onsite-messaging)                 |

## Sandbox testing

We recommend that you start by configuring On-Site Messaging in the [Sandbox Business Hub](https://hub.us-sandbox.afterpay.com) to review the Cash App Afterpay messaging on your development store before you go live in production.

To test, you need access to the Sandbox Business Hub.

Before deploying to production, ensure that:

* Messaging appears correctly on all product pages
* Messaging updates when price changes
* Messaging appears correctly on cart page
* Multiple products in cart show correct total installment amount
* Ineligible products/carts correctly hide messaging
* Messaging is responsive on mobile devices
* All required attributes are properly populated

When you are satisfied with your testing, you're ready to go to the production [Business Hub](https://hub.us.afterpay.com) to configure your messaging. From this portal, you can configure Cash App Afterpay messaging for the live site.

## On-Site Messaging quickstart guide

### Configure On-Site Messaging

Start by accessing either environment's Business Hub:

* [Sandbox](https://hub.us-sandbox.afterpay.com) — we recommend that you start here
* [Production](https://hub.us.afterpay.com)

1. Once logged in, navigate to the On-Site Messaging tab in the sidebar
   <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/OSM implementation 1.png" alt="OSM implementation 1.png" noZoom />

2. From the On-Site Messaging tab, go to the Placements sub-page
   <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/OSM implementation 2.png" alt="OSM implementation 2.png" noZoom />

3. Select the Product or Cart page to customize your messaging from the options available. You can make adjustments to the logo, text size, and theme by placement.
   <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/OSM implementation 3.png" alt="OSM implementation 3.png" noZoom />

4. Navigate to the Settings sub-page to find additional advanced configuration options.
   <img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/OSM implementation 4.png" alt="OSM implementation 4.png" noZoom />

5. Once your configuration settings are ready, click the Implementation Guide sub-page and follow the instructions there to add the messaging to your associated environment storefront in three steps.

Here's an example from the production On-Site Messaging tab:

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/OSM implementation 5.png" alt="OSM implementation 5.png" noZoom />

### Add On-Site Messaging to your storefront

To display installment messaging on your storefront, add the respective `<square-placement>` tag from the Implementation Guide to the product page and cart page files in your codebase. Place the messaging immediately below the price element of the product and the total element of the cart.

Example square placement on product page:

```javascript
<square-placement
  data-mpid="{Replace with your MPID}"
  data-placement-id="{Replace with your product Placement ID}"
  data-page-type="product"
  data-amount="{Replace with your own price variable}"
  data-currency="{Replace with your own currency variable}"
  data-consumer-locale="{Replace with consumer locale variable}"
  data-item-skus="{Replace with SKU variable}"
  data-item-categories="{Replace with category variable}"
  data-is-eligible="true"
>
</square-placement>
```

Make sure to correctly configure the following dynamic properties for each `<square-placement>` tag added on your site:

1. Set the `data-amount` with the amount that appears on the page to calculate the installments. Keep the `data-mpid` and `data-placement-id` attributes in place with their current values unchanged.

2. Set the `data-currency` to the customer's currency and `data-consumer-locale` to the customer's country.

3. Set `data-item-skus` to any unique product identifier you use, provided as a string. If you have multiple products in the cart, separate them with a comma.

4. Set `data-item-categories` as one or more category names for the relevant product. This is provided as a string or for multiple categories, separate them with a comma.

5. To restrict a product from sale with Cash App Afterpay, set the `data-is-eligible` attribute to false. To restrict a cart from sale with Cash App Afterpay, set the `data-cart-is-eligible` attribute to false. This is optional.
