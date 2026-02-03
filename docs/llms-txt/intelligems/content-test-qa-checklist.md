# Source: https://docs.intelligems.io/content-testing/content-test-qa-checklist.md

# Content Test QA Checklist

{% hint style="info" %}
This QA list is specific to a content test. If you are QAing a [shipping test](https://docs.intelligems.io/shipping-testing/shipping-test-qa-checklist) or a [pricing test](https://docs.intelligems.io/price-testing/price-test-qa-checklist), please check out QA checklists for those types of tests!
{% endhint %}

Once your content test is setup, you'll need to QA your site to make sure everything is working as it should be. Before heading to your site, there are a few things you should check first to make sure your integration is functional:

* [ ] Is Intelligems JavaScript in your live theme? Check out [this article](https://docs.intelligems.io/developer-resources/intelligems-javascript) for more information on where to find this.
* [ ] Are you running a [Theme test](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-theme-test)? If you are, is Intelligems JavaScript in the themes you are testing as well? Including in checkout.liquid, if you have that file?
* [ ] Are you running a [Theme Template test](https://docs.intelligems.io/content-testing/how-to-set-up-a-content-test/how-to-set-up-a-template-test) on specific templates only? If you are, have you added [this snippet](https://docs.intelligems.io/developer-resources/intelligems-javascript#template-testing-snippet) to your theme yet?

Once you have confirmed all of the above, you can preview the test on your live site. Enter Preview mode by clicking the `...` next to your test and select `Preview`

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5592dfbbfebbec7b54aad766bb3a8fe672c06f6f%2FScreenshot%202023-08-30%20at%2010.19.27%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>

This will open your site up in a new window with the Intelligems preview widget enabled. In the preview widget, you'll see:

1. The name of the test you are previewing in the top left
2. A dropdown to switch between different test groups in the bottom left
3. A toggle to highlight any replacements in the top right
4. An edit button in the bottom right; this enables integration mode, where you can edit any replacements

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5a4a1f2cd8a39ab512cb2dfeecfe33154d385823%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

Now that you are on your site, use the preview widget to toggle between your test groups to make sure the correct content is showing on your site for each test group. What you should check depends on what type of content test you are previewing. For a few areas you should check for each test type, see below.

#### Theme Tests

* [ ] When you switch test groups in the dropdown, does the theme update to display the correct theme? You can check this based on differences that you know of in the test theme, or by searching the source code for the current theme name. You should also see a message similar to the below at the bottom of the preview widget for any themes that are not currently live.

  <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-db71becacc192f075f3615a2501c2a3a7d2c2b68%2FScreenshot%202023-10-20%20at%203.38.01%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>
* [ ] Does a Shopify preview bar show at the bottom of your window when you are in a test theme? This shouldn't happen; confirm that the Intelligems JavaScript is in all themes included in the test in both the theme.liquid and the checkout.liquid files.
* [ ] **Key Steps:**

  1. Enter preview mode in the control group
  2. Open JavaScript Console (`Cmd+Option+J` Mac / `Ctrl+Shift+J` Windows)
  3. Type `Shopify.theme` to see current theme details
  4. Switch groups and check that theme changes

  **What to verify:** Control shows your live theme name and version, variant shows the different test theme name and version.

{% embed url="<https://www.loom.com/share/2d8b66808aa64e038e76dd60d5f49bcb>" %}

#### Theme Template Tests

* [ ] When you switch test groups in the dropdown, are the correct templates used where they are being tested? You can check this based on differences that you know of in the templates.
* [ ] **Key Steps:**

  1. Start in preview mode on the control group
  2. Open Chrome Developer Tools → JavaScript Console (`Cmd+Option+J` Mac / `Ctrl+Shift+J` Windows)
  3. Type `_template` to see the current template name
  4. Switch groups and verify the template name changes

  **What to verify:** Control shows base template (e.g., `product`), variant shows template with suffix (e.g., `product.123456`)

{% embed url="<https://www.loom.com/share/a0252eca479a4ea3b092089e15343e45>" %}

#### Page Redirect Tests

* [ ] Go to a page that is included in a redirect while in a non-control group in the preview widget. Are you redirected to the correct link?
* [ ] Check the above for each test group and page being tested. You'll need to navigate away from the test page and go back once you have changed groups to be redirected.
* [ ] Do you have the Redirect Once checkbox selected for any of your redirects? Read more about how that functions [here](https://docs.intelligems.io/content-testing/how-to-set-up-a-content-test/how-to-set-up-a-page-redirect-test#redirect-once) and confirm you have the correct setting on for your test.

#### Find & Replace Tests

* [ ] Navigate to a location on your website where you have set up a text, image, or CSS / JS replacement. Switch groups in the widget and confirm that the content is updating as expected.
* [ ] Continue the above until you have checked all locations where a replacement has been set up.
* [ ] Do a sweep of the site to make sure content is not being updated somewhere that it shouldn't be. Our replacements are based on selectors. If there is a selector that is the exact same somewhere else on the site, the content there could be updated inadvertently. To avoid this happening, try setting up [Page Targeting](https://docs.intelligems.io/content-testing/targeting#what-is-intelligems-page-targeting) or including a "Find" in your Find & Replace.

#### A few other things to keep in mind:

* [ ] Do you have Page Targeting set up on your test? If so, if you are on a URL that does not match your targeting, you'll see a message like the below in the preview widget. This will confirm that your page targeting is working as expected since you are not meeting any of the conditions.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9f4330b499b6e779677e9ccd56f5150857add2f3%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

* [ ] You can further confirm that Page Targeting is working by going to one of the URLs that does match your targeting. Once you do so, you'll see the widget will no longer show a message on the bottom about being excluded.
