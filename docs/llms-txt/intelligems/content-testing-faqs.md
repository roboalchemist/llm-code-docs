# Source: https://docs.intelligems.io/content-testing/content-testing-faqs.md

# Content Testing FAQs

## General

<details>

<summary>Why should I run a template or content replacement test instead of a theme test?</summary>

Theme tests are a great way to test large changes to your store, or experiments that would otherwise require a developer to implement. There are a few drawbacks to keep in mind, however, so you may choose to run a template test or content replacement test instead:

1. A theme test means you have multiple live themes. Your customers are accessing your store via multiple themes, so you need to ensure any changes unrelated to the test (e.g., adding a landing page, editing copy or imagery) are made in all themes in the test.
2. Every visitor goes through a redirect. As mentioned above, theme tests are relatively high performing, but every visitor placed into a non-control group will still go through a one-time redirect to bring them to the correct theme for their group. While the UX impact of this one-time redirect is generally low, you may be able to avoid it altogether by using a content replacement test to dynamically edit content or inject HTML/CSS/JS.
3. You won't be able to delete any themes in the test for a while. During the experiment, visitors are sent to draft themes, and their browser will "remember" which theme to open the next time they visit your store via a session cookie. Once the test is over, if a visitor who was in one of the test groups re-visits your store and the cookie is still active, Shopify will first load the draft theme, and Intelligems will then immediately reset them back to the live theme. However, if the draft theme that was in the test has since been deleted, Intelligems won't be loaded and won't have the opportunity to reset the visitor's theme. Instead, the visitor see an error from Shopify, since they're trying to load a theme that does not exist.\
   \
   So, it's important to leave any themes that were tested in draft mode (rather than deleting them) for a while after the experiment (we recommend at least 1 week), to ensure any returning visitors are reset back to the live theme.

</details>

<details>

<summary>I'm running a content test and noticed the control content (i.e. URL, theme, language, etc.) flashes for a second before I see the test group content. How can I fix this?</summary>

Intelligems has two options for installing our JavaScript in your theme:

1. By using our app embed
2. By manually installing it into the theme code

The app embed works really well in most cases, but it can cause some flashing for certain tests and sites. If you notice this happening on your site, we recommend following these steps:

1. Turn the app embed off in all theme included in the test. You can do this by going to Shopify and in the online store section, click "Customize" next to each theme. In the left side menu, click the bottom option, which is "App Embeds". Turn the toggle off next to Intelligems and hit save.
2. Follow [these steps](https://docs.intelligems.io/developer-resources/intelligems-theme-snippets#option-2-add-script-tag-in-theme-head) to manually add the Intelligems script tag to your theme's head in the theme.liquid and all theme.\*.liquid files.

If you still notice any flashing after making that change, please reach out to our support team [here](https://docs.intelligems.io/content-testing/broken-reference) - there are a few settings we can turn on that allows us to load more information more quickly to avoid any flashing.

</details>

<details>

<summary>Can I test the One Page vs Three Page checkout, or test specific components on the checkout page, such as whether to include upsells?</summary>

Unfortunately we cannot A/B test the One Page vs Three Page checkout currently - this option has to be either on or off, so there isn't a way for us to turn it on for some visitors and not others. This is a Shopify limitation.

We can test other components on the checkout page if you are on Shopify Plus. You can test components on that page using our Checkout Experiences feature, which you can read more about [here](https://docs.intelligems.io/checkout/testing-checkout-experiences). This feature is limited to Shopify Plus because it uses Shopify's Checkout Blocks feature, which is only available for brands on Shopify Plus.

</details>

## Split URL Tests

<details>

<summary>Why must visitors visit the Origin URL to be included in the test?</summary>

Visitors must visit the Origin URL because this is the only page where Intelligems can detect their arrival and assign them to a test group. When a visitor lands on the Origin URL, our system:

1. Identifies that they've entered the test
2. Assigns them to either the Control Group or a test variation
3. Redirects test group visitors to their designated destination URL

Without visiting the Origin URL first, there's no trigger point for test group assignment, so visitors remain outside the test entirely. This also keeps the test's denominator limited to people who have been exposed to the test, keeping your data as actionable as possible.

Another thing to note is that URL redirect tests work in **one direction only**: from the Origin URL to the test destination URLs. Therefore, if a visitor lands directly on a destination URL (bypassing the Origin URL), they won't be included in the test. This is because:

* They never triggered the test assignment process
* Intelligems doesn't know they should be part of the test
* They won't be tracked in test results or analytics

To ensure accurate test results, visitors must enter through the Origin URL to be properly allocated and tracked.

</details>

<details>

<summary>I got an error that said I am on the wrong destination URL for my test group while previewing my test - what does this mean?</summary>

In a split URL test, Intelligems monitors site visitors who visit your Origin URL, then either keeps them there or redirects them based on their assigned test group. Our preview widget detected that you're on a destination URL for a test group that you're not currently previewing. Please note, Intelligems will not redirect you away from a destination URL, as our redirects only function in one direction: from the origin to the destination.

To continue testing your split URL test, please navigate to the Origin URL again.

</details>

<details>

<summary>I got an error that said I have enabled the setting for "Redirect One Time" for this test, and I have already been redirected while previewing my test - what does this mean?</summary>

Intelligems has two options for how a visitor can be redirect in a split URL test -

1. Redirect One Time: A visitor will only be redirected the first time they land on the origin URL
2. Redirect Every Time: A visitor will be redirected every time they land on the origin URL

Because you have enabled "Redirect One Time" for your test, and you have already been redirected one time, Intelligems will not redirect you again, unless you clear your redirect history by clicking the button to do so in the preview widget.

If you'd prefer to change this setting, please see our help guide [here](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test#redirect-one-time-vs.-redirect-every-time) on where you can do so.

</details>

## Onsite Edits Tests

<details>

<summary>What is a query selector and why does Intelligems use them?</summary>

A query selector is a way to select an element on a webpage using CSS-style syntax in JavaScript. In this case, we created a query selector based on the element you clicked on, which means it automatically targets that specific part of the page. However, this selector is just a starting point—you can edit it to be more general, more specific, or to target a different element altogether, depending on what you need your code to do.

</details>

<details>

<summary>Can we test an image vs. a video (MP4)?</summary>

Yes! This can be done using an [HTML Onsite Edit](https://docs.intelligems.io/general-features/onsite-editor).

</details>

<details>

<summary>Can we test our Pop-Ups with Intelligems?</summary>

Yes!

**Overview**

Testing pop-ups is a common way to evaluate the impact of on-site messaging, promotions, or lead capture strategies without making permanent code changes.

With Intelligems, you can run A/B or multivariate tests on pop-ups to measure their effect on conversion rates, email capture rates, or profit per visitor.

Pop-ups are often powered by third-party apps (e.g. Klaviyo, Justuno, Alia, Privy, Postscript etc.), or sometimes implemented natively in a Shopify theme. Intelligems can generally integrate with either approach by letting you toggle visibility, edit content, or inject custom logic on who sees the pop-up.

**Test Setup Types**

Pop-ups can be tested using multiple Intelligems test setups. The right choice depends on how the pop-up is built and what aspect you want to test:

**1. Onsite Edits Test - CSS or Javascript Injection**

* **Best for:**
  * Turning a third-party app’s pop-up hide/show.
  * Swapping content or offers inside an existing pop-up container.
  * Changing timing (e.g., show at 5s vs. 20s).
* **How it works:** Use Intelligems’ editor to show, hide, or modify a pop-up on-page.

**Example to show the Pop Up:**

```css
#my-popup {
    display: block;
}
```

***

**Example to hide the Pop Up:**

```css
#my-popup {
    display: none !important;
}
```

**Notes:** We generally recommend having the Pop-Up on your theme and using Intelligems to Show/Hide it rather than "injecting" the popup itself. If you want to change which popup is displaying, you should either:

1. Have multiple present in your theme, with all but one hidden by default, then use CSS to swap which one is hidden
2. Use JS to "tell" the popup provider which version to render

If you would like us to take a deeper look at your set up, please reach out to our support team for help!

**2. Split URL Test**

* **Best for:**
  * Comparing two entirely different pop-up designs built in Shopify or a page builder (e.g. Replo, Shogun).
  * Testing different pop-up apps without overlap.
* **How it works:** Control and variant each point to different Shopify pages or landing pages, each with their own pop-up configuration.
* **Notes:** Each page must be self-contained with its own tracking and pop-up triggers.

***

**Setup**

To test pop-ups with Intelligems, you’ll generally follow one of these approaches:

1. **Follow the steps to set up an** [**Onsite Edits Test**](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test)
   * In Control: no pop-up (or your original pop-up).
   * In Variant: show new pop-up design, offer, or timing.
2. **Swap Pop-Up Content**

   In your new group, adjust the pop up using the one of the methods described above. This can be useful for testing offers (e.g. “10% Off” vs. “Free Shipping”).
3. **Adjust Targeting & Triggering**
   * Combine Intelligems audience targeting with your pop-up (e.g. first-time visitors vs. returning customers).
   * Change when or how the pop-up fires (e.g. on scroll, after X seconds, exit intent).
   * Compare whether different timing increases conversions without disrupting browsing.

**Use Custom Events to Filter Results**

**Tracking Engagement with Custom Events**

For deeper analysis, you can use [**custom events**](https://docs.intelligems.io/analytics/custom-events) to track whether a visitor actually engaged with a pop-up. This allows you to segment and filter results in reporting (e.g., conversion rates among users who saw or clicked the pop-up vs. those who did not).

**Why this matters:**

By tagging these events, you can evaluate whether the pop-up itself is influencing conversion behavior — not just whether the variant group had higher performance. This makes results easier to interpret and helps confirm if engagement with the pop-up is the driver of uplift.

**Best Practices**

* **Isolate one variable at a time**: Test *either* the offer, design, or timing, but not all at once, to avoid confounding results.
* **Connect to downstream KPIs**: Go beyond email sign-ups—measure profit per visitor by adding your COGS in Intelligems to confirm the pop-up improves business results.
* **Consider device experience**: Pop-ups can behave differently on mobile vs. desktop. Always QA on both.

**Limitations**

* **Third-party app restrictions**: Some pop-up apps don’t expose all timing/triggering logic to external scripts. In these cases, Intelligems can usually control *visibility* or *injection*, but not the app’s internal scheduling.
* **Theme-level vs. app-level**: If the pop-up is baked into the theme code, edits must be structured as content tests. If powered by an app, you may need to coordinate app settings with Intelligems settings and targeting.

</details>

## Template Tests

<details>

<summary>Why must visitors visit a page assigned to the Control Group's template in Shopify to be included in a Template test?</summary>

Visitors must visit a page that uses the Control Group's template because this is the only way Intelligems can detect their arrival and assign them to a test group. When a visitor lands on a page using the control template, our system:

1. Identifies that they've entered the test
2. Assigns them to either the Control Group or a test variation
3. Dynamically serves the appropriate template based on their test group

Without visiting a page that uses the control template, there's no trigger point for test group assignment, so visitors remain outside the test entirely.

You can check which pages are assigned to a template in Shopify by following [these steps](https://www.loom.com/share/5f4cd7c9e008488287d4086d370a50f3?sid=b4028c6b-b07d-4b6b-8690-ff1507766205), or in your Shopify admin.

If your control template isn't assigned to any pages in Shopify, no visitors will be included in your test. To fix this:

1. Assign your control template to relevant pages in Shopify
2. Or choose a different template to use as your Control that's already assigned to pages you want to test

</details>

<details>

<summary>How can I roll out a winning homepage template?</summary>

Shopify doesn't allow you to switch homepage templates. The winning template will have to be recreated in the original template.

An easy way to do this is within the theme editor. Find the test template and copy its contents into the default template (usually `index.json`).

![](https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0d56f6bf7fdff603a65918567a58a7342ff236bd%2Fimage%20\(13\).png?alt=media)

</details>

## Theme Tests

<details>

<summary>Why do I see the Shopify theme preview bar during my theme test?</summary>

During a properly functioning Intelligems theme test, visitors will never see the Shopify theme preview bar. If you're seeing the preview bar, it's likely because the Intelligems JavaScript is not installed in all themes being tested. The Intelligems script needs to be in the live theme, plus all themes in the test.

If the script is in only the live theme, for example, visitors will be put into test groups and will be redirected to a draft theme, but since the Intelligems script is not in the draft theme, the preview bar will not be hidden once they're there, and Intelligems' analytics tracking will not function properly.

To fix this issue, install the Intelligems script in the live theme and all themes that you're testing. Since theme tests require a redirect, we recommend installing the Intelligems script synchronously by adding the script tag to your theme's head in the theme.liquid and all theme.\*.liquid files (learn more [here](https://docs.intelligems.io/developer-resources/intelligems-theme-snippets#option-2-add-script-tag-in-theme-head)).

</details>

<details>

<summary>How does a theme test impact page load speeds?</summary>

Theme tests are relatively high performing, however, there may be a performance impact on a visitor's first page view. If Intelligems detects that a visitor is in the wrong theme, it will immediately reload the page in the correct theme. From then on, that visitor will be in the correct theme for their test group, which may be an unpublished theme. Our benchmarking shows that there is no performance impact on these subsequent page views, even for unpublished themes. If you're concerned abotu the potential performance impact of a reload on the first page view, you might consider using an onsite edit test instead.

</details>
