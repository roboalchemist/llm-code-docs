# Source: https://developers.cash.app/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay.mdx

***

## stoplight-id: 5fduu327ov6ue

# Migrate from Afterpay to Cash App Afterpay

<Warning title="Important">
  If your app uses an explicit allowlist of Afterpay domains, you 

  *must*

   add 

  `api.cash.app`

   and 

  `cash.app`

   to the allowlist.
</Warning>

## API integration

There are no changes to the APIs, so you don't need to make any changes to your backend systems. While the terminology has changed, the API endpoints are the same.

## Afterpay Messaging

We currently support two messaging products, both of which work with Cash App Afterpay.

[On-Site Messaging](../AFTERPAY-MESSAGING/Getting-Started-with-Afterpay-On-Site-Messaging.md) is our current messaging product. Our previous product is messaging from the [JavaScript Library](../AFTERPAY-MESSAGING/JavaScript-Library.md).

**On-Site Messaging**

If you use On-Site Messaging, it will be updated automatically, with advance notice sent via email.

If you use elements of Afterpay Messaging, then see the [Getting Started with Afterpay On-Site Messaging](../AFTERPAY-MESSAGING/Getting-Started-with-Afterpay-On-Site-Messaging.md) page for more information.

**JavaScript Library**

If you use the JavaScript Library for your messaging, it will be updated automatically, with advance notice sent via email.

<Note>
  If you use a specific version of the script, update to version 

  `1.x.js`

  .
</Note>

## Differences between Afterpay and Cash App Afterpay

* Cash App Afterpay is only available in the USA. Australia, New Zealand, and Canada use the Afterpay brand. The United Kingdom uses the Clearpay brand.

* Cash App Afterpay operates in US dollars only. [Cross Border Trade](../WELCOME/caa-cross-border-trade.md) is available.

* US customers will see *Cash App Afterpay* on your product and payment pages instead of *Afterpay*.

## Brand Assets

See the [Brand Assets](../MARKETING/Brand-Assets.md) page in this guide for new assets.

See the [Cash App Afterpay Merchant guidelines](https://www.figma.com/deck/yC8BbsBfhxkSnxrw8VtYna/Cash-App-Afterpay-%E2%80%93-Merch\[…]kF1jqQt-1\&scaling=min-zoom\&content-scaling=fixed\&page-id=0%3A1) online presentation for detailed information on how to display Cash App Afterpay.

Custom messaging updates must be reviewed by your Account Manager.

## FAQs

If you have a technical question on the migration, view our [FAQ](faq-migration.md) page.

# Platforms

This section is for merchants who use a platform for their integration. Find your platform in the list below for information on migration from Afterpay to Cash App Afterpay.

* [Adobe Commerce (Magento 2)](adobe-commerce-migration.md)

* [Adyen](adyen-migration.md)

* [Big Commerce](big-commerce-migration.md)

* [Ecwid](ecwid-migration.md)

* [PrestaShop](prestashop-migration.md)

* [Salesforce Commerce Cloud](salesforce-cc-migration.md)

* [Shopify](shopify-migration.md)

* [Stripe](stripe-migration.md)

* [Wix](wix-migration.md)

* [WooCommerce](woocommerce-migration.md)

<Info title="Don't see your platform?">
  Some platforms can't host Cash App Afterpay because these platforms are not available in the United States. Other platforms are not be available for Cash App Afterpay yet, but will be in the future. Contact us for more information.
</Info>
