# Source: https://docs.intelligems.io/shipping-testing/shipping-testing-faqs.md

# Shipping Testing FAQs

<details>

<summary>Is a shipping threshold based on a pre or post discount subtotal?</summary>

The shipping threshold is based on the post-discount subtotal. This matches how Shopify provides shipping rates when set up directly within Shopify.&#x20;

</details>

<details>

<summary>I want to test my shipping threshold! What should I do about the progress bar in my cart?</summary>

There are two options for how to correctly update your progress bar for a shipping threshold test!

**Option 1:** Use Intelligems' progress bar! See our integration guide [here](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration) on how to integrate this with your site.

**Option 2 (more advanced):** Use our [JavaScript API](https://docs.intelligems.io/developer-resources/javascript-api/user-object) to look up which test group a visitor is in, then update your progress bar with custom code. This is only necessary if your progress bar has a unique design or specific tiers you want to preserve.

</details>

<details>

<summary>What happens when I end my shipping test?</summary>

If the test was run using the Third Party Rate Carrier, the rate carrier will no longer provide shipping rates, and we will restore the rates that we removed when you started the test.

</details>

<details>

<summary>Can I run more than one shipping test at the same time?</summary>

No, you cannot even have more than one pending and/or running shipping test at the same time! This is because Intelligems installs the rate carrier when you set up a shipping test, and it can cause issues if you create or start another shipping test at the same time. If you want to create a new shipping test, you'll need to end any live shipping tests, and/or delete any pending shipping tests.

</details>

<details>

<summary>Can I run a shipping test on specific products?</summary>

At the moment, Intelligems doesn't support running shipping tests at the **product level. S**hipping tests can only be applied **sitewide** or based on broader cart conditions like cart value or destination.

This limitation exists because Shopify doesn’t offer a straightforward way to assign different shipping rules to specific products within the same test environment. Since shipping is calculated at the cart level, it's tricky to ensure a consistent and accurate experience when trying to apply different shipping logic to only a subset of products without causing conflicts or confusion at checkout.

That said, if you’re looking to test how shipping impacts conversion or AOV, we can help you structure a sitewide test that isolates the variable cleanly. Feel free to reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) with any additional questions.

</details>

<details>

<summary>Can I run a shipping test in a currency other than my store's default currency?</summary>

**Yes, you can run shipping tests in currencies other than your store's default currency. You can update the currency for the shipping rates by using the Rate Currency dropdown at the top of the "Set Rates Per Group" test setup step.**

However, there's an important technical limitation to be aware of:

**How shipping thresholds are calculated:**

* Shipping thresholds (like "free shipping over $50") will always be calculated using your store's **default currency**
* This happens because Shopify's third-party rate carrier API (which Intelligems uses to run shipping tests) only receives cart totals in the store's default currency
* The threshold amounts you set in your shipping test will be interpreted in your default currency, regardless of what currency the customer is viewing

**Example:**

* Store default currency: USD
* Customer viewing in: EUR
* Shipping test threshold: $50 free shipping
* The system will check if the cart total is ≥ $50 USD (converted from the EUR cart value), not €50

</details>

<details>

<summary>I duplicated my shipping test. What are the steps I need to take to complete the setup?</summary>

Once you've duplicated a shipping test, you will need to edit the test and select the profiles, zones and rates that you'd like to test. [Here is a video](https://www.loom.com/share/e7dd1ec7b5174eb6ac0fefdf7ea6df75) walking through these steps. Please reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions!

</details>
