# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/additional-features/express-checkout/integrated-shipping.mdx

***

## stoplight-id: p7fa9810hdhqm

# Set up express checkout with integrated shipping

Express checkout uses the same APIs as standard checkout. Integrated shipping enhances the experience by embedding your shipping options directly into Afterpay express checkout, streamlining the process. When paired with the Buy Now flag, it creates a one-step checkout.

To set it up:

1. Generate a Cash App Afterpay [order token](#generate-an-afterpay-order-token) to start the express checkout process
2. Create an express checkout [button](#create-an-express-checkout-button) to load the checkout window
3. Create the [checkout](#create-checkout) using Afterpay.js
4. Capture [payment](#capture-payment) to finalize the order

<Warning>
  When using integrated shipping, you must launch the checkout in a popup. The redirect method isn't supported.
</Warning>

## Generate an Afterpay order token

Before launching Cash App Afterpay express checkout, create an order token by calling the [Create Checkout](/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1) endpoint. This lets you specify the order amount, items, and other details.

The backend call is triggered when the express checkout button is clicked. A new token is required for each order. If you store the token in a database, be sure to support arbitrary string length and content, as a token’s format can change.

For express checkout orders, there are two key differences from standard checkout:

* Set `mode` to `express`
* Use a single `popupOriginUrl` instead of `redirectConfirmUrl` and `redirectCancelUrl`

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
* `addressMode`: One of the provided address mode constants
* `target`: The ID or class of the button that triggers checkout
* Set the `buyNow` flag to `true`. This shows customers a "Buy Now" button for one-step checkout.
* Handle lifecycle events:
  * `onCommenceCheckout`: Retrieve the Afterpay token from your server, then call `actions.resolve(TOKEN)` to start checkout.
  * `onComplete`: See [Finalize the Order](#finalize-the-order) for details.
  * `onShippingAddressChange`: See [Listen for Address Changes](#listen-for-address-changes) for details.

```html
<html>
  <head>
    <script>
      // ensure this function is defined before loading Afterpay.js
      function initAfterpay () {
        Afterpay.initializeForPopup({
          countryCode: 'AU',
          onCommenceCheckout: function (actions) {
            /* retrieve Afterpay token from your server */
            /* then call `actions.resolve(token)` */
          },
          onComplete: function (data) {
            /* handle success/failure of checkout */
          },
          target: '#Afterpay-express-button',
          addressMode: Afterpay.ADDRESS_MODES.ADDRESS_WITH_SHIPPING_OPTIONS,
          buyNow: true,
        })
      }
    </script>
    <script src="https://portal.sandbox.Afterpay.com/Afterpay.js? async onload="initAfterpay()">
    </script>
  </head>
  <body>
    <button id="Afterpay-express-button" 
    data-Afterpay-entry-point="mini-cart">
    data-Afterpay-checkout-button-label="Checkout using Afterpay Express">
      Checkout using Afterpay Express
    </button>
  </body>
</html>
```

#### Address mode

To support different shipping types in the checkout, configure the `addressMode` property using one of the provided constants in the format `Afterpay.ADDRESS_MODES.<NAME>`, where `<NAME>` is one of the following:

| Constant                                         | Description                                                                                                                                                                                        |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **With Shipping Options**                        |                                                                                                                                                                                                    |
| `ADDRESS_WITH_SHIPPING_OPTIONS`                  | Displays checkout with the option for the customer to configure their shipping address and be able to select from the merchant's list of available shipping options.                               |
| `SHIP_TO_ORDER_ADDRESS`                          | Displays checkout with the chosen customer shipping address and be able to select from the merchant's list of available shipping options. See preselected shipping address order for more details. |
| `PICKUP_FROM_ORDER_ADDRESS`                      | Displays checkout with the chosen merchant pickup address for the order. See pickup orders for more details.                                                                                       |
| **Without Shipping Options**                     |                                                                                                                                                                                                    |
| `ADDRESS_WITHOUT_SHIPPING_OPTIONS`               | Displays checkout with the option for the customer to configure their shipping address only.                                                                                                       |
| `SHIP_TO_ORDER_ADDRESS_WITHOUT_SHIPPING_OPTIONS` | Displays checkout with the option for the customer to configure their shipping address only with the intention to continue their order back on the merchant.                                       |
| `NO_ADDRESS`                                     | Displays checkout with the option for the customer to configure their shipping address only with the intention to buy now.                                                                         |

<Note>
  If `addressMode` isn't specified, `ADDRESS_WITH_SHIPPING_OPTIONS` is used by default.
</Note>

### Customer completes checkout

When the customer clicks the Cash App Afterpay checkout button, a popup opens. The customer is prompted to log in and review their order details. They can select a payment method, delivery address, and shipping option.

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

| **Property**      | **Type**   | **Description**                                                                                                         |
| ----------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------- |
| `shippingAddress` | `Contact`  | The shipping address for the order.                                                                                     |
| `shippingOption`  | object     | Contains `shippingOptionIdentifier`, indicating the ID of the user’s chosen shipping option (integrated shipping only). |
| `consumer`        | `Consumer` | Contains the user’s `givenNames`, `surname`, and `email`. `phoneNumber` isn't defined here.                             |

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

Retrieve the transaction details by calling the [Get Checkout](/cash-app-afterpay/api-reference/reference/checkouts/get-checkout) endpoint. This is the source of truth for the order. It includes the user's name, email address, delivery address, phone number, and order total.

Verify the order details to ensure that the shipping address, `shippingOptionIdentifier`, and resulting amount are valid and match your records.

### Capture payment

Capture payment using the [immediate payment flow](/cash-app-afterpay/guides/api-development/api-quickstart/immediate-capture). For express checkout, the payload must include an `amount` field.

Once payment is captured, the express checkout order is complete.

<Note>
  For Cross Border Trade orders, ensure that the currency is consistent throughout the entire checkout flow.

  For example, if  you're a UK merchant displaying a 100 GBP order in AUD for an Australian consumer on your site. For example, if you initiate checkout by sending us the order amount in GBP, then at capture the final order amount must also be in GBP.
</Note>

### Listen for address changes

The `onShippingAddressChange` callback lets you dynamically update shipping options and taxes based on the consumer’s shipping address. It receives two arguments: `data` (the address) and `actions` (callback functions).

Afterpay calls `onShippingAddressChange` when the customer first enters the Cash App Afterpay summary page, and again whenever they update their shipping address. During these calls, you should:

* Use the address details in `data` to determine supported shipping options (e.g. by contacting your backend API).
* Use `actions.resolve` to return the options to the Afterpay express checkout, or
* Use `actions.reject` to signal any errors, providing an appropriate shipping constant

#### Data argument

| Property      | Type   | Description                                                                                      |
| ------------- | ------ | ------------------------------------------------------------------------------------------------ |
| `name`        | String | Full name of the consumer                                                                        |
| `address1`    | String | First line of the address.                                                                       |
| `address2`    | String | Second line of the address                                                                       |
| `area2`       | String | Village/local area of the address                                                                |
| `suburb`      | String | Suburb/City of the address                                                                       |
| `state`       | String | AU: State<br />NZ: Region<br />UK: County<br />US: State<br />CA: Province or Territory          |
| `postcode`    | String | ZIP or postal code. If the country does not have postcodes, the countryCode will be sent instead |
| `countryCode` | String | The ISO 3166-1 alpha-2 country code.                                                             |
| `phoneNumber` | String | The phone number, in E.123 format.                                                               |

#### Actions argument

| Property  | Type     | Description                                                                                                                                                                                                                                     |
| --------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `resolve` | Function | Call this method to provide the shipping options applicable to the consumer’s address. Takes an array of Shipping Option objects.                                                                                                               |
| `reject`  | Function | Call this method when you are unable to handle the request. Do not throw an error, instead call this method with a Shipping Constant as the first argument to indicate a status, e.g. `actions.reject(Afterpay.CONSTANTS.SHIPPING_UNSUPPORTED)` |

#### Shipping options model

| Attribute        | Type              | Description                                                  |
| ---------------- | ----------------- | ------------------------------------------------------------ |
| `id`             | String (required) | A shipping option identifier. Max length 128.                |
| `name`           | String (required) | The name of the shipping option.                             |
| `shippingAmount` | Money (required)  | The shipping amount (without tax, if including taxAmount).   |
| `taxAmount`      | Money (optional)  | The tax amount.                                              |
| `orderAmount`    | Money (required)  | The total amount for the order including shipping and taxes. |
| `description`    | String            | A description for this shipping option.                      |

#### Retrieve shipping options via API

```js
Afterpay.initializeForPopup({
  // ...
  onShippingAddressChange: function (data, actions) {
    fetch('/your-shipping-endpoint', {
      method: 'POST',
      headers: { 'content-Type': 'application/json' },
      body: JSON.stringify(data),
    }).then(function(options) {
      actions.resolve(options)
    }).catch(function(error) {
      // Parse the response and send a Afterpay rejection, e.g.:
      actions.reject(Afterpay.CONSTANTS.SHIPPING_UNSUPPORTED)
    })
  },
})
```

#### Calculate shipping options in Afterpay.js

```js
Afterpay.initializeForPopup({
  // ...
  onShippingAddressChange: function (data, actions) {
    if (data.countryCode !== 'AU') {
      // Reject any unsupported shipping addresses
      actions.reject(Afterpay.CONSTANTS.SHIPPING_UNSUPPORTED)
    } else {
      // Calc shipping inline
      actions.resolve([ {
        id: '1', name: 'Standard', description: '3 - 5 days',
        shippingAmount: { amount: '0.00', currency: 'AUD'},
        taxAmount: { amount: '3.18', currency: 'AUD'},
        orderAmount: { amount: '34.99', currency: 'AUD'},
      }, {
        id: '2', name: 'Priority', description: 'Next business day',
        shippingAmount: { amount: '10.99', currency: 'AUD'},
        taxAmount: { amount: '4.28', currency: 'AUD'},
        orderAmount: { amount: '47.08', currency: 'AUD'},
      } ])
    }
  },
})
```

#### Shipping constants

To indicate error scenarios, call `actions.reject()` with the appropriate constant. The constants are in the form `Afterpay.CONSTANTS.<NAME>`, where `<NAME>` is one of the following:

| **Constant**                    | **Description**                              |
| ------------------------------- | -------------------------------------------- |
| `SHIPPING_ADDRESS_UNRECOGNIZED` | Unrecognized address.                        |
| `SHIPPING_ADDRESS_UNSUPPORTED`  | Recognized address, but will not ship there. |
| `SERVICE_UNAVAILABLE`           | General service error.                       |

<Note>
  Express checkout doesn't perform any calculations. Your web app is responsible for calculating the correct total, including taxes and shipping, for each shipping option.
</Note>

### Optional callbacks

#### Listen for shipping option changes

The `onShippingOptionChange` callback is optional, allowing you to track the customer's chosen shipping option as it changes. It will be called with a single Shipping Option argument each time the customer selects a shipping option.

```js
Afterpay.initializeForPopup({
  // ...
  onShippingOptionChange: function (data) {
    console.log(data)
  },
})
```

If you need to modify the shipping option amounts after the user has selected a shipping option, use `onShippingOptionChange` with an additional action argument to update the checkout. When `onShippingOptionChange` is triggered:

1. Use the shipping option data to perform the required modification (for example, recalculate the tax via your backend API).

2. Once updated, use `actions.resolve` to return an object containing:
   * `id`: The same shipping option id from `onShippingOptionChange`
   * `shippingAmount`: The updated shipping amount for the selected option
   * `taxAmount`: The updated tax amount for the selected option
   * `orderAmount`: The updated order amount for the selected shipping option

3. Use `actions.reject` to signal any errors.

```js
Afterpay.initializeForPopup({
  // ...
  onShippingOptionChange: function (data, action) {
      fetch('/your-update-shipping-option-endpoint', {
          method: 'POST',
          headers: { 'content-Type': 'application/json' },
          body: JSON.stringify(data),
      }).then(function(options) {
          actions.resolve({
             id: data.id, 
             shippingAmount: { amount: '0.00', currency: 'AUD'},
             taxAmount: { amount: '3.18', currency: 'AUD'},
             orderAmount: { amount: '34.99', currency: 'AUD'},
          })
      }).catch(function(error) {
          // Parse the response and send the error, e.g.:
          actions.reject(error)
      })
  },
})
```

### Listen for error messages

To facilitate handling of log/warning/error messages, you can optionally replace `Afterpay.onMessage` with a custom function. It receives the following payload:

| Property   | Type   | Description                                     |
| ---------- | ------ | ----------------------------------------------- |
| `severity` | String | One of: `log`, `warning`, or `error`            |
| `message`  | String | The message (normally displayed on the console) |

```js
Afterpay.onMessage = function (payload) {
  console[payload.severity](payload.message)
}
```

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

### Pickup orders

To support pickup orders using integrated shipping, follow these steps:

1. Allow customers to select pickup options (e.g. pickup location and date) that impact shipping costs **before** launching express checkout.
2. When a customer selects pickup, use the pickup address in the `shipping` body parameter when creating the order.
3. When calling `initializeForPopup`, set `addressMode` to `Afterpay.ADDRESS_MODES.PICKUP_FROM_ORDER_ADDRESS`.
   ```js
   Afterpay.initializeForPopup({
     // ...
     addressMode: Afterpay.ADDRESS_MODES.PICKUP_FROM_ORDER_ADDRESS,
   })
   ```
4. Configure `onShippingAddressChange` to return the name and description of the pickup selection. This typically means returning a single option, for example:
   ```js
   actions.resolve([ {
     id: 'pickup-store-123', name: 'Click & Collect',
     description: 'Available for next-day pickup',
     shippingAmount: { amount: '0.00', currency: 'AUD'},
     taxAmount: { amount: '3.18', currency: 'AUD'},
     orderAmount: { amount: '34.99', currency: 'AUD'},
   } ])

   ```
5. Optionally, you can collect additional pickup information (for example, an alternate pickup person) on your order review page.

<Tip>
  If `initializeForPopup` is called before you know whether a customer has selected pickup, you can safely call `initializeForPopup` again. Each call overwrites the previous calls.
</Tip>

### Preselect shipping option

If customers can choose a shipping option on your site before launching express checkout, you can send us this information when checkout launches.

1. Set the `shippingOptionIdentifier` in the body parameter when creating the order. This preselects the option if it's returned from `onShippingAddressChange` when checkout loads.
2. Set `addressMode` in `Afterpay.initializeForPopup()` to define how the shipping address is handled.
   * To provide a list of shipping options, use `Afterpay.ADDRESS_MODES.SHIP_TO_ORDER_ADDRESS`
   * To **not** provide a list of shipping options, use `Afterpay.ADDRESS_MODES.SHIP_TO_ORDER_ADDRESS_WITHOUT_SHIPPING_OPTIONS`
3. Include the shipping address in the `shipping` parameter when creating the order.

```curl
curl --request POST \
 --url https://api-sandbox.afterpay.com/v2/checkouts \
 --header 'accept: application/json' \
 --header 'content-type: application/json' \
 --data '{"amount":{"amount":"10.00", “currency”: “AUD”}, “mode”: “express”, "merchant": {"popupOriginUrl": "https://example.com"}, "shipping": {"name": "Your Store Name", "line1": "123 Store Address", "postcode": "0000"}, shippingOptionIdentifier: “standard”
}}'
```

## Errors

The following errors can occur during Cash App Afterpay express checkout with integrated shipping:

| **Error**                                                             | **How to Proceed**                                                                                                                                                               |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Uncaught ReferenceError: Afterpay is not defined`                    | Ensure that `Afterpay.js` is being loaded on your page before referencing it, e.g. by using the `onload` script attribute.                                                       |
| `Uncaught ReferenceError: initAfterpay is not defined`                | Ensure that `initAfterpay` is defined **before** the script tag that loads `Afterpay.js`.                                                                                        |
| Afterpay popup opens but doesn't launch a checkout                    | Ensure your `onCommenceCheckout` handler has no errors (check the console), and that it calls `actions.resolve` with a valid token.                                              |
| `onComplete` callback is not called when checkout finishes            | This can occur due to issues with `postMessage` communication, especially with in-app browsers. Contact Cash App Afterpay with steps to replicate the issue.                     |
| `onShippingAddressChange` is not being called on address changes      | Ensure that `popupOriginUrl` was correctly defined when creating the checkout token.                                                                                             |
| Afterpay checkout does not display shipping options from the merchant | Ensure your `onShippingAddressChange` handler calls `actions.resolve` with a valid list of shipping options.                                                                     |
| The shipping address is invalid or ineligible for shipping            | Use `actions.reject` with a valid Shipping Constant to signal your rejection of the address to Afterpay.                                                                         |
| There are missing fields on the provided address                      | `onShippingAddressChange` sends a reduced address payload with only the data needed to calculate shipping. Full address details should be retrieved after the checkout finishes. |
