# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/add-cash-app-pay-to-your-site/overview.mdx

***

## stoplight-id: 6db8pqa5v9f5y

# Adding Cash App Pay to Your Site

Cash App Pay is a fast and simple *pay now* payment method for your customers. Currently it is only available in the USA.

There are two ways customers can pay you with Cash App Pay:

* [Shopping from a Desktop Device with a QR code](#shopping-from-a-mobile-device-with-a-qr-code)

* [Shopping from a Mobile Device by Tapping](#shopping-from-a-mobile-device-by-tapping)

These two payment flows are summarized below:

#### Shopping from a Desktop Device with a QR Code

1. From their desktop device, the customer selects Cash App Pay as the payment method during checkout.

2. The customer holds their mobile device camera or Cash App’s QR scanner over the QR code that appears on the desktop screen to scan the QR code.

3. The customer follows the prompts on their mobile device to complete the transaction.

#### Shopping from a Mobile Device by Tapping

1. From their mobile device, the customer taps Cash App Pay to select it as the payment method during checkout.

2. The customer is redirected to Cash App, where they can follow the prompts to complete the transaction.

<Note>
  Remember that Cash App Pay is a **pay now** payment method. Customers use Cash App Pay to  pay for goods and services in a single payment at the time of purchase.

  Cash App Afterpay is a **pay later** payment method. Customers use Cash App Afterpay to pay for goods and services in several interest-free payments.
</Note>

## Appearance

If you implement Cash App Pay with Cash App Afterpay, expect the appearance of your checkout and payment pages to change slightly.

On checkout or other payment screens, Cash App Pay appears as a separate payment option alongside Cash App Afterpay. Cash App Pay is not within Cash App Afterpay, but provided alongside it. Customers with Cash App accounts can use their Cash App balance as a payment source to pay in installments.

## Availability

It is important you are aware of Cash App Pay availability along with its related products:

* Cash App Pay is only available in the USA

* Cash App Pay on file is only available in the USA

## Detailed Information

The following sections are on this page:

* [Integrating Cash App payments using the existing Cash App Afterpay API](#integrating-cash-app-payments-using-the-existing-cash-app-afterpay-api)
* [Mobile Redirection](#mobile-redirection)
* [Restarting Cash App Pay for a New Checkout Request](#restarting-cash-app-pay-for-a-new-checkout-request)
* [Payment refunds with Cash App](#payment-refunds-with-cash-app)
* [Settlement with Cash App](#settlement-with-cash-app)
* [Add Your Logo to the QR Code Scanner](#add-your-logo-to-the-qr-code-scanner)
* [Advanced Rendering Control](#advanced-rendering-control)

Cash App Pay on file has a page of its own:

* [Cash App Pay on file](/cash-app-afterpay/guides/api-development/add-cash-app-pay-to-your-site/cash-app-pay-on-file)

## Integrating Cash App Payments Using the Existing Cash App Afterpay API

<Warning title="Disclaimer">
  To successfully launch the Cash App Pay screenflow on your website's front-end, you must use the exact same JS script employed for [launching the Cash App Afterpay screenflow](/cash-app-afterpay/guides/api-development/api-quickstart/create-a-checkout).

  For example, `<script onload="initAfterPay()" src="https://portal.sandbox.afterpay.com/afterpay.js" async defer></script>`
</Warning>

Accepting Cash App Pay payments uses the standard API for the Cash App Afterpay [checkout process](/cash-app-afterpay/guides/api-development/api-quickstart/create-a-checkout), with your existing Cash App Afterpay credentials. The Cash App Afterpay backend handles the transaction with Cash App Pay. The implementation process is as follows:

1. Call the [Create Checkout API](/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1) with the addition of the following parameter `isCashAppPay: true` to create an order token.

2. Use the token in combination with the [Standard Checkout](/cash-app-afterpay/guides/api-development/api-quickstart/create-a-checkout) flow, but call `AfterPay.initializeForCashAppPay` instead of Afterpay. like in the code sample below:

   ```js
   function initAfterPay() {

       var cashAppPayOptions = {
           button: {
               size: 'small', // "medium" | "small"
               width: 'full', // "full" | "static"
               theme: 'dark', // "dark" | "light"
               shape: 'round' // "round" | "semiround"
           },
           onComplete: function(event) {
               const {
                   status,
                   cashtag
               } = event.data;
           },
           /* Optional event listeners for merchants to track customer behavior and listen for transaction events in the lifecycle */
           eventListeners: {
               "CUSTOMER_INTERACTION": ({
                   isMobile
               }) => {
                   console.log(`CUSTOMER_INTERACTION`)
                   if (isMobile) {
                       // captureMobileMetrics()
                   } else {
                       // captureDesktopMetrics()
                   };
               },
               "CUSTOMER_REQUEST_DECLINED": () => {
                   console.log(`CUSTOMER_REQUEST_DECLINED`)
               },
               "CUSTOMER_REQUEST_APPROVED": () => {
                   console.log(`CUSTOMER_REQUEST_APPROVED`)
               },
               "CUSTOMER_REQUEST_FAILED": () => {
                   console.log(`CUSTOMER_REQUEST_FAILED`)
               }
           }
       }
       AfterPay.initializeForCashAppPay({
           countryCode: "US",
           token: "ORDER_TOKEN_PLACEHOLDER",
           cashAppPayOptions
       });
   }
   ```

3. Add a div with `id="cash-app-pay"` where you want the Cash App Pay button to be rendered.

4. On clicking the button the customer is shown a QR code (on desktop).

   ![Cash App Pay QR Code](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/qrcode-cash-app-pay.png)

5. If the customer confirms the order, an Order Token, the customer's Cashtag, and a SUCCESS status is returned. If the customer cancels the order, the Order Token and CANCELLED status are returned. We recommend that you display the Cashtag to the customer on the review or confirmation page. This is an example event object:

```JavaScript

event: {
    "data": {
        "status": "SUCCESS",
        "cashtag": "$CASHTAG_PLACEHOLDER",
        "orderToken": "ORDER_TOKEN_PLACEHOLDER",
    }
}
```

<Info title="Cashtags are returned based on the environment">
  * **Sandbox:** The Cash App Afterpay Sandbox always returns the Cashtag: `$CASHTAG_C_TOKEN`.
  * **Production:** In production, each customer's actual Cashtag is returned.
</Info>

6. Depending on the payment flows you use for Cash App Afterpay, you follow the same process to complete an order. Either call [Auth](/cash-app-afterpay/guides/api-development/api-quickstart/deferred-capture) or [Direct Capture](/cash-app-afterpay/guides/api-development/api-quickstart/immediate-capture). You receive an APPROVED or DECLINED status from Cash App Afterpay once the Auth or Direct Capture API has been completed.

## Mobile Redirection

On Mobile, instead of a QR code, the customer is redirected to the Cash App. When the customer approves, they are returned to the URL specified in the `redirectConfirmUrl` in the Create Checkout call. This can be the same page where the Cash App Pay button is rendered e.g. merchant.com/checkout, or a new page for example, `merchant.com/review`

<Tip title="Query Params can be added to the redirectConfirmURL">
  If you want to determine if the page is loading as a result of redirect from the Cash App, you can add a query param to your redirectConfirmURL. e.g. merchant.com/checkout?cashapppay=true
</Tip>

<Info title="The redirectCancelURL is not used by Cash App Pay">
  On mobile, the customer is always redirected to the redirectConfirmUrl for approved and declined flows.
</Info>

The page the `redirectConfirmUrl` points to should initialize afterpay.js and define the below `onComplete` callback on page load:

```JavaScript

function onPageLoad () {
    var cashAppPayListenerOptions = { 
        onComplete: function(event) {
          const { status, cashtag, orderToken} = event.data;
        },
        /* Optional event listeners for merchants to track customer behavior and listen for transaction events in the lifecycle */
           eventListeners: {
                "CUSTOMER_INTERACTION": ({ isMobile }) => {
                    console.log(`CUSTOMER_INTERACTION`)
                    if (isMobile) {
                        // captureMobileMetrics()
                    } else {
                        // captureDesktopMetrics()
                    };
                },
                "CUSTOMER_REQUEST_DECLINED": () => {
                    console.log(`CUSTOMER_REQUEST_DECLINED`)
                },
                 "CUSTOMER_REQUEST_APPROVED": () => {
                    console.log(`CUSTOMER_REQUEST_APPROVED`)
                },
                "CUSTOMER_REQUEST_FAILED": () => {
                    console.log(`CUSTOMER_REQUEST_FAILED`)
                }
            }
      }

    AfterPay.initializeCashAppPayListeners({countryCode: "US", cashAppPayListenerOptions});
}
```

## Restarting Cash App Pay for a New Checkout Request

<Info>
  To implement this functionality, you must be using 

  [advanced rendering](#advanced-rendering-control)

  .
</Info>

### After checkout completion

After a successful checkout, the customer may visit another page, and then return to the checkout page to place an order without refreshing the page. Or in another scenario, you may want to provide an upsell immediately after the customer completes the checkout.

When you need to take a new order with Cash App Pay, you can call `AfterPay.restartCashAppPay`.

```js
AfterPay.restartCashAppPay()
AfterPay.renderCashAppPayButton()
```

When restarted, AfterPay.js "forgets" all previous authorizations and previously charged amounts. It also removes all Cash App Pay UI (for example, the Cash App Pay button, QR code modal, or approved Cashtag).

We recommend that in a single page app, you call `AfterPay.restartCashAppPay` whenever the customer leaves the checkout page. When restarting at the exit of each page, if a customer comes back to the checkout page, your initialization flow works as normal. The customer never sees the QR code for a previous customer request.

### Before checkout completion

In some cases, the payment button must be re-rendered and re-initialized without a successful checkout. For example, if a customer selects Cash App Pay, switches to a different payment method, and then re-selects Cash App Pay.

When a customer re-selects Cash App Pay, call `AfterPay.renderCashAppPayButton` to re-render the button. Next, restart Cash App Pay by calling `AfterPay.restartCashAppPay`.

```js
AfterPay.restartCashAppPay()
AfterPay.renderCashAppPayButton()
```

Since the original checkout token is unused, you can use that token with `AfterPay.initializeForCashAppPay(...)`.

## Payment Refunds with Cash App

Cash App Pay purchase and refund flows follow the standard Cash App Afterpay payment refund and void processes.

However, if there is an error when refunding a Cash App pay order, additional information will be supplied in the payload. See the example code below to see this in action.

**Example Code**

```
{
"errorCode": "declined",
"errorId": "ERROR_ID_PLACEHOLDER",
"message": "Cash App declined refund request (permanent decline): PAYMENT_PROCESSING_ERROR REFUND_DECLINED_OTHER  Refund could not be created.",
"httpStatusCode": 422
}
```

<Info>
  You can find a complete list of Cash App Pay error codes [here](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/errors/error-code-reference).
</Info>

## Settlement with Cash App

All payment resolution is handled by Cash App Afterpay. Your settlement information differentiates between Cash App Afterpay and Cash App sales.

## Add Your Logo to the QR Code Scanner

Add your company or organization's logo to the QR code pop-up that appears during Cash App Pay checkout. You host this logo, send us its URL and we place it next to the QR code. See an example in the picture below:

![qr-code-afterpay-resized.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/qr-code-afterpay-resized.png)

To do this:

1. Host your logo with its own URL. An appropriate logo must be:

* At least 256 x 256 pixels in size

* No larger than a 2MB file size

* A square logo, because other shapes get distorted.

* Produced with spacing/padding around the logo image, so that no part of the logo is cut-off when it is displayed

* In a format of either .png, .jpg, or .jpeg

2. Contact your Cash App Afterpay sales contact or Cash App Afterpay merchant services representative and send them the logo URL.

3. We (Cash App Afterpay) will ensure your logo appears next to the Cash App Pay QR code.

A brand logo is not necessary for Cash App Pay to work, although the co-branding enhances the customer experience at checkout. Your brand logo is required to pass certification testing.

## Advanced Rendering Control

As standard, we provide a fully managed and branded UI that includes a Cash App Pay button.

In some situations you may want advanced controls. For example, you may want to validate information a customer has given during checkout before the transaction continues. When `AfterPay.renderCashAppPayButton` is called, a begin method is returned through the `onBegin` callback for you to call when you're ready.

### Create Your Custom Button

You have two choices - to use JavaScript to create the custom button, or to use HTML direct.

**JavaScript**

```JavaScript
function createCustomButton() {
  // Create custom button
  const cashAppPayCustomButton = document.createElement('button');
  cashAppPayCustomButton.classList.add('btn', 'cash-app-pay-custom-button');
  cashAppPayCustomButton.textContent = "Continue with";

  // Attach cash app pay logo to button
  const cashAppPayLogo = document.createElement('cash-app-pay-logo');
  cashAppPayCustomButton.appendChild(cashAppPayLogo);
  document.getElementById('cash-app-pay').after(cashAppPayCustomButton);
}

```

**HTML**

```HTML
<button class="btn cash-app-pay-custom-button">
  Continue with<cash-app-pay-logo></cash-app-pay-logo>
</button>
```

The `<cash-app-pay-logo>` element renders a Cash App Pay logo. You can use this logo on your "choose a payment method page," or to enhance your checkout button.

### Initialize the Authorization Flow when Ready

You may want to use a specific button in your checkout experience for consistency across payment methods. When the manage option is `false`, you can also set the button option to `false`. This stops a Cash App Pay button from being rendered. You can now provide your own button and manage the authorization flow.

```JavaScript
// Attach event listener to the custom button described in the previous section
function addEventListenerToCashAppPayButton(func) {
  const customButton = document.querySelector('.cash-app-pay-custom-button')
  customButton.addEventListener('click', func);
}

// Initialize the CashAppPay flow
// This can be by itself or within the onBegin callback from renderCashAppPayButton 
function initializeForCashAppPay(token) {
  var cashAppPayOptions = {
    onComplete: function(event) {
      console.log(`onComplete: ${JSON.stringify(event.data, null, 4)}`);
      var { cashtag } = event.data;
      document.querySelector('.cash-app-pay-custom-button').setAttribute('hidden', true); // hide the button
      var cashAppPayCustomer = document.querySelector('cash-app-pay-customer');
      cashAppPayCustomer.setAttribute('cashtag', cashtag);
      cashAppPayCustomer.removeAttribute('hidden'); // show the cashtag
    },
    /* Optional event listeners */
    eventListeners: {
      "CUSTOMER_INTERACTION": ({ isMobile }) => {
        console.log(`CUSTOMER_INTERACTION is on Mobile: ${isMobile}`)
      },
      "CUSTOMER_REQUEST_DECLINED": () => {
        console.log(`CUSTOMER_REQUEST_DECLINED`)
      },
      "CUSTOMER_REQUEST_APPROVED": () => {
        console.log(`CUSTOMER_REQUEST_APPROVED`)
      },
      "CUSTOMER_REQUEST_FAILED": () => {
        console.log(`CUSTOMER_REQUEST_FAILED`)
      },
      "CUSTOMER_DISMISSED": () => {
        console.log(`CUSTOMER_DISMISSED`)
      }
    }
  }

  AfterPay.initializeForCashAppPay({
    countryCode: "US",
    token,
    cashAppPayOptions
  });
}

// Load PayKit and render the CashAppPayButton without making any additional API calls. Token from createCheckout is not required.
function renderCashAppPayButton() {
  var cashAppPayButtonOptions = {
    button: false, // button set to false prevents a Cash App Pay button from being rendered so you can use your own custom button
    manage: false, // when the manage option is false, a begin function will be returned for merchant to call when they're ready
    onBegin: function({ begin }) {
      addEventListenerToCashAppPayButton(async (event) => {
        event.preventDefault();
        const token = await createCheckout(true);
        initializeForCashAppPay(token);
        begin();
      });
    },
  }
  //This allows you to render the button without a token
  AfterPay.renderCashAppPayButton({
    countryCode: "US",
    cashAppPayButtonOptions
  });
}
```

## Troubleshooting

### CSP - Content Security Policy

If you want to use Cash App Pay and have a CSP (Content Security Policy), please ensure that the CSP whitelists paykit's `pay.css` file.

This whitelisting must apply equally to both the production and sandbox versions of Cash App Pay.
