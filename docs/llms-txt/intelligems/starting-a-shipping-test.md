# Source: https://docs.intelligems.io/shipping-testing/starting-a-shipping-test.md

# Starting a Shipping Test

{% hint style="info" %}
The contents of this article are only relevant if you are using the Intelligems Carrier Rate Implementation of the shipping test. If you are using checkout scripts to run your shipping test, [please reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) to get your test launched!

Additionally, to use the Intelligems Rate Carrier out of the box, your store needs to be on the Advanced Shopify or Plus plan. If you're on the Shopify plan or lower, then you'll need to reach out to Shopify Support to enable third-party carrier-calculated shipping; see more on that [here](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/enabling-shipping-carriers). Additionally, please note that as of January 1st, 2023, Shopify will be no longer support this feature for Shopify Basic plans.
{% endhint %}

## **Step 1: Confirm Intelligems JavaScript is in Your Live Theme**

In addition to Intelligems JavaScript, confirm any other theme changes completed during the integration are in your live theme as well. **If not**, please publish the script and any changes before proceeding.

## **Step 2: Press the Start Button**

In the Intelligems app, navigate to the A/B Tests tab and click the green play button next to the shipping test you are wanting to start.

## Step 3: Verify that Intelligems has been Added as a Rate Provider

1. From the Shopify admin console, navigate to Settings → Shipping and Delivery.
2. Select the relevant shipping profile(s).

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-6a026ad03d457fa8cd4139a9d1b7cb410af91d5f%2FScreenshot%202024-12-05%20at%2011.46.16%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

3. Scroll down to the section titled "Shipping zones" and navigate to the region(s) you've chosen to run your shipping test in. Verify that Intelligems is installed as a rate provider. This will look like the below.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-40c8064053ec9cf6721ed4b38115a526d7a91a73%2FScreenshot%202024-12-05%20at%2011.48.56%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 4: Check Your Site**

Now that the test is live, we recommend going through the add to cart and checkout process in a few incognito browsers so you can get added to different test groups and ensure everything is working as expected. If you have not already QA'ed your test before launching it, we recommend going through [this checklist](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist). [Please reach out to our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) with any issues!
