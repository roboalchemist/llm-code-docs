# Source: https://docs.intelligems.io/shipping-testing/shipping-testing-getting-started.md

# Shipping Testing - Getting Started

## What is Shipping Testing?

Intelligems gives you the tools to test your shipping rates, free shipping threshold, and beyond. Testing your shipping rates with Intelligems allows you to find rates that work for you and your customers. The right shipping profile can allow you to boost profits, maximize conversion without sacrificing on margin, or boost AOV.

## How does it work?

Intelligems typically runs shipping tests using a Shopify feature called the [Third Party Rate Carrier API](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/enabling-shipping-carriers). This feature allows Intelligems to calculate a user's shipping rate based on which test group they are in, what products they are purchasing, and where they will be shipping to. Because Intelligems will be providing shipping rates while you are running a test, we will automatically remove the rates that you select to test when you start your test.

Intelligems also provides features to manage the onsite merchandising required for a shipping test. A few examples of this include:

* A shipping progress bar. If you are testing your shipping threshold, you will likely want to use the Intelligems [shipping progress bar](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration) (which can be found in your **Global Styles** components)while your test is live so that the correct threshold displays in your cart for each group.
* An onsite editor to display different language for each group. If you have any text on the site that mentions your control shipping options, such as in your announcement bar or on a shipping FAQ page, you can use the Intelligems [Find & Replace](https://docs.intelligems.io/general-features/onsite-editor) feature to show the correct copy for each test group.

{% hint style="danger" %}
To activate the third-party carrier-calculated shipping, your store needs to be on the Advanced or Shopify Plus plan. This is a Shopify limitation.\
\
If you're on the Shopify plan, then you can add this feature for a monthly fee (paid to Shopify) or switch from monthly to yearly billing. For more information, contact [Shopify Support](https://help.shopify.com/questions).
{% endhint %}

## How can I get started?

Before you can run a shipping test using Intelligems, you'll need to add the Intelligems script to your theme; [here is our help guide](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) on adding that snippet.

Once the snippet has been added to your theme, see the guides below for more information on shipping testing:

{% content-ref url="how-to-set-up-a-shipping-test" %}
[how-to-set-up-a-shipping-test](https://docs.intelligems.io/shipping-testing/how-to-set-up-a-shipping-test)
{% endcontent-ref %}

{% content-ref url="shipping-test-qa-checklist" %}
[shipping-test-qa-checklist](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist)
{% endcontent-ref %}

{% content-ref url="starting-a-shipping-test" %}
[starting-a-shipping-test](https://docs.intelligems.io/shipping-testing/starting-a-shipping-test)
{% endcontent-ref %}

{% content-ref url="ending-a-shipping-test" %}
[ending-a-shipping-test](https://docs.intelligems.io/shipping-testing/ending-a-shipping-test)
{% endcontent-ref %}

{% content-ref url="shipping-progress-bar-integration" %}
[shipping-progress-bar-integration](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration)
{% endcontent-ref %}

{% content-ref url="shipping-testing-faqs" %}
[shipping-testing-faqs](https://docs.intelligems.io/shipping-testing/shipping-testing-faqs)
{% endcontent-ref %}
