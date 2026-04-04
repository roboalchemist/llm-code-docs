# Source: https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-announcement-bar-text.md

# Testing Announcement Bar Text

## Introduction

By A/B testing your announcement bar, you can identify the most effective design and content for driving conversions and profit. Even simple changes to your announcements can sway customers toward conversion.

Here are a few ideas for A/B testing your Shopify announcement bar using Intelligems:

* **Test different text.** Try using different wording or calls to action in your announcement bar to see what gets the best results.
* **Test different colors.** Experiment with different color schemes to see what is most visually appealing and effective at grabbing attention.
* **Test different positions.** You can also test different positions for your announcement bar on the page.

## Setting the Test Up

Here are the steps to follow to use an Intelligems Onsite Edits test to A/B test your Shopify announcement bar:

* **Check if your theme has a built-in announcement bar feature.** You can do this by going to **Online Store > Themes** and then clicking **Customize**. If your theme has an announcement bar, **Announcement bar** will be displayed in the list of sections or within the "Header" settings.
* **If your theme has a built-in announcement bar feature, follow your theme’s documentation to add it to your online store.** If you’re using a Shopify-supported theme, you can refer to *Free themes from Shopify*.

If your theme does not have a built-in announcement bar feature, you'll need to download a banner app from the Shopify app store.

Once you have an announcement bar set up, you can use Intelligems to A/B test different versions of it. Here are the steps on how to set up an onsite edits test in Intelligems:

1. **Create a new test.** From the A/B tests page, create a new onsite edits test.
2. **Create your test groups.** You will need to create a test group for each variation of your announcement bar that you want to test. Fill in the Test Name and Test Description. You can add new groups by clicking on the ‘+’ button. Use the slider to allocate what percentage of traffic will go to each group.
3. **Make your content edits.** In the Modifications tab, this can be done one of two ways:
   1. **Select Content Edits, then Add & Edit Changes in Visual Editor.** This will take you to your website with Intelligems' edit mode enabled.
   2. Alternatively, you could enter a CSS injection in the Styles & Javascript section.
4. **Set up targeting (optional).** Targeting allows you to apply specific conditions to certain site visitors. You can learn more about targeting [here](https://docs.intelligems.io/general-features/targeting).
5. **Save your changes and start your test.** Intelligems will start tracking the performance of each variation of your announcement bar. You can then use the Intelligems analytics dashboard to see which variation is performing best.

Here's a video demonstrating those steps, using the visual editor:

{% embed url="<https://www.loom.com/share/24da9a9022954036b80368fac39fbc2c?sid=8baeba04-86cf-489d-9ddc-20d9b26829e2>" %}
Video demonstrating how to A/B test the announcement bar with Intelligems
{% endembed %}

{% hint style="info" %}
Note that onsite edits are based on [query selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector). Some themes and announcement bar apps have a different query selector for the announcement bar depending on the specific page. Confirm in preview mode that the updates you've made to the announcement bar are working on all of the pages you intend to change.
{% endhint %}
