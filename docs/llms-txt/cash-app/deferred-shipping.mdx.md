# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/additional-features/express-checkout/deferred-shipping.mdx

***

## stoplight-id: 32jjjhtnjflxu

# Set up express checkout with deferred shipping

Express checkout uses the same APIs as standard checkout. To set it up:

1. Generate an Afterpay [order token](#generate-an-afterpay-order-token) to set up the express checkout process
2. Create an express checkout [button](#create-an-express-checkout-button) to load the checkout window
3. Create the [checkout](#create-checkout) using Afterpay.js
4. Continue the [checkout process](#continue-the-checkout-process) on your website
5. Show and update the payment schedule using the [checkout widget](/cash-app-afterpay/guides/api-development/additional-features/checkout-widget)
6. Capture [payment](#capture-payment) to finalize the order

## Generate an Afterpay order token

Before launching Cash App Afterpay express checkout, create an order token by calling the Create Checkout endpoint. This lets you specify the order amount, items, and other details.

The backend call is triggered when the express checkout button is clicked. A new token is required for each order. If you store the token in a database, be sure to support arbitrary string length and content, as a token’s format can change.

For express checkout orders, there are two key differences from standard checkout:

* Set `mode` to `express`
* Optionally, use a single `popupOriginUrl` instead of `redirectConfirmUrl` and `redirectCancelUrl`. With deferred shipping, you can also use a [redirect](#use-a-redirect-flow).

```curl
curl --request POST \
  --url https://api-sandbox.Afterpay.com/v2/checkouts \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"amount":{"amount":"10.00", “currency”: “AUD”}, “mode”: “express”, "merchant": {"popupOriginUrl": "https://example.com"}}'
```

## Create an express checkout button

When a customer clicks this button on a cart or product page, it launches Cash App Afterpay checkout in a popup.

1. Add a standard HTML `<button>` element wherever you want it to appear on your website.
2. Assign a unique ID (for example, `Afterpay-express-button`). This allows you to have multiple buttons on the same page.
3. Set the entry point using the `data-Afterpay-entry-point` attribute. Allowed values are:
   * `product-page`
   * `mini-cart`
   * `cart`
4. Set the button label using the `data-Afterpay-checkout-button-label` attribute. This identifies the button for analytics or tracking purposes.

```html
<button id="Afterpay-express-button"
        data-Afterpay-entry-point="mini-cart"
        data-Afterpay-checkout-button-label="Check out using Cash App Afterpay">
  Check out using Cash App Afterpay
</button>
```

### Button options

Multiple button styles are available, each clearly communicating the next step to the customer.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Button Types - All in one.png" alt="Button Types - All in one.png" noZoom />

<Info>
  Integration assets are available 

  [here](/cash-app-afterpay/guides/welcome/migrate-from-afterpay-to-cash-app-afterpay/brand-assets)

  , or contact your Cash App Afterpay merchant services representative.
</Info>

## Create checkout

### Load Afterpay.js

Add the Afterpay.js script to your website. Set the `onload` attribute to point to a custom function that will initialize the popup (for example, `initAfterpay`).

```js
<script src="https://portal.sandbox.Afterpay.com/Afterpay.js? async onload="initAfterpay()">
  </script>
```

### Initialize the popup window

Define your `initAfterpay()` function before loading the script. This function uses `Afterpay.initializeForPopup()` to configure the express checkout behavior. Configure the following properties:

* `countryCode`: Your merchant account's two-character ISO 3166-1 code
* `target`: The ID or class of the button that triggers checkout
* Set the flag `shippingOptionRequired` to `false`
* Handle lifecycle events:
  * `onCommenceCheckout`: Retrieve the Afterpay token from your server, then call `actions.resolve(TOKEN)` to start checkout.
  * `onComplete`: See "[finalize the order](#finalize-the-order)" for details.

```html

<html>
  <head>
    <script>
      // ensure this function is defined before loading afterpay.js
      function initAfterpay () {
        AfterPay.initializeForPopup({
          countryCode: 'US',
          onCommenceCheckout: function (actions) {
            /* retrieve afterpay token from your server */
            /* then call `actions.resolve(token)` */
          },
          onComplete: function (data) {
            /* handle success/failure of checkout */
          },
          target: '#afterpay-button',
          shippingOptionRequired: false,
        })
      }
    </script>
    <script src="https://portal.sandbox.afterpay.com/afterpay.js" async onload="initAfterpay()">
    </script>
  </head>
  <body>
    <button id="afterpay-button" 
    data-afterpay-entry-point="mini-cart">
      Checkout now with Cash App Afterpay
    </button>
  </body>
</html>
```

### Customer completes checkout

When the customer clicks the Cash App Afterpay checkout button, a popup opens or they're sent to your redirect link. The customer is prompted to log in and review their order details. They can select a payment method and delivery address.

After confirming their order, the popup closes and the customer returns to your site. Checkout completion is communicated via the `onComplete` callback.

## Finalize the order

When the customer completes Cash App Afterpay express checkout, the `onComplete` Javascript function is called. It receives an `event` argument with a `data` field containing the following properties:

| **Property**        | **Type**          | **Description**                                          |
| ------------------- | ----------------- | -------------------------------------------------------- |
| `status`            | string            | The order status: `"SUCCESS"` or `"CANCEL"`              |
| `orderToken`        | string            | The order token provided when initializing the checkout. |
| `merchantReference` | string (optional) | The merchant’s ID or reference number for the order.     |
| `orderInfo`         | object (optional) | The order info (if available) from the checkout.         |

**orderInfo data properties**

| **Property**      | **Type**   | **Description**                                                                             |
| ----------------- | ---------- | ------------------------------------------------------------------------------------------- |
| `shippingAddress` | `Contact`  | The shipping address for the order.                                                         |
| `consumer`        | `Consumer` | Contains the user’s `givenNames`, `surname`, and `email`. `phoneNumber` isn't defined here. |

```js
Afterpay.initializeForPopup({
  // ...
  onComplete: function (event) {
    if (event.data.status == "SUCCESS") {
      // The consumer has confirmed the payment schedule.
      // Call your server here to retrieve the order details.
    } else {
      // The consumer cancelled the payment or closed the popup window.
    }
  },
});
```

### Get order details

Retrieve the transaction details by calling the Get Checkout endpoint. This is the source of truth for the order. It includes the user’s name, email address, delivery address, phone number, and order total.

### Continue the checkout process

After getting the order details, continue the checkout on your site. To continue:

* Prefill your checkout using the Cash App Afterpay order details
* Have the customer select a delivery method
* Optionally, offer promo codes and allow changes to the order details
* Display the Cash App Afterpay [checkout widget](/cash-app-afterpay/guides/api-development/additional-features/checkout-widget) on the final review page or at all steps of your checkout. We recommend setting up the checkout widget before continuing.

<Warning>
  The Afterpay connected checkout widget is 

  **mandatory**

   for deferred shipping.
</Warning>

### Capture payment

You can capture payment using either the immediate payment flow or the deferred payment flow. For express checkout, the payload must include an `amount` field, which verifies that the final amount matches the amount including the shipping and taxes.

<Note>
  This section uses code examples from the immediate payment flow, but you can adapt these to use the deferred payment flow.
</Note>

For deferred shipping, in addition to the required `amount` field, include these additional fields in the payload. These are required to verify that the final order amount and payment schedule match the submitted order details.

* `isCheckoutAdjusted`: Indicates whether changes were made since order creation
* `items`: Updated list of order items (if changed)
* `shipping`: Updated shipping address (if changed)
* `paymentScheduleChecksum`: Latest value from your widget's `onChange` call (see Getting the widget's state)

```curl
curl --request POST \
  --url https://api-sandbox.Afterpay.com/v2/payments/capture \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"token":"YOUR_TOKEN", "amount":{"amount":"10.00", “currency”: “AUD”},  "isCheckoutAdjusted":true, "shipping":{"name":"Joe Consumer","line1":"123 Fake Street", "postcode":"3000", "region":"VIC", "countryCode":"AU"}, "items":[{"price":{"amount":"10.00", "currency":"AUD"}, "name":"item1", "quantity":1}], "paymentScheduleChecksum":"YOUR_PAYMENT_SCHEDULE_CHECKSUM" }'
```

If the final amount (including shipping and taxes) or the `paymentScheduleChecksum` doesn't match the expected values, the request will be rejected.

Once payment is captured, the express checkout order is complete.

#### Data payload properties

| Property                  | Type    | Description                                                                                                                                 |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `token`                   | String  | (required) The token returned in the Create Checkout request.                                                                               |
| `amount`                  | Money   | (required) Amount to be checked against the amount including shipping and taxes. If the amounts do not match, the request will be rejected. |
| `merchantReference`       | String  | Order id or reference this order corresponds to.                                                                                            |
| `isCheckoutAdjusted`      | Boolean | Whether there have been changes to the order since the initial order creation.                                                              |
| `paymentScheduleChecksum` | String  | A unique value representing the payment schedule that must be provided when there has been changes since the initial order creation.        |
| `items`                   | Item\[] | An array of order items that have been updated  to be provided if it has changed since the initial order creation.                          |
| `shipping`                | Contact | The shipping address for this order to be provided if it has changed since the initial order creation.                                      |

<Note>
  For Cross Border Trade orders, ensure that the currency is consistent throughout the entire checkout flow.

  For example, if you're a UK merchant displaying a 100 GBP order in AUD for an Australian consumer on your site. When initiating Afterpay checkout, If you initiate checkout by sending us the order amount in GBP (e.g. 100 GBP), then at capture the final order amount must also be in GBP.
</Note>

## Optional features

### Target multiple checkout buttons

If you have multiple checkout buttons on the same page, these can be targeted by adding a common class to each of these buttons:

```html
<button class="Afterpay-express-button”>
  Button 1 - Checkout using Afterpay Express
</button>
<button class="Afterpay-express-button”>
  Button 2 - Checkout using Afterpay Express
</button>
```

Then, set the target in the Afterpay.js initialize function with the common class. For example, set target in `initializeForPopup`:

```js
Afterpay.initializeForPopup({
  // ...
  target: ".Afterpay-express-button",
});
```

### Use a redirect flow

With deferred shipping, you can also use a redirect flow with express checkout. There are a few main differences when setting up the button for redirect, including:

* Creating an order token for redirect
* Using the `initializeForRedirect` method
* Redirecting the customer to finalize the order

To set up your redirect flow, first create an Afterpay order token using the Create Checkout API. Make sure to set the `mode` to `express`.

```curl
curl --request POST \
  --url https://api-sandbox.Afterpay.com/v2/checkouts \
  --header 'accept: application/json' \
  --header 'content-type: application/json' \
  --data '{"amount":{"amount":"10.00", “currency”: “AUD”}, “mode”: “express”, "merchant":{"redirectConfirmUrl":"https://example.com/checkout/confirm", "redirectCancelUrl":"https://example.com/checkout/cancel"}}'
```

Then, start by creating the Cash App Afterpay express checkout button, adding an entry point, and loading Afterpay.js. This is similar to the popup flow.

In your onload function, initialize the redirect flow by calling `initializeForRedirect` and configure the following:

* `countryCode`: The two-character ISO 3166-1 code for your merchant account
* `addressMode`: Use a mode without shipping options, as integrated shipping isn't supported for redirect flows.
* `target`: The ID or class of the button that initiates checkout
* Handle lifecycle events:
  * `onCommenceCheckout`: Retrieve the Afterpay token from your server, then call `actions.resolve(TOKEN)` to start the checkout process.

```html
<html>
  <head>
    <script>
      // ensure this function is defined before loading Afterpay.js
      function initAfterpay () {
        Afterpay.initializeForRedirect({
          countryCode: 'AU',
          onCommenceCheckout: function(actions) {
            /* retrieve Afterpay token from your server */
            /* then call `actions.resolve(token)` */
          },
          target: '#Afterpay-express-button',
          addressMode: Afterpay.ADDRESS_MODES.ADDRESS_WITHOUT_SHIPPING_OPTIONS,

        })
      }
    </script>
   <script src="https://portal.sandbox.Afterpay.com/Afterpay.js? async onload="initAfterpay()">
   </script>
  </head>
  <body>
    <button id="Afterpay-express-button" 
    data-Afterpay-entry-point="mini-cart">
      Checkout using Afterpay Express
    </button>
  </body>
</html>
```

#### Address mode

To support different shipping types in the checkout, configure the `addressMode` property using one of the provided constants in the format `Afterpay.ADDRESS_MODES.<NAME>`, where `<NAME>` is one of the following:

| Constant                                         | Description                                                                                                                                                  |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ADDRESS_WITHOUT_SHIPPING_OPTIONS`               | Displays checkout with the option for the customer to configure their shipping address only.                                                                 |
| `SHIP_TO_ORDER_ADDRESS_WITHOUT_SHIPPING_OPTIONS` | Displays checkout with the option for the customer to configure their shipping address only with the intention to continue their order back on the merchant. |
| `NO_ADDRESS`                                     | Displays checkout with the option for the customer to configure their shipping address only with the intention to buy now.                                   |

Next, finalize the order. When you created the Afterpay order token for redirect, you defined the properties `redirectConfirmUrl` and `redirectCancelUrl`. After the customer completes Afterpay express checkout, these properties are used to direct them to the specified URL:

* If successful, they are redirected to `redirectConfirmUrl`
* If cancelled, they are redirected to `redirectCancelUrl`

Once the customer returns to your site, follow the steps to get the order details.

## Errors

The following errors can occur during Cash App Afterpay express checkout with deferred shipping:

| **Error**                                                  | **How to Proceed**                                                                                                                                           |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Uncaught ReferenceError: Afterpay is not defined`         | Ensure that `Afterpay.js` is being loaded on your page before referencing it, e.g. by using the `onload` script attribute.                                   |
| `Uncaught ReferenceError: initAfterpay is not defined`     | Ensure that `initAfterpay` is defined **before** the script tag that loads `Afterpay.js`.                                                                    |
| Afterpay popup opens but doesn't launch a checkout         | Ensure your `onCommenceCheckout` handler has no errors (check the console), and that it calls `actions.resolve` with a valid token.                          |
| `onComplete` callback is not called when checkout finishes | This can occur due to issues with `postMessage` communication, especially with in-app browsers. Contact Cash App Afterpay with steps to replicate the issue. |
