# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/technical-reference.mdx

***

## stoplight-id: 5fb427816ed9c

## Pay

Pay Kit initializes to `window.CashApp` when you include our script and exposes an asynchronous `pay` method which requires a [Client ID](/cash-app-pay-partner-api/guides/partnerships/partner-onboarding-requirements). The Promise resolves an instance of `Pay`.

```html
<script src="https://kit.cash.app/v1/pay.js"></script>
<script>
  const pay = await window.CashApp.pay({ clientId: 'YOUR_CLIENT_ID');
</script>
```

{/* markdownlint-disable MD001 -- keeps table of contents hierarchical */}

#### Parameters

{/* markdownlint-enable MD001 -- keeps table of contents hierarchical */}

| Name       | Type     | Description                                                                                   |
| :--------- | :------- | :-------------------------------------------------------------------------------------------- |
| `clientId` | `string` | A short application identifier that Cash App uses to attribute API calls to your integration. |

### addEventListener

`Pay` exposes an `addEventListener` method that listens for events throughout the lifecycle of paying.

```js
pay.addEventListener('CUSTOMER_REQUEST_APPROVED', (data) => {});
```

#### Parameters

| Name       | Type                                                                                                                                                | Description   |
| :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ |
| `type`     | `"CUSTOMER_INTERACTION"` \| `"CUSTOMER_DISMISSED"` \| `"CUSTOMER_REQUEST_APPROVED"` \| `"CUSTOMER_REQUEST_DECLINED"` \| `"CUSTOMER_REQUEST_FAILED"` | event type    |
| `listener` | `PayEventListener`                                                                                                                                  | event handler |

**PayEventListener**: (`data`: `PayEventData`) => `void`

The `"CUSTOMER_REQUEST_DECLINED"` and `"CUSTOMER_REQUEST_FAILED"` events will not receive data.

**PayEventData**: `CustomerInteractionData` | `CustomerRequestData`

##### CustomerInteractionData

| Name       | Type      | Description                                                                               |
| :--------- | :-------- | :---------------------------------------------------------------------------------------- |
| `isMobile` | `boolean` | Value is `true` if the customer is using a mobile device where Cash App can be installed. |

##### CustomerRequestData

| Name              | Type                                          | Description                                                                       |
| :---------------- | :-------------------------------------------- | :-------------------------------------------------------------------------------- |
| `customerProfile` | `Customer`                                    | [Customer](/cash-app-pay-partner-api/api-reference/network-api/retrieve-customer) |
| `grants`          | `Partial<Record<keyof Actions, GrantDetail>>` | A map of actions to details about a grant                                         |
| `referenceId`     | `string`                                      | A reference to your system (for example, a cart or checkout identifier)           |

##### Customer

The Customer who approved the request.

| Name      | Type     | Description                                                                                                |
| :-------- | :------- | :--------------------------------------------------------------------------------------------------------- |
| `cashtag` | `string` | Public identifier for the customer on Cash App. [Learn more](https://cash.app/help/us/en-us/3123-cashtags) |
| `id`      | `string` | Unique identifier for this customer issued by Cash App.                                                    |

##### Grants

The map of action to details about a grant may have keys `payment` or `onFile` (same as `Actions` below). `GrantDetail` has the following properties:

| Name        | Type     | Description                                                                                                             |
| :---------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| `expiresAt` | `Date`   | When the grant will expire, at which point, you will need to create a new Customer Request.                             |
| `grantId`   | `string` | ID of Grant that can be used to [create a payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment). |

#### Returns

`void`

***

### removeEventListener

`Pay` exposes a `removeEventListener` method that removes an event listener previously registered with `addEventListener`.

```js
const createPayment = ({ grants }) => {
  // create your payment with the grant
};

pay.addEventListener('CUSTOMER_REQUEST_APPROVED', createPayment);

// when your application needs to destroy, teardown, unmount, etc.
pay.removeEventListener('CUSTOMER_REQUEST_APPROVED', createPayment);
```

#### Parameters

| Name       | Type                                                                                                                                                | Description   |
| :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :------------ |
| `type`     | `"CUSTOMER_INTERACTION"` \| `"CUSTOMER_DISMISSED"` \| `"CUSTOMER_REQUEST_APPROVED"` \| `"CUSTOMER_REQUEST_DECLINED"` \| `"CUSTOMER_REQUEST_FAILED"` | event type    |
| `listener` | PayEventListener                                                                                                                                    | event handler |

#### Returns

`void`

***

### customerRequest

`Pay` exposes a `customerRequest` method that creates a [Customer Request](/cash-app-pay-partner-api/api-reference/customer-request-api/create-request) with one or more actions. You'll need a [Merchant](/cash-app-pay-partner-api/api-reference/network-api/create-merchant) to create a payment.

```js
await pay.customerRequest({
  actions: {
    payment: {
      amount: {
        currency: 'USD',
        value: 1234, // $12.34
      },
      scopeId: 'merchant_id_from_network_api',
    },
  },
  redirectURL: window.location.href, // where mobile customers should be redirected to
  referenceId: 'your_reference_id', // perhaps a cart or checkout identifier
});
```

#### Parameters

The `customerRequest` method takes a `CustomerRequestDetails` object as its only argument. It has the following properties:

| Name                     | Type      | Description                                                                                                                 |
| :----------------------- | :-------- | :-------------------------------------------------------------------------------------------------------------------------- |
| `actions`                | `Actions` | Actions the customer will allow the merchant to perform.                                                                    |
| `redirectURL`            | `string`  | The destination for the customer after approving (or declining) in Cash App for mobile redirect flow. Must be a secure URL. |
| `referenceId` (optional) | `string`  | A reference to your system (for example, a cart or checkout identifier). Maximum length 1024 characters.                    |

**Actions** is an object with optional `onFile` and `payment` properties, but at least one must exist.

##### onFile

| Name                 | Type     | Description                                                             |
| :------------------- | :------- | :---------------------------------------------------------------------- |
| `scopeId`            | `string` | ID of the client or brand account that will charge Customers.           |
| `accountReferenceId` | `string` | Identifier of the account or Customer associated to the on-file action. |

##### payment

| Name                | Type     | Description                                                                  |
| :------------------ | :------- | :--------------------------------------------------------------------------- |
| `amount` (optional) | `Amount` | The amount to charge the customer.                                           |
| `scopeId`           | `string` | The ID of the client, brand, or merchant account that will charge customers. |

###### Amount

Amount to charge the customer.

| Name       | Type     | Description                                                              |
| :--------- | :------- | :----------------------------------------------------------------------- |
| `currency` | `string` | "USD" is currently the only accepted value.                              |
| `value`    | `number` | The lowest unit of the associated currency (for example, cents for USD). |

#### Returns

`Promise<CustomerRequestController>`

##### CustomerRequestController

`CustomerRequestController` controls the Customer Request.

```js
const details = { referenceId: 'initial', redirectURL: '...', actions: { ... } };
const { update } = await pay.customerRequest(details)

details.referenceId = 'final'

const success = await update(details)
if (success) {
  // continue creating payment with latest details
} else {
  // creating payment could possibly fail if a more complex change was made to `details`
}
```

###### update

The `update` method will update your Customer Request. The same validation applies (for example, must have at least one action) except `redirectURL` cannot be changed.

| Name      | Type                     | Description                                        |
| :-------- | :----------------------- | :------------------------------------------------- |
| `details` | `CustomerRequestDetails` | New value for the details of the Customer Request. |

Returns `Promise<boolean>` to indicate if the update was successful. An example of when an update would not be successful is if the Customer Request has already been approved.

***

### render

`Pay` exposes a `render` method that renders a managed Cash App Pay UI into your DOM.

```js
await pay.render('#cash-app-pay');
```

#### Parameters

| Name                 | Type                      | Description                                           |
| :------------------- | :------------------------ | :---------------------------------------------------- |
| `target`             | `string` \| `HTMLElement` | The location to insert Cash App Pay's UI in your DOM. |
| `options` (optional) | `RenderOptions`           | See details about `RenderOptions` below.              |

**RenderOptions** is an object with these optional properties:

| Name     | Type                       | Description                                                                                                                         |
| :------- | :------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| `button` | `ButtonOptions` \| `false` | See details about `ButtonOptions` below. If `false`, no button will be rendered, and you should provide your own.                   |
| `manage` | `boolean`                  | If `true`, Pay Kit will manage beginning the authorization flow. See `RenderController` below for more details. Defaults to `true`. |

**ButtonOptions** is an object with these optional properties:

| Name    | Type                       | Description                                                |
| :------ | :------------------------- | :--------------------------------------------------------- |
| `shape` | `"round"` \| `"semiround"` | The shape of the Cash App Pay button. Defaults to "round"  |
| `size`  | `"medium"` \| `"small"`    | The size of the Cash App Pay button. Defaults to "medium"  |
| `theme` | `"dark"` \| `"light"`      | The theme of the Cash App Pay button. Defaults to "dark"   |
| `width` | `"full"` \| `"static"`     | The width of the Cash App Pay button. Defaults to "static" |

#### Returns

`Promise<RenderController>`

##### RenderController

`RenderController` can control rendering.

###### begin

The `begin` method will begin the authorization flow for the customer if the `manage` option was `false`. Otherwise, it is a no-op. To use your own button and control the flow, you must set both `manage` and `button` to `false`.

```js
const { begin } = await pay.render('#cash-app-pay', {
  button: false,
  manage: false,
});

document.querySelector('#my-checkout-button').addEventListener('click', () => {
  // NB: a customer may be redirected away from your page
  begin();
});
```

###### destroy

The `destroy` method will remove the Cash App Pay UI from your DOM.

```js
const { destroy } = await pay.render('#cash-app-pay');

// when your application needs to teardown, unmount, etc.
destroy();
```

### restart

`Pay` exposes a `restart` method that removes all rendered UI as well as the current customer request.

In a single page app,`pay.restart()` must be called whenever the buyer leaves the checkout page. You can only make a new customer request after restart, if the current customer request is approved.

```js
await pay.restart();
```

#### Parameters

None

#### Returns

`void`

## Custom elements

Pay Kit provides [custom elements](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_custom_elements) to help customize checkout experiences while making it easy to follow brand guidelines.

### Logo

The `<cash-app-pay-logo>` element renders the Cash App Pay logo and can be customized with two attributes:

| Name  | Type                    | Description            |
| :---- | :---------------------- | :--------------------- |
| size  | `"medium"` \| `"small"` | The size of the logo.  |
| theme | `"dark"` \| `"light"`   | The theme of the logo. |

### Customer

The `<cash-app-pay-customer>` element renders the Cash App Pay logo and a customer's \$Cashtag. The `cashtag` attribute is required and will be automatically truncated if needed. The element will grow to fill its parent container.

```html
<cash-app-pay-customer cashtag="$jack" />
```
