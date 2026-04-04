# Source: https://docs.intelligems.io/shipping-testing/ending-a-shipping-test.md

# Ending a Shipping Test

{% hint style="info" %}
The contents of this article are only relevant if you are using the Intelligems Carrier Rate Implementation of the shipping test. If you are using checkout scripts to run your shipping test, please[ reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to end your test!
{% endhint %}

## Step 1: Press the Stop Button

To end a test, navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems portal. Once you're there, locate the test you'd like to end in the Intelligems tests console. Click the stop button.

## Step 2: Configure the Shipping Rates in Shopify to Roll Out

Navigate to "Settings" → "Shipping and Delivery" from within the Shopify admin console and select the shipping profile(s) you'd like to update. Update to match what you'd like to roll out.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-6a026ad03d457fa8cd4139a9d1b7cb410af91d5f%2FScreenshot%202024-12-05%20at%2011.46.16%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

## Step 3: Update Your Progress Bar, if Applicable

If you used an Intelligems shipping progress bar during your test, you can continue to use it for a Shopify-powered free shipping offer. You'll simply need to create a sitewide [free shipping offer experience](https://docs.intelligems.io/personalizations/personalization-modifications/offer-modifications#free-shipping-offer) in Intelligems and select the "powered by Shopify" option.

## Step 4: Update Any References to the Shipping Policy on Your Site, if Needed

Often these are addressed using the Intelligems Onsite Edit feature during the test, but will revert to whatever is configured in your theme once the test has ended. If you've chosen to roll out a new shipping fee, you'll want to change these in your theme. A few spots to check include:

* Banner Text
* Shipping Policy Page
* FAQ's

{% hint style="success" %}
We recommend executing all steps of these instructions as concurrently as possible to ensure a seamless experience for your store's customers!
{% endhint %}
