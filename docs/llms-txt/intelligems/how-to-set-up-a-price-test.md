# Source: https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test.md

# How to Set Up a Price Test

## Step 1: Create a new test

Go to the **Tests** tab in the left menu in the Intelligems app. Click **Create New Test** above the experiments table.

Enter a **Name** and **Description** for your test. This information is internal only - add enough detail so you'll remember your goals when reviewing results weeks later. Select **Pricing Test** and **Create Test**.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0a39ce7ab59190f09e46c94e4ef56bf84aff4273%2Fpricing.gif?alt=media" alt=""><figcaption></figcaption></figure>

## Step 2: Create your test groups

Create 2-5 groups by clicking **+**. Name each group and use the slider to allocate traffic percentage. Click **Next step** when ready.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-2739082419b331410d0060bb73416741fc77043b%2Ftest%20groups.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The more groups you have, the longer it will take to get statistically significant results. You’ll need about 300 orders for each group in the test to detect a 10% change in conversion with 90% confidence.
{% endhint %}

## Step 3: Choose your products

In the Modifications tab, click **+ Add/Remove Products** and select which products you want to include in the test by checking the boxes to the left of each product.

**A few tips and tricks:**

* You can select all products if you'd like to test your whole store, or all products matching the filters you have set up, by using the select all box at the top left-hand side of the table. Once you click the select all box, you will also need to click **Select all 20+ products in your store**.

{% hint style="info" %}
If you have subscription products, you may be missing the select all checkbox! Please reach out to [Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for assistance with this.
{% endhint %}

* Use the search bar at the top of the table if you are looking for a specific product
* The filter drop downs to the left of the table are helpful when looking for specific vendors, tags, product types, or statuses.

{% hint style="info" %}
If you have 250+ Product Types, Vendors or Product Tags set up in Shopify, Shopify will not allow us to load them all. In this case, you can use the search bar in the Intelligems app to filter instead. For example, if you were looking for all products with the product tag 'Test', you would want to search for 'tag:Test'. For product type, you would use 'product\_type:Test' and for vendor, you would use 'vendor:Test'. Please reach out to [Intelligems support](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) if you have any questions on this!
{% endhint %}

Once you have selected all necessary products, click 'Add' in the top right corner.

## Step 4: Set the test prices

There are three different options for filling in your prices:

<details>

<summary>Uploading a Spreadsheet</summary>

This is best suited for cases where you have already set up your prices in a CSV or Excel file.

To upload a spreadsheet, first click on the 'Quick Fill' button, navigate to the 'Fill By Upload' tab, and then click 'Download Template'. Wait until we load the template, then click 'Template Ready - Click to Download' - your download will start automatically.

<img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-a2dda3e5ee61de8782a0e00a8d433d1abd6e116a%2F06%20-%20Download%20Template.gif?alt=media" alt="" data-size="original">

Using Microsoft Excel, Google Sheets, Numbers, or another spreadsheet editing tool, manually input the prices for the test groups and save the file with a .csv, .xls or .xlsx extension.

The following fields (columns) are **required** in the uploaded file.

* product\_title
* product\_id
* variant\_title
* variant\_id
* handle
* Price - \[Test Group Name] (*for each test group*)
* Compare Price - \[Test Group Name] (*for each test group*)

The rest of the fields in the template are provided for reference and are not required.

\
Back in the Intelligems app, click the 'Upload Prices' button and select the saved .csv, .xls or .xlsx file. Once it has uploaded, save the test to see the price changes.

</details>

<details>

<summary>Quick Fill</summary>

This is best suited for cases where you want to test uniform changes to all products in the test, such as a 10% or $10 dollar increase and decrease across all test products. Autofill is based on the control group product prices that are pulled in from Shopify.

To use this option, click 'Quick Fill', then configure the percentage or dollar amount change for each group and whether the change should be an increase or decrease relative to the control, as well as whether the amount should be rounded. Note that increase / decrease, the amount and % / $ selector are three separate fields. Click 'Apply All' when you are done.

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-6f04cfbdac942a52ebb1cee7c3cdf4f9c21acc67%2F07%20-%20Quick%20Fill.gif?alt=media)

</details>

<details>

<summary>Manually Set Prices</summary>

This is best suited for cases where you'd like to configure the prices for each product separately, such as a $10 increase to Product A and a $5 increase to Product B.

Input the prices and 'compare at' prices (if desired) for each product and test group in the table. You can drag prices from one cell to the next if the prices are the same.

You can expand all rows or collapse all rows by pressing 'Expand All' or 'Collapse All' at the top left of the table.

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-d5d164cacc99e01157c443f9774c564598059e5b%2F08%20-%20Set%20Prices%20manually.gif?alt=media)

</details>

{% hint style="info" %}
There are two relevant fields for each entry:

* Price: The price of the product; this is the price the user will actually be charged when they purchase the product in the given test group, before any discounts.
* Compare Price: Also known as the 'compare at price', this price will be shown as a strikethrough. This field is optional and there is no need to populate the 'Compare Price Field' if you do not wish to show a strikethrough. Your theme must be configured to show strikethroughs in order for Intelligems to display one.
  {% endhint %}

Click 'Next step' when you are done setting up your prices.

## Step 5: Set up targeting if needed

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using its random split-test mechanism. This assignment is determined at the first visit and is stored via a first‐party cookie, ensuring that the visitor remains in the same group on subsequent visits during the price test period.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the [Mutually Exclusive Tests](https://docs.intelligems.io/general-features/targeting/mutually-exclusive-experiments) option.

You can learn more about targeting [here](https://docs.intelligems.io/general-features/targeting)! Once you are done setting up targeting, or if you're skipping this step, click 'Next step'.

## Step 6: Save and Preview your Test

Once you have completed all the steps, you'll be able to save your test with the green **Save** button in the top right.

In the **Preview** tab, you'll find a few options to load the test's preview:

* **Open Full Screen Preview:** this will open your website with the Intelligems widget loaded, so you can easily alternate between test groups to preview each group's experience, as well as do onsite edits if necessary (see [step 8](#step-8-edit-content-on-your-site-if-needed) for more details). You can also choose which theme you'd like to preview in if you need to be somewhere other than your live theme!
* **Open Mobile Preview:** you'll see a QR code for each test group, so you can load the preview directly on your mobile device.
* **Copy Preview URL:** this will copy the preview URL to your clipboard automatically.

{% hint style="danger" %}
Don’t worry, this won’t set the test live yet and you can come back and edit if you need to make changes!
{% endhint %}

## Step 7 (optional): Set up your Goals

In the 'Goals' tab, you'll find the option to select what your primary goal is, as well as whether analytics should by default consider only orders containing certain products, or orders containing any products in your shop.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-46f4a7c5c7552888c83a54e1b59aaa3412f0b832%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Neither of these choices will affect what data is tracked or available to view, but will allow Intelligems to display analytics so that the most important information is surfaced first. You can change this later after the test has started by changing the option in your Analytics filters.

## Step 8 (optional): Edit content on your site if needed

This step is also optional. This tool allows you to dynamically update content on your site based on a visitor's test group. Check out [this article](https://docs.intelligems.io/general-features/onsite-editor) for more details on configuring this option.

Please note this is not how you should update price components on your site for a Price Test - that should be completed by [tagging your prices](https://docs.intelligems.io/getting-started/pricing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices)!

## What happens next?

Now that you've created your pricing test, you can QA your test using [this checklist](https://docs.intelligems.io/price-testing/price-test-qa-checklist)! If you have not completed the integration yet, please see our integration guides [here](https://docs.intelligems.io/price-testing/price-testing-integration-guides).
