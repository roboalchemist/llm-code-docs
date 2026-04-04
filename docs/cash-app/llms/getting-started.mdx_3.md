# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/getting-started.mdx

***

## stoplight-id: 0466b6b44a3ff

# Getting Started

Pay Kit is a JavaScript SDK that allows you to accept Cash App Pay online. On desktop devices, a QR code is displayed to customers. When they scan it with their phone, it opens Cash App to approve the payment.

On mobile devices such as iPhone and Android phones, the customer is redirected from your checkout experience to Cash App. Customers can then approve the payment before they are redirected back to your site.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/pay-kit-visualization.png" alt="Pay Kit visualization" noZoom />

<Note title="Before you start">
  You need a merchant identifier from the [Network API](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/network-api) to get started. We recommend that you have a working API integration.
</Note>

## Include the Pay Kit script

Pay Kit must be loaded from our global CDN and cannot be bundled into your application. This allows us to provide the best security and helps you avoid compliance issues.

```html
<script src="https://sandbox.kit.cash.app/v1/pay.js"></script>
```

<Note title="Ready for production?">
  Change the script URL to `https://kit.cash.app/v1/pay.js`
</Note>

## Initialize Pay Kit

Once loaded, start Pay Kit with the same [Client ID](/cash-app-pay-partner-api/guides/partnerships/partner-onboarding-requirements) you use for API access.

```js
const pay = await window.CashApp.pay({ clientId: 'YOUR_CLIENT_ID' });
```

<Note title="Ready for production?">
  Remember to change `clientId` from your sandbox ID (i.e. `CAS-CI_...`) to your production ID (i.e. `CA-CI_...`)
</Note>

## Listen for events

Pay Kit emits a number of events throughout the lifecycle of a payment. One of the most important ones is `CUSTOMER_REQUEST_APPROVED`. This is emitted after a customer approves a one-time payment or other action. You use this data to [create a payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment).

```js
const amount = {
  currency: 'USD',
  value: 1234, // $12.34
};
const scopeId = 'merchant_id_from_network_api';

pay.addEventListener(
  'CUSTOMER_REQUEST_APPROVED',
  ({ customerProfile, grants, referenceId }) => {
    // create your payment with the grant and same amount and scope
  }
);
```

<Note title="Mobile Redirect">
  After a customer has redirected back from Cash App on mobile devices, the `CUSTOMER_REQUEST_APPROVED` event occurs almost immediately. It's important to add your listener right after initializing.
</Note>

### Other supported events

`CUSTOMER_INTERACTION`

```js
pay.addEventListener(
  'CUSTOMER_INTERACTION',
  (customerInteractionData) => {
    console.log("customerInteractionData:", customerInteractionData);
  }
);

```

`CUSTOMER_DISMISSED`

```js
pay.addEventListener(
  'CUSTOMER_DISMISSED',
  (customerDismissedData) => {
    console.log("customerDismissedData:", customerDismissedData);
  }
);
```

`CUSTOMER_REQUEST_DECLINED`

```js
pay.addEventListener(
  'CUSTOMER_REQUEST_DECLINED',
  () => {
    console.log("Customer request declined");
  }
);
```

`CUSTOMER_REQUEST_FAILED`

```js
pay.addEventListener(
  'CUSTOMER_REQUEST_FAILED',
  (data) => {
    console.log("Customer request failed", data);
  }
);
```

## Render Cash App Pay

Pay Kit provides a fully managed user interface that you can customize to fit your checkout experience.

```html
<div id="cash-app-pay"><!-- populated by Pay Kit --></div>
```

```js
await pay.render('#cash-app-pay');
```

See [Technical Reference](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/technical-reference) to read more about customization.

## Create a customer request

Merchants request to perform actions on a customer's account. Approved actions result in grants which can be used to create payments or refunds. A merchant needs to be [created](/cash-app-pay-partner-api/api-reference/network-api/create-merchant) before you can create a one-time payment. We also assume you have calculated the correct amount and currency for the payment.

One-time, on-file, or both one-time and on-file payment actions are supported in the `customerRequest` API.

```js
async function onCashAppPayLoaded() {
	const pay = await window.CashApp.pay({ clientId: CASH_APP_CLIENT_ID });
    
    // Customer request supports both one-time on-file payments simultaneously. 
    const customerRequest = {
      referenceId: REFERENCE_ID, // perhaps a cart or checkout identifier
      redirectURL: window.location.href, // where mobile customers should be redirected to
      actions: {
        payment: {
          amount: {
            currency: 'USD',
            value: 1234, // $12.34
          },
          scopeId: MERCHANT_ID
        },
        onFile: {
          scopeId: BRAND_ID,
          accountReferenceId: EXTERNAL_ID
        },
      },
    };

await pay.customerRequest(customerRequest);
};
```

You should now have a functioning integration.

### Interactive code samples

#### On file payment

[https://codepen.io/erinn-xyz/pen/OPPLKxz](https://codepen.io/erinn-xyz/pen/OPPLKxz)

#### One-time payment

[https://codepen.io/erinn-xyz/pen/JooPgaK](https://codepen.io/erinn-xyz/pen/JooPgaK)

## Use cases

Discover all the ways you can use Pay Kit.

### Rendering

[Getting Started](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/getting-started) uses the simplest selector, a string. You can also render Cash App Pay to an HTML element.

```js
const target = document.querySelector('#cash-app-pay');
await pay.render(target);
```

#### Customize the Cash App Pay Button

The Cash App Pay button that is initially rendered can be customized to fit your payment experience.

##### Button shapes

Pay Kit provides two shapes: `round` (default) and `semiround` which has less rounded corners.

```js
await pay.render('#cash-app-pay', { button: { shape: 'semiround' } });
```

##### Button sizes

Pay Kit provides two sizes: `medium` (default) and `small` which is, predictably, smaller.

```js
await pay.render('#cash-app-pay', { button: { size: 'small' } });
```

##### Button themes

Pay Kit provides two themes: `dark` (default) and `light` which has a white background.

```js
await pay.render('#cash-app-pay', { button: { theme: 'light' } });
```

##### Button widths

Pay Kit provides two widths: `static` (default) and `full` which expands to fill its container.

```js
await pay.render('#cash-app-pay', { button: { width: 'full' } });
```

#### Advanced controls

By default, Pay Kit provides a fully managed and branded UI as you saw in the [Getting Started](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/getting-started) guide. You may want advanced controls in certain situations such as validating information a customer has provided during checkout before continuing. The `render` method accepts a boolean `manage` option that allows you to control when to begin the authorization flow. When the `manage` option is `false`, a `begin` method will be returned for you to call when you're ready.

```js
const target = document.querySelector('#cash-app-pay');

const { begin } = await pay.render(target, { manage: false });

let hasBegun = false;
target.addEventListener('click', () => {
  if (!hasBegun) {
    // TODO: validate customer information
    begin();
  }
  hasBegun = !hasBegun; // on desktop, clicks to the container could be closing the modal
});
```

Your checkout experience may want to use its own button for consistency across payment methods. When the `manage` option is `false`, you can also set the `button` option to `false` to prevent a Cash App Pay button from being rendered. You can now provide your own button and manage the authorization flow.

```html
<div id="cash-app-pay"></div>

<button class="checkout-button">Checkout</button>
```

```js
const { begin } = await pay.render('#cash-app-pay', {
  button: false,
  manage: false,
});

document.querySelector('.checkout-button').addEventListener('click', () => {
  begin();
});
```

##### Custom elements

Pay Kit provides [custom elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements) to help customize checkout experiences while making it easy to follow brand guidelines.

The `<cash-app-pay-logo>` element renders a Cash App Pay logo which can be used when choosing a payment method or to enhance your checkout button.

```html
<button class="checkout-button">
  Continue with
  <cash-app-pay-logo size="small" theme="dark" />
</button>
```

The `<cash-app-pay-customer>` element renders the Cash App Pay logo and a customer's \$Cashtag with automatic truncation to easily fit your layout. You can combine these advanced render options and custom elements to use your own checkout button, manage the authorization flow, and display the Cash App Pay brand before and after approval with just a few lines of JavaScript.

```html
<cash-app-pay-customer class="hidden" />
```

```js
const button = document.querySelector('.checkout-button');

pay.addEventListener('CUSTOMER_REQUEST_APPROVED', ({ customerProfile }) => {
  button.classList.add('hidden'); // hide the checkout button

  const customer = document.querySelector('cash-app-pay-customer');
  customer.setAttribute('cashtag', customerProfile.cashtag);
  customer.classList.remove('hidden'); // show the cashtag
});

const { begin } = await pay.render('#cash-app-pay', {
  button: false,
  manage: false,
});

await pay.customerRequest(details);

button.addEventListener('click', () => {
  begin();
});
```

See [Technical Reference](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/technical-reference) to read more about customization.

### Placing another order in a single page app

After a successful checkout, the buyer may visit another page. Then, the buyer may come back to the checkout page to order without refreshing the page. Or in another scenario, you may want to provide an upsell right after the buyer completes the checkout.

When you need to take a new order with Pay Kit, you can call `restart` on the Pay instance:

```js
pay.restart();
```

When restarted, Pay Kit will forget about all previous authorizations and previously charged amounts. It will also remove all managed UI (for example, the Cash App Pay button, QR code modal, or approved Cashtag).

After restarting you can start another order as usual:

```js
pay.render(...) // to show a new Cash App Pay button
pay.customerRequest(...) // to specify amount for the new charge
```

We recommend that in a single page app, you should call `pay.restart()` whenever the buyer leaves the checkout page. When restarting at the exit of each page, if a buyer comes back to the checkout page, your initialization flow will work as usual without the buyer ever seeing the QR code for a previous customer request.

### Working with customer requests

Pay Kit allows you to `render` independently of creating a `customerRequest` so you can control the authorization experience as a customer checks out. Pay Kit's managed UI will adapt as you update your Customer Request.

```js
const details = {};
```

All `customerRequest` calls require a `redirectURL` which is where a customer will be taken after authorizing if they begin on a mobile device such as an iPhone or Android phone. This page should initialize Pay Kit and expect a `CUSTOMER_REQUEST_APPROVED` [event](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/technical-reference#addeventlistener). If approved, Pay Kit will render a customer's \$Cashtag, and you will be ready to create a payment.

```js
details.redirectURL = window.location.href;
```

You may optionally specify a `referenceId` which can be helpful to associate a cart, checkout, or order to a payment.

```js
details.referenceId = 'cart123';
```

#### One-time payments

The [Getting Started](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/getting-started) guide uses the simplest action: a one-time payment. The `amount` should match what you intend to charge when [creating a payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment).

```js
details.actions = {
  payment: {
    amount: {
      currency: 'USD',
      value: 23.45, // $23.45
    },
    scopeId: 'merchant_id_from_network_api',
  },
};
```

#### On-file payments

You can also request to store a customer's account, allowing you to create payments on a recurring basis. The scope ID can be a client or brand account.

```js
details.actions.onFile = {
  scopeId: 'brand_id_from_network_api',
};
```

See [On-file Payments](/cash-app-pay-partner-api/guides/technical-guides/payment-processing/on-file-payments) to know more.

#### Update customer requests

After creating a Customer Request, you can update it as long as the customer has not begun to interact (for example, scanned a QR code or been redirected to Cash App).

```js
const { update } = await pay.customerRequest(details);
```

Let's start simple by updating the `referenceId`:

```js
details.referenceId = 'cart456';

let success = await update(details);
if (success) {
  // referenceId was successfully updated
}
```

##### Update a one-time payment

Initially, we intended to charge the customer \$23.45, but if they changed their shipping option or applied a promotion, that amount value may have changed. You can apply the new value to `details` and then call `update`:

```js
details.actions.payment.amount.value = 3456; // $34.56
success = await update(details);
```

##### Update an on-file payment

Initially, we scoped our on-file action to the brand level which is a best practice. If you need to perform recurring charges for all of your brands, you can assign your client ID to `details` and then call `update`:

```js
details.actions.onFile.scopeId = 'client_id';
success = await update(details);
```

##### Remove an action

Initially, we constructed `details` to include both a one-time payment action and on-file action, but if a customer chooses not to enable recurring payments, the set of actions should be updated. You can delete an action from `details` and then call `update`:

```js
delete details.actions.onFile;
success = await update(details);
```

#### Unknown amounts

There may be times where `amount` for a one-time payment is difficult to calculate or simply unavailable. You may omit it, but be aware this may diminish the customer experience and increase the likelihood the payment is declined.

```js
await pay.customerRequest({
  actions: {
    payment: {
      scope_id: 'merchant_id_from_network_api',
    },
  },
  redirectURL: window.location.href,
});
```

## Going to production

When you use Pay Kit in production, remember to update the script URL and your Client ID.

```js
<script
-   src="https://sandbox.kit.cash.app/v1/pay.js"
+   src="https://kit.cash.app/v1/pay.js"
></script>

<script>
    const pay = await window.CashApp.pay({
-       clientId: 'CAS-CI_...',
+       clientId: 'CA-CI_...',
    });
</script>
```

Always load Pay Kit in a secure context (i.e. valid `https`).
