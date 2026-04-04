# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/api-quickstart/create-a-checkout.mdx

***

## stoplight-id: po3qixnmb26wy

# Create a checkout

There are three steps to create a Cash App Afterpay checkout:

1. Call [Get Configuration](/cash-app-afterpay/api-reference/reference/configuration/get-configuration) to retrieve your order limits
2. Call [Create Checkout](/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1) to generate a checkout token
3. Launch the Cash App Afterpay checkout flow using a redirect or a popup window

| **Action**                                                                                      | **Endpoint**                 | **Purpose**                                          |
| ----------------------------------------------------------------------------------------------- | ---------------------------- | ---------------------------------------------------- |
| [Get Configuration](/cash-app-afterpay/api-reference/reference/configuration/get-configuration) | `/v2/platform/configuration` | Retrieve Afterpay order limits (min/max values).     |
| [Create Checkout](/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1)       | `/v2/checkouts`              | Provide order details and generate a checkout token. |

## Retrieve your order limits

Call the [Get Configuration](/cash-app-afterpay/api-reference/reference/configuration/get-configuration) endpoint to retrieve your minimum and maximum Cash App Afterpay order amounts.

We recommend calling this endpoint once a day as part of a scheduled background process, and storing the `minimumAmount` and `maximumAmount` values on your server.

Use these values to determine:

1. The correct [Cash App Afterpay Messaging](/cash-app-afterpay/guides/afterpay-messaging/getting-started) to show on the Product Detail pages
2. Whether Cash App Afterpay should be presented as an available payment method

A request to create a checkout will be declined if the order grand total is less than the minimum or more than the maximum Cash App Afterpay amount. To change your minimum and maximum order values, contact Cash App Afterpay.

<div>
  ```mermaid
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
        'noteBorderColor': '#000',
        'background': '#fff'
      }
    }
  }%%
  sequenceDiagram
      Merchant Website ->> Cash App Afterpay: GET/v2/configuration
      Cash App Afterpay -->> Merchant Website: Configuration
  ```
</div>

## Create a checkout

Call the [Create Checkout](/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1) endpoint to communicate the order details to Cash App Afterpay. Your request should include:

1. Customer information
2. Order details
3. Order total
4. Shipping details
5. Redirect URLs

<Info>
  Cash App Afterpay uses the order total value to calculate the installment plan and to assist with the customer's pre-approval process.
</Info>

Cash App Afterpay responds with a token used to identify this checkout.
For example, `002.5lmerr3k945d00c7htvcrdff83q36kp10a247m212fjpa5ju`. This token is used to launch the Cash App Afterpay checkout flow using Afterpay.js.

#### Afterpay.js

| **Environment** | **URL**                                           |
| --------------- | ------------------------------------------------- |
| Sandbox         | `https://portal.sandbox.afterpay.com/afterpay.js` |
| Production      | `https://portal.afterpay.com/afterpay.js`         |

<div>
  ```mermaid
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
      Merchant Website ->> Cash App Afterpay: POST/v2/checkouts
      Cash App Afterpay -->> Merchant Website: Token
  ```
</div>

## Set up your checkout experience

As part of your integration, decide how customers will complete the Cash App Afterpay checkout flow. There are two options:

* **Redirect method:** Customers are redirected from your website to Cash App Afterpay to complete their payment. At the end of the Cash App Afterpay checkout flow, the customer is redirected back to your website. Most merchants use this method.
* **Popup method:** The Cash App Afterpay checkout flow opens in a popup window on top of your site. For windowed applications, your website is dimmed with a semi-transparent overlay. For full-screen applications (such as mobile interfaces), the flow opens in a new tab. At the end of the Cash App Afterpay checkout flow, the popup closes.

### Implement the redirect method

To use the redirect method, call the following two JavaScript functions, in order:

1. `AfterPay.initialize`: Prepares the Afterpay JavaScript to start the Cash App Afterpay screenflow in the appropriate geographical region.
   * Accepts an object with a required `countryCode` (the two-character ISO 3166-1 country code of the merchant account)
2. `AfterPay.redirect`: Redirects the customer's browser from your website to Cash App Afterpay.
   * Accepts an object with a required `token` (the checkout token returned by the Create Checkout API call)

```js
<html>
<head>
 <script onload="initAfterPay()" src="https://portal.sandbox.afterpay.com/afterpay.js"></script>
</head>
<body>
 <p>Your HTML here</p>
 <script>
 function initAfterPay () {
   AfterPay.initialize({countryCode: "AU"});
   AfterPay.redirect({token: "YOUR_TOKEN"});
 }
 </script>
</body>
</html>
```

If the customer successfully completes the checkout flow, they’re returned to your `redirectConfirmUrl` with a checkout token and a `SUCCESS` status appended as HTTP query parameters: `www.merchant-example.com/confirm?&status=SUCCESS&orderToken=002.5lmerr3k945d00c7htvcrdff83q36kp10a247m212fjpa5ju`

If the customer cancels the checkout, they’re returned to your `redirectCancelUrl` with a checkout token and a `CANCELLED` status appended as HTTP query parameters: `www.merchant-example.com/confirm?&status=CANCELLED&orderToken=002.5lmerr3k945d00c7htvcrdff83q36kp10a247m212fjpa5ju`

<Info title="Recommendation">
  Try using your Sandbox merchant credentials to get a token from [Create Checkout](/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1). Use this token to test the Cash App  Afterpay screenflow on JSFiddle: [https://jsfiddle.net/afterpay/cyd3pxfj/](https://jsfiddle.net/afterpay/cyd3pxfj/)

  <br /><br />Note that the login and redirect features won't work, because JSFiddle loads the Cash App Afterpay screenflow inside a frameset.
</Info>

### Implement the popup method

To use the popup method, call the following JavaScript functions, in order:

1. `AfterPay.initialize`: Prepares the Afterpay JavaScript to start the Cash App Afterpay screenflow in the appropriate geographical region.
2. `AfterPay.open`: Opens the Cash App Afterpay popup window, launching the checkout flow for the customer.
3. `AfterPay.onComplete`: Defines a callback function. It checks whether the customer successfully completes the checkout flow and handles successful payments and cancellations.
4. `AfterPay.transfer`: Sends the checkout token to Cash App Afterpay, finalizing the payment process.

When a customer’s payment is complete, Cash App Afterpay uses `postMessage` to call a JavaScript method on your front end system.

<Note>
  The popup method doesn't redirect customers to the `redirectConfirmUrl` or `redirectCancelUrl`, but these fields are still required for the Create Checkout call. These fields are used for context on `postMessage`.
</Note>

```js
<html>
<head>
 <script type="text/javascript" src="https://portal.sandbox.afterpay.com/afterpay.js"></script>
</head>
<body>
 <button id="afterpay-button">
   Cash App Afterpay it!
 </button>
 <script type="text/javascript">
   document.getElementById("afterpay-button").addEventListener("click", function() {
     AfterPay.initialize({countryCode: "AU"});
     // To avoid triggering browser anti-popup rules, the AfterPay.open()
     // function must be directly called inside the click event listener
     AfterPay.open();
     // If you don't already have a checkout token at this point, you can
     // AJAX to your backend to retrieve one here. The spinning animation
     // will continue until `AfterPay.transfer` is called.
     // If you fail to get a token you can call AfterPay.close()
     AfterPay.onComplete = function(event) {
       if (event.data.status == "SUCCESS") {
         // The customer confirmed the payment schedule.
         // The token is now ready to be captured from your server backend.
       } else {
         // The customer cancelled the payment or closed the popup window.
       }
     }
     AfterPay.transfer({token: "YOUR_TOKEN"});
   });
 </script>
</body>
</html>
```

If the customer successfully completes the checkout flow, Cash App Afterpay calls the `onComplete` method on your website. Cash App Afterpay passes the checkout token and a `SUCCESS` status as properties of a data object. The popup closes.

If the customer cancels the checkout, Cash App Afterpay calls the `onComplete` method on your website. Cash App Afterpay passes the checkout token and a `CANCELLED` status as properties of a data object. The popup closes.

<Note>
  At the end of the checkout flow, if the protocol, host, and port of the opening window don't match those provided in Create Checkout, the customer's browser won't dispatch the JavaScript event for security reasons.
</Note>

**Cash App Afterpay checkout screen**

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/create-a-checkout.png" alt="create-a-checkout.png" noZoom />
