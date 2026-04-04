# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/additional-features/express-checkout/reference-information.mdx

***

## stoplight-id: vdnra0owfphes

# Express checkout reference

## Sequence diagram

Express checkout has similar behaviour across both deferred and integrated shipping. The sequence diagram below shows a high-level checkout sequence for a customer using integrated shipping.

<div>
  ```mermaid
  ---
  config:
    sequence:
      mirrorActors: true
      width: 250
  ---
  %%{
    init: {
      'theme': 'base',
      'themeVariables': {
        'primaryColor': '#FFF',
        'primaryTextColor': '#000',
        'primaryBorderColor': '#000',
        'lineColor': '#000',
        'secondaryColor': '#fff',
        'tertiaryColor': '#fff',
        'noteBkgColor': '#fff',
        'noteBorderColor': '#000'
      }
    }
  }%%
  sequenceDiagram
      title Cash App Afterpay Express Checkout Happy Path
      participant C as Consumer
      participant M as Merchant
      participant AP as $Afterpay
      participant XCO as Express Checkout
      Note over C,XCO: shopping cart
      C->>M: Checkout using $Afterpay express
      M->>AP: Create order
      AP-->>M: Order token
      Note over C,XCO: $Afterpay checkout
      M-->>C: Open $Afterpay Checkout
      C->>XCO: Select shipping address
      XCO->>M: Shipping address change callback
      M-->>XCO: Shipping options and taxes
      C->>XCO: Choose shipping method
      XCO->>XCO: Update order value
      C->>XCO: Complete order
      XCO->>M: onComplete
      Note over C,XCO: Review and confirm
      M->>AP: Get order
      AP-->>M: Afterpay order
      M->>M: Verify transaction
      M->>C: Review order
      C->>M: Confirm
      M->>AP: Capture payment
  ```
</div>

1. A customer (consumer) chooses *Checkout with Cash App Afterpay Express* from the shopping cart or product.
2. The merchant calls the *Create Order* or *Create Checkout* endpoint, passing an option to enable dynamic pricing in the Express Checkout.
3. The merchant uses the token in combination with the Javascript `afterpay.js` to direct the customer through the Cash App Afterpay Express checkout flow using the popup method.
4. The customer enters Express Checkout and selects the shipping address they want from their existing Cash App Afterpay details.
5. Cash App Afterpay calls the `onShippingAddressChange()` callback function on the merchant site to retrieve all shipping options and taxes for the chosen address.
6. The customer selects the shipping method and the order total, including the payment schedule, is updated to include the relevant shipping and taxes.
7. The customer confirms their Cash App Afterpay order and Cash App Afterpay notifies the merchant using the `onComplete()` callback function.
8. The merchant verifies the transaction by fetching the Order from Cash App Afterpay and comparing it to their own records.
9. The merchant shows the customer a confirmation page (optional).
10. The customer confirms their order. The merchant calls Cash App Afterpay to capture the payment, passing the calculated order amount for verification.

```json
AfterPay.initializeForPopup({
  countryCode: 'US',
  onCommenceCheckout: function(actions) {
    /* retrieve cash app afterpay token from your server */
    /* then call `actions.resolve(token)` */
  },
  onShippingAddressChange: function (data, actions) {
    /* required for Integrated Shipping  */
    /* address in `data` */
    /* calc options, then call `actions.resolve(options)` */
  },
  onShippingOptionChange: function (data) {
    /* optional - chosen option in `data` */
  },
  onComplete: function (data) {
    /* handle success/failure of checkout */
  },
  target: '#afterpay-express-button',
  buyNow: false,
  pickup: false,
  shippingOptionRequired: true
})
```

<Note>
  Integrated Shipping is enabled by default for Express orders. To disable it, set `shippingOptionRequired` to false.
</Note>

**Integrated and Deferred Shipping**

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Afterpay-EC-Flows-2.png" alt="Afterpay-EC-Flows.png" noZoom />

**Flow Diagram Key**

* Auth = Payment authorization
* Cart = Online shopping cart or basket
* Checkout = Checkout page
* Config = Configuration
* EC = Express Checkout
* PDP = Product Display Page

### Feature variant combinations

**InitializeForPopup only**

addressMode: `ADDRESS_WITH_SHIPPING_OPTIONS` - no widget needed.

This is the default configuration.

Within the Cash App Afterpay Checkout flow, the customer can:

* Select a shipping address from within their Cash App Afterpay account.
* View shipping options from the merchant and select one.
* Complete the order

The merchant must:

* Listen to the `onShippingAddressChange` and provide the relevant shipping options.

**Recommended:** for orders that need to be shipped to the customer’s address and have up to five simple shipping options

***

addressMode: `PICKUP_FROM_ORDER_ADDRESS` - no widget needed.

Within the Cash App Afterpay Checkout flow, the customer can:

* See their pickup address (previously selected on the merchant site), but not change it
* View pickup options from the merchant and select one
* Complete the order

The merchant must:

* Send pickup address when creating an order token

* Listen to the `onShippingAddressChange` and provide the relevant pickup options

**Recommended** for orders picked up at a specific location (e.g. your physical store)

***

addressMode: `SHIP_TO_ORDER_ADDRESS` - no widget needed.

Within the Cash App Afterpay Checkout flow, the customer can:

* See their chosen order address from the merchant site (but not change it)

* View shipping options from the merchant and select one\
  Complete the order

The merchant must:

* Send shipping address when creating an order token

* Listen to the `onShippingAddressChange` and provide the relevant shipping options

**Recommended** for orders to be shipped to the customer’s address chosen on your site (before launching Express Checkout). In this case, the address displayed within the Cash App Afterpay checkout flow is locked and customers cannot change it.

***

**initializeForPopup or initializeForRedirect**

addressMode: `NO_ADDRESS` - no widget needed.

Within the Cash App Afterpay Checkout flow, the customer can:

* Complete the order

Customers cannot do the following actions within the Cash App Afterpay checkout flow

* View a shipping or pickup address
* View shipping options from the merchant and select one

**Recommended** for when there is no shipping or pickup needed (eg.digital goods or services).

***

addressMode: `SHIP_TO_ORDER_ADDRESS_WITHOUT_SHIPPING_OPTIONS` - no widget needed.

Within the Cash App Afterpay Checkout flow, the customer can:

* See their chosen order address from the merchant site (but not change it)
* Complete the order

Customer cannot do the following actions within the Cash App Afterpay checkout flow:

* View shipping options from the merchant and select a shipping option

The merchant must:

* Send the shipping address when creating an order token

**Recommended** for orders that must be shipped to the customer’s address chosen on your site (before launching Express Checkout), and there are no shipping options available for customers to choose from.

## Security - postMessage()

`afterpay.js` uses the HTML `postMessage()` API to exchange information between the Cash App Afterpay checkout popup and the page that spawned it. This allows Javascript code running on different origins to communicate with each other in a bidirectional manner.

The bidirectional communication allows a merchant to dynamically update shipping options and transaction information based on a chosen shipping address.

`afterpay.js` hides this complexity and restricts the use of `postMessage()` to ensure a secure environment. Specifically:

* Cash App Afterpay’s checkout window only receives messages from the merchant window, and vice versa

* Correctly handles multiple concurrent, and possibly out-of-order requests

* Message data is validated and sanitized

Using `postMessage()` in this way is considered very secure. For more information please refer to the [specification](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage).
