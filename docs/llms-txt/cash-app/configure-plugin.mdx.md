# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/woo-commerce/configure-plugin.mdx

***

## stoplight-id: qtz27kfz1zu86

# Configure Plugin

**How can I add Cash App Afterpay as a payment method and display Cash App Afterpay Site Messaging?**

***

## Configuration

Complete the steps below to enable and display Cash App Afterpay as a Payment Method, and add Cash App Afterpay messaging to product pages.

<Info>
  If you have completed the Cash App Afterpay Gateway Installation steps, go to Step 3.
</Info>

1. Go to the *WordPress Admin Dashboard*.

2. Go to *Plugins*\* > *Installed Plugins*.

3. Find the *Cash App Afterpay Gateway for WooCommerce* in the plugin list and click the **Settings** button.

   ![woo-config-1.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-config-1.png)

4. Go to the *Core Configuration* section.

   ![woo-config-2.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-config-2.png)

5. Enter the Merchant ID provided by Cash App Afterpay into the *Merchant ID* field.

   ![woo-config-3.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-config-3.png)

6. Enter the Secret Key provided by Cash App Afterpay into the *Secret Key* field.

   ![woo-config-4.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-config-4.png)

7. Click the **Save changes** button at the bottom of the page.

<Info>After a successful save of the Cash App Afterpay credentials, the *Merchant Public ID*, *Minimum Payment Amount*, *Maximum Payment Amount* and *Settlement Currency* values are updated.</Info>
![woo-config-5.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-config-5.png)

<Info>
  The 

  **Sandbox**

   API Environment is only applicable for dedicated test websites. Contact your Cash App Afterpay Account Manager if you need test credentials.
</Info>

## Enable Express Checkout

To enable Express Checkout:

1. Go to **WordPress Admin Dashboard**.

2. Go to **Plugins** > **Installed Plugins**.

3. Find the *Cash App Afterpay Gateway for WooCommerce* in the plugin list and click the **Settings** button.

4. Find *Express Checkout Configuration* and enable the checkbox.

   ![woo-config-6.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-config-6.png)

## Enabling the Cash App Afterpay Messaging for WooCommerce

The Cash App Afterpay messaging can be enabled on:

* Category Pages

* Product Pages

* Cart Page

To start do the following:

1. Login to the Wordpress Dashboard.

2. Go to *Plugins* > *Installed plugins* > *Cash App Afterpay Gateway for Woocommerce* and click *Settings*.

![woo-plugin-1.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-plugin-1-3.png)

Under *Settings*, you can see settings for:

* [Express Checkout Configuration](#enable-express-checkout)

* [Payment Info on Category Pages](#payment-info-on-category-pages)

* [Payment Info on Individual Product Pages](#payment-info-on-individual-product-pages)

* [Payment Info Display for Product Variant](#payment-info-display-for-product-variant)

These settings are described below.

### Payment Info on Category Pages

![woo-plugin-4.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-plugin-4-2.png)

To enable the messaging on the Category page, do the following:

1. Ensure the *Enable* checkbox is enabled.

2. Enter the correct hook to position the messaging and set the priority to increase or decrease the height of the Messaging position. See the [Hook](#hook) section below.

#### Hook

The positioning of the Messaging for Woocommerce relies on a hook. [This link](https://www.businessbloomer.com/woocommerce-visual-hook-guide-archiveshopcat-page/) is a guide to understanding hook positioning on Category pages.

<Warning>The hooks for Category pages and Product pages are completely different.</Warning>
For example, use the hook `woocommerce_after_shop_loop_item`to position the messaging under the price:

![woo-plugin-5.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-plugin-5-2.png)

Below is an example of a category page with Cash App Afterpay messaging:

![woo-plugin-6.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-plugin-6-2.png)

<Info>
  For more information on hooks, see the 

  [Hooks](WC-Hooks.mdx)

   page.
</Info>

### Payment Info on Individual Product Pages

To enable the messaging on the individual Product page, do the following:

1. Ensure the Enable checkbox is enabled.

2. Enter the correct hook to position the messaging and set the priority to increase or decrease the height of the Messaging position. See the **Hook** section below.

#### Hook

The positioning of the Messaging for Woocommerce relies on a hook. [This link](https://www.businessbloomer.com/woocommerce-visual-hook-guide-single-product-page/) is a guide to understanding hook positioning for Product pages.

<Warning>The hooks for Category pages and Product pages are completely different.</Warning>
For example, use the hook `woocommerce_before_add_to_cart_form` to position the messaging directly under the Product Page price:

![woo-plugin-8.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-plugin-8-2.png)

Below is an example of a Product Page with Cash App Afterpay messaging:

![woo-plugin-9.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/woo-plugin-9-2.png)

<Info>
  For more information on hooks, see the 

  [Hooks](WC-Hooks.mdx)

   page.
</Info>

### Payment Info Display for Product Variant

This option enables the Cash App Afterpay Messaging for any variant products.

For example, a product that has a price range from between $50 to $200. The Cash App Afterpay Messaging also displays the instalment breakdown according to a price range.

When a customer selects a variant, a specific price appears. This option enables the Cash App Afterpay Messaging to display a specific price breakdown.
