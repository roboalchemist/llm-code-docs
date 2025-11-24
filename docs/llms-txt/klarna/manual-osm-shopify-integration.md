# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/manual-osm-shopify-integration.md

# Manual On-site messaging

## This guide covers the manual integration of Klarna On-site messaging with a Shopify store when the app isn’t compatible with your store.

The manual integration is considered custom merchant code. You should use it only when it has been confirmed that the On-site messaging app can’t work inyour Shopify store. You’re responsible for supporting and maintaining the custom code if you choose to integrate OSM manually. If the Klarna On-site messaging (OSM) Shopify app isn’t compatible with your store, you can integrate Klarna On-site messaging manually or use a combination of the app and custom code. If you’re integrating Klarna On-site messaging manually, you can choose to either use custom code for all features, or use a combination of the Klarna OSM Shopify app’s features with some custom code for JavaScript functions and refreshing placements. To make sure on-site messaging complies with legal requirements, make sure that your custom code includes functions that refresh the placements when variants change.

## 1. Get the On-site messaging JavaScript library from Klarna

To add the JavaScript library to your Shopify store, you have to first retrieve the URL of a JavaScript library specific to your Merchant ID (MID). You can find the URL in the [Klarna Merchant portal](https://portal.klarna.com/).

## 2. Use API to add the Klarna On-site messaging JavaScript library to the Shopify store

Once you know the URL of the JavaScript library specific to your MID, you have to add it to your Shopify store by sending a POST request to Shopify’s API.

``` json
{
  "script_tag": {
    "event": "onload",
    "src": "https:\/\/na-library.klarnaservices.com\/merchant.js?data-client-id=711111-222222-333333"
  }
}
```

An example body of a `POST` request to the Shopify API that adds a new script to a Shopify store. You can find full documentation about using a POST request to add JavaScript to a Shopify store in the [article on Shopify’s developer documentation page](https://help.shopify.com/en/api/reference/online_store/scripttag). Below is an example body of a POST request that adds a new script tag file to a Shopify store. For example, if the URL of your Shopify store is *<https: yourshopifystorename.myshopify.com="">*, the file containing the OSM script can be added to <https: admin="" script_tags.json="" yourshopifystorename.myshopify.com="">.

## 3. Add placement tags to the theme

Once you’ve added the Klarna On-site messaging JavaScript library to your store, you have to insert placement tags into the correct theme files.

``` html
<!-- Placement v2 -->
<klarna-placement data-key="credit-promotion-standard" data-locale="en-SE" data-purchase-amount="{{ current_variant.price }}"></klarna-placement>
<!-- end Placement -->
```

Example placement code for a Shopify theme. The specific files to be updated with the OSM placement tags differ between Shopify themes. For example, if you’re using the *Brooklyn* theme, both the klarna-placement tag and refresh code are put into the product.liquid file. The correct liquid variable for the product price, which also depends on the store’s theme, must be used for the placement. In the example code, current_variant.price is the correct variable. Depending on your store’s theme and section of code, you may use variant.price, current_variant.price, or another liquid variable.  You can find the placement code snippets in **Klarna Merchant portal**\> **On-site messaging**\> **Placements**.

## 4. Add code to refresh placements when product variants change

If the products in your store have variants, you also need to add code to update the placement when a customer selects a different variant. Here's an example of code to refresh placements:

``` javascript
document.getElementsByTagName("klarna-placement")[0].setAttribute("data-purchase-amount", variant.price);
window.KlarnaOnsiteService = window.KlarnaOnsiteService || []
window.KlarnaOnsiteService.push({ eventName: 'refresh-placements' })
```

An example code that forces placements to be refreshed when a product variant changes. We've documented this in detail in the [frequently asked questions](https://docs.klarna.com/platform-solutions/e-commerce-platforms/shopify/conversion-boosters/frequently-asked-questions) **To summarize:**

- The Klarna On-site messaging (OSM) Shopify app may not be compatible with all stores, but manual integration is possible.
- Integrating Klarna On-site messaging manually requires adding the JavaScript library to the Shopify store using API and inserting placement tags into the correct theme files.
- Custom code is necessary to refresh placements when product variants change, ensuring compliance with legal requirements.</https:></https:>