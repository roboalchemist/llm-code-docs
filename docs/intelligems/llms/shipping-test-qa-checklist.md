# Source: https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist.md

# Shipping Test QA Checklist

{% hint style="info" %}
This QA list is specific to a shipping test. If you are QAing a price test, please check out [this article](https://help.intelligems.io/qaing-your-new-test)!
{% endhint %}

## Prerequisites: How Shipping Tests Work:

When you create and save your shipping test, Intelligems will automatically be added as a [third party rate carrier](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/enabling-shipping-carriers) in your Shopify admin. With the Intelligems rate carrier installed, once you start your test, Intelligems will provide rates to shoppers at checkout based on their test group, cart value and item weight, if relevant.

## What to Check First:

Before heading to your site to preview your test, there are a few things you should check to make sure your integration is functional:

* [ ] Is Intelligems JavaScript in your live theme? Check out [this article](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) for more information on where to find this.
* [ ] Has Intelligems been added as a rate provider in Shopify? You can follow the steps below to check this:
  1. From your Shopify admin console, navigate to 'Settings' in the lower left corner and select the 'Shipping and Delivery' tab.
  2. Select the shipping profile you've chosen to run your shipping test in.
  3. Scroll down to the zone you've chosen to run your shipping test in.
  4. In the zone you'll be testing in, you should see "Intelligems Shipping (Rates priovided by app)" under "Carrier and app rates" like the screenshot below.

     <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-3eec3961119132b89fef02a5037e030b4b1883ab%2FScreenshot%202024-02-22%20at%2011.44.04%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>
  5. If you do not see 'Intelligems Shipping (Rates provided by app)' listed, please [reach out to Intelligems Support ](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)for help troubleshooting.

## Previewing your Test:

Once you have confirmed both of those items are true, you can preview the test on your live site. Enter Preview mode by clicking on the eyeball icon next to your test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8ea64d8459b26f69a8b992af991aeb457d142a2e%2FScreenshot%202024-12-05%20at%2010.13.31%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>

This will open your site up in a new window with the Intelligems preview widget enabled. In the preview widget, you'll see:

1. The name of the test you are previewing in the top left
2. A dropdown to switch between different test groups in the bottom left
3. A toggle to highlight any replacements in the top right
4. An edit button in the bottom right: this enables integration mode, where you can edit price selectors and text replacements

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-1defc4f1a22458167719b236da5b7fb1f608f1a3%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Step 1: Confirm that Onsite Edits are working correctly

Did you set up any [Onsite Edits](https://docs.intelligems.io/general-features/onsite-editor) for your test? If so, view any locations you used the Onsite Editor to change shipping prices or language on your store, such as a banner or FAQ page. Confirm copy or images are correctly updating when switching the test group in the Intelligems Preview Widget. Note that you may need to hard refresh when switching groups in the widget!

### Step 2: Confirm that the Intelligems Progress Bar is working correctly

Did you add the Intelligems [Progress Bar](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration)[ ](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration)to your cart? If so, confirm that the threshold is updating when you switch test groups (if you are testing thresholds), and that the math is correct on the bar as you add and remove items to the cart.

### Step 3: Confirm that you are getting the correct shipping rates in cart

Choose one of the test groups, and empty your cart if it is not already. Add a product, or a few products, to your cart and proceed to the checkout page. Enter address information (either your own, or a test address that is within the profile/zone you are testing) so that you can proceed to the shipping step. Confirm that your test rate(s) are showing up here. A few things to note:

* Your test rate will include "Intelligems Preview:" at the beginning of the rate name. This is expected, and will only show up in Preview Mode so that you know where the rate is being provided from in case it has the same name as your normal rates.
* You will still see the rate(s) that you've chosen to test. This is because Intelligems removes the rates you are testing from Shopify when you start your test.
* Be sure to test multiple scenarios to ensure the rates are always being provided correctly. This list is not exhaustive, and these may not all be applicable to your site, but a few scenarios we recommend testing include:
  * Below your shipping threshold
  * Above your shipping threshold
  * Different shipping tiers
  * When using a discount
  * Adding to cart from different locations on the site
  * Adding products from different shipping profiles and zones
  * Test on multiple devices and browsers (such as desktop Chrome and mobile Safari) to confirm there are no discrepancies
  * Test using discounts to confirm shipping rates are still as expected

Complete these steps in each test group, being sure to empty your cart when you switch to a new test group! If you notice any issues, or have any questions, please feel free to [reach out to Intelligems support!](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)

### What happens next?

Now that you've completed the QA checklist for your shipping test, you can start the test!
