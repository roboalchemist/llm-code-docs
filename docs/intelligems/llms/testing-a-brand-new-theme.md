# Source: https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/testing-a-brand-new-theme.md

# Testing a Brand New Theme

## Introduction

Your team has spent the last month perfecting a new theme for your store. They’ve spent hours QAing it and are confident that it is ready to launch. Testing this new theme compared to your live theme can be a great way to confirm whether the new theme is better than your old theme, and that no issues were overlooked. The goal of this test is to see either no difference, or some uplift, for the new theme. If there is a negative impact, this may be a sign that there are still bugs to work out.

You can use Intelligems to test your brand new theme by setting up a [Theme Test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test). Before getting started, make sure you've [added the Intelligems Script](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) to all themes that will be included in the test. This allows Intelligems to hide the theme preview bar and track all data correctly.

## Setting the Test Up

Theme tests allow you to test entire themes against each other using redirects. When a visitor lands on your website, they are randomized into a test group, and, if they're not in the control group, they'll be redirected to the test theme where they'll stay for the remainder of the test. This test type is the **only way to test two or more entirely different themes against each other**, so it is the best option when you are looking to launch a brand new theme.

To set up a Theme Test for your new theme:

1. Create your new theme in Shopify. Make sure you've [added the Intelligems Script](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) to all themes that will be included in the test!
2. Create a new Theme Test by clicking "Create New Test" on the [Intelligems homepage](https://app.intelligems.io/), then choose "Content Test" and then "Theme Test"
3. Rename "New Group 1" to match the name of your new theme.
4. Select your live theme for the control group, and your new theme for the test group.

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-db3afa5028716b81b2a67677611c1406677b0dd4%2FScreenshot%202024-10-14%20at%2010.53.28%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>
5. Save and preview your experiment. You can refer to our [QA guide](https://docs.intelligems.io/content-testing/content-test-qa-checklist#page-redirect-tests) for tips on what to look for when testing.
6. Launch!

A few things to keep in mind while testing your new theme:

* If the new theme is performing well, you can gradually increase the percent of traffic being sent to that theme by editing your test in the Test Groups tab:

<div data-full-width="false"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-aa063070633b2b95e64d2340e7c85c4ed6bd00cc%2Ftheme-traffic-split.png?alt=media" alt=""><figcaption></figcaption></figure></div>

* Running a theme test means that you need to keep all themes that are part of the test up to date! Any changes that you make to your live theme while a Theme Test is running must also be made to any themes included in your test.
* When you end a Theme Test, do not delete any themes that were part of the test. You can read more on why [here](https://docs.intelligems.io/content-testing/ending-a-theme-test)!
