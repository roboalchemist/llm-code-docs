# Source: https://docs.intelligems.io/developer-resources/mcp-server/troubleshooting.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting.md

# Source: https://docs.intelligems.io/developer-resources/mcp-server/troubleshooting.md

# Source: https://docs.intelligems.io/price-testing/price-testing-integration-guides/troubleshooting.md

# Troubleshooting

## Background <a href="#intelligems-isnt-updating-a-price-for-a-product-that-is-included-in-the-test" id="intelligems-isnt-updating-a-price-for-a-product-that-is-included-in-the-test"></a>

If you notice that anything isn't working while you are completing the integration for a price test, such as the price not updating on the site, or adding to cart incorrectly, this is a great resource to help resolve your issues. If after reading through this document, you are still running into issues, please feel free to reach out to our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request)!

## Intelligems Isn't Updating a Price for a Product that is Included in the Test on the Homepage, Collection Page or Product Page <a href="#intelligems-isnt-updating-a-price-for-a-product-that-is-included-in-the-test" id="intelligems-isnt-updating-a-price-for-a-product-that-is-included-in-the-test"></a>

In addition to knowing which elements in your store are prices, Intelligems also needs to know which product and/or variant each price is for. Typically, Intelligems is able to figure this out automatically, but in some circumstances, you may need to set it explicitly on a price element. If a price on your website that is included in your test is not updating in preview mode, or is highlighted in blue in integration mode, that is a good sign that you need to follow [these steps](https://docs.intelligems.io/getting-started/pricing-integration-guides/troubleshooting/how-to-add-the-data-product-id-and-or-data-variant-id-attribute-to-an-element) to fix it.

## Intelligems Doesn't Add the Line Item Property <a href="#intelligems-doesnt-add-the-line-item-property" id="intelligems-doesnt-add-the-line-item-property"></a>

When adding a product that's being tested to the cart, Intelligems should add line item property \_igDiscount or \_igp. This indicates the amount of discount to apply to the line item or what the price of the line item should be to affect the correct price for the user's test group. Some common issues with this are:

* The add to cart happened on a page where the Intelligems Javascript was not loaded, such as a landing page that Intelligems has not been integrated with. Check the page source or network traffic to ensure that the Intelligems JavaScript snippet is loading on the page. Learn more about adding the Intelligems JavaScript snippet to your theme [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
* There's an error causing the Intelligems JavaScript to exit early. Check the JavaScript console for errors raised by Intelligems, and check the `window.igData.errors` object for any suppressed error messages.
* The add to cart is happening via a mechanism that Intelligems does not support, or skipping add to cart altogether. Common examples include quick buy buttons, third-party apps that use Draft Orders or landing pages that use checkout permalinks.

## Intelligems Doesn't Swap Duplicate Products When Adding to Cart <a href="#intelligems-doesnt-swap-duplicate-products-when-adding-to-cart" id="intelligems-doesnt-swap-duplicate-products-when-adding-to-cart"></a>

*This is applicable only to non-Shopify Plus stores.* When adding a product that's being tested to cart, Intelligems should swap the duplicate product in that corresponds to the user's test group, unless the user is in the control group, in which case Intelligems will not swap. Some common issues that may cause this to not work correctly are:

* The add to cart happened on a page where the Intelligems Javascript was not loaded, such as a landing page that Intelligems has not been integrated with. Check the page source or network traffic to ensure that the Intelligems JavaScript snippet is loading on the page. Learn more about adding the Intelligems JavaScript snippet to your theme [here](https://docs.intelligems.io/getting-started/adding-intelligems-script-to-your-theme).
* There's an error causing the Intelligems JavaScript to exit early. Check the JavaScript console for errors raised by Intelligems, and check the `window.igData.errors` object for any suppressed error messages.
* The add to cart is happening via a mechanism that Intelligems does not support, or skipping add to cart altogether. Common examples include quick buy buttons, third-party apps that use Draft Orders or landing pages that use checkout permalinks.
