# Source: https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test.md

# How to Set Up a Theme Test

{% embed url="<https://www.loom.com/share/d4d81d1875804300bfbe52e3d88b65ae?live_rewind=1>" %}

## **Step 1: Create a new test**

Navigate to the "A/B Tests" tab in the menu on the left-hand side of the Intelligems app. Once you're there, click 'Create New Test' above the experiments table. Select "Content Test" , then "Theme Test", then "Create Test".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-6e622c44b830e3e55cfdb81f36864a390c643427%2FStep%201.gif?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 2: Create your test groups**

Create a test group for each theme you want to include in the test. Fill in the Test Name and Test Description for the experiment you are creating. This information is all internal - the more detail you include here the better! Tests can be live for several weeks, and your future self will thank you for including the details here.

You can add new groups to include in the test by clicking on the ‘+’ button. Name the groups for the experiment and use the slider to allocate what percentage of traffic will go to each group. Click ‘Continue’ when you are done.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-e60ceeed21b77b8fccffbfc784190adbec485cd9%2FTest%20Groups.gif?alt=media" alt=""><figcaption></figcaption></figure>

## **Step 3:** Select the themes you want to test

Select the theme you'd like to test for each test group.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-bc3217f51a2029e0eeaadb320e3b97542a17a154%2FStep%202.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Make sure the [Intelligems script is installed](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) in all themes that you're testing! This is how we will hide the preview bar at the bottom of the theme. If you have checkout.liquid, ensure you have installed the Intelligems script on this page as well, so that the preview bar is hidden at checkout (if you do not have checkout.liquid, the bar will be hidden automatically).
{% endhint %}

{% hint style="info" %}
Product page templates are set at the product level, and the template name must be available in the live theme. When testing two different themes, make sure the template names match, so that the templates you've chosen for each product exist in both themes. If the product pages look correct when previewing the test theme(s), then you're good to go!
{% endhint %}

## **Step 4: Set up targeting if needed**

Targeting is an optional step. By default, a visitor will be immediately assigned to one of the test groups using its random split-test mechanism. This assignment is determined at the first visit and is stored via a first‐party cookie, ensuring that the visitor remains in the same group on subsequent visits during the theme test period. Every theme that you include in your test configuration—both the live theme and the test themes—is part of the theme test.

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

## Previewing Themes through Shopify Admin

When trying to preview a theme through Shopify Admin, you might get redirected to a different theme if that theme has been used in an Intelligems theme test. Let's look at an example when there is a live Intelligems theme test:

Control Group: Default Theme (Theme ID: 1)

Test Group: Secondary Theme (Theme ID: 2)

If you preview Secondary Theme from Shopify Admin and have not been previously included in the live Intelligems theme test, you'll be randomly assigned a test group when you enter Secondary Theme. Depending on your test group assignment, you'll either remain in the Secondary Theme if you were assigned to the test group, or you'll be redirected to the Default Theme indicating you were assigned to the Control Group.

Let's say you were assigned the test group and remain in Secondary Theme. If you were to preview the Default Theme from Shopify Admin, you'll be redirected to the Secondary Theme since that is the theme assigned to your test group. If you wish to preview the Default Theme, you can use the Intelligems preview widget to switch your group.

## Why am I still being redirected away from a theme when I don't have a theme test live?

This is to ensure all users who were assigned a preview theme during your test do not remain in a preview theme once that test is ended. This redirection will only happen for themes that were included in an Intelligems theme test and will only occur once. After your initial redirection, you'll be able to preview that theme through Shopify Admin normally.
