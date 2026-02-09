# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products/step-1-add-intelligems-javascript.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts/step-1-add-intelligems-javascript.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-1-add-intelligems-javascript.md

# Step 1: Add Intelligems JavaScript

## Introduction

If you have not already done so, you will need to add the Intelligems script to your site. There are two options below for doing this.

## Option 1: Use the App Embed Block

{% hint style="success" %}
This is the easiest installation method that works for most stores!
{% endhint %}

The fastest way to add Intelligems JavaScript to your theme is to enable it in the "Customize" section of your theme editor. You can do so by logging into your Shopify Admin, and navigating to Sales Channels > Online Store > Live theme - Customize > App Embeds. Search "Intelligems", make sure it is toggled on, and click "Save" in the top right.\
\
This will load Intelligems in a fashion that works optimally for performance and A/B testing on most stores. If for any reason you encounter performance concerns, see our docs on [performance optimization](https://docs.intelligems.io/performance-optimization/optimizing-your-price-test-integration).

{% hint style="warning" %}
For any **password protected store**, we will not be able to automatically detect the script, so you will continue to get an error message in the app regarding the script not being in your theme.
{% endhint %}

## Option 2: Add to Your Theme Code

{% hint style="info" %}
If you are on Shopify Plus and are still using checkout.liquid, you will still need to manually add Intelligems JavaScript to your checkout.liquid file in order to hide the discount or preview bar at checkout. Your individual script tag is located on the settings page in the Intelligems App.
{% endhint %}

{% hint style="danger" %}
This will need to be manually removed if you uninstall Intelligems.
{% endhint %}

To complete this, go to the settings page in the Intelligems app. Once there, you'll see a section called "Theme Script". Click the blue button in that block that says "Copy Script". This will copy your unique Intelligems script to your clipboard.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-c397ff4b2768cc623336aea8cc0d1844d214f9d0%2FScreenshot%202025-09-25%20at%205.30.44%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure>

Now head over to your Shopify account, and paste the Intelligems Script as a source into the `<head>` of each of these files:

* theme.liquid
* any other theme.\*.liquid files (e.g., theme.gempages.liquid if you have this file)

Here's a video walking through those steps as well:

{% embed url="<https://www.loom.com/share/187128fe3b9c4334b5904d4c4de48dbf?sid=477d7023-fb18-4218-accd-fbd0775fee88>" %}
