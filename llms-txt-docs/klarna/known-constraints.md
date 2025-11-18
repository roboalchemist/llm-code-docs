# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/known-constraints.md

# Known constraints for On-site Messaging in Shopify

## Read about some limitations that can affect the Klarna On-site messaging in your Shopify store.

## Known incompatibilities

The following libraries, apps, and features are incompatible with the Klarna On-site messaging (OSM) Shopify app as they either block the preview of the storefront page within the app or block the storefront functionality of the app:

- [instantclick.io](http://instantclick.io) 
- [fastclick](https://www.npmjs.com/package/shopify-fastclick)
- [Locksmith (app or script)](https://apps.shopify.com/locksmith)
- [<https: code="" www.filamentgroup.com=""></https:>](https://www.filamentgroup.com/code)
- some RECAPTCHA apps
- page counters
- quick view product modal page overlays, as described in [this article](https://archetypethemes.co/blogs/streamline/why-don-t-my-apps-work-in-quick-view)
- lazy loading of JavaScript as the app’s functionality requires its JavaScript library to not being lazy loaded

### Discount on Cart Pro

The [Discount on Cart Pro Shopify app](https://apps.shopify.com/discount-on-cart-pro) updates a `klarna-placement` HTML element’s `data-purchase-amount` attribute based on items in the cart. When the items in the cart don’t match the product page, `data-purchase-amount` doesn’t match the product price, causing On-site messaging price to be inaccurate. For additional debugging, you can get logging by adding the URL parameter `?docp-test-log`.

### Theme incompatibilities

The Klarna OSM Shopify app relies on Shopify standard use of certain theme variables, such as the product and template variables. If a theme’s code overwrites these variables in a non-standard manner, the theme isn’t compatible with Klarna On-site messaging. For example, this can happen if a liquid file contains either of the following lines of JavaScript code: `{%- assign product = null -%}` or `{%- assign template = template.name | handle -%}`

### GemPages

[GemPages](https://help.gempages.net/articles/introduction-to-gempages) doesn't generally offer a standard CSS selector that can be used across product pages for this app to inject the klarna-placement HTML element. Because of that, themes built using GemPage may require [manual coding](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/manual-osm-shopify-integration.md) until GemPages supports Shopify's Online store 2.0 app blocks.

## Known limitations

### Multi-currency support in the Klarna On-site messaging Shopify app

As Klarna payments as a direct alternative payment integration can only accept orders in the store’s base currency (which is a Shopify restriction for alternative payment methods per [Known issues](https://docs.klarna.com/platform-solutions/shopify/payments/klarna-payments/known-constraints)), the messaging is hidden when the selected currency doesn’t match the store’s base currency when using standard currency switcher functionality.

### Adding on-site messaging to mini-carts or pop-out carts

If your store's theme supports mini-cart as HTML, on-site messaging can work for mini-carts. To learn how to check if you can add placements to the mini-cart, refer to the [Troubleshooting section of this documentation](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/troubleshooting).

### Does the app configuration work in the Safari browser?

Yes, the Klarna On-site messaging Shopify app admin works on the Safari browser within the Shopify store admin.

### The app’s not working on a phone, tablet, Chromebook, or other device

Device manufacturers don’t provide infinite support and operating system upgrades. After manufacturers stop providing operating system upgrades, the web browsers aren’t always kept up-to-date and remain on an older version compatible with the device. While we make every effort to support as many browsers and platforms as possible, we unfortunately can’t provide support for these outdated browsers without providing a worse experience for users of more recent browsers. If the Klarna On-Site Messaging Shopify app doesn’t work on your device, make sure you have upgraded the operating system to the latest version. If the Klarna OSM Shopify app still doesn’t work, your device may not support modern web browser features.

### Does the app support App Blocks within Online Store 2.0 theme architecture?

Yes, App Blocks are now supported by the Klarna On-site messaging within the app, but the Vintage option is still available for any theme. For more information about Shopify's Online Store 2.0, refer to the [Theme architecture versions article](https://help.shopify.com/en/manual/online-store/themes/managing-themes/versions) in Shopify's documentation.

### Supporting multiple Klarna merchant IDs for a single store

Currently, the Klarna On-site messaging Shopify app only supports connecting a store with a single Klarna merchant ID, which you can do in your store’s **Shopify admin**\> **Settings**\> **Apps**\> **Klarna On-Site Messaging**.  Some Klarna for Shopify integrations, for example, [Global-e](https://www.global-e.com/klarna-partnership), can support multiple Klarna MIDs. As an alternative, you can [manually integrate Klarna On-site messaging with your store](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/manual-osm-shopify-integration.md). **To summarize**:

- The Klarna On-site messaging (OSM) Shopify app is incompatible with libraries/apps such as instantclick.io, fastclick, Locksmith, and some RECAPTCHA apps, among others.
- The app has limitations including lack of multi-currency support, inability to add on-site messaging to mini-carts or pop-out carts without certain theme support, and potential compatibility issues on older devices or outdated browsers.
- The OSM Shopify app currently only supports connecting a single Klarna merchant ID to a store.