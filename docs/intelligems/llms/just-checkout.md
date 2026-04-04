# Source: https://docs.intelligems.io/integrations/just-checkout.md

# JUST Checkout

## Overview

[JUST Checkout](https://app.gitbook.com/o/HNmChKUZY1pAEPfel38z/s/2SvefuMLsJyJPAcVXeWc/~/edit/~/changes/1069/developer-resources/just-checkout) is a high-performance checkout solution designed to streamline the purchasing process by reducing friction and increasing conversion rates. It offers a "one-click" style experience that bypasses traditional multi-step forms.

## Compatibility

JUST Checkout and Intelligems work seamlessly together. In most cases, **no integration work is required** to run Intelligems experiments alongside JUST Checkout.

### Supported Test Types

The following Intelligems test types work out-of-the-box with JUST Checkout:

* **Price Tests** – Test different pricing strategies without any additional configuration
* **Shipping Tests** – Experiment with shipping thresholds and rates
* **Offer Tests** – Run tiered discounts, cart discounts, and free shipping offers
* **Content Tests** – A/B test product descriptions, images, and other on-page elements

Intelligems will track conversions and revenue accurately regardless of whether customers complete their purchase through JUST Checkout or your standard checkout flow.

### Important Compatibility Note: Free Gift Offers

There is **one specific scenario** where manual intervention is required: **Free Gift Offer Tests that utilize auto-add functionality**.

#### The Issue

When running a Free Gift Offer test with auto-add enabled, the integration behaves differently depending on where the customer clicks the JUST Checkout button:

* **Product Page:** If a shopper clicks the JUST Checkout button directly on a Product Page, the system will **fail to automatically add the free gift** to the cart.
* **Cart Page:** If the shopper selects the JUST Checkout button from the Cart Page, the integration **works correctly** because the gift has already been added to the cart.

#### Recommended Solution

If you are running an active Free Gift Offer test with auto-add enabled, we recommend **hiding the JUST Checkout buttons on product pages** to ensure:

* A consistent customer experience across all test variations
* Accurate test data and attribution
* Proper free gift fulfillment for all eligible customers

You can leave JUST Checkout buttons visible on the Cart Page, where the integration functions correctly.
