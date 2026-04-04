# Source: https://docs.intelligems.io/price-testing/price-testing-getting-started.md

# Price Testing - Getting Started

## What is Price Testing?

Intelligems takes the guesswork out of setting your product prices by allowing you to test prices in real time in order to find the “right” product prices to drive profit, revenue, and conversion boosts.

You can easily build product price split tests with just a few clicks in the Intelligems app. Tests are easy to build and customize: add multiple test groups with configurable traffic distribution rules, select which products to include in the test, and set test group prices.

## How does it work?

For all Shopify brands, Intelligems displays the correct price on the frontend by manipulating the DOM to show the correct price depending on a user's test group once your [prices have been tagged](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices). Intelligems displays the correct price in the cart and charges the correct amount at checkout using one of the three below methods:

1. **Using Shopify Cart Transform Functions.** Intelligems will automatically set your prices to the highest prices in the test in Shopify when you start your test, and we will use a Shopify Cart Transform Function to dynamically adjust the price for any users in a group lower than the highest price in the test so that they get the same price in the cart and at checkout that they saw everywhere else on the site. This method is available for brands on any Shopify plan, and will be Intelligems' primary method moving forward.
2. **Using a Checkout Script.** Intelligems will automatically set your prices to the highest prices in the test in Shopify when you start your test, and we will use a Checkout Script to run a behind the scenes adjustment for any users in a group lower than the highest price in the test so that they get the same price in the cart and at checkout that they saw everywhere else on the site. This method is only available for brands on Shopify Plus, and Intelligems is beginning to move away from this method as Shopify will be deprecating the Script Editor app in August 2025.
3. **Using Duplicate Products.** In certain cases, such as testing something more complex or if you offer subscriptions, Intelligems will swap in a duplicate product when a user adds to cart in any group other than the control group to ensure the price is correct in the cart and at checkout.

## How can I get started?

There is a short integration required before you can begin a price test. Please see the appropriate guide [here](https://docs.intelligems.io/getting-started/pricing-integration-guides) depending on which version of our integration you are on. If you are not sure which integration guide you should be following, please reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

If you prefer, we'll be happy to complete the integration for you - in that case, please book a demo with our team [here](https://meetings.hubspot.com/igsam/igdemo?uuid=09e10934-25f6-4485-9f0e-4ceb6e80f099) so we can learn more about your store and get it integrated with Intelligems.

Once the integration has been completed, see the guides below for more information on price testing:

{% content-ref url="price-testing-integration-guides" %}
[price-testing-integration-guides](https://docs.intelligems.io/price-testing/price-testing-integration-guides)
{% endcontent-ref %}

{% content-ref url="how-to-set-up-a-price-test" %}
[how-to-set-up-a-price-test](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test)
{% endcontent-ref %}

{% content-ref url="price-test-qa-checklist" %}
[price-test-qa-checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist)
{% endcontent-ref %}

{% content-ref url="starting-a-price-test" %}
[starting-a-price-test](https://docs.intelligems.io/price-testing/starting-a-price-test)
{% endcontent-ref %}

{% content-ref url="ending-a-price-test" %}
[ending-a-price-test](https://docs.intelligems.io/price-testing/ending-a-price-test)
{% endcontent-ref %}

{% content-ref url="testing-prices-with-subscriptions" %}
[testing-prices-with-subscriptions](https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions)
{% endcontent-ref %}

{% content-ref url="multi-currency-testing" %}
[multi-currency-testing](https://docs.intelligems.io/price-testing/multi-currency-testing)
{% endcontent-ref %}

{% content-ref url="price-testing-faqs" %}
[price-testing-faqs](https://docs.intelligems.io/price-testing/price-testing-faqs)
{% endcontent-ref %}
