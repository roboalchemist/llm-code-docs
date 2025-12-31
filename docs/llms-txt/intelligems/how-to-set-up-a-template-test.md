# Source: https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-template-test.md

# How to Set Up a Template Test

Template testing allows you to split-test Shopify templates to determine which is the best for conversion, revenue, and profit. Take a look at Shopify's documentation on templates [here](https://help.shopify.com/en/manual/online-store/themes/theme-structure/templates)!

{% embed url="<https://www.loom.com/share/09533b20ec24444191e621001893c7b8>" %}
Video: Setting up a template test in Intelligems
{% endembed %}

{% hint style="warning" %}
Make sure that the Intelligems template snippet is installed in your theme. If you are using the Intelligems Theme Block, it will automatically be added. If you are using the Intelligems javascript snippet, [more information can be found here](https://docs.intelligems.io/developer-resources/intelligems-theme-snippets). This snippet must be included in your theme for template tests to work properly.
{% endhint %}

{% hint style="warning" %}
All templates for a Template Test must be in a live theme.
{% endhint %}

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click 'Create New Test' above the experiments table. Select "Content Test" , then "Template Test", then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5bf931c709fedb6bc8ddc670d392f5caecc58980%2FStep%201.gif?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create a test group for each template variation you want to include in the test. Fill in the Test Name and Test Description for the experiment you are creating. This information is all internal; the more detail you include here the better. Tests can be live for several weeks, and your future self will thank you for including the details here.

You can add new groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. Click ‘Continue’ when you are done.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-e60ceeed21b77b8fccffbfc784190adbec485cd9%2FTest%20Groups.gif?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 3:** Assign a template for each test group

Select a template for each test group. You can choose an existing template or duplicate the template selected for the control group by selecting `Duplicate Control:`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-c83d5b9644709e0ae444f6b04308b3ca452d5df8%2FStep%202.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Please note that only templates chosen for your test groups will be tested. For example, if you choose `product-template-a` (control group) vs. `product-template-b`, only products assigned to the template in the control group will be affected by the test.

If you're testing templates, a visitor will only be included in the test if they visit a page that is by default assigned to the template selected for the control group. Therefore, the template that is currently in use on your site must be chosen as the control group.
{% endhint %}

You can hover over each test group screenshot to view the following options:

* Edit in Shopify: links to the test group template in your Shopify admin (must be a live theme)
* Quick View: opens a snapshot with a desktop and mobile preview of the test group template
* View in Browser: links to a preview of the template in a new tab
* Template Name: opens edit mode for the test group template

If you have made changes to a selected template in Shopify, you can use the "refresh" button next to the test group name to refresh the screenshot shown.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-dc54f1c54560833b5c66de9b8d0d9b1cb2e4b6fa%2FStep%204.gif?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 4: Set up targeting if needed**

Targeting is an optional step. By default, a visitor will only be included in a template test if they visit a page that is by default assigned to the template selected for the control group. Therefore, the template that is currently in use on your site must be chosen as the control group.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

## Step 5: Set Your Test Goals

Finally, select whether analytics should by default consider only orders containing certain products you want to test (for example something related to a particular PDP), or orders containing any products in your shop.\
\
You can always change this later after the test has started by changing the option in your Analytics filters.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-30759deb494b8ba43c416c776fdac30a0f3d3a2c%2FGoals.gif?alt=media" alt=""><figcaption></figcaption></figure>
