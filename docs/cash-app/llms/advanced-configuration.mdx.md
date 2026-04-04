# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/woo-commerce/advanced-configuration.mdx

***

## stoplight-id: 6z1l8mazyhk2h

# Advanced Configuration

This section outlines the advanced configuration options related to the Cash App Afterpay WooCommerce integration and site-specific customisation.

The *Cash App Afterpay Gateway for WooCommerce* plugin is available for extension or customisation, without alterations to the plugin code.

This allows for a greater level of compatibility with future updates.

Advanced Configuration is divided into the following sections:

* [Hooks](#hooks)

* [Shortcodes](#shortcodes)

## Hooks

### Product Eligibility

The Cash App Afterpay plugin runs a series of checks to determine whether Cash App Afterpay should be an available payment option for each individual product. Third-party plugins can exclude Cash App Afterpay from products that would otherwise be considered supported. To fix the exclusion problem, attach the following filter hook:\
`afterpay_is_product_supported`

**Example**

```php
/**
 * @param bool		$bool_result
 * @param WC_Product	$product
 */
function afterpay_ips_callback( $bool_result, $product ) {
	# My custom products don't support Afterpay.
	if ($product->get_type() == 'my-custom-product-type') {
		$bool_result = false;
	}
	return $bool_result;
}
add_filter( 'afterpay_is_product_supported', 'afterpay_ips_callback', 10, 2 );
```

### Customising Hooks & Priorities

Various WooCommerce hooks are assumed to be implemented by the active WordPress theme. Cash App Afterpay methods can be detached from their default hooks and reattached to different hooks, or to the same hooks with different priorities.

Since version 2.1.0, hooks and priorities can be customised from within the plugin settings page.

![hook-1.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/hook-1.png)

## Shortcodes

This section outlines the shortcodes utilised by the Cash App Afterpay WooCommerce integration.

### Cash App Afterpay Product Logo

This is provided for rendering an advanced `img` tag to display the Cash App Afterpay logo on individual product pages. The `img` tag uses the `srcset` attribute to include 3 different resolutions of the logo for screens with varying pixel density ratios.

```html
[afterpay_product_logo]
```

There are 3 different versions of the logo to chose from:

* `colour`
* `black`
* `white`

The default theme is `colour`. This can be overridden by including a `theme` attribute inside the shortcode. For example, if you have a dark themed website and wish to use the white mono version of the Cash App Afterpay logo:

```html
[afterpay_product_logo theme="white"]
```

### Cash App Afterpay Product Messaging

To use the shortcode on product pages, please make sure the **Payment Info on Individual Product Pages** has been enabled. Edit the text content as appropriate. Optionally, clear the hook name if you would like to disable the default behaviour of rendering the content when the hook is triggered. Instead, the content will then only render wherever the shortcode is added.

![shortcode-1.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/shortcode-1.png)

Then paste `[afterpay_paragraph]` into the product description, or into a content area using your page builder.

![shortcodes-2.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/shortcodes-2.png)

![shortcodes-3.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/shortcodes-3.png)

To use the shortcode on custom pages, provide a product ID in the shortcode:

```html
[afterpay_paragraph id="99"]
```

![shortcodes-4.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/shortcodes-4.png)
