# Source: https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-test-using-our-javascript-api.md

# How to Set Up a Test using our JavaScript API

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click "Create New Test" above the experiments table.

Fill in the Name and Description for the experiment you are creating. This information is all internal - the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here. Select 'Content Test", then "Onsite Edits", and then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f7de4f4d4a5fb1fd5c99bd00db1ae83abcfdb443%2FAPI-%20Create%20New%20Test.gif?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create between two and five groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. When you are done adding groups, click "Next step" in the top right.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-b37b8dbcd56e53048fbd0b39abb406ff684a5acb%2FCreate%20Test%20Groups.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The more groups you have, the longer it will take to get statistically significant results. You’ll need about 300 orders for each group in the test to detect a 10% change in conversion with 90% confidence.
{% endhint %}

## Step 3: Skip "Modifications"

No need to set up any Content Edits, Styles or JavaScript in this step of the set up if you are planning to use our JavaScript API. Go ahead and move on to step 4.

## **Step 4: Set up targeting if needed**

Targeting is an optional step. This tool allows you to apply specific conditions to certain site visitors.

There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

## Step 5: Choose how you'd like to measure your results and save your test

Finally, select whether analytics should by default consider only orders containing certain products you want to test (for example something related to a particular PDP), or orders containing any products in your shop. You can change this later after the test has started by changing the option in your Analytics filters. Go ahead and save the test, and move on to step 6.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-916f96ab2473a85ca5179def3563b28c0ee4a1af%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

## Step 6: Get relevant IDs

Custom content tests require you to know the experiment ID and test group IDs so that you can branch your design or logic accordingly. You can get this information by clicking the "Show Info" button in the more menu:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-bf71e1d6c19fb211f6f3860be91973d1fa4f45b2%2FGet%20Relevant%20IDs.gif?alt=media" alt=""><figcaption></figcaption></figure>

## Step 7: Use the Intelligems window object API to set up your custom test

Now that you have your test group IDs, you can use Intelligems' [window object Javascript API](https://docs.intelligems.io/developer-resources/javascript-api) to get the current user's test group for the given experiment. Once you know the user's test group, you can branch logic and styling with it. For example, you might set a class or show/hide an element to affect styling, or conditional logic in your own Javascript code to provide a different experience.
