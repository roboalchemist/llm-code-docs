# Source: https://docs.intelligems.io/general-features/onsite-editor.md

# Onsite Editor

## What is the Onsite Editor?

Intelligems' Onsite Editor allows you to adjust site text, HTML or CSS for site visitors based on their test group. You will select where you want to update these items and what should be displayed for each test group.

## Why would I need to use the Onsite Editor?

If you're running a price test, Intelligems will automatically update prices on collections pages, the primary price on PDPs, in the cart and at checkout if you have completed your [Price Testing integration](https://docs.intelligems.io/price-testing/price-testing-integration-guides). Similarly, if you're running a shipping test, Intelligems will automatically display a rate at checkout base off of a user's test group. The Onsite Editor is typically *not* required for these elements.

The Onsite Editor is typically used to update copy that may be hard coded into your theme and does not pull from a Shopify product variant (in the case of a price test) or from your shipping settings (in the case of a shipping test). Some examples of where you might use the Onsite Editor include:

* Announcement bar where a shipping offer is displayed while you are testing the shipping threshold
* Hard-coded prices on landing pages or PDPs while running a price test
* The shipping policy page while running a shipping test
* Shipping announcement on a PDP
* To run a content test on a smaller component on your site, such as:
  * Changing the CTA on a button
  * To change the color of a button
  * To change a product description

## How to Set Up an Onsite Edit

From within the test setup flow for any type of test, navigate to the Modifications step and select "Add & Edit changes in Visual Editor" in the Content Edits section - this will bring you to your site with Edit mode enabled. You can also add a new Onsite Edit by previewing your test and clicking the "Edit" button in preview mode.

{% hint style="warning" %}
You'll need to have the [Intelligems script installed](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) in the theme you are working in for the Onsite Editor to be available!
{% endhint %}

Once you are in Edit mode, follow these steps:

1. **Activate the element selector** by clicking the pencil and ruler button (circled in red below), then selecting to either select an element, paste a selector, or describe an element to the AI.

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-cdf632951feaa41e1c026ff425dcf0d87b33afb4%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

   1. **Select an element:** This option will enable a point-and-click flow. Hover your mouse over your page to identify the element you want to edit. The available elements will have a blue highlighting appear around them and you can simply click to select one.
   2. **Paste a selector:** This option will provide you with a text box where you can paste or type the CSS selector you'd like to target. Once you hit submit, you will be notified if this CSS selector matches more than one element, and if so, given the option to target all elements in the list or choose a specific one before setting up the necessary edits.
   3. **Describe element to AI:** This option will provide you with a text box where you can describe the element you'd like to target. Once you hit submit, the AI will work to find the correct element and then you can set up the necessary edits.
2. **Configure your variations** in the popup that appears once you've added your selector and chosen which type of edit you'd like to make. Here you'll define what each test group sees for the selected element. Options include:
   * Custom text for each group
   * Remove the element entirely
   * Leave unchanged for certain groups
3. **Save your edit** by clicking 'Done' and repeat this process for any additional elements you want to modify.
4. **Save your work** using the Save button in the top-right corner once you've finished adding all your Onsite Edits.

A few tips and tricks to keep in mind:

* If you are making a text edit and using the optional "Find" field, the text is case sensitive. You may need to use your browser's inspector tools to determine the case of the text you're replacing. Some fonts render as ALL CAPS but the source text could be lowercase or Mixed Case.
* If you are having trouble targeting the correct element(s) on your site, please see our expanded guide [here](https://docs.intelligems.io/general-features/onsite-editor/selecting-the-right-element) on finding the correct element.
* If you only want your Onsite Edits to occur on a select page or pages, set up [Page Targeting](https://docs.intelligems.io/general-features/targeting/page-targeting)!
