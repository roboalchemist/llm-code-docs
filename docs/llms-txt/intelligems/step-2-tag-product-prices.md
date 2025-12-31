# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products/step-2-tag-product-prices.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts/step-2-tag-product-prices.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-duplicate-products/step-2-tag-product-prices.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-checkout-scripts/step-2-tag-product-prices.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/integration-guide-using-shopify-functions/step-2-tag-product-prices.md

# Step 2: Tag product prices

## Introduction

To enable Intelligems to dynamically modify price elements for each test group during testing, it is essential to tag their locations on your website. This entails adding the query selector for price elements into the Intelligems configuration so the Intelligems plugin knows where those prices live. This guide will walk you through the process to do so.

{% hint style="warning" %}
Before you can use the Intelligems Widget, please confirm that you've added Intelligems JavaScript as a source into your theme.liquid file! See more on how to add our JavaScript to your site [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
{% endhint %}

## Step 1: Accessing the Widget <a href="#accessing-the-widget" id="accessing-the-widget"></a>

To get started, you'll need to create a price test in the Intelligems app, and open the Intelligems preview widget for that test. There are two ways to access the Intelligems Preview Widget:

1. Navigate to the "Tests" tab in the Intelligems app. Click on the eyeball icon to the right of the Price Test you have created. This will open a new browser window up with your website with the widget enabled.
2. You can also enter this mode by adding /?ig-preview=true to the end of your website's URL (e.g. <https://mystore.com/?ig-preview=true>). This will open a modal where you can choose which experiment you would like to see in the onsite widget. To tag prices, be sure to select a price test from this dropdown.

Once you are in Preview mode, select the "Edit" button followed by the dollar sign. The video below will walk you through this process:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9f356697b5849898d37325f1ad158f6886e831b9%2F12%20-%20preview%20selectors.gif?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The Intelligems Widget offers full support for **Google Chrome**. Support for any other browsers is limited. If you are having an issue with the Widget in another browser, we suggest trying to run it in Google Chrome. For more support, please open a ticket with our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!
{% endhint %}

## Step 2: Adding Price Selectors <a href="#adding-price-selectors" id="adding-price-selectors"></a>

Now that you are in Edit mode, it is time to tag price elements everywhere on your site. Follow the steps below:

1. **Enable price tagging mode** - Click the $ icon in the edit widget
2. **Enable price selector mode** - Click the box labeled 2 in the image below
3. **Tag price elements** - Move your cursor to see blue dotted lines around page elements. Click a price element to add it to the query selector list. Click Save to highlight the element:
   * Green = product is in the test you are currently previewing
   * <mark style="color:blue;">Blue</mark> = product is **not** in the test you are currently previewing
   * If the price for a product in your test is highlighted in blue, Intelligems can't identify the product or variant ID - see [this guide](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element) for the required theme change
4. **Tag all prices** - Add query selectors to the correct section (compare at price for strikethrough prices, price for regular prices, etc.) for all prices on your site, except for products added to your cart or your checkout page
5. **Save your work** - Click Save periodically to avoid losing progress

<div data-with-frame="true"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-65658f56dd772da04b1b57df9c3a28c86eb56b6b%2FScreenshot%202025-10-06%20at%2010.59.01%E2%80%AFAM.png?alt=media" alt=""><figcaption><p>1. The type of selector - see more below for what each type is for.<br>2. Enable selector mode - clicking this button will allow you click on your prices on your site and automatically add a new selector.<br>3. Query selectors that have been added.<br>4. Delete a query selector.<br>5. Simplify a selector - use this function if the selector added was too specific.<br>6. Add a query selector manually.<br>7. Auto add all price selectors on your site using AI.</p></figcaption></figure></div>

<details>

<summary>A few places to keep in mind as you tag all of the prices elements in your store include:</summary>

* Homepage
* Collection Pages
* Product Detail Pages (PDPs) - make sure you don't miss tagging any related or recommended products listed on your PDPs!
* Search Results Page or Bar, depending on where results show price
* Product Quiz
* Upsells in the cart or at checkout

</details>

<details>

<summary>Here are all of the different selector types:</summary>

**Price:** Use this section to select product prices on your store's site.

**Compare At Price:** Use this section to select compare prices on your store's site.

**Installment:** Use this section to select installments on your store's site. The default number of payments is 4. To change the payment amount, add the below to the element containing your installment in your theme.

```
data-payment-count="{{payment_amount}}" 
```

The Installment selector is compatible with installments that are:

1. Directly in your liquid
2. Not in the liquid, but is wrapped in its own \<span>

This selector is **not** compatible with installments that are:

1. Wrapped in a Shadow DOM
2. Not wrapped in its own span

**Savings (Price):** Use this option to select the dollar savings amount. This is normally located on your product pages.

**Savings (Percentage):** Use this option to select the percentage savings amount. This is normally located on your product pages.

**Cart Discount Message:** Use this option to hide a discount message (i.e. DISCOUNT or INTELLIGEMS) in your cart.

</details>

<details>

<summary>A few tips &#x26; tricks:</summary>

**Per Unit Prices.** If you have per unit prices listed for a product, you can follow these steps to update those prices accordingly during a price test:

1. Tag the per unit prices with a normal Price selector.
2. In your theme code, add `data-price-multiplier=".X"` to the per unit element, where X is what you want to multiple the price by. For example, if you wanted to show the per unit price when there are three units included, you would add `data-price-multiplier=".33"` to the element.

**Discounted Prices.** Many brands use the compare price field in Shopify to show a perceived discount - these are easy to tag using our various selector types. However, some brands will use a different method to show discounted prices by manipulating the frontend prices & using something like a Checkout Script to achieve a perceived discount. If this is the case for your store, follow these steps to accurately tag those prices:

1. Tag the per unit prices with a normal Price selector.
2. In your theme code, add `data-price-multiplier=".X"` to the discounted price element, where X is the inverse of the discount you are applying. For example, if you were running a 20% discount, you would add `data-price-multiplier=".8"` to the element.

</details>

You'll know you're done when all price, compare at price, installment and savings elements are highlighted in blue or green on all pages in your store!

{% hint style="danger" %}
Note that you **should not tag prices in the cart or cart drawer** as we will manage updating those using Cart Transform Functions.
{% endhint %}

{% hint style="info" %}
Having issues? Checkout our troubleshooting guide [here](https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting) or submit a ticket to our support team [here](https://portal.usepylon.com/intelligems/forms/price-test-integration-request)!
{% endhint %}
