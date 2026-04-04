# Source: https://docs.intelligems.io/price-testing/testing-prices-with-subscriptions/testing-prices-with-recharge-2.0-or-stay.ai.md

# Testing Prices with Recharge 2.0 or Stay.Ai

{% hint style="danger" %}
This article only applies if you use Stay.AI, you are using Shopify Plus, and have access to the Script Editor app. If you are using Stay.AI, you must also only offer one delivery option (i.e. Every 30 Days). If any of these are not true, please see our following guides on using duplicate products, or reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).
{% endhint %}

### Step 1: Authorize the integration

In the Intelligems App, navigate to "Integrations" on the bottom left.

You need to create an API key from your Stay.AI dashboard. Log into Stay, under Settings > API keys, create a new key.

* Name: **Intelligems**
* Description: **Used for Intelligems <> Stay Integration**
* Email: **Your email**
* Scopes: **All**

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-280d834c01d4d0e880125efe6b330225e8c5387f%2Fimage.png?alt=media)

Then Copy the API key into the Intelligems dashboard into the Stay.ai API key

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-80bead7632ad5d80d9de6cb25d325efecca28f52%2Fimage.png?alt=media)

### Step 2: Set up test in the Intelligems app

See our detailed guide [here](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test) on setting up your Price Test. Make sure to do this ***after*** you have authorized the integration with your subscription provider. If you have not, you should delete your old test and create a new test from scratch.

### Step 3: QA your test

Assuming you've already completed the [integration](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts) that is required for Price Testing, the next step is to QA your test! Because tests that involve subscriptions have more moving pieces, we recommend spending some extra time on QA - follow [this checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist) to make sure you don't miss anything!

### Handling custom widgets and UI

If you're not using a standard widget from your subscription provider on your PDP, our onboarding team would be happy to help integrate your own custom UI with Intelligems. It's relatively straightforward, we just need to identify the PDP elements identified in this example screenshot.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-70aa7d844f9e05c9ffb91e112576588c1249aaa5%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

If you have questions, please reach out to support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
