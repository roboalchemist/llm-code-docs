### 1\. Integrate front end

Set up your front end to integrate expanded checkout payments.

### Front-end process

1. Your app shows the PayPal card fields and payment buttons
2. Your app calls server endpoints to create the order and capture the payment. The request details depend on a number of factors, such as the type of payment method, and SDK component.

3. Set up your app to call `cardField.isEligible()` for each card field to determine if a payment is eligible for card fields. If not, the card fields won't show up during the payment flow.

4. Render each card field by declaring it as an object in `cardField` and then applying a `render()` function.

5. Create the order by calling the `createOrder` function.

6. Define styles for the card fields. You can change these styles as needed for your implementation.

7. Define the `selector` and `placeholder` values for the input fields. You can edit this section as needed for your implementation, such as adding more fields. For more information about optional configurations, see [Options in the JavaScript SDK reference](https://developer.paypal.com/sdk/js/reference/#link-options).

8. Define the `selector` and `placeholder` values for the input fields. You can edit this section as needed for your implementation, such as adding more fields. For more information about optional configurations, see [Options in the JavaScript SDK reference](https://developer.paypal.com/sdk/js/reference/#link-options).

9. Include a function that shows a message to the user by passing data to the `result-message` HTML element container of `index.html`.

10. Your app needs to call the JavaScript SDK that defines the PayPal card fields and links them to the `createOrder()` function.

If your website handles shipping physical items, [this](https://developer.paypal.com/sdk/js/reference/on-shipping-address-change) documentation includes details about our shipping callbacks.

### Step 2. Initialize JavaScript SDK

Add the JavaScript SDK to your web page and include the following:

- Your app's client ID.
- A `<div>` to render the PayPal buttons.
- A `<div>` to render each of the card fields.

The JavaScript file included in the sample code includes reference routes on the server that you’ll add in a later step.

Include the `<script>` tag on any page that shows the PayPal buttons. This script will fetch all the necessary JavaScript to access the buttons on the `window` object.

Pass a `client-id` and specify which `components` you want to use. The SDK offers Buttons, Marks, Card Fields, and other components. This sample focuses on the `buttons` component.

In addition to passing the `client-id` and specifying which `components` you want to use, you can also pass the currency you want to use for pricing. For this exercise, we'll use `USD`.

### Step 3. Customize the Card Fields OPTIONAL

This section explains how to customize the PayPal buttons and card fields for your integration.

#### Configure the layout of the card fields

- Copy and paste both [examples of card field style objects](https://developer.paypal.com/docs/checkout/advanced/customize/card-field-style/#link-examples) into your existing `src/index.html` and `src/app.js` files.
- Include the required card form elements: `card number`, `security code`, and `expiration date`. To learn about the available card form elements, see [card fields](https://developer.paypal.com/sdk/js/reference/#link-cardfields).
- Add your own fields to accept billing address information.
- A complete set of sample integration code is available from the [GitHub repo](https://github.com/paypal-examples/docs-examples/tree/main/advanced-integration/v2/).

Optional: Change the layout, width, height, and outer styling of the card fields, such as `border`, `box-shadow`, and `background`. You can modify the elements you supply as containers.

#### Style parent fields

- Style parent fields
- Style Cardholder Name field

#### Handle Billing Address

### Step 4. Configure the layout of the Buttons component OPTIONAL

Depending on where you want these buttons to show up on your website, you can lay out the buttons in a horizontal or vertical stack. You can also customize the buttons with different colors and shapes.

To override the default style settings for your page, use a `style` object inside the `Buttons` component. Read more about how to customize your payment buttons in [the style section of the JavaScript SDK reference](https://developer.paypal.com/sdk/js/reference/#style) page.

### Step 5. Integrate back end SERVER

This section explains how to set up your backend to integrate PayPal checkout payments.

The PayPal Server SDK provides integration access to the [PayPal REST APIs](https://developer.paypal.com/api/rest/). The API endpoints are divided into distinct controllers:

- Orders Controller:
  [Orders API v2](https://developer.paypal.com/docs/api/orders/v2/)
- Payments Controller:
  [Payments API v2](https://developer.paypal.com/docs/api/payments/v2/)

### Backend process

- Your app creates an order on the backend by calling to the `ordersCreate` method in the Orders Controller. See [Create Orders V2 API endpoint](https://developer.paypal.com/docs/api/orders/v2#orders_create).
- Your app calls the `ordersCapture` method in the Orders Controller on the backend to move the money when the payer confirms the order. See [Capture Payment for Order V2 API endpoint](https://developer.paypal.com/docs/api/orders/v2#orders_capture).

- Include a function that shows a message to the user by passing data to the `result-message` HTML element container of `index.html`.
- Your app needs to call the JavaScript SDK that defines the PayPal buttons and links them to the `createOrder()` function.

If your website handles shipping physical items, [this](https://developer.paypal.com/sdk/js/reference/on-shipping-address-change) documentation includes details about our shipping callbacks.

### Step 6. Test integration

Before going live, test your integration in the [sandbox environment](https://developer.paypal.com/tools/sandbox/).

Learn more about the following resources on the [Card Testing](https://developer.paypal.com/tools/sandbox/card-testing/) page:

- Use [test card numbers](https://developer.paypal.com/tools/sandbox/card-testing/#link-testcardnumbers) to simulate successful payments for expanded checkout integrations.
- Use [rejection triggers](https://developer.paypal.com/tools/sandbox/card-testing/#link-rejectiontriggers) to simulate card error scenarios.
- Test [3D Secure authentication](https://developer.paypal.com/tools/sandbox/card-testing/#link-simulate3dsecurecardpayments) scenarios.
- Test your integration by following these [recommended use cases](https://developer.paypal.com/tools/sandbox/card-testing/#link-testintegration).

### Step 7. Go live

If you have fulfilled the requirements for accepting Expanded Credit and Debit Card Payments for your [business account](https://www.paypal.com/myaccount/bundle/business/upgrade), review the [Move your app to production](https://developer.paypal.com/api/rest-production/) page to learn how to test and go live.

If this is your first time testing in a live environment, follow these steps:

- Log into the [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/) with your PayPal business account.
- Complete [production onboarding](https://www.paypal.com/unifiedonboarding/entry?country.x=US&locale.x=en_US&products=PPCP) so you can process card payments with your live PayPal business account.
- Request [Expanded Credit and Debit Card Payments](https://paypal.com/merchantapps/setup/checkout/advanced) for your business account.

### Step 8. Custom Integration

### Handle buyer checkout errors (optional)

Use `onError` callbacks and alternate checkout pages to handle buyer checkout errors.

If an error prevents buyer checkout, alert the user that an error has occurred with the buttons using the `onError` callback. This error handler is a catch-all. Errors at this point are not expected to be handled beyond showing a generic error message or page.

### Handle funding failures (optional)

If your payer's funding source fails, the Orders API returns an `INSTRUMENT_DECLINED` error.

A funding source might fail because the billing address associated with the payment method is incorrect, the transaction exceeds the card limit, or the card issuer denies the transaction. To handle this error, restart the payment so the payer can select a different payment option.

### Refund a captured payment

Refund a captured payment from a seller back to a buyer.

### Step 9. Test integration

Before going live, test your integration in the [sandbox environment](https://developer.paypal.com/tools/sandbox/).

Learn more about the following resources on the [Card Testing](https://developer.paypal.com/tools/sandbox/card-testing/) page:

- Use [test card numbers](https://developer.paypal.com/tools/sandbox/card-testing/#link-testcardnumbers) to simulate successful payments for expanded checkout integrations.
- Use [rejection triggers](https://developer.paypal.com/tools/sandbox/card-testing/#link-rejectiontriggers) to simulate card error scenarios.
- Test [3D Secure authentication](https://developer.paypal.com/tools/sandbox/card-testing/#link-simulate3dsecurecardpayments) scenarios.
- Test your integration by following these [recommended use cases](https://developer.paypal.com/tools/sandbox/card-testing/#link-testintegration).

### Step 10. Go live

If you have fulfilled the requirements for accepting Expanded Credit and Debit Card Payments for your [business account](https://www.paypal.com/myaccount/bundle/business/upgrade), review the [Move your app to production](https://developer.paypal.com/api/rest-production/) page to learn how to test and go live.

If this is your first time testing in a live environment, follow these steps:

- Log into the [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/) with your PayPal business account.
- Complete [production onboarding](https://www.paypal.com/unifiedonboarding/entry?country.x=US&locale.x=en_US&products=PPCP) so you can process card payments with your live PayPal business account.
- Request [Expanded Credit and Debit Card Payments](https://paypal.com/merchantapps/setup/checkout/advanced) for your business account.