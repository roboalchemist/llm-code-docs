# Source: https://docs.intelligems.io/getting-started/common-use-cases/content-test-common-use-cases/landing-page-testing.md

# Landing Page Testing

## Introduction

Testing landing pages for an eCommerce site is crucial for maximizing conversion rates & ROAS, as well as enhancing user experience. A few examples may include:

* Testing different layouts or calls to action for your landing pages from Google ads
* Sending your Facebook traffic to a landing page versus directly to a collection page or your homepage
* Experimenting with different offers for ad traffic, such as 10% vs 20% off their first order

You can use Intelligems to test landing pages in a few different ways. Here, we'll explore testing landing pages using [Split URL](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test) tests and [Onsite Edit](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-an-onsite-edits-test) tests. Before getting started, make sure you've [added the Intelligems script](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme) to your Shopify theme.

## Setting the Test Up

### Option 1: Split URL Test

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9c7d6e184c69910c4671a8cf43321ddb3f72d4e4%2Fimage.png?alt=media" alt=""><figcaption><p>Two example landing pages that we'd like to test against each other</p></figcaption></figure>

Split URL tests let you test pages against each other using redirects. When a visitor lands on the control page, they are randomized into a test group, and, if they're not in the control group, they'll be redirected to the corresponding page for their group.

This test type is a great option if you want to get your test up and running quickly, especially if you're using a page builder or making large changes to the page you're testing.

To set up a Split URL landing page test:

1. **Create the versions of the page you want to test.** Create the pages you want to test, for example, with a page builder or with the Shopify theme editor, and make sure they're accessible on your store through a URL. Note down the URLs of the pages you're testing.
2. **Create a new Intelligems Split URL test** by clicking "Create New Test" on the [Intelligems homepage](https://app.intelligems.io/), choosing "Content Test," and then "Split URL Test"
3. **Create a test group for each variation you'd like to test**. In my example, I'll be testing the existing control page against one variant, so I'll have two test groups total: Control and Test.\
   \\

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-cf6da5e7a16936838e08c16e1be0f35e33aac358%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

4. **Enter the URLs of the two landing pages** in the test setup. A "Simple" redirect should work for our purposes, since we just want to split between two known URLs. "Advanced" redirects are for when you'd like to match or replace wildcard text.\
   \
   Choose "Redirect Every Time" if a visitor who's assigned to test page should be redirected sent to it any time they reach the Control. Choose "Redirect One Time" if they should be redirected only the first time. In our case, since we're testing fully replacing the control page with the test page, we'll choose "Redirect Every Time."

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-ba6982237bb435ab137730d1e43639ff4fc43342%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

   **Multi-domain brands:** If you operate multiple domains (e.g., yourbrand.com and yourbrand.co.uk), make sure all domains are registered in **Settings → Domain Settings**. You can then set up separate Split URL tests for landing pages on each domain.
5. **Save and preview your experiment**. You can refer to our [QA guide](https://docs.intelligems.io/content-testing/content-test-qa-checklist#page-redirect-tests) for tips on what to look for when testing.
6. **Launch!**

{% hint style="warning" %}
If you use a page builder like PageFly, Replo or GemPages, be sure to add Intelligems JavaScript to their theme files as outlined [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme)! If this step is missed, Intelligems will not be able to track the data for those pages.
{% endhint %}

### Option 2: Onsite Edit Test

Another option is an Onsite Edit test. In an Onsite Edit test, you can use Intelligems' visual editor, injected Javascript, or CSS to insert, hide, and re-arrange elements on a page.

This test type is a good fit if you're making a smaller adjustment to a page (e.g., adding or removing a section, etc.), or if you'd like to avoid redirecting any users for performance or other reasons, and you're comfortable with basic HTML and CSS.

To set up an Onsite Edit landing page test:

1. **Decide on a strategy for switching content**. For example, if you're testing a new section, it's often easiest to add this section to the page, hidden by default with CSS, and then use CSS injection to unhide it for the test group. Another option would be to use Intelligems' visual editor to *add* the section for the test group. We'll go through both techniques below.
2. **Create a new Intelligems Onsite Edit test** by clicking "Create a Test" on the [Intelligems homepage](https://app.intelligems.io/), choosing "Content Test," and then "Onsite Edit"
3. **Create a test group for each variation you'd like to test**. Here, we're testing the existing control page against one variant with an added section, so we'll have two test groups total: Control and Test
4. **Use Page Targeting to target the test on the landing page**. We want the onsite edits to execute only on the landing page, and we want to make sure only visitors to the landing page enter the test and factor into analytics. We can do this by targeting the test on the landing page by URL. For example:\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-e31a2b7dc1b3f3ccb3314e43b103fe9016f7b2e5%2Fpage-targeting.png?alt=media" alt=""><figcaption><p>Page Targeting in an Onsite Edits Test</p></figcaption></figure>
5. **Set up the onsite edit.**
   1. Injected CSS: one way to test a new section of a page is to put the section in the page, but hidden by default, and then inject CSS to unhide it for the test group. For example, you could add a CSS class to your theme:\
      \
      `.hidden-section { display: none; }`\
      \
      And add this class to new page section in the theme editor or page builder (if you're unable to edit the section's classes you could also write a different selector rather than adding a new class, and add this CSS to your theme's code or with injection for the control group).\
      \
      Then, for the test group, inject some CSS to override this and unhide the section:\
      \
      `.hidden-section { display: block !important; }`\\

      <div data-full-width="true"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9c0c7f7c730d141cdf60e57d916014c601b376cd%2Fcss-styles.png?alt=media" alt=""><figcaption><p>CSS injection in an Onsite Edits Test</p></figcaption></figure></div>
   2. Insert the section: another way to test a new section is to insert it using Intelligems' onsite editor. For example, to insert a testimonials section above the featured collection on this page, first open the Intelligems onsite editor, then choose the featured collection section and choose "Edit HTML / CSS":\\

      <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-6d8814e4acc1e926c796668981f8acd76867abc4%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

      In the dialog, choose "Prepend Outside" in the dropdown in the bottom left. This tells Intelligems to inject the HTML you enter before the section you selected, instead of replacing it.\\

      <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-3f895396929f7008eb328ba9b05b023be790334e%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

      Next, enter the HTML for the new section in the text editor, and click "Apply." You'll now see the new section appear above the one we selected:\\

      <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-4d68cf4f5ff3bcbc688118cd10d95f54e368a689%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
6. **Save and preview your experiment**. You can refer to our [QA guide](https://docs.intelligems.io/content-testing/content-test-qa-checklist#page-redirect-tests) for tips on what to look for when testing.
7. **Launch!**
