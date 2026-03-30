# Source: https://developers.cash.app/cash-app-afterpay/guides/platforms/adobe-commerce-magento/configure-extension.mdx

***

## stoplight-id: nxhrpl3ewdktj

# Adobe Commerce - Configure Extension

*Basic Settings, Advanced Settings, Advanced Front End Settings and Express Checkout Settings.*

***

## Basic Settings

1. Login to Adobe Commerce Admin and go to  **Stores → Configuration → Sales → Payment Methods → Afterpay** (scroll down).

2. Click **Basic Settings**.

![acm2-a-small.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/acm2-a-small.png)

| Setting      | Value                                                                                                                                                                                      |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Enabled      | **Yes** - Cash App Afterpay switched on. <br />**No** - Cash App Afterpay disabled.<br /> Click the *Use Default* checkbox to use the default setting, which is Yes.                       |
| API Mode     | **Sandbox** - for development or staging environments. <br /> **Production** - for your live website.<br /> Click the *Use Default* checkbox to use the default setting, which is Sandbox. |
| Merchant ID  | Your Sandbox or Production Cash App Afterpay Merchant ID.                                                                                                                                  |
| Merchant Key | Your Sandbox or Production Cash App Afterpay Secret Key.                                                                                                                                   |

## Advanced Settings

1. Click **Advanced Settings**.

![acm-2-b-revised.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/acm-2-b-revised.png)

| Setting                  | Value                                                                                                                         |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Minimum Order Total      | Shows the minimum price for an order payable with Cash App Afterpay.                                                          |
| Maximum Order Total      | Shows the maximum price for an order payable with Caash App Afterpay.                                                         |
| CBT Available Currencies | Lists the currencies available for [Cross Border Trade](/cash-app-afterpay/guides/welcome/getting-started/cross-border-trade) |

The above three settings are all read-only display fields. The information they display comes from the Cash App Afterpay API, so you cannot edit them here.

| Setting                              | Value                                                                                                                                                                                                                                                                                                               |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Public Id                            | A publishable API key used by Cash App Afterpay's Dynamic Messaging feature. It is a unique identifier for the merchant account.                                                                                                                                                                                    |
| Consumer Lending Enabled             | Shows if the merchant account is enabled for Pay Monthly (US merchants only). If you want Pay Monthly enabled and are a US merchant, contact Cash App Afterpay Sales.                                                                                                                                               |
| Consumer Lending Minimum Order Total | The minimum order total for the use of the customer lending facility.                                                                                                                                                                                                                                               |
| Update Merchant Configuration        | Click this button to update the limit configuration and specific countries from the Cash App Afterpay API.                                                                                                                                                                                                          |
| Debug                                | **Yes** - Debug logs are written to  "h-0": "/var/log/afterpay.log <br />**No** - Disabled. Click the *Use Default* checkbox to use the default setting, which is Yes.                                                                                                                                              |
| Display on Product Page              | **Yes** - Cash App Afterpay Displays on Product Page. Click the *Use Default* checkbox to use the default setting, which is Yes.                                                                                                                                                                                    |
| Display on Cart Page                 | **Yes** - Adobe Commerce Checkout - proceed to checkout page as normal.<br /> **Yes** - Express Checkout - enable Cash App Afterpay Express Checkout from cart page. <br />**No** - Cash App Afterpay will not display on the Cart page. Click the *Use Default* checkbox to use the default setting, which is Yes. |
| Sort Order                           | The order of payment methods at checkout.                                                                                                                                                                                                                                                                           |

![acm2-c-small.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/acm2-c-small.png)

| Setting               | Value                                                                                                                                                                                                                                                            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Exclude Categories    | Select the relevant categories to exclude Cash App Afterpay from being available. Click the *Use Default* checkbox to use the default setting, which excludes nothing.                                                                                           |
| Payment Flow          | **Immediate Payment Flow** - Capture full payment. <br />**Deferred Payment Flow** - Capture incremental amounts as items are dispatched.                                                                                                                        |
| Enable Auto-Reversals | This is useful if an exception occurs when Adobe Commerce is finalising an order after Afterpay have approved the payment. In this case the payment is reversed automatically. This reversal helps prevent customers paying for orders that cannot be fulfilled. |

<Warning>
  In the table above, we do not recommend the use of the Auto-Reversals feature if you use an external Order Management System (OMS).
</Warning>

## Advanced Frontend Settings

Use these settings for custom-built themes on your website. The default of these settings is NO (disabled), which means your pages display in the default Adobe Commerce Luma theme, or similar.

These custom-built themes are not dependent on [Knockout.js](https://knockoutjs.com), which is the default frontend framework included with Adobe Commerce. If enabled, Advanced Frontend Settings allow Afterpay messaging to display on the product page, cart and mini-cart, regardless of the frontend framework used by your theme.

You, the merchant, must configure the Placement selectors and the Price selectors according to the theme you have designed and your web page type.

<Note>This feature is only available for Adobe Commerce 2.4 (and above) users.</Note>
Do the following:

1. Login to Adobe Commerce Admin and go to  **Stores → Configuration → Sales → Payment Methods → Afterpay** (scroll down).

2. Click **Advanced Frontend Settings**. The advanced frontend settings fields display, in the default setting of No, which means they are disabled. See screenshot below:

![Configuration-Settings-Stores-Magento-Admin.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Configuration-Settings-Stores-Magento-Admin.png)

The example screen below shows the range of settings when the advanced frontend settings fields are enabled:

![Hyva-Configuration-Settings-Stores-Magento-Admin.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Hyva-Configuration-Settings-Stores-Magento-Admin.png)

See the table below for information on the various settings.

<Note>
  In all cases, you should place Afterpay messaging immediately below the price element in the PDP (Product Page), cart and mini cart.
</Note>

| Setting                                  | Value                                                                                                                                                         |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable for Product Page                  | Select **Yes** to enable Advanced Frontend Settings for product pages.                                                                                        |
| Placement selector (Product Page)        | Enter a CSS (Cascading Style Sheet) selector for a target element on the product page. Afterpay asset placement is injected below the first matching element. |
| Price selector (Product Page)            | Enter a CSS selector for the product price element. The product price is extracted from the first matching element.                                           |
| Placement selector (Bundle Product Page) | Enter a CSS selector for a target element on the bundle product page. Afterpay asset placement is injected below the first matching element.                  |
| Price selector (Bundle Product Page)     | Enter a CSS selector for the bundle product price element. The bundle product price is extracted from the first matching element.                             |
| Enable for Cart Page                     | Select **Yes** to enable Advanced Frontend Settings for the shopping cart page.                                                                               |
| Placement selector (Cart Page)           | Enter a CSS selector for a target element on the cart page. Afterpay asset placement is injected below the first matching element.                            |
| Price selector (Cart Page)               | Enter a CSS selector for the order price element. The order price is extracted from the first matching element.                                               |
| Enable for Mini Cart                     | Select **Yes** to enable Advanced Frontend Settings for the mini cart.                                                                                        |
| Placement selector (Mini Cart)           | Enter a CSS selector for a target element on the mini cart. Afterpay asset placement is injected below the first matching element.                            |
| Container selector (Mini Cart)           | Enter a CSS selector to select a container on the mini cart page. In the example above the container selector is #cart-drawer.                                |
| Price selector (Mini Cart)               | Enter a CSS selector for the mini cart order price element. The order price is extracted from the first matching element.                                     |

## Express Checkout Settings

1. Click **Express Checkout Settings**.

![express-checkout-settings-small.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/express-checkout-settings-small.png)

| Setting                 | Value                                                                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Display on Product Page | **Yes** - Can checkout directly from Product Page. <br />**No** - No checkout from the Product Page. Click the *Use Default* checkbox to use the default setting, which is Yes.  |
| Display on Cart Page    | **Yes** - Can checkout directly from Cart Page. <br />**No** - No checkout from the Cart Page. Click the *Use Default* checkbox to use the default setting, which is Yes.        |
| Display on Mini-Cart    | **Yes** - Can checkout directly from Mini-Cart. <br />**No** - No direct checkout from the Mini-Cart. Click the *Use Default* checkbox to use the default setting, which is Yes. |
