# Source: https://docs.intelligems.io/personalizations/personalization-modifications.md

# Personalization Modifications

When setting up a Personalization, you can add one or more modifications based on your goal - whether it’s as simple as a text change or as complicated as a rebrand with interactive javascript elements.

There are 3 classes of modifications:

* **Content changes -** these modify your text, layouts, and functionality.
* **Price changes -** used to update the prices on one or more products directly
* **Offers -** these deliver discounts and other promotions that appear on the PDP, in the cart, and at checkout without the need for coupon codes.

You can combine several modifications in one Personalization, subject to limitations.

You can also limit which site pages your changes apply to by using [Page Targeting](https://docs.intelligems.io/targeting-personalizations#page-targeting).

## **URL Redirects**

URL Redirects allow you to set rules that re-route visitors from one page to another permanently or on a one time basis. This is useful in a variety of scenarios, and especially for showing a different version of a PDP to visitors coming from a specific channel or campaign.

**When to use Redirects:** URL redirects should be limited to a particular audience. When a Personalization is aimed at all visitors rather than a specific segment, it’s best practice to just update all of your links directly in Shopify. This ensures better performance and keeps your baseline site set up the way you want it.

You can read more about URL Redirects [here](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-split-url-test).

{% hint style="danger" %}
**Mixing URL Redirects with other Modifications:** Any modifications mixed with URL Redirects in the same Personalization will not take effect until visitors hit the redirect origin page. For example, if your Personalization contains a redirect from page A to page B, and also contains CSS change and Content Edit modifications, the CSS and Content Edits will not be visible until a visitor has visited page A. Once they have, all modifications will take effect and continue taking effect on all pages where they are applicable. To get around this, you can create two Personalizations with identical audiences - one with the URL Redirect and the other with remaining modifications.
{% endhint %}

## **Content Edits**

Content edits allow you to modify text, images, and other page elements. Content Edits are made by clicking elements directly in your site using our visual builder. To make one or more content edits:

* Add the Content Edits modification
* Click to enter the visual editor in a new tab. Once you're there, click the icons on the top left to select text, images, and other page elements that you wish to change.
  * Read more about editing site images [here](https://docs.intelligems.io/general-features/image-onsite-editor)
  * Read more about editing other site elements [here](https://docs.intelligems.io/general-features/onsite-editor)
  * You can also change CSS and javascript here. Read more [here](https://docs.intelligems.io/general-features/css-and-javascript-injection)
* Once you’ve finished making changes, click Save. You can close this tab.
* Return to your original Personalization’s browser tab where you will see the list of edits you’ve made and can continue editing your Personalization.

{% hint style="info" %}
*You cannot use Content Edits if you have a headless storefront.*
{% endhint %}

## **Styles & Javascript**

If you're a technical user, you can use this Modification to inject custom CSS or Javascript into your site’s pages for visitors to this Personalization. CSS modifications can be used to hide buttons or text, change layouts and spacing, swap backgrounds, or change your color palette and fonts. Javascript changes can be used to pop up messages, modify button behavior, send information elsewhere, and much more.

{% hint style="info" %}
You can find additional tips and tricks for writing effective CSS and javascript [here](https://docs.intelligems.io/general-features/css-and-javascript-injection), including how to ensure the page has loaded before your code runs.
{% endhint %}

## **Theme Changes**

This modification allows you completely overhaul your site - from branding to navigation - by showing a different Shopify theme for visitors in this Personalization.

To set up a theme change, choose the theme you’d like to be shown instead of your shop’s live theme, making sure the theme is integrated so that Intelligems can function correctly.

Note that a Personalization can not contain both a Theme Change and Template Change modification, as a particular template may not be present in the target theme.

{% hint style="danger" %}
Theme changes can leave your site unstable so generally should be[ applied directly in Shopify](https://help.shopify.com/en/manual/online-store/themes/adding-themes) if you are targeting all visitors. If you are targeting a specific audience, you should follow a number of precautions, preview carefully, and test your live site frequently. [Learn more here](https://docs.intelligems.io/personalizations/theme-personalization-precautions).
{% endhint %}

{% hint style="danger" %}
To ensure that your shop continues to function smoothly, do not delete your chosen theme for at least a month, even after stopping a Personalization. [Learn more here](https://docs.intelligems.io/personalizations/theme-personalization-precautions).
{% endhint %}

{% hint style="info" %}
You cannot have more than one theme change active at the same time across your Personalizations and tests. Multiple theme changes can cause endless loops or failure in redirection. If you do have multiple theme changes live, make sure that your tests and Personalizations are targeting exclusive audiences.
{% endhint %}

## **Template Changes**

Template Changes allow you to overhaul the layout and appearance of a particular page or types of pages on your site by swapping out one page template in your site for another. You can read more about Shopify templates [here](https://help.shopify.com/en/manual/online-store/themes/theme-structure/templates).

You can read more about the ins and outs of Template Changes [here](https://docs.intelligems.io/content-testing/content-testing-getting-started/how-to-set-up-a-template-test).

{% hint style="info" %}
Note that a Personalization can not contain both a Theme Change and Template Change modification.
{% endhint %}

{% hint style="info" %}
We encourage using Template Changes targeted to specific audiences, but if you are targeting all visitors it's best to just change the template directly in Shopify to maximize performance, stability, and prevent unforeseen interactions between tests and Personalizations.
{% endhint %}

Note also that each Personalization is limited to swapping one single template for another. If you’d like to swap more than one template you can create multiple Personalizations and assign them the same audience.

## **Offers**

There are multiple Offer modifications:

* Amount off products
* Amount off orders
* Volume discounts
* Free shipping
* Free gift

Offers can be configured to display customizable popups, progress bars, and quantity button components. Learn more about **Global Styles components**.

Unlike Price Modifications, Offers do not update prices on your site pages and collections. Instead, like Shopify discount codes, they update the costs and totals shown in your cart and at checkout. If you want to update the prices shown on your site’s pages directly, use a Price modification instead.

[Have a look at this guide](https://docs.intelligems.io/offer-personalizations/offer-modifications) for more details on offers and how to set them up.

{% hint style="info" %}
You cannot combine Offers and Price Modifications in a single Personalization
{% endhint %}

## **Price Changes**

Unlike offers, Price changes allow you to modify the actual price and compare-to (strikeout) price shown on individual PDPs and other pages across your site, rather than just showing a discount in your cart and at checkout.

To set up the Price Modification

* Tag Prices: before you display new prices, you must indicate to Intelligems where prices appear across the pages of your theme. This can be done in two ways: 1. (recommended) ask the Intelligems team do this for you as part of your site’s Integration process 2. Do it yourself in the onsite editor, [closely following these instructions](https://docs.intelligems.io/getting-started/price-testing-integration-guides). This only needs to be done one time.
* Select one or more products whose prices you’d like to reduce
* Enter new prices as well as compare-to prices. You can do this by
  * Manually typing them in
  * Using the quick-fill option to quickly reduce by a certain amount or percent
  * Downloading a spreadsheet of products selected, specifying new prices in the `Price-Control Group`, and `Compare Price - Control Group` columns, and uploading it again. Find out more about filling out the spreadsheet [here](https://docs.intelligems.io/price-testing/how-to-set-up-a-price-test#uploading-a-spreadsheet).
* Note that you can only reduce prices on products in a Personalization for technical reasons.

{% hint style="info" %}
You cannot combine Price Modifications and Offers in a single Personalization.
{% endhint %}

{% hint style="info" %}
Duplicate products and Subscriptions products are not supported for Personalizations.
{% endhint %}

{% hint style="info" %}
Price Modifications do not work across currencies. Any Personalization using a Price Modification will have [currency targeting ](https://docs.intelligems.io/targeting-personalizations#currency-targeting)activated and set to the default store currency. This means only visitors using the store's default currency will see the Personalization.
{% endhint %}

Click [here](https://docs.intelligems.io/price-testing/price-testing-getting-started) to read more about price changes.

## Next Steps

Once you’ve set up your Modifications, you can go on to:

* Preview them to make sure everything functions correctly on your site before activating the Personalization. Click [here](https://docs.intelligems.io/personalizations/previewing-personalizations) to read our Preview guide.
* Optionally Set Audience Targeting to limit who should see this Personalization and which pages, if not all, the modifications should appear on. Click [here](https://docs.intelligems.io/personalizations/targeting-personalizations) to read the full Targeting guide.
