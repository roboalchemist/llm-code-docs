# Source: https://docs.intelligems.io/shipping-testing/shipping-progress-bar-integration.md

# Shipping Progress Bar Integration

## Overview

Intelligems offers a progress bar for Shopify carts / slide-out carts that shows visitors how much they have left to spend before reaching free shipping. The progress bar can be used as part of a shipping threshold test (visitors will be shown the correct bar based on their test group) or outside of a test.

{% hint style="info" %}
You'll need the Intelligems JavaScript snippet added to your theme to render the Intelligems shipping progress bar. If you haven't done so, see our integration guide [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
{% endhint %}

## Step 1: Add the shipping progress bar to your Shopify theme

Paste the following code snippet into your Shopify theme code, in the theme file that renders your cart. This file may be called something like cart.liquid, slideout-cart.liquid, etc. We recommend adding this code snippet at the top of the section that relates to your cart:

```html
<ig-shipping-progress-container></ig-shipping-progress-container>
```

{% hint style="danger" %}
If you already have a progress bar, remember to comment out the existing progress bar to avoid showing two!
{% endhint %}

## Step 2: Customization / Styling

You can customize the Intelligems Cart Progress Bar in the Global Styless tab. Some examples of stylizing options available include:

* Bar Styles
* Bar Colors
* Text Options

## Integrating with Rebuy Carts

1. Create a Rebuy custom smart cart template. Follow [this](https://help.rebuyengine.com/en/articles/6120362-how-to-use-a-custom-template-with-smart-cart) article for instructions.
2. Edit the template to replace the Rebuy progress bar with the Intelligems progress bar snippet. See Step 1 above.

## Using the Progress Bar With Your Existing Shopify Rates

You can use the Intelligems Shipping Progress Bar with your existing Shopify rates using an Intelligems Offer Experience. You'll simply add the code snippet above to your Shopify theme and configure the visual appearance of the progress bar in the Intelligems app. Then in the Intelligems app, create a new free shipping offer, ensure you opt for the offer to be "powered by Shopify", and save your offer.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-62da580cf884915a47b500cb930f4b8f908dabc9%2FShipping%20Progress%20Bars.png?alt=media" alt=""><figcaption><p>Edit Shipping Progress Bar</p></figcaption></figure>
