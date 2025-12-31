# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions.md

# Integration Guide using Shopify Functions

Historically, Intelligems has used either Checkout Scripts or duplicate products to run Price Tests. Shopify will be sunsetting Checkout Scripts in August 2026, and with that transition, Intelligems will be using Shopify Cart Transform Functions instead. This is the integration we mostly use currently, and it is enabled by default on new installs.

{% hint style="warning" %}
A few caveats when using Functions:

* If your store is on Shopify Plus, and you are using any Line Item Checkout Scripts, there may be conflicts between those and the Function we run.
* Please note that only one Shopify Cart Transform Function can run on a single line item.

If you use Cart Transform Functions for other capabilities, or you are in doubt about conflicts with existing Checkout Scripts, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to discuss options for your integration.
{% endhint %}

Before you can run a Price Test on your Shopify store, there is a small integration that needs to be done. There are four steps in the integration:

1. Add Intelligems JavaScript
2. Tag product prices
3. Update your cart
4. QA your integration, and publish your changes

{% hint style="success" %}
The Intelligems team is happy to complete the integration for you - please reach out [here](https://portal.usepylon.com/intelligems/forms/price-test-integration-request) to get this process started.
{% endhint %}
