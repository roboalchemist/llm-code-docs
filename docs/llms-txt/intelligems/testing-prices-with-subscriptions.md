# Source: https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions.md

# Testing Prices with Subscriptions

## Introduction

If you offer subscriptions as an option on your product(s), testing prices is a bit more complex. Intelligems supports testing both one-time and subscription prices for your store's products, and this article will walk through the basics on what is possible, and how to get started.

{% hint style="warning" %}
Testing subscriptions is only available on our **Blue** plan.
{% endhint %}

## What kind of subscription tests are supported?

Intelligems supports a wide variety of tests on subscription products. Some examples include:

* Testing different one-time prices while keeping subscription discount percentages consistent
* Testing different one-time prices while keeping subscription prices consistent
* Testing different subscription discounts

## How does Intelligems implement subscription tests?

Generally, Intelligems implements subscription tests by creating duplicate products (one duplicate per test group for each product). Duplicate products are often required because subscription providers display one-time and subscription prices on PDPs directly based on the product URL. Therefore, a separate product needs to be created to show different prices. To learn more about how these products will be configured, check out our article [here](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps).

If your store is on Shopify Plus and uses Recharge 2.0 or Stay.ai, we may be able to implement your test without duplicate products. Please [contact us](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to learn more.

## Which subscription apps is Intelligems compatible with?

Intelligems is generally compatible with all major subscription providers. Most require us to create duplicates of the products you want to test. See below for a list of subscription providers and implementation methods available for each.

| **Provider**                    | **API + Checkout Scripts** | **Duplicate Products** |
| ------------------------------- | -------------------------- | ---------------------- |
| Recharge 2.0 (Unified Checkout) | ✓                          | ✓                      |
| Stay.Ai                         | ✓                          | ✓                      |
| Skio                            |                            | ✓                      |
| Prive                           |                            | ✓                      |
| Smartrr                         |                            | ✓                      |
| Loop                            |                            | ✓                      |
| Ordergroove                     |                            | ✓                      |

## Which Intelligems plans qualify for subscription testing?

You must be on a **Blue** plan to qualify for subscription testing. [See plan details](https://www.intelligems.io/pricing).

## Can I perform the integration with Intelligems on my own if I offer subscriptions?

Testing subscriptions often requires a more involved integration & setup than typical price tests. As a result, we recommend having Intelligems perform the integration if this applies to your store. [Reach out to our support team to learn more](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!

## I've read all of the above and am ready to set up my test. How do I do this?

Check out the guides below to learn more about setting up a price test where subscription products are involved:

{% content-ref url="testing-prices-with-subscriptions/testing-prices-with-recharge-2.0-or-stay.ai" %}
[testing-prices-with-recharge-2.0-or-stay.ai](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/testing-prices-with-recharge-2.0-or-stay.ai)
{% endcontent-ref %}

{% content-ref url="testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-recharge-subscriptions" %}
[how-to-set-up-a-price-test-using-duplicate-products-and-recharge-subscriptions](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-recharge-subscriptions)
{% endcontent-ref %}

{% content-ref url="testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-skio-subscriptions" %}
[how-to-set-up-a-price-test-using-duplicate-products-and-skio-subscriptions](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/how-to-set-up-a-price-test-using-duplicate-products-and-skio-subscriptions)
{% endcontent-ref %}

{% content-ref url="testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps" %}
[managing-duplicate-products-when-redirecting-to-duplicate-pdps](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/managing-duplicate-products-when-redirecting-to-duplicate-pdps)
{% endcontent-ref %}
