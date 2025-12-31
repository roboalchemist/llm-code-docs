# Source: https://docs.intelligems.io/getting-started/updating-the-intelligems-script.md

# Updating the Intelligems Script

{% hint style="success" %}
The **CommonJS script will remain supported for current features.** However, **new features will** **only be available with the ESM script**, so we recommend updating your Script code as soon as you are able to. Additionally, the ESM script improves plugin performance, making it faster!
{% endhint %}

## Context

Historically, Intelligems utilized a version of its script known as the CommonJS script. In December 2024, an update was released, transitioning to a new and improved version called the ESM script.

Here’s how the scripts differ:

#### Pre-December 9, 2024 (CommonJS Script)

The final line of the script looks like this (with `abcdefghijk` replaced by your unique customer ID):

```html
<script src="https://cdn.intelligems.io/abcdefghijk.js"></script>
```

#### Post-December 9, 2024 (ESM Script)

The updated script uses the following format (with `abcdefghijk` replaced by your unique customer ID):

```html
<script type="module" src="https://cdn.intelligems.io/esm/abcdefghijk/bundle.js"></script>
```

Key differences include:

1. **`type="module"`** – the script is now a JavaScript module.
2. **`esm`** – the directory structure reflects the new ESM format.
3. **`bundle`** – the updated structure for improved performance.

{% hint style="info" %}
The first eight lines of the script remain unchanged.
{% endhint %}

## Required Changes

If you are seeing the below error in your Intelligems app:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-7a84f4af637cfff79b678c59fbc31b5295d0c9f8%2FScreenshot%202025-03-10%20at%2010.08.32%20AM.png?alt=media" alt=""><figcaption></figcaption></figure>

This means you need to update your theme code to reflect the new ESM Script. Here are the steps to do so:

1. Go to the settings page in the Intelligems app.
2. Once you're there, you'll see a section called "Theme Script". Click the blue button in that block that says "Copy Script". This will copy your unique Intelligems script to your clipboard.
3. Now head over to your Shopify account, and replace your current Intelligems Script with your new one. The script should be included as a source in the `<head>` of each of these files:
   1. theme.liquid
   2. any other theme.\*.liquid files (e.g., theme.gempages.liquid if you have this file)
   3. checkout.liquid (if you have this file; most themes do not)

Here is a video walking through those steps:

{% embed url="<https://www.loom.com/share/0c95974114f94e1797cbd4896a88dd10?sid=960987e2-93e7-4cde-8430-5ad15d09a71e>" %}

#### Post-Purchase Page for Theme Tests

If you are planning to run a theme test, you should also update your script in the Additional Scripts section for the Post-purchase page if you are using this. This will hide the theme preview bar from showing up on your thank you page. You can get to the Additional Scripts section pictured below by going to Settings -> Checkout -> Scroll about halfway down to "Post-purchase page".

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0e043169cb168eea43b0239be9661bf1a7a840b0%2FScreenshot%202024-07-31%20at%2012.22.21%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>
