# Source: https://docs.intelligems.io/getting-started/best-practices/best-practices-during-a-test.md

# Best Practices During a Test

## QA'ing your Test (Before and Throughout the Test)

Before launching any new test, it is important to QA the test to ensure everything is working as you would expect. See our checklists below for more information on how to QA each type of test:

* [Price Test QA Checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist)
* [Shipping Test QA Checklist](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist)
* [Content Test QA Checklist](https://docs.intelligems.io/content-testing/content-test-qa-checklist)

We also recommend doing a sweep through the site immediately after starting the test, and at least every few days during the test to ensure nothing has changed that would affect the test (after all, sites change frequently). The best way to do this is in a **new** private or incognito window; this will get you assigned randomly to a new test group.

***

## Handling External Areas that Mention Price or Shipping Rates

We recommend thinking through any areas other than on your Shopify site that could create inconsistencies with the test. Where possible, we will do our best to integrate with these external sources, but in certain cases we may recommend removing these instances. Some examples include:

* **Advertisements:** It is often possible to keep test groups consistent with ad prices utilizing traffic selectors during test setup. Please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have questions on this!
* **Google Shopping:** Monitor your Google Merchant Center frequently throughout the test. We will do our best to work with you to minimize issues with your Google Shopping feed. We also recommend turning on automatic price updates in your Google Merchant Center. See [here](https://support.google.com/merchants/answer/3246284?hl=en) for Google's documentation on this feature.
* **A few other places to think about:** retargeting and newsletter emails, landing pages, affiliate marketing, social handles, PDP sections

***

## Theme Changes

It is generally recommended to avoid major theme changes while a test is live. Examples include:

* Major changes to theme code
* Changes to text that mentions price or shipping rates (relevant if the test utilizes the find-replace function)
* Installing or reconfiguring apps that are close to checkout (e.g. cart or upsell apps)

***

## Customer Experience

Pay close attention to customer experience issues that arise. While issues are rare, we always recommend keeping your customer support team in the loop on tests. Additionally, we recommend equipping the team with a discount code to honor lower prices in the rare occurrence that a customer sees multiple prices (for instance, on multiple devices).

***

## Monitoring Results

While it may take a while to start seeing significant results, we recommend checking the results in the Intelligems analytics dashboard frequently. This will help you discover any potential issues, and if necessary, can prompt you to end tests early if there's a material effect on conversion and profit.

***

## Iterate and Learn

A/B testing is an iterative process. Use the insights gained from each test to inform future tests. Document your findings and build on what you learn to continually improve your store’s performance.
