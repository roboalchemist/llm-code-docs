# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/troubleshooting.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/troubleshooting.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/troubleshooting.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/troubleshooting.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/troubleshooting.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/troubleshooting.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/troubleshooting.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/adobe-commerce/payments/troubleshooting.md

# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/klarna-osm-app-for-shopify/troubleshooting.md

# Shopify troubleshooting

## In this section you can read about some common issues with the Klarna On-site messaging Shopify app and learn how to fix them in your store.

## Debug issues with console debugging

You can debug Klarna On-site messaging Shopify app issues and review the app’s functionality in the browser by enabling console debugging. To do so, open a store where a placement is located and append `?consoleDebug=true` to the URL. If there are already parameters in the URL, append `&consoleDebug=true` instead. Then, navigate to your browser’s **Developer tools**\> **Console** and look for messages related to Klarna On-site messaging, as shown in the screenshot below.


![ In a browser’s Console, enter osm to filter logs for messages related to Klarna On-site messaging.](f257227f-76ce-4f2a-940b-0dc3eadd8e68_consoleDebug.jpeg)
*In a browser’s Console, enter osm to filter logs for messages related to Klarna On-site messaging.*

## The placement isn’t displayed on my product pages

If a placement isn’t displayed on a product page, we recommend testing in a new incognito window to avoid caching. Also, please wait a few minutes and refresh a few times after changes are made to give the code time to update. If you have chosen geolocation you will also need to use a locale that is supported by what is on your Klarna merchant ID and matches your store currency. If it's an unsupported locale, the placement won't show. This is correct behaviour. When using the app, don’t manually update your store’s theme files with code from the On-site messaging section within the Klarna Merchant portal, as that can prevent the On-site messaging Shopify app from working. If the on-site messaging doesn’t appear on the storefront for any page, try the following troubleshooting options:

1.  **Verify that the geolocated locale is supported for your store's single base currency** as currently [only a single currency can be accepted for Klarna orders](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/payments/known-constraints.md). You can check the locale identified with [consoleDebug logging](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/troubleshooting), and also test by [setting your locale in the session variables to any desired country](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/locale-and-display-language.md).
2.  **Inspect the page to check if the placement exists on the page but is hidden**, for example, with the CSS `display: none` property. If the placement is hidden, try a different CSS selector to find one that isn’t hidden.
3.  **Verify that the store doesn’t have any manual on-site messaging code**, such as extra `script` or `klarna-placement` tags, copied from the Klarna Merchant portal. Manual on-site messaging code often interferes with the OSM Shopify app and causes the placement to not show in the storefront. The placement may be injected, but not show the content as the empty 0 by 0 pixels element. The OSM code is available in the Klarna Merchant portal for any merchant, but adding the JavaScript library to a Shopify store isn’t necessary as the app’s code retrieves the necessary OSM JavaScript and data real-time API requests to Klarna’s API.
4.  **Check for JavaScript errors** as these can sometimes prevent the Klarna OSM app from working correctly.

If the placements display on some pages but not others, try the following troubleshooting options:

- **Verify that the product price is within the configured minimum and maximum of supported prices** applicable to Klarna payment options. If the product price falls outside of that range, the ad may display for some products but not others.
- **Verify that the CSS selector used for the Ad Position exists on all pages**. If the chosen CSS selector only exists for some pages, for example, desktop theme pages but not mobile theme pages, the ad will only display on pages where the CSS selector exists.

While we’ve worked hard to build the Klarna OSM Shopify app to work with most themes, if it isn’t able to find correct anchor tags for your theme, you can either inspect the page or view the source to manually choose a CSS selector or manually edit your theme to insert the custom selector. If you need further support, please contact [your regional Klarna merchant support team](http://klarna.com/merchant-support).

## The placement isn’t displayed on my cart pages

If you have an active cart placement, verify that on-site messaging is displayed on the full page cart. An example URL of a cart page can be *<https: %7bstore=""> name}/cart*. The Klarna On-site messaging Shopify app doesn’t inject on-site messaging for mini-cart or pop-cart pages for the Cart page type Ad Position or Cart App Block. Depending on your store’s theme, you may be able to add on-site messaging to mini-cart pages. To check if your theme supports this, do the following:

1.  Go to the page where you want to add the placement.
2.  Use the browser's Developer tools to inspect the `mini-cart` HTML
3.  Right-click on the page and select **View Page Source**.
4.  Look for the `mini-cart` HTML element in the page’s source code. If the `mini-cart` HTML element is present in the page source code, the page supports adding Klarna On-site messaging placements.

For the Klarna OSM Shopify app's Ad Position for mini-cart, select the **Product** page type and use the CSS install method (Vintage option, not App Blocks, unless your theme supports a mini-cart theme template for App Blocks). In order to use the CSS install method, you need to determine an appropriate CSS selector, which can be found using the browser’s Developer Tools. A unique selector on the page that is consistent for any variation of the page works best. Alternatively, you can add a [custom CSS selector to the page](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/troubleshooting).

## The On-site Messaging Script loads on every page

This is likely related to using [vintage ad placements](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/vintage-ad-placements) (instead of [App Blocks](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/app-block-placements)), that are going to be deprecated in 2025. You can follow these steps to change this using our app block functionality within the app:

1.  Go to App Blocks instructions
2.  Scroll down and click *Verify* and *Continue*. **This action will delete all vintage placements** **from the online store**, but the action is reversible (see point 3.)
3.  *note*: If you don't have an app block on your site already, a warning banner saying Unable to detect App Blocks will appear. The process can still be continued.
4.  If you would like to Switch to Vintage mode again, you can still go to App Blocks Instructions and click Switch to Vintage mode, although **switching back is not recommended** as the Vintage mode functionality will be deprecated in 2025.


![klarna docs image](Zwy7XoF3NbkBXYbm_Screenshot2024-10-14at07.02.14.jpeg)image

## How to have messaging at a specific location (custom CSS)

 To insert a placement at a specific location, add a new custom `span` HTML element in the specific, desired location on your theme page by updating your appropriate theme liquid file, for example, `product.liquid`, in the correct place:

``` html
<span id="ShopifyKlarnaOnSiteMessagingAppElement"></span>
```

A `span` element lets you insert a placement in a specific place in the source code. This can be a one-line code change to your theme, but the above code snippet won’t display on the storefront if added in the right location. Instead, it creates a specific anchor element to which the Ad Position can be attached. The location is consistent across all the applicable storefront pages. When you’re adding the `span` element, be careful to add it in a location that doesn’t interfere with the code within your team. For example, don’t add it inside JavaScript code or other code functions. Theme developers or [Klarna merchant support](https://www.klarna.com/uk/business/merchant-support/) can help you with this step if needed. Once the element exists on the theme page, go to the **Shopify admin**\> **Apps**\> **Klarna On-site Messaging**\> **Dashboard**. Then, select the correct Ad Position and update the Ad Position by entering`#ShopifyKlarnaOnSiteMessagingAppElement` as the CSS selector. This will specify the anchor element.


![ Creating an anchor element for a custom CSS selector.](47704c23-bcab-4cff-8c3e-07a367596ccb_Shopify_Klarna_span_2023_08-01.jpeg)
*Creating an anchor element for a custom CSS selector.*

If the placement doesn’t display on the storefront, view the HTML source of the page and search for your custom `span` element, `ShopifyKlarnaOnSiteMessagingAppElement`. If it doesn’t exist, edit the theme’s liquid files to put the custom CSS selector in a location that does exist for the page.

## The placement isn’t updating when I change the variant

The Klarna On-site messaging Shopify app attempts to update the price attribute of the placement when variants are changed. The app then calls the r`efresh-placements` event on the `KlarnaOnsiteService` data layer. For the app to detect changes in variants and to retrieve the price, the shop theme must be configured in a way that appends the variant id to the URL, for example, *<https: myshop.com="" products="" test-product?variant="1234567890123">*. The app detects changes in variants by listening to input/select elements. If the theme is using a different approach, you have to customize the theme so that the following JavaScript function is called within the appropriate theme JavaScript code that is triggered by the theme when variants change. This way, the updated purchase amount is passed.

``` javascript
window.KOSMApp.updatePurchaseAmount(newPurchaseAmount);
```

## Messaging disappears after switching themes

Klarna On-site messaging for a Shopify store utilizes CSS data within a theme. If the theme is changed for a store, all active Ad Positions are deactivated by the Klarna On-site messaging Shopify app by default. After changing a theme, you need to reactivate, and possibly reposition, the On-site messaging placements in the app using the new theme. You can use the app’s **Ad position settings** configuration to disable deactivating the placements, as shown on the screenshot below. As described in Shopify admin, we recommend that you test the placements after making theme changes.


![ The Ad position settings configuration for the Klarna OSM Shopify app lets you keep placements active after your store theme changes.](83e8cde2-ac01-49e7-9636-b96d52855a50-shopify-skosm-deactivate-after-theme-change.jpeg)
*TheAd position settingsconfiguration for the Klarna OSM Shopify app lets you keep placements active after your store theme changes.*

## On-site messaging displays the wrong currency

If a currency displayed on a placement is incorrect, verify that the country selected for your Ad Position uses the same currency as your store’s base currency. For example, if your store is selling in EUR, make sure to select a country that uses EUR.

## My country isn't listed in the select box

When you first install the app, it connects to a Klarna endpoint based on your Shopify store’s base address, which determines the countries available in the app. If those countries aren’t appropriate for your Klarna account, go to your store’s **Shopify admin**\> **Apps**\> **Klarna On-Site Messaging**\> **Settings** and click **Disconnect account**. Then, reconnect the account. When reconnecting, choose the correct endpoint from the **Select Endpoint** dropdown as shown in the screenshot below:


![ The endpoint you select while connecting your Klarna account determines which countries are available in the app.](91857f63-cfa1-47e8-8511.jpeg)
*The endpoint you select while connecting your Klarna account determines which countries are available in the app.*

## A fallback placement is displayed instead of the selected one

If storefront pages display the fallback placement, for example, a top-strip-promotion placement, instead of the desired amount-based placement you configured placement, verify that the app’s code can retrieve the product's price.

## On-site messaging is loading slowly in my store

Following Shopify’s requirements for apps for loading app asserts, the JavaScript for Klarna’s On-site messaging is loaded using Shopify’s [ScriptTag API](https://help.shopify.com/en/api/reference/online-store/scripttag), which can be confirmed by searching for the `asyncLoad()` function in the HTML source code of the storefront page.


![ Searching for the asyncLoad() function in the page’s HTML source code.](19c41b56-7cc2-4bfe-9528-d0b06df582e0-shopify-skosm-asyncLoad.jpeg)
*Searching for the asyncLoad() function in the page’s HTML source code.*

Following this standard, Klarna On-site messaging JavaScript is loaded asynchronously, after the main content of the page has loaded, and scripts are loaded in order of app install to the store. This prevents the app’s JavaScript from slowing the page load, but it also means that the JavaScript is loaded along with all app’s JavaScript libraries, so other apps in the store that use JavaScript affect the loading time for Klarna’s On-site messaging. The more app JavaScript libraries a store loads, the more time needed for Klarna On-site messaging to load. If On-site messaging is slow to load in a store, review the installed apps to verify they are all still needed and review all the resources loaded for the page, for example, using the browser’s developer tools. Other factors, for example, network speed, device, and location, also affect load times. You can check your store's Online store speed in **Shopify admin**\> **Settings**\> **Sales channels**\> **Online Store**. The Klarna On-site messaging Shopify app can only update the placement after a variant change if the theme follows Shopify standards to allow this app to listen to the event listeners in order to track variant changes. Some themes, for example, [Simple](https://themes.shopify.com/themes/simple/styles/light) and [Brooklyn](https://themes.shopify.com/themes/brooklyn/styles/classic), have the event listeners unset. If that’s the case, you can add the below code in the `theme.liquid` file to override the listeners being unset. The code forces input listeners to reinitialize after 100 ms.

``` html
<script>
     setTimeout(function() {
       if (window.KOSMApp) {
               window.KOSMApp.listenForInputChange();
       }
     }, 100);
  </script>
```

A code snippet that forces input initializers to reinitialize. In this example, the value is 100 ms.

## Error when upgrading to Checkout Extensibility


![ An error related to upgrading to the Checkout Extensibility](ZvErC7VsGrYSvqhB_image-20240830-133021.jpeg)
*An error related to upgrading to the Checkout Extensibility*

If seeing this error when upgrading to the Checkout Extensibility, you likely have old configuration in your store or checkout.liquid files in your themes. The error is unrelated to the Klarna On-site Messaging app, even if it may be indicated that the app customizes thank you and order confirmation pages. Once the old configuration or checkout-liquid files are updated, the error will no longer be displayed.

## Common warnings and errors

### “Risky Ad Position” error message in preview

When changing the position of a placement, you may see a following error: “Warning. Risky Ad Position. An ID has been selected. Ensure that the id isn’t unique to the preview page, or it might get hidden on other pages”. The “Risky Ad Position” error can appear when there’s a risk of the placement being hidden on pages other than the preview page. If you see this error, try a different position on the page or a different preview product for the Shopify Ad. The position of a placement attaches to a CSS selector on the page, which should be a CSS option that is available on all product pages. You can view the chosen CSS selector in **Install methods**\> **CSS**. If you don’t find a correct selector by dragging and dropping, you can manually enter an appropriate CSS selector from your page, or, if the placement is already the desired position, review the frontend store view and verify that it’s working correctly across products.

### Error: Request failed with the status code 404

If this error is shown in the On-Site Messaging app there are usually two solutions: 1. You need to disable test mode in the Klarna Payments app settings. 2. You have connected the On-Site Messaging app to the incorrect endpoints (Europe/North America/Australia) in which case you will need to disconnect and reconnect the app.


![klarna docs image](8db078a9-00a0-472c-966a-5d1e849eb0be-404-Error.jpeg)image

![klarna docs image](419f4541-0aea-41a8-afd9-c7e65249ed12_Endpoints.jpeg)image

### JavaScript console error: getRandomValues

If the `klarna-placement` HTML element exists on the page (**Developer tools**\> **Elements**), but doesn’t display on the storefront, check the browser’s **Console** for JavaScript errors. If you find the following error: “Uncaught (in promise) TypeError: Cannot read property 'getRandomValues' of Undefined”  update the store to not overwrite the window variable. On-site messaging code expects window.self property to proxy the window object as documented in the [the Window: self property documentation in MDN](https://developer.mozilla.org/en-US/docs/Web/API/Window/self). You can also try to debug this error by entering window.self in your browser’s **Developer tools**\> **Console**. The window.self property is expected to return data as shown below, which you can test in the browser's console at [<https: klarnastore.myshopify.com="">](https://klarnastore.myshopify.com/).

``` javascript
Window {parent: Window, opener: null, top: Window, length: 1, frames: Window, …}
```


![klarna docs image](5e4ab062-e23b-48be-938b-79cf5e143b7c-shopify-skosm-window-self.jpeg)image

### SameSite attribute cookie browser warnings in the app preview

These warnings can be ignored in the app preview; only warnings in your storefront should be reviewed. These warnings are due to cookies not set by this app, so these warnings can’t be resolved by the app. Below is a copy of the error message for reference:

- A cookie associated with a cross-site resource at <https: shopify.com=""></https:> was set without the \`SameSite\` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with \`SameSite=None\` and \`Secure\`. You can review cookies in developer tools under Application\>Storage\>Cookies and see more details at [<https: 5088147346030592="" feature="" www.chromestatus.com="">](https://www.chromestatus.com/feature/5088147346030592) and [<https: 5633521622188032="" feature="" www.chromestatus.com="">](https://www.chromestatus.com/feature/5633521622188032)."


![klarna docs image](58f31f4e-adde-40cc-b79a-2a186a7cb266_-hopify-skosm+same-site-cookie.jpeg)image

### “Warning: This Ad Position may not work..." message in preview

If the error following error appears in preview: "Warning: This Ad Position may not work, as it was not found when the page was loaded initially.” it’s possible that the JavaScript library was [lazy loaded](https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading), which isn’t compatible with the Klarna OSM Shopify app.

## Known Constraints

Some incompatibilities can affect the Klarna On-site messaging in your Shopify store. Below you will find examples of known incompatibilities.

### Known incompatibilities

The following libraries, apps, and features are incompatible with the Klarna On-site messaging (OSM) Shopify app as they either block the preview of the storefront page within the app or block the storefront functionality of the app:

- [instantclick.io](http://instantclick.io) 
- [fastclick](https://www.npmjs.com/package/shopify-fastclick)
- [Locksmith (app or script)](https://apps.shopify.com/locksmith)
- [<https: code="" www.filamentgroup.com=""></https:>](https://www.filamentgroup.com/code)
- [Core Web Vitals Booster](https://apps.shopify.com/superspeed-your-store-faster)
- some RECAPTCHA apps
- page counters
- quick view product modal page overlays, as described in [this article](https://archetypethemes.co/blogs/streamline/why-don-t-my-apps-work-in-quick-view)
- lazy loading of JavaScript as the app’s functionality requires its JavaScript library to not being lazy loaded
- Several compliance tools, such as Termly.

### Discount on Cart Pro

The [Discount on Cart Pro Shopify app](https://apps.shopify.com/discount-on-cart-pro) updates a klarna-placement HTML element’s data-purchase-amount attribute based on items in the cart. When the items in the cart don’t match the product page, data-purchase-amount doesn’t match the product price, causing On-site messaging price to be inaccurate. For additional debugging, you can get logging by adding the URL parameter ?docp-test-log.

### Theme incompatibilities

The Klarna OSM Shopify app relies on Shopify standard use of certain theme variables, such as the product and template variables. If a theme’s code overwrites these variables in a non-standard manner, the theme isn’t compatible with Klarna On-site messaging. For example, this can happen if a liquid file contains either of the following lines of JavaScript code: {%- assign product = null -%} or {%- assign template = template.name \| handle -%}

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

Currently, the Klarna On-site messaging Shopify app only supports connecting a store with a single Klarna merchant ID, which you can do in your store’s **Shopify admin**\> **Settings**\> **Apps**\> **Klarna On-Site Messaging**.  Some Klarna for Shopify integrations, for example, [Global-e](https://www.global-e.com/klarna-partnership), can support multiple Klarna MIDs. As an alternative, you can [manually integrate Klarna On-site messaging with your store](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/manual-osm-shopify-integration.md).</https:></https:></https:></https:></https:>