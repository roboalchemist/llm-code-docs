# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/woo-commerce/faq.mdx

***

## stoplight-id: 313iqgfm6pt81

# Woo Commerce FAQ

**Frequently Asked Questions about the Cash App Afterpay WooCommerce Integration.**

***

## Why is Cash App Afterpay not showing on product pages?

To display the Cash App Afterpay installment detail on the product pages, the active WordPress theme must implement the below action hook:\
`woocommerce_single_product_summary`

<Note>
  You must also enable the *Payment Info on Individual Product Pages*\* setting, and the product must be eligible.

  For advanced configuration, see the **Hooks** section of the [WooCommerce Advanced Configuration](/cash-app-afterpay/guides/platforms/woo-commerce/advanced-configuration) page in this guide.
</Note>

***

## Why is Cash App Afterpay not showing on category and search result pages?

To display the Cash App Afterpay installment detail on the category and search result pages, the active WordPress theme must implement the below action hook:\
`woocommerce_after_shop_loop_item_title`

<Note>
  You must also enable the **Payment Info on Category Pages** setting, and the product/s must be eligible.

  For advanced configuration, see the **Hooks** section of the [WooCommerce Advanced Configuration](/cash-app-afterpay/guides/platforms/woo-commerce/advanced-configuration) page in this guide.
</Note>

***

## Why is Cash App Afterpay not showing on the cart page?

To display the Cash App Afterpay installment detail on the cart page, the active WordPress theme must implement the below action hook:\
`woocommerce_cart_totals_after_order_total`

<Note>
  You must also enable the **Payment Info on Cart Page** setting, and all the cart items must be eligible.

  For advanced configuration, see the **Hooks** section of the [WooCommerce Advanced Configuration](/cash-app-afterpay/guides/platforms/woo-commerce/advanced-configuration) page in this guide.
</Note>
