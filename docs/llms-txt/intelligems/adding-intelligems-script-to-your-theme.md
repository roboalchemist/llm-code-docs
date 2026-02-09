# Source: https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme.md

# Adding Intelligems Script to your Theme

## Introduction

Adding the Intelligems script to your site is the most important step to getting started with testing with Intelligems! Adding the Intelligems script to your site is the only mandatory integration step for Content, Shipping and Campaigns testing, and is the first step to integrating for Price testing. There are two options below for adding the Intelligems script to your site.

## Option 1: Use the App Embed Block

{% hint style="success" %}
This is the easiest installation method that works for most stores!
{% endhint %}

The fastest way to add Intelligems JavaScript to your theme is to enable it in the "Customize" section of your theme editor. You can do so by logging into your Shopify Admin, and navigating to Sales Channels > Online Store > Live theme - Customize > App Embeds. Search "Intelligems", make sure it is toggled on, and click "Save" in the top right.\
\
This will load Intelligems in a fashion that works optimally for performance and A/B testing on most stores. If for any reason you encounter performance concerns, [see our docs on performance optimization](https://docs.intelligems.io/performance-optimization/optimizing-your-price-test-integration).

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

### Post-Purchase Page for Theme Tests (Legacy Checkout Only)

**Note:** *This step only applies if your store still has access to the legacy Shopify checkout (`checkout.liquid`). Most stores have been migrated to Checkout Extensibility and will not see this section in their Shopify admin. If you don't see a "Post-purchase page" section under Settings → Checkout, you can skip this step—the preview bar will be hidden automatically.*

If you are planning to run a theme test and still have access to the Additional Scripts section for the Post-purchase page, you should add our script there. This will hide the theme preview bar from showing up on your thank you page.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0e043169cb168eea43b0239be9661bf1a7a840b0%2FScreenshot%202024-07-31%20at%2012.22.21%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>
