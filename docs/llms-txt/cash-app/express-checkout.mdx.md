# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/additional-features/express-checkout.mdx

***

## stoplight-id: 9z8nxn7pcamz2

# Introduction to express checkout

Cash App Afterpay express checkout reduces the overall checkout steps on desktop and mobile so that your shoppers can complete their orders quickly.

Customers can check out directly from the shopping cart or product page, using their pre-filled Cash App Afterpay account information (name, shipping address, phone number, email) to complete their orders on your website.

Simply put, there are fewer checkout steps, leading to higher conversion.

## Express checkout vs standard checkout

### Standard checkout flow

With standard checkout, the customer proceeds through the checkout process as normal, selecting Cash App Afterpay as a payment option in your payments section.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Checkout Flow - Standard.png" alt="Checkout Flow - Standard.png" noZoom />

### Express checkout flow

With express checkout, the customer can choose to ‘buy now with Cash App Afterpay’ on a product page, or shop for multiple items and choose to ‘checkout with Cash App Afterpay’ from the cart.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Checkout Flow - Express.png" alt="Checkout Flow - Express.png" noZoom />

There are two ways to implement express checkout:

#### Integrated shipping

Customers select delivery options inside the Cash App Afterpay checkout flow. The order is completed within Cash App Afterpay checkout.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Integrated Shipping.png" alt="Integrated Shipping.png" noZoom />

#### Deferred shipping

The customer returns to your website's checkout to select delivery options and complete their order.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Deferred Shipping.png" alt="Deferred Shipping.png" noZoom />

### Which one is right for you?

| Integrated Shipping                                           | Deferred Shipping                                               |   |
| ------------------------------------------------------------- | --------------------------------------------------------------- | - |
| Less than 5 shipping options                                  | 5 or more shipping options                                      |   |
| Simple shipping options (e.g. single option for whole order)  | Complex shipping options (e.g. individual options at SKU level) |   |
| Simple tiered shipping options (e.g. standard, express, rush) | Customized shipping options (e.g., timeslot booking)            |   |
| Click and collect pickup selection before checkout entry      | Third party click and collect pickup                            |   |
