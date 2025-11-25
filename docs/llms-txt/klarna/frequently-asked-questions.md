# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/frequently-asked-questions.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/wix/payments/frequently-asked-questions.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/frequently-asked-questions.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/wix/payments/frequently-asked-questions.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/frequently-asked-questions.md

# Shopify FAQ

## Get answers to common questions about Klarna’s On-site Messaging App for Shopify, including integration, localization, and customization to match your store’s branding.

## Which placement should I pick?

See our recommendations below!

| **Placement** | **Best for** | **Use on** | **Additional Info** |
|----|----|----|----|
| `credit-promotion-badge` `credit-promotion-auto-size` | \| Showing customers the price breakdown and available Klarna Payment methods | Product page, cart page | Dynamically updates when the price changes For best results, put the placement close to the product price or cart total Will not work on homepage or collections pages |
| `info-page` | \| Explaining how Klarna works to new customers | FAQ page, or use this placement on a page of its own | You cannot customize the images in this placement |
| `top-strip-promotion-auto-size` `top-strip-promotion-standard` `top-strip-promotion-badge` | \| Announcing that Klarna is available on any page | Header section, but can be used on any page | To add this to your header while using app blocks, you must add a section in the header ​​​​​You can use this placement on product pages if the app has difficulty picking up the correct variant price |
| `footer-promotion-auto-size` | \| Displaying Klarna with other available payment options | Footer section section, but can be used on any page | To add this to your footer while using app blocks, you must add a section in the footer |
| `homepage-promotion-tall` ​`homepage-promotion-wide` ​`homepage-promotion-box` | \| Displaying Klarna during product/brand discovery | Collection pages, home pages |  |
| `sidebar-promotion-auto-size` | \| Displaying Klarna during product/brand discovery | Collection pages, home pages |  |

## How does Klarna On-site Messaging show the correct language and currency to my customers?

Klarna’s On-site Messaging app ensures the currency your customers see in the placement matches the currency displayed on your storefront. The app uses information from your Shopify store ([localization object](https://shopify.dev/docs/api/liquid/objects/localization) and [cart currency](https://shopify.dev/docs/api/liquid/objects/cart#cart-currency)) to show the correct language and currency. When customers are shopping your site in different countries, the language and currency of Klarna On-Site messaging will update automatically.  If it is not possible to change the currency/country of your store, Klarna On-site Messaging will use the default market from your Shopify settings. If your customer is browsing your site in a currency and country combination that does not match [Klarna’s strict locale mappings](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales.md), the Klarna placement will not show.   In addition, Klarna On-site messaging will only show in countries where you can offer Klarna, and will only display the Klarna payment options that are configured on your account.

- Klarna Payments app: your store can only transact in the base currency of your store, and On-site Messaging placements will only show in the country/countries where that currency is used
- Klarna for Shopify Payments: On-site messaging placements will show for the markets/currencies you have enabled.

The placement will disappear if you select a country or currency where you do not offer Klarna. This ensures that you are displaying Klarna placements to customers who can use it for their purchase. In addition, different markets require different legal disclaimers. Klarna On-site messaging will automatically include the appropriate disclaimers, terms & conditions, and privacy policy for each market.

## How do I customize Klarna placements?

You can customize the placements’ font, layout, and other display options to match your brand’s look and feel. You cannot customize the copy inside of the placements. The Klarna On-site Messaging app allows you to apply very basic changes including

- Theme: Default, Dark, Custom
- Padding
- Message prefix: no prefix, “Or”, “or”

Merchants using the Klarna Payments app can further customize the placement by following these instructions in the [Merchant Portal](https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/osm-customise-merchant-portal.md) or by using [CSS styling](https://docs.klarna.com/conversion-boosters/on-site-messaging/additional-resources/styling-on-site-messaging-with-css.md). Merchants using Klarna for Shopify Payments can only use CSS styling. Note that if you’re customizing placement in the Merchant Portal, you have to select the default theme in the Klarna On-site messaging (OSM) Shopify app. The placements in the dark theme aren't customizable.

## Does the Klarna placement update the price breakdowns automatically?

Yes! However the only placements that update automatically are ***credit-promotion-auto-size*** and ***credit-promotion badge***. These display price-based information to the customers. The rest of the placements do not contain price breakdowns, and therefore do not update. **For product pages**: On-site messaging is updated when a different variant is selected. If that isn’t working on your storefront, see [the entry in our troubleshooting guide](https://docs.klarna.com/platform-solutions/shopify/klarna-osm-app-for-shopify/troubleshooting). On-site messaging is ***not*** updated when the product ***quantity*** is changed. **For the cart page:** On-site messaging is updated when product quantities are updated and the page is refreshed. The price breakdown is based on the total cart amount. If On-site messaging isn’t updated on cart quantity changes, you can update the to directly call the JavaScript function, and pass the value of the new purchase amount.

``` javascript
window.KOSMApp.updatePurchaseAmount(updatedPurchaseAmount);
```

A sample JavaScript function to update On-site messaging with a new purchase amount.

## Where can I find the placement data on my storefront page?

To see all instances of the `klarna-placement` HTML element, open your browser’s **Developer tools**\> **Elements** tab. You won’t see the `klarna-placement` element directly in the HTML source of the page as the placements get injected into the DOM by JavaScript when a page is loaded.

## Can I exclude certain products from On-site messaging?

<span>**App blocks placements (theme editor)**: you can assign a Klarna app block placement to individual product templates. This can be used to only display Klarna for certain products.</span> **Vintage placements (Auto Picker,Drag and drop, and CSS)**: the Klarna placement will be displayed for all products.

## Why is the app rating low?

We are continuously improving our products and services to make sure that merchants like you have a smooth experience adding Klarna to your stores. While the app rating isn’t as good as we’d like, we’ll continue working hard to earn your positive reviews. If you use the app, we would appreciate your [feedback in the Shopify App store](https://apps.shopify.com/klarna-on-site-messaging#reviews). For the best experience using the On-site Messaging app, we highly recommend using a theme supporting [Shopify's Online Store 2.0 architecture](https://www.shopify.com/partners/blog/shopify-online-store). You can find solutions to common OSM issues in our  [troubleshooting guide](https://docs.klarna.com/platform-solutions/shopify/klarna-osm-app-for-shopify/troubleshooting). If you still need help to resolve the problem in your store, your region’s Klarna merchant support team is [always here to support you](https://docs.klarna.com/platform-solutions/shopify/support).