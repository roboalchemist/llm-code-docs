# Source: https://docs.intelligems.io/checkout/what-you-can-and-cannot-test-in-checkout.md

# What You Can and Cannot Test in Checkout

Shopify Checkout is a protected environment, so not everything can be tested the same way you would test pages, pricing, or content elsewhere on your site. This guide explains what is fully supported, what is sometimes possible, and what is not possible today.

Use this page to answer **"Can I run this Checkout test with Intelligems?"**

{% hint style="success" %}
If the content block is powered by Intelligems or Shopify Checkout Blocks app, you can test it.\
If the content is from another app, you can only test it if the app supports Intelligems.
{% endhint %}

{% hint style="warning" %}
Checkout Personalizations and Checkout Testing is only available for Shopify Plus merchants
{% endhint %}

### Tests You *Can* Do

These test types are fully supported and work the same way for every merchant.

### Price Tests

You can test

* Product prices
* Compare at prices
* Variant level price changes

### Shipping Tests

You can test

* Shipping rates
* Shipping thresholds
* Any other rate based logic controlled in Shopify
* Free shipping offers

### Intelligems Checkout Personalizations

All Intelligems owned checkout content blocks can be tested. This includes turning blocks on or off, testing different versions, and testing different locations.

### Shopify Checkout Blocks

Shopify’s native Checkout Blocks can be tested because they support conditional rules based on cart attributes.

You can test\
• Turning a Checkout Block on or off\
• Versions of the same block with different content or settings

If a content block is built by Shopify or Intelligems, you can test it. More on [How to Set up a Checkout Blocks Test](https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-checkout-blocks).

## Tests You Can *Sometimes* Do

These test types require the third party app to support Intelligems. They are possible, but only if the app developer adds a simple integration.

### Third Party Checkout Apps

This includes apps for

* Upsells
* Shipping protection
* Gift wrap
* Insurance
* Warranty
* Donations
* Most other enhancements in checkout

These apps can be tested only if they support listening to a cart attribute set by Intelligems. If a checkout app does not support an Intelligems integration, it cannot be A/B tested.

#### Requirement

The app must be able to

* Read an attribute on the cart
* Hide or show their block based on that attribute
* Optionally adjust pricing or settings based on that attribute

Some apps already support this. Others are usually willing to add support if the merchant requests it.

{% hint style="info" %}
If you want to test a third party app, contact the app developer and ask whether they support A/B testing through a cart attribute with Intelligems. Many smaller apps can add this quickly with an easy integration.
{% endhint %}

## Tests You Cannot Do Today

These items are not supported in Shopify Checkout, for any app or testing platform.

### Checkout Layout

You cannot test

* One page vs three page checkout
* Reordering the steps in checkout
* Changing the structure of the Shopify checkout flow

{% hint style="info" %}
Shopify only allows one checkout layout to be active at a time.
{% endhint %}

## FAQs

* **Can I test my upsell app?**\
  Yes, if the app supports an Intelligems integration.\
  We recommend creating a Product Upsell Checkout Test. [More steps here](#intelligems-checkout-experiences).&#x20;
* **Can I test my gift message block?**\
  Yes, if it is a Shopify Checkout Block or an Intelligems Checkout Personalization.\
  No, if it is a third party app without integration.
* **Can I test a "clean" checkout versus my current checkout?**\
  If your current checkout has multiple third party apps running outside of Shopify Checkout Blocks or Intelligems Checkout Personalizations, the answer is No.
* **Can I test one page vs three page checkout?**\
  No. Shopify does not allow multiple checkout layouts to run at the same time.
* **Can I test shipping insurance pricing?**\
  Yes, if the insurance app supports an Intelligems integration. [Navidium](https://docs.intelligems.io/integrations/navidium-testing) supports this today.
* **Can I use a Theme Test to test multiple checkouts?**\
  No. Theme tests cannot be used to compare different versions of checkout. Shopify only allows one checkout to be live at a time, draft checkout versions cannot be assigned to customers, and the preview banner cannot be hidden. Theme tests work because multiple themes can be served to real shoppers. Checkout does not work this way.

## Need Help?

If you want to confirm a specific test idea or need support with a third party app, [contact Intelligems Support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we can walk through the best approach.
