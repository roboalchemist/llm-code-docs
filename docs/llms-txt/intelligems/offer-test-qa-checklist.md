# Source: https://docs.intelligems.io/offer-experiences/offer-test-qa-checklist.md

# Offer Test QA Checklist

## How Offer Tests Work:

When you create and save your Offer Test, Intelligems will automatically create the necessary Discount Function in your Shopify account. With the Discount Function created, once you start your test, Intelligems will provide the correct discounts to your shoppers based on their test group and other defined criteria.

## What to Check First:

Before heading to your site to preview your test, there are a few things you should check to make sure your integration is functional:

* [ ] Is Intelligems JavaScript in your live theme? Check out [this article](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) for more information on where to find this.
* [ ] Have you added the necessary snippets for any relevent merchandising components? Check out [this article](https://docs.intelligems.io/personalizations/personalization-modifications/offers-integrating-widgets) for more information on how to do this.

## Previewing your Test:

Once you have confirmed both of those items are true, you can preview the test on your live site. Enter Preview mode by clicking on the eyeball icon next to your test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8ea64d8459b26f69a8b992af991aeb457d142a2e%2FScreenshot%202024-12-05%20at%2010.13.31%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>

This will open your site up in a new window with the Intelligems preview widget enabled. In the preview widget, you'll see:

1. The name of the test you are previewing in the top left
2. A dropdown to switch between different test groups in the bottom left
3. A toggle to highlight any replacements in the top right
4. An edit button in the bottom right: this enables integration mode, where you can edit onsite content

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-1defc4f1a22458167719b236da5b7fb1f608f1a3%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Step 1: Confirm that Onsite Edits are working correctly

Did you set up any [Onsite Edits](https://docs.intelligems.io/general-features/onsite-editor) for your test? If so, view any locations you used the Onsite Editor to change language on your store to merchandise the offer, such as a banner or content on the PDP. Confirm copy or images are correctly updating when switching the test group in the Intelligems Preview Widget. Note that you may need to hard refresh when switching groups in the widget!

### Step 2: Confirm that any Components are visible and working correctly

Did you add an [Offer Message](https://docs.intelligems.io/personalizations/personalization-modifications/offers-integrating-widgets#offer-message), [Quantity Buttons](https://docs.intelligems.io/personalizations/personalization-modifications/offers-integrating-widgets#quantity-buttons) or [Progress Bar](https://docs.intelligems.io/personalizations/personalization-modifications/offers-integrating-widgets#offer-progress-bar) to your Offer Test? If so, confirm that each Component is visible on your site, in the correct location and working correctly when you switch test groups.

### Step 3: Confirm that you are getting the correct discounts or gifts in cart and at checkout

Choose one of the test groups, and empty your cart if it is not already. Add the appropriate product, or products, to your cart to trigger the offer defined for that test group.

* [ ] If you are testing a **Discount Offer** (Amount Off Product, Amount Off Order or Volume Discount), you should see the discount show up in both the cart and at checkout for any products it is applicable to.
* [ ] If you are testing a **Free Gift Offer**:
  * [ ] If the gift is set up to be automatically added to cart, you should see the defined product get auto-added and discounted to free once you have met the minimum requirement for it.
  * [ ] If the gift is not set up to auto-add, you will need to manually add the defined product to cart and will then see it discounted to free as long as you have met the minimum requirement for it.
  * [ ] You should see the gift get removed from cart if you drop below the minimum requirement.
* [ ] If you are testing a **Shipping Offer**, you will need to enter address information on the checkout page (either your own, or a test address that is within the country you are testing) so that you can see shipping rates. Confirm that the correct rate(s) are discounted to free at the correct thresholds.

Be sure to test multiple scenarios to ensure the Offers are always being provided correctly. This list is not exhaustive, and these may not all be applicable to your site, but a few scenarios we recommend testing include:

* Below the defined minimum
* Above the defined minimum
* When using a discount code that should stack
* When using a discount code that shouldn't stack
* Adding to cart from different locations on the site
* Adding products from different shipping profiles and zones for shipping offers
* Test on multiple devices and browsers (such as desktop Chrome and mobile Safari) to confirm there are no discrepancies.

Complete these steps in each test group, being sure to empty your cart when you switch to a new test group! If you notice any issues, or have any questions, please feel free to [reach out to Intelligems support!](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)

### What happens next?

Now that you've completed the QA checklist for your Offer Test, you can start the test!
