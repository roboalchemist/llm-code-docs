# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/additional-features/checkout-widget.mdx

***

## stoplight-id: 1bbxbjre0fz2e

# Display the checkout widget

Use the checkout widget to display the Cash App Afterpay payment schedule on your website. There are three ways to use the widget:

* **[Connected](#connected-widget):** Displayed after the checkout process, using an order token. If the order amount changes post-checkout, use the connected widget to update the payment schedule

* **[Unconnected](#unconnected-widget):** Displayed before the customer starts the checkout process, with no order token—just an amount

* **[With on file grant](#with-on-file-grant):** Displayed before the customer places the order, using an alias from a grant

The widget is responsive and can fit into any container with a minimum width of 300px. You can render the widget into a target container on your page using JavaScript.

## Connected widget

Use the connected widget on your checkout page **after** a customer completes the Cash App Afterpay checkout flow. This widget serves several purposes:

* Ensures that the customer sees and agrees to an accurate payment schedule.
* Verifies that the final amount charged matches what the customer was shown during checkout.
* Provides the merchant with important information, like the first payment amount.
* Informs the merchant if there are any barriers to purchase, such as exceeding the Cash App Afterpay payment limit.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Connected Widget.png" alt="Connected Widget.png" noZoom />

<Info title="Important">Only show the connected widget after the customer has successfully completed the Cash App Afterpay checkout (when the onComplete status is SUCCESS). You must display the connected widget during the Deferred Shipping flow.</Info>
The connected widget requires:

* The Cash App Afterpay checkout token to retrieve and render the payment schedule.
* The final order amount

```json
<html>
 <body>
   <div id="afterpay-widget-container"></div>
   <script>
     // Ensure this function is defined before loading afterpay.js
     function createAfterpayWidget () {
       window.afterpayWidget = new AfterPay.Widgets.PaymentSchedule({
         token: 'YOUR_TOKEN', // required
         amount: { amount: "123.45", currency: "USD" }, // required, amount of the total order post checkout, must be a positive value
         target: '#afterpay-widget-container',
         locale: 'en-US', 
         onReady: function (event) {
           // Fires when the widget is ready to accept updates.
           // An initial call to "update" must be made here.
         },
         onChange: function (event) {
           // Fires after each update and on any other state changes.
           // See "Getting the widget's state" for more details.
         },
         onError: function (event) {
           // See "Handling widget errors" for more details.
         },
       })
     }
   </script>
   <script src="https://portal.sandbox.afterpay.com/afterpay.js" async onload="createAfterpayWidget()">
   </script>
 </body>
</html>
```

### Capturing payment with the connected widget

Because you can update the order after checkout has completed, the connected widget has
unique considerations. When calling the /v2/payments/capture API, the payload must contain the required amount field plus additional properties. This allows Cash App Afterpay to verify that the final order amount and payment schedule match the calculated values from the corresponding order details. These properties are:

* `isCheckoutAdjusted`: Indicates whether any changes have been made to the order since the initial creation
* `items`: The list of order items if it has changed
* `shipping`: The shipping address if it has changed
* `paymentScheduleChecksum`: The latest paymentScheduleChecksum retrieved from your widget’s `onChange` call (see ‘Getting the widget’s state’).

```json
curl --request POST  
  --url <https://api-sandbox.afterpay.com/v2/payments/capture>  
  --header 'accept: application/json'  
  --header 'content-type: application/json'  
  --data '{"token":"YOUR_TOKEN", "amount":{"amount":"10.00", “currency”: USD},  "isCheckoutAdjusted":true, "shipping":{"name":"Joe Customer","line1":"123 Fake Street", "postcode":"12345", "region":"NY", "countryCode":"US"}, "items":[{"price":{"amount":"10.00", "currency":"USD"}, "name":"item1", "quantity":1}], "paymentScheduleChecksum":"YOUR_PAYMENT_SCHEDULE_CHECKSUM" }'
```

<Info title="Important">
  If the final 

  `amount`

   doesn’t match the calculated 

  `amount`

   (including shipping, taxes, etc.), or if the 

  `paymentScheduleChecksum`

   doesn’t match the calculated payment schedule, the capture request will be rejected.
</Info>

| Property                  | Type              | Description                                                                                                                          |
| ------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `token`                   | String (required) | The token returned in the Create Checkout request.                                                                                   |
| `amount`                  | Money (required)  | Amount to be checked against the amount including shipping and taxes. If the amounts do not match, the request is rejected.          |
| `merchantReference`       | String            | Order ID or reference this order corresponds to.                                                                                     |
| `isCheckoutAdjusted`      | Boolean           | Whether there have been changes to the order since the initial order creation.                                                       |
| `paymentScheduleChecksum` | String            | A unique value representing the payment schedule that must be provided when there has been changes since the initial order creation. |
| `items`                   | Item              | An array of order items that have been updated  to be provided if it has changed since the initial order creation.                   |
| `shipping`                | Contact           | The shipping address for this order to be provided if it has changed since the initial order creation.                               |

### Getting the widget's state

After each update and on any other state changes, the onChange callback is called with an HTML event argument. At this point the widget’s state is retrieved from event.data, which will have the properties in the table:

| Property                  | Type    | Description                                                                                                                                                                                                                           |
| ------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `isValid`                 | Boolean | Whether the order is okay to proceed. If false, the order should be prevented from completing.                                                                                                                                        |
| `amountDueToday`          | Money   | The amount owing today. Displaying this value in your Order Summary will give your customer more confidence when they place their order. `amountDueToday.format()` returns a formatted string that you can easily display in your UI. |
| `paymentScheduleChecksum` | String  | A unique value representing the payment schedule that must be provided when capturing the order.                                                                                                                                      |
| `error`                   | Error   | The current error state, if any.                                                                                                                                                                                                      |

We recommend using the `isValid` and `amountDueToday` states to update your checkout UI as described above, and persisting the `paymentScheduleChecksum` on your backend to be used when capturing. The widget itself informs customers what has gone wrong when `isValid` is false.

In addition to the `onChange` callback, these states are exposed as properties on the widget and can be accessed directly at any time, for example:

```
var isValid = afterpayWidget.isValid
var amountDueToday = afterpayWidget.amountDueToday
var paymentScheduleChecksum = afterpayWidget.paymentScheduleChecksum
var error = afterpayWidget.error
```

### Handling widget errors

| Property | Type                                                                    | Description                                   |
| -------- | ----------------------------------------------------------------------- | --------------------------------------------- |
| error    | [Error](/cash-app-afterpay/api-reference/reference/introduction/errors) | Representing the current error state, if any. |

Any errors on the widget trigger the `onError` callback with an HTML event (see table below), and have a false `isValid` status.

If the `onChange` callback is activated and fails due to an error, the `onError` event is also triggered for convenience. In this case, a response to `onError` events is not needed, provided all `onChange` events are handled.

#### `onError` event.data properties table

| Property  | Type                                                                    | Description                                                                                                                |
| --------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `isValid` | Boolean                                                                 | Whether the order is okay to proceed. For the `onError` event this will be **false** so prevent the order from completing. |
| `type`    | String                                                                  | For an `onError` event, the type is set to the value of **error**.                                                         |
| `error`   | [Error](/cash-app-afterpay/api-reference/reference/introduction/errors) | Represents the current error state.                                                                                        |

<Note>
  If you are getting errors during the rendering of the widget, open the browser console. The console may display some additional error loggings to help identify some common integration misconfigurations.
</Note>

## Unconnected widget

Use the unconnected widget on your checkout page **before** the customer starts the Cash App Afterpay checkout flow. This version of the widget displays an estimated payment schedule based on the initial order amount; this is only an approximation based on the initial order total.

The unconnected widget requires a defined positive `amount` to calculate the estimated payment schedule.

<img src="https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Unconnected Widget.png" alt="Unconnected Widget.png" noZoom />

If the order total changes (due to shipping method, promo code, or cart contents), the widget must be notified of the new amount. Only call the update function after the widget’s `onReady` callback has been triggered.

```json
<html>
 <body>
   <div id="afterpay-widget-container"></div>
   <script>
     // Ensure this function is defined before loading afterpay.js
     function createAfterpayWidget () {
       window.afterpayWidget = new AfterPay.Widgets.PaymentSchedule({
         amount: { amount: "123.45", currency: "USD" }, // required, must be a positive value

         target: '#afterpay-widget-container',
         locale: 'en-US', 
         onReady: function (event) {
           // Fires when the widget is ready to accept updates.
           // An initial call to "update" must be made here.
         },
         onChange: function (event) {
           // Fires after each update and on any other state changes.
           // See "Getting the widget's state" for more details.
         },
         onError: function (event) {
           // See "Handling widget errors" for more details.
         },
       })
     }
   </script>
   <script src="https://portal.sandbox.afterpay.com/afterpay.js" async onload="createAfterpayWidget()">
   </script>
 </body>
</html>
```

## With on file grant

You can use the widget when customers place an order with an existing Cash App Afterpay On File grant. This is helpful for customers, allowing them to see their payment schedule despite not going through the Cash App Afterpay checkout flow.

To display the widget:

1. First, call the Create Grant Alias endpoint [(/v2/grants/alias)](/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/alias-grant) to retrieve the payment schedule token.
2. Pass the token to the widget.
3. If there are changes to the order total, call the `updateAmount` function to update the widget.

<Info title="Considerations for cross-border trade">
  Always ensure that the currency is consistent throughout the entire checkout flow. For Cross Border Trade orders, the checkout widget displays the payment schedule and 'Due today' amounts in the customer’s currency, which may be different from the currency on your site. The capture amount must be in the same currency in which the checkout is initiated.

  For example, you are an American merchant displaying a 100 USD order in AUD for an Australian customer on your site. When you start the Cash App Afterpay checkout, if you start the checkout by sending us the order amount in USD (e.g. 100 USD), then at capture the final order amount must also be in USD.

  Likewise, if you initiate checkout by sending us the order amount in AUD post currency conversion on your side (e.g. 150 AUD), ensure that the capture amount is sent in AUD.
</Info>

## Styling the checkout widget

### Standard widget

The default version of the widget displays accurate payment schedule information, the payment amount due today, and the legal disclaimer.

Here's an example of how to initialize the standard widget, and a sample function for updating the amount to a new value.

```html
<html>
  <body>
    <div id="afterpay-widget-container"></div>
    <script>
      // Ensure this function is defined before loading afterpay.js
      function createAfterpayWidget () {
        window.afterpayWidget = new AfterPay.Widgets.PaymentSchedule({
          target: '#afterpay-widget-container',
          locale: 'en-US',
          amount: {
            amount: "1338.00",
            currency: "USD"
          },
          // Use your payment schedule token to reflect an accurate payment schedule to your customers
          paymentScheduleToken: "PAYMENT_SCHEDULE_TOKEN_PLACEHOLDER",
        })
      }

      function updateAmount() {
        window.afterpayWidget.update(
            amount: { amount: "1000.00", currency: "USD" }
        )
      }


    </script>
    <script src="https://portal.afterpay.com/afterpay.js" async onload="createAfterpayWidget()">
    </script>

    <button onclick="updateAmount()">Update amount</script>
  </body>
</html>
```

### Compact widget

This is a more compact version of the widget. It presents the same information as the standard widget, but takes up less space.

Here's an example:

```html
<html>
  <body>
    <div id="afterpay-widget-container"></div>
    <script>
      // Ensure this function is defined before loading afterpay.js
      function createAfterpayWidget () {
        window.afterpayWidget = new AfterPay.Widgets.PaymentSchedule({
          target: '#afterpay-widget-container',
          locale: 'en-US',
          amount: {
            amount: "1338.00",
            currency: "USD"
          },
          style: {
             theme: "TIMELINE"
          },
          // Use your payment schedule token to reflect an accurate payment schedule to your customers
          paymentScheduleToken: "PAYMENT_SCHEDULE_TOKEN_PLACEHOLDER",
        })
      }
    </script>
    <script src="https://portal.afterpay.com/afterpay.js" async onload="createAfterpayWidget()">
    </script>
  </body>
</html>
```

### Style attributes

There is an optional style attribute that you can use to toggle particular features on or off in the widget. The current styles are:

* `border` - If false, the border around the widget container is removed. Default: true
* `heading` - If false, the heading “Your 4 interest-free payments” is removed.  Default: true
* `logo` - If false, the Cash App Afterpay logo is removed. Default: true
* `theme` (string) - allows you to customize the look of the widget. Following themes are available ‘CLASSIC’ | ‘TIMELINE’ | ‘COLLAPSIBLE’ | ‘MODAL’. Default: ‘CLASSIC’

Here are some theme examples:

**Timeline**
![Timeline.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Timeline.png)

**Collapsible**
![collapsible.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/collapsible-3.png)

**Collapsible (extended)**
![collapsible-expanded.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/collapsible-expanded.png)

**Modal**
![Modal.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-afterpay/assets/images/Modal.png)

**Modal (open)**
!\[Modal open.png]\(../../assets/images/Modal open.png)

**Code example:**

```
window.afterpayWidget = new AfterPay.Widgets.PaymentSchedule({
  // ...
    style: {
        border: true, 
        heading: true, 
        logo: true,
        theme: ‘TIMELINE’, // ‘COLLAPSIBLE’‘MODAL’
   }
  // ...
});
```
