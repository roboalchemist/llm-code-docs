# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/woocommerce/conversion-boosters/how-to-install-express-checkout-in-woocommerce.md

# How to install Express Checkout in WooCommerce

## This guide explains how to add Express Checkout to your WooCommerce store.

## What is Express Checkout?

Express Checkout gives your customers a fast and convenient way to purchase with Klarna. Partners who have integrated Express Checkout see an improved customer experience, increased conversion rates, and a higher AOV. To learn more about Express Checkout, refer to the [product documentation](https://docs.klarna.com/express-checkout).


![ When you add Express Checkout to the store, a button prompting customers to pay with Klarna is displayed in checkout.](51bda528-9267-4a78-87d7-5718d61482fa-KEC-Example.jpeg)
*When you add Express Checkout to the store, a button prompting customers to pay with Klarna is displayed in checkout.*

## Prerequisites

To be able to offer Express Checkout, you have to first enable Klarna in your WooCommerce store by installing the [Klarna for WooCommerce](https://wordpress.org/plugins/klarna-payments-for-woocommerce/) plugin.

## Install Express Checkout in WooCommerce

Express Checkout is applied to both product and cart pages for a Woo shop, dependent upon compatibility with the shop's theme. To install Express checkout in a WooCommerce store, follow these steps: 1. In the **Klarna Merchant portal**, go to **Payment settings**\> **Client identifiers**. There you can click **Manage origins** and enter your store's URL in the **Register new origin** section. 2. Proceed to add your store's URL to the allow list (**Register new origin**) and to generate the Klarna Client ID.


![ To use Express Checkout in your WooCommerce store, you have to allowlist your store's URL.](4d4622ee-d3d5-447e-9cbd-0193cdd2a65d_Whitelisting.jpeg)
*To use Express Checkout in your WooCommerce store, you have to allowlist your store's URL.*

Later, you can also manage your **Allowed origins for your integrations** in **Payment settings**\> **Client identifiers**. There you can click **Manage origins** and enter your store's URL in the **Register new origin** section.


![ You can manage Allowed origins for your integrations in Payment settings.](af9e9cd4-44f4-4179-8287-87f3c7d49937-Allowed-origin.jpeg)
*You can manage Allowed origins for your integrations in Payment settings.*

3\. Click on **Generate client identifier** in the Client identifiers menu and then copy it from the **Client ID**field.


![ The generated Client ID links your Klarna merchant account to your WooCommerce store.](b1f1f769-0f32-4b2f-81b4-83555781d458-image.jpeg)
*The generatedClient IDlinks your Klarna merchant account to your WooCommerce store.*

4\. In your WooCommerce admin, in the **Credentials**section, paste the **Client ID** you copied in the **Client Id** field. Make sure the ID doesn't contain any quotes or whitespace. 5. In the Express Checkout section, check the **Enable Klarna Express Checkout** checkbox to enable the Express Checkout in the Klarna plugin.


![klarna docs image](ZwPblrVsGrYSwcjn_image-11.jpeg)image

## Customize the Express Checkout button

You can customize the Express Checkout button by choosing a [theme](https://docs.klarna.com/conversion-boosters/express-checkout/additional-resources/button-styling.md) and a [shape](https://docs.klarna.com/conversion-boosters/express-checkout/additional-resources/button-styling.md). The styling options are available in the WooCommerce plugin settings.

1.  From the **Theme** dropdown, select a [theme](https://docs.klarna.com/conversion-boosters/express-checkout/additional-resources/button-styling.md) for the button — dark, light, or outlined.
2.  From the **Shape** dropdown, select a [shape](https://docs.klarna.com/conversion-boosters/express-checkout/additional-resources/button-styling.md) for the button — rounded, rectangular, or pill.
3.  Select the **Placements**: product and/or cart pages.

To learn more about Express Checkout in the Klarna plugin for WooCommerce, refer to the [Krokedil documentation](https://docs.krokedil.com/klarna-payments-for-woocommerce/get-started/klarna-express-checkout/).