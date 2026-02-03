# Source: https://docs.intelligems.io/shipping-testing/how-to-set-up-a-shipping-test.md

# How to Set Up a Shipping Test

## Step 1: Create a new test

Go to the **Tests** tab in the left menu in the Intelligems app. Click **Create New Test** above the experiments table.

Enter a **Name** and **Description** for your test. This information is internal only - add enough detail so you'll remember your goals when reviewing results weeks later. Select **Shipping Test** and then **Create Test**.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-c690e6f7ed68e894583b0935b66158603894dd0c%2FOct-13-2025%2015-41-07.gif?alt=media" alt=""><figcaption></figcaption></figure>

## Step 2: Create your test groups

Create 2-5 groups by clicking **+**. Name each group and use the slider to allocate traffic percentage. Click **Next step** when ready.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-2739082419b331410d0060bb73416741fc77043b%2Ftest%20groups.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The more groups you have, the longer it will take to get statistically significant results. You’ll need about 300 orders for each group in the test to detect a 10% change in conversion with 90% confidence.
{% endhint %}

## Step 3: Select shipping profiles and zones to test

Using the expander for each shipping profile, select the zone(s) where the Intelligems rate will be added. The Intelligems rate will *only* apply to the profiles and zones selected here and will apply to *all* orders that meet the criteria for the selected profiles and zones, subject to other cart value and weight criteria which you'll configure in the next step.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-b56e47ce59251032dcb3f06c12f4ea0ab3781d9f%2FSelect%20Profile.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Consider carefully which profile(s) you add the Intelligems rate to. If your store's products are spread across multiple profiles, adding the Intelligems rate to a subset of profiles may lead to unexpected behavior at checkout. Learn more about how Shopify combines rates [here.](https://help.shopify.com/en/manual/shipping/setting-up-and-managing-your-shipping/shipping-profiles/combined-shipping-rates)
{% endhint %}

## Step 4: Select the rates you want to replace for this test

Once you have selected the profiles and zones you want Intelligems rates to apply to, you will select which rates from those zones you want to test. These rates will be hidden during the test and replaced by an Intelligems rate, which will vary by test group.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-00a412216460c6c7f50f3520801e361aa67801d9%2FRates%20To%20Remove.gif?alt=media" alt=""><figcaption></figcaption></figure>

## Step 6: Configure the Intelligems rate(s)

In this step, you will configure the rate(s) to be added to the previously selected profiles and zones for each test group.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9b8cf9d4f799e295c63e0486397de20aec382723%2FSet%20Rates%20Per%20Group.gif?alt=media" alt=""><figcaption></figcaption></figure>

For each group, choose the rate type that most closely aligns with what you're *testing* (i.e. what you want to change in each test group). See below for some tips on when to select each rate type and examples of combined rates:

## Different Rate Types

![Rates in blue are provided by Intelligems; rates in green are configured in Shopify](https://hs.intelligems.io/hs-fs/hubfs/8-png.png?width=600\&height=48\&name=8-png.png)

#### **Flat Rate:** You are testing rate(s) that are not set up with conditions in Shopify ("flat rates")

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/2-1.png?width=447&#x26;height=95&#x26;name=2-1.png" alt=""><figcaption><p>Example 1: Testing a single flat rate</p></figcaption></figure>

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/1-1.png?width=449&#x26;height=97&#x26;name=1-1.png" alt=""><figcaption><p>Example 2: Testing multiple flat rates</p></figcaption></figure>

#### **Flat Rate with Threshold**: You are testing a flat rate and the threshold for free shipping

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/3-1.png?width=449&#x26;height=115&#x26;name=3-1.png" alt=""><figcaption><p>Example 3: Testing flat rate and a threshold</p></figcaption></figure>

#### **Threshold Only**: You are testing a free shipping threshold but want to keep your existing rates for those that do not reach the threshold

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/4.png?width=449&#x26;height=92&#x26;name=4.png" alt=""><figcaption><p>Example 4: Testing a free threshold with rates under threshold provided by third party app</p></figcaption></figure>

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/5.png?width=448&#x26;height=118&#x26;name=5.png" alt=""><figcaption><p>Example 5: Testing a free threshold with weight-based rates under threshold configured in Shopify</p></figcaption></figure>

#### **Tiered by Price or Weight**:

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/6.png?width=449&#x26;height=115&#x26;name=6.png" alt=""><figcaption><p>Example 6: Testing rates for each weight-based tier</p></figcaption></figure>

<figure><img src="https://hs.intelligems.io/hs-fs/hubfs/7.png?width=445&#x26;height=91&#x26;name=7.png" alt=""><figcaption><p>Example 7: Testing rates and conditions for each weight-based tier</p></figcaption></figure>

#### **Custom**: Have something else you want to test?

[Let us know](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) and we'll see what we can do!

## Step 7: Review your rates

Use the drop-downs to review profiles, zones, and test groups.

1. Select profile and zone to preview
2. Select test group for cart preview
3. Input sample cart totals and weight to see what shipping options will be available at checkout

{% hint style="warning" %}
Rates displayed at checkout during the test may differ from preview if order products are included in multiple shipping profiles.
{% endhint %}

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-8575b0569773069e59a259c5141537ac5fe2e32d%2Fimage.png?alt=media" alt=""><figcaption><p>Review combined rates</p></figcaption></figure>

## Step 8: Enable & customize your progress bar if needed

If you currently show a shipping progress bar on your site or if you would like to include one for your test and you are testing shipping thresholds, it is recommended to use the built-in option from Intelligems found in the [**Global Styles**](https://app.intelligems.io/global-styles/experiences) components so that the bar will update with the test group. Adding the Intelligems progress bar typically requires adding a component to your theme's liquid code and customizing the bar's style in the Intelligems app.

Learn more about adding the Intelligems shipping progress bar and other components [here](https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration).

See below for a few examples of a configured shipping progress bar during a live test.

<table data-header-hidden><thead><tr><th></th><th width="180"></th><th></th></tr></thead><tbody><tr><td><img src="https://d33v4339jhl8k0.cloudfront.net/docs/assets/624c7e54ed4a0c44b4e6013a/images/627c03f7b2de5178f8882dd8/file-GLKo2WKNwT.png" alt=""></td><td><img src="https://d33v4339jhl8k0.cloudfront.net/docs/assets/624c7e54ed4a0c44b4e6013a/images/627c03ff68d51e779443f8bf/file-CFmEk6N22o.png" alt=""></td><td><img src="https://d33v4339jhl8k0.cloudfront.net/docs/assets/624c7e54ed4a0c44b4e6013a/images/627c0405c01fce37d9b12613/file-JoWvYs5xWG.png" alt=""></td></tr><tr><td>Example 1: Under the Free Shipping Threshold</td><td>Example 2: Exceeded the Free Shipping Threshold</td><td>Example 3: Under the Cart Minimum Threshold</td></tr></tbody></table>

## Step 9: Edit content on your site if needed <a href="#step-7-edit-content-on-your-site" id="step-7-edit-content-on-your-site"></a>

This step is also optional. This tool allows you to dynamically update content on your site based on a visitor's test group. Check out [this article](https://docs.intelligems.io/content-testing/find-and-replace) for more details on configuring this option.

## Step 10: Set up targeting if needed

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using its random split-test mechanism. This assignment is determined at the first visit and is stored via a first‐party cookie, ensuring that the visitor remains in the same group on subsequent visits during the shipping test period.

The targeting tool allows you to apply specific conditions to certain site visitors. There are a few different ways you can do this:

* You can set up currency and country targeting that allows you to limit your test to a single currency and/or a list of specific countries. This feature is defaulted to your store currency for price test.
* You can use UTM parameters to customize your user experience under the Audience option.
* You can filter traffic based on JavaScript Expressions under the Audience option.
* You can filter traffic based on device type (i.e. mobile or desktop) under the Audience option.
* You can filter traffic based off of whether a visitor is new or returning under the Audience option.
* You can prevent users from being targeted by related experiments to reduce undesired interactions under the Mutually Exclusive Tests option.

You can learn more about targeting [here](https://docs.intelligems.io/content-testing/targeting)!

## Step 11: Save and Preview your Test

Once you have completed all the steps, you'll be able to save your test with the green **Save** button in the top right.

In the **Preview** tab, you'll find a few options to load the test's preview:

* **Open Full Screen Preview:** this will open your website with the Intelligems widget loaded, so you can easily alternate between test groups to preview each group's experience, as well as do onsite edits if necessary (see [Step 8](#step-8-edit-content-on-your-site-if-needed) for more details). You can also choose which theme you'd like to preview in if you need to be somewhere other than your live theme!
* **Open Mobile Preview:** you'll see a QR code for each test group, so you can load the preview directly on your mobile device.
* **Copy Preview URL:** this will copy the preview URL to your clipboard automatically.

Once the test is saved, you should be able to see Intelligems as a rate carrier in your Shopify shipping settings for each profile and zone you selected in step 2. If you do not see it there automatically, you may need to click 'Add rate' and select it from the carrier options.

{% hint style="info" %}
Don’t worry, this won’t set the test live yet and you can come back and edit if you need to make changes!
{% endhint %}

## Step 12: Enter the test goals

Here you will choose the primary goal for the test. This will not affect what data is tracked or displayed, but will allow Intelligems to show the most important analytics first.

## What happens next?

Now that you've created your shipping test, you can QA your test using [this checklist](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist)!
