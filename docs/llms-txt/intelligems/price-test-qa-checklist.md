# Source: https://docs.intelligems.io/price-testing/price-test-qa-checklist.md

# Price Test QA Checklist

This QA list is specific to a price test. If you are QAing a shipping test, please check out [this article](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist)!

Before heading to your site, there are a few things you should check to make sure your integration is functional:

* [ ] Is Intelligems JavaScript in your live theme? Check out [this article](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) for more information on where to find this.
* [ ] If you are using the [Checkout Script integration](https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts), is the Intelligems Checkout Script live in the Script Editor app?

Once you have confirmed both of those items are true, you can preview the test on your live site. Enter Preview mode by clicking the `...` next to your test and select `Preview`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-cb507b5295da0da7f5f07ff1a316b4851eaf8c86%2F10%20-%20Open%20Preview.gif?alt=media" alt=""><figcaption></figcaption></figure>

This will open your site up in a new window with the Intelligems preview widget enabled. In the preview widget, you'll see:

1. The name of the test you are previewing in the top left
2. A dropdown to switch between different test groups in the bottom left
3. A toggle to highlight any replacements in the top right
4. An edit button in the bottom right. This enables integration mode where you can edit price selectors and text replacements

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-dea4176bb6abc678c2b5b43aa11f2a896a76948c%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please note that if you sell in multiple currencies, a price test which includes prices higher than the control group's prices may have implications for any non-default currencies if they are set to dynamically convert against your store's default currency.\
\
In Shopify Markets, or wherever your store's currency pricing is managed, be sure to set non-default currency prices as fixed/static for the duration of the test if you would like to avoid any unintended price increases in these markets.
{% endhint %}

To get started in preview mode, turn the `Highlight Replaces` toggle on in the top right corner of the widget to highlight the prices in your test. This will highlight all of the prices that have been tagged on your site in green or blue.

* [ ] Confirm that any prices tagged in green *are* part of the test. Green highlighting means we recognize that element is a price, and *it is being changed* by the Intelligems app in accordance with the different groups for the test you are previewing.
* [ ] Confirm that any prices tagged in blue *are not* part of the test. Blue highlighting means we recognize that element is a price, but *it is not* being changed by the Intelligems app because that product is not included in the test you are previewing. This is important as you may test this price in the future, so we want to make sure we know its a price.
  * [ ] Is the price of a product *that is included in the test* highlighted blue? This most likely means that we are not able to tell which product and/or variant ID this price is for. Follow [these steps](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element) to add the `data-product-id` and/or `data-variant-id` attribute to that price element so that we are able to tell which product it is for.
* [ ] Confirm that the price for each product and variant that are part of the test matches the test designed in the app for all test groups. You can switch groups with the drop down in the bottom left corner of the preview widget. A few pages we recommend checking:
  * [ ] Homepage
  * [ ] Collection Pages
  * [ ] Search Bar
  * [ ] Search Results
  * [ ] Product Page
  * [ ] Recommended Items on Product Page (e.g. `You May Also Like` or `Recently Viewed`)
  * [ ] Upsells in Cart
  * [ ] Product Quiz
  * [ ] Landing pages
  * [ ] Navigation
* [ ] Confirm that the below is all true on the Product Page:
  * [ ] The correct price displays for each test group. Be sure to check out different variants if this is an option.
  * [ ] Bulk purchase and/or subscription options match the live site and/or test design.
  * [ ] Ratings and/or reviews match the live site.
  * [ ] Other media, such as images, video and text, match the live site.
  * [ ] Text is being updated if it references price. For example, text that says `20% off for subscriptions` or references value of individual items in a bundle should update accordingly.

Now that you have confirmed prices look right everywhere on the site, go through the add to cart process and click checkout for a handful of products that are a part of the test.

* [ ] Confirm that the status of duplicate products (if applicable) has been set to Unlisted.
* [ ] Confirm price is being calculated correctly at each step (e.g. in the mini cart, on the cart page, and on the checkout page) based on which test group is selected in the widget. *Note that if you are using Duplicate Products for your test, the price should match the test group in the cart.*
* [ ] Increase the quantity of a test item to two from within the cart; confirm that the prices are still correct.
* [ ] If you offer options other than one-time purchase, such as subscription or bulk, confirm that these are correct at each step.
* [ ] If there is custom code for creating bundles within the site (i.e. if you add all the products that are part of the bundle and the discount is applied), confirm that functionality is working properly.
* [ ] If you have a quick buy button (e.g., Buy with ShopPay) in cart or at checkout, confirm that the price is correct when you use this functionality. Please note that these buttons likely won't work for price tests if they are found on the PDP or collections pages.
* [ ] Confirm that `ig_discount` or other `ig_items` are not showing in the cart or at checkout.
* [ ] Confirm that any payment plan options (e.g. AfterPay or ShopPay) are calculating monthly payments correctly if available.
* [ ] Compare shipping rates to the live site. This is most relevant if there are custom shipping rates set up.
* [ ] Add to cart from all landing pages from different test groups and confirm the price at checkout is correct.
* [ ] **We highly recommend placing a test order. This is particularly important in the below scenarios:**
  * [ ] If you are testing subscription products - once you have placed your test order, check the refill prices in your subscription app.
  * [ ] If you use Line Item Properties for any information that is pertinent after the order has been submitted, such as customization information. **If you are not on Shopify Plus, these Line Item Properties are not compatible with Functions, and they will be wiped from the order.**

{% hint style="info" %}
Check all of the above items in mobile as well. Here is a [guide](https://www.browserstack.com/guide/view-mobile-version-of-website-on-chrome) on how you can view mobile mode on your desktop on Chrome.
{% endhint %}

Once you have confirmed all of the above items look correct, you can hit start on your test in the app! Please [reach out to Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions.
