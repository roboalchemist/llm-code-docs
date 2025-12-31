# Source: https://docs.intelligems.io/checkout/checkout-test-qa-checklist.md

# Checkout Test QA Checklist

## How Checkout Tests Work:

When you create and save your Checkout Experience Test, you configure blocks in Intelligems and add them to your Shopify checkout using unique Location IDs. Once you start your test, Intelligems will automatically display the correct block to each shopper based on their test group and other defined criteria.

## What to Check First:

Before heading to your site to preview your test, there are a few things you should check to make sure your integration is functional:

* [ ] Is Intelligems JavaScript in your live theme? Check out [this article](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) for more information on where to find this.
* [ ] Have you added the necessary Intelligems A/B Testing blocks to your Shopify checkout? Check out [this article](https://docs.intelligems.io/testing-checkout-experiences#step-5-add-blocks-to-shopify-checkout) for more information on how to do this.

## Previewing your Test:

Once you have confirmed both of those items are true, you can preview the test on your live site. Enter Preview mode by clicking on the eyeball icon next to your test.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8ea64d8459b26f69a8b992af991aeb457d142a2e%2FScreenshot%202024-12-05%20at%2010.13.31%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>

This will open your site up in a new window with the Intelligems preview widget enabled. In the preview widget, you'll see:

1. The name of the test you are previewing in the top left
2. A dropdown to switch between different test groups in the bottom left
3. A toggle to highlight any replacements in the top right
4. An edit button in the bottom right: this enables integration mode, where you can edit onsite content

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-1defc4f1a22458167719b236da5b7fb1f608f1a3%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Step 1: Confirm that blocks are displaying correctly

Now it's time to verify your blocks are appearing correctly in your checkout. Choose one of the test groups from the preview widget dropdown, and add a product to your cart.

#### Navigate to the checkout page

Proceed through your cart to the checkout page. This is where your blocks will appear.

#### Verify the correct block is visible

**If you're testing one block in multiple locations:**

* [ ] Check that the block appears in the correct position for the selected test group
* [ ] If you're in the "Header" group, confirm the block appears near the top/header area
* [ ] If you're in the "Below Total" group, confirm the block appears below the order total
* [ ] Switch between test groups and verify each block appears in its designated position
* [ ] Confirm that only one block appears at a time (not multiple blocks simultaneously)

**If you're testing different content in the same checkout location:**

* [ ] Check that the correct design/content appears for the selected test group
* [ ] If testing different colors, verify the correct color variation shows
* [ ] If testing different text, verify the correct messaging appears
* [ ] If testing different icons, verify the correct icons display
* [ ] Switch between test groups and confirm the content updates while staying in the same position

### Step 2: Check block styling and formatting

Regardless of test type, verify that:

* [ ] Icons display correctly and are the right size
* [ ] Text is readable and properly formatted
* [ ] Colors match your configuration
* [ ] Spacing looks correct (not too cramped or too spread out)
* [ ] The block fits well within the checkout design
* [ ] All badges within the block are visible (if you have multiple badges)

Be sure to test multiple scenarios to ensure the blocks are always displaying correctly. This list is not exhaustive, and these may not all be applicable to your site, but a few scenarios we recommend testing include:

* Different checkout states and products
* If you have a control group with no block, verify nothing appears
* Verify targeting is working (if applicable)
* Test on multiple devices and browsers (such as desktop Chrome and mobile Safari) to confirm there are no discrepancies.

Complete these steps in each test group, being sure to refresh or newly navigate to checkout when you switch to a new test group! If you notice any issues, or have any questions, please feel free to [reach out to Intelligems support!](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)

### What happens next?

Now that you've completed the QA checklist for your Offer Test, you can start the test!
