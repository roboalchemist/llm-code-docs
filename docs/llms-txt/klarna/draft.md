# Source: https://docs.klarna.com/conversion-boosters/express-checkout/integrate-express-checkout/integrate-one-step-express-checkout/draft.md

# How to integrate Express checkout

## Follow this guide to integrate Express checkout.

Currently there are two (2) supported integration paths for Klarna Express Checkout:

1.  [Version New integration method](https://docs.klarna.com/conversion-boosters/express-checkout/integrate-express-checkout/integrate-one-step-express-checkout.md), Express Checkout has just been added to the new Klarna Web SDK
2.  [Version Previous integration method](https://docs.klarna.com/conversion-boosters/express-checkout/integrate-express-checkout/integrate-one-step-express-checkout.md) using Klarna Payments library.

With the new integration method, you’ll get access to the latest Express Checkout features such as **Shipping Options**, which allows you to let customers choose their preferred shipping method right within Express Checkout. If you are integrating Express Checkout for the first time, it is recommended you follow the latest integration path available to get access to the latest features available. Alternatively, If you’ve been using the previous integration with the Klarna Payments library, don’t worry—it’s still supported and might be a better fit depending on your needs. Currently, only the previous integration method supports the multi-step flow, but don’t worry; this feature will soon be available in the new Klarna Web SDK too.

## Current version

## Overview

The simplest and fastest way to start using **Express checkout** is to use the minimal template below. Please refer to the [Before you start](https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start.md) article for instructions on how to obtain your `CLIENT_ID` .

```html
<html>
<head>
<!-- 
      1. Add SDK with `defer` attribute 
      to ensure DOM creation was finished. 
  -->
<script defer="" src="https://js.klarna.com/web-sdk/v2/klarna.js">
</script>
<!-- 
      2. Implement KlarnaSDKCallback
      to add the Express checkout button and
      handle events.
  -->
<script>
    window.KlarnaSDKCallback = async function () {
      // 2.1 Initiate the SDK
      const klarna = await Klarna.init({
        clientId: "klarna_live_client_elZGI1B5dHBIRWcjZrNldnbEVj[...]"
      });
      // 2.2 Create a button instance with specific configuration
      const klarnaExpressCheckout = klarna.Payment.button({
        id: "klarna-payment-button",
      });
      // 2.3 Display the button in the container
      klarnaExpressCheckout.mount("#kec-button-container");
      // 2.4 Handle click event
      klarnaExpressCheckout.on("click", (paymentRequest) => {
        return paymentRequest.initiate({
          "paymentAmount": 1000,
          "currency": "EUR",
        });
      });
    }
  </script>
</head>
<body>
<!-- 
    3. Add a container in which 
    the button should be displayed.
  -->
<div id="kec-button-container">
</div>
</body>
</html>
```

## Integration details

Learn more about each of the steps.

### Initialize SDK

Integrate Klarna's functionality by adding the SDK to your web page. You can find the library at this URL: [https://js.klarna.com/web-sdk/v2.js](https://js.klarna.com/web-sdk/v2.js). Important: Only include this script once per page to avoid any side-effects.

```html
<script defer="" src="https://js.klarna.com/web-sdk/v2/klarna.js">
</script>
```

Within your page's `<head>` tag, add the following script to initialize the Klarna Web SDK. Make sure to place the SDK interactions within the `KlarnaSDKCallback` function - this guarantees that the SDK is fully loaded and ready to use.

```javascript
<script>
  window.KlarnaSDKCallback = async function () {
    const klarna = await Klarna.init({
      clientId: "klarna_live_client_elZGI1B5dHBIRWcjZrNldnbEVj[...]"
    });
  }
</script>
```

### Display the Express checkout button

Web SDK provides the `button` method that allows to create and mount the Express checkout button programmatically.

```javascript
<script>
  window.KlarnaSDKCallback = async function () {
    const klarnaExpressCheckout = klarna.Payment.button({ 
        id: "klarna-payment-button",
        // style the button according to what the partner provided
        shape: "default",
        theme: "default"
    });
    klarnaExpressCheckout.mount("#kec-button-container");
  }
</script>
```

If the button method is called more than once with the configuration object, it will create multiple button instances. If you do not need more than one button, please make sure the button method is only called once. If you do need multiple buttons, make sure you provide an id attribute to each button instance.

### Create payment request

In Express checkout, a Payment Request represents a specific payment session. To initiate a payment, you'll need to create a Payment Request when a user clicks the "Pay with Klarna" button. To create a basic Payment Request, you'll need to provide the following information:

- **Payment Amount:** The total amount to be charged.
- **Currency:** The currency code for the transaction.

To enable specific features like shipping address collection, shipping option selection, and customer information collection, you can configure the Payment Request with additional settings. Please refer to the "Additional Features" section for more details.

```javascript
<script>
  window.KlarnaSDKCallback = async function () {
    // Handle click event
    klarnaExpressCheckout.on("click", (paymentRequest) => {
      return paymentRequest.initiate({
        "paymentAmount": 1000,
        "currency": "EUR",
        "supplementaryPurchaseData": {
          "lineItems": [
            {
              name: 'Product 1',
              quantity: 1,
              totalAmount: 1000,
              totalTaxAmount: 100
            }
          ]
        }
      }, {
        "interactionMode": "ON_PAGE"
      }
      );
    });
  }
</script>
```

| **Parameter** | **Type and description** |
|----|----|
| `currency`*required* | **Type:** string, Currency in ISO 4217 format. **Description:** Supported currencies: AUD, EUR, CAD, CZK, DKK, HUF, MXN, NZD, NOK, PLN, RON, SEK, CHF, GBP, USD. |
| `paymentAmount`*required* | **Type:** integer **Description:** Total amount of a one-off purchase, including tax and any available discounts. The value should be in non-negative minor units. Eg: 25 Dollars should be 2500. This is the amount that Klarna will charge the customer for a one-off purchase. Should not include any amounts for subscriptions. |
| `lineItems` | **Type:** object **Description:** Detailed line item information of the purchase. This data is used for fraud detection and customer communication. |
| `customer` | **Type:** object **Description:** This represents who the customer is according to the merchant. These data points may be used by Klarna to simplify sign-up and during fraud assessment, they will not be used for underwriting and will not be persisted on created Payment Transactions. |

### Confirm payment

Once the user completes the payment, you’ll receive a confirmation_token upon a successful transaction. Use this token to confirm the payment and complete the process. On the frontend, you can listen for the `update` event. When the customer successfully completes the purchase flow, the payment request’s status will change to `PENDING_CONFIRMATION`, and you can then retrieve the confirmation_token.

```javascript
klarna.Payment.on("update", async (paymentRequest) => {
  // The customer has successfully completed the payment flow and
  // the payment request can be confirmed using the confirmation token.
  if (paymentRequest.state == "PENDING_CONFIRMATION") {
    // The confirmation token is available in paymentRequest.stateContext.confirmationToken
    // Use it to confirm the payment request server side.
  }
});
```

###### *Example stateContext value*

```json
{
  "paymentRequestId": "krn:payment:eu1:request:64be490f...",
  "state": "PENDING_CONFIRMATION",
  "stateContext": {
      "state": "PENDING_CONFIRMATION",
      "shipping": {
          "recipient": {
              "givenName": "Bob",
              "familyName": "Test",
              "email": "generated_email_de+1715945998626@example.com",
              "phone": "+49123456789"
          },
          "address": {
              "country": "DE",
              "streetAddress": "Bodestr. 1-3",
              "postalCode": "10178",
              "city": "Berlin"
          }
      },
      "paymentConfirmationToken": "krn:payment:eu1:confirmation-token:91b3d170..."
  }
}
```

To confirm a payment request, provide the `confirmation_token` that was returned after a successful payment flow. Confirmation is done via the Klarna Payments endpoint, which is idempotent - meaning you can call it multiple times with the same confirmation_token and receive the same response each time. Use the following URLs:

- **Production:** [https://api-global.klarna.com/v2/accounts/{account_id}/payment/confirmation-tokens/{payment_confirmation_token}/confirm](https://api-global.klarna.com/v2/accounts/%7Baccount_id%7D/payment/confirmation-tokens/%7Bpayment_confirmation_token%7D/confirm)
- **Playground:** [https://api-global.test.klarna.com/v2/accounts/{account_id}/payment/confirmation-tokens/{payment_confirmation_token}/confirm](https://api-global.test.klarna.com/v2/accounts/%7Baccount_id%7D/payment/confirmation-tokens/%7Bpayment_confirmation_token%7D/confirm)

On this request, you must provide the `payment_confirmation_token` returned after a successful payment flow. Use the credentials from your current integration or obtain new ones from Klarna's Partner portal. `klarna_api_key` AND `klarna_partner_account` The request body follows the same format as the previously defined payment request. The data included in the confirmation call must match the information provided to the Express Checkout.

#### Payments Confirmation PATH parameters

| Parameter | Type and description |
|----|----|
| `account_id`*required* | **Type:** string (AccountIdentifier) **Description:** Identifier of the **Account** the action is done on behalf of Example: krn:partner:global:account:live:LWT2XJSE |
| `payment_confirmation_token`*required* | **Type:** string (PaymentConfirmationToken) <= 255 characters **Description:** The payment confirmation token of the Payment Request to confirmExample: krn:payment:eu1:confirmation-token:e15432a5-ebcc-45bc-944c-e61399db597b |

#### Payments Confirmation body

*application/json***application/json***

| Parameter | Type and description |
|----|----|
| `currency`_required_ | **Type:** string^[A-Za-z]{3}$ **Description:** Currency of the payment amount in 3-letter ISO 4217 currency code. Must be identical to the value in the payment request creation. |
| `payment_amount`_required_ | **Type:** string^[A-Za-z]{3}$ **Description:** Currency of the payment amount in 3-letter ISO 4217 currency code. Must be identical to the value in the payment request creation. |
| `payment_transaction_reference` | **Type:** string (PaymentTransactionReference) [ 1 .. 255 ] characters **Description:** Reference to the payment or equivalent resource created on your side. This will be exposed in the Payment Transaction webhooks for the purpose of correlating your resource with the Klarna Payment Transaction. |
| `supplementary_purchase_data` | **Type:** object **Description:** This represents additional information that provide more detailed information about the transaction, which helps reduce the risk of fraud and enhances transparency. |
| `supplementary_purchase_data.shipping` | **Type:** array of objects (Shipping) **Description:** Confirmation of shipping details if not collected by Klarna. If the details passed here do not match the details passed in the payment request the confirmation will be rejected. |
| `supplementary_purchase_data.shipping.recipient`_required_ | **Type:** object **Description:** The recipient of the shipment. |
| `supplementary_purchase_data.shipping.recipient.given_name`_required_ | **Type:** string (GivenName) [ 1 .. 99 ] characters **Description:** The given name of the person |
| `supplementary_purchase_data.shipping.recipient.family_name`_required_ | **Type:** string (FamilyName) [ 1 .. 99 ] characters **Description:** The family name of the person |
| `supplementary_purchase_data.shipping.recipient.email` | **Type:** string (Email) **Description:** E-mail address |
| `supplementary_purchase_data.shipping.recipient.phone` | **Type:** string (PhoneLocal) <= 99 characters ^(?=.*\d)[+\d\s().-]{1,99}$ **Description:** Phone number in local format |
| `supplementary_purchase_data.shipping.recipient.attention` | **Type:** string [ 1 .. 99 ] characters **Description:** Attention string for the recipient |
| `supplementary_purchase_data.shipping.address` | **Type:** object **Description:** The shipping address as provided by the customer at the merchant web site. |
| `supplementary_purchase_data.shipping.address.street_address`_required_ | **Type:** string [ 1 .. 99 ] characters **Description:** Street address, line 1 |
| `supplementary_purchase_data.shipping.address.street_address2` | **Type:** string [ 1 .. 99 ] characters **Description:** Street address, line 2 |
| `supplementary_purchase_data.shipping.address.postal_code` | **Type:** string [ 1 .. 10 ] characters **Description:** Postal code formatted according to country |
| `supplementary_purchase_data.shipping.address.city` | **Type:** string [ 1 .. 99 ] characters **Description:** City/town |
| `supplementary_purchase_data.shipping.address.region` | **Type:** string [ 1 .. 99 ] characters **Description:** State/county/province/region formatted according to country. Mandatory for US and AU market. Validations according to ISO 3166-2 format, e.g. OH, NJ, etc. |
| `supplementary_purchase_data.shipping.address.country` | **Type:** string _^[A-Za-z]{2}$_ **Description:** Country in ISO 3166-1 alpha-2 format. **Allowed countries:** AD, AE, AF, AG, AI, AL, AM, AN, AO, AQ AR, AS, AT, AU, AW, AX, AZ, BA, BB, BD BE, BF, BG, BH, BI, BJ, BL, BM, BN, BO BQ, BR, BS, BT, BV, BW, BY, BZ, CA, CC CD, CF, CG, CH, CI, CK, CL, CM, CN, CO CR, CU, CV, CW, CX, CY, CZ, DE, DJ, DK DM, DO, DZ, EC, EE, EG, EH, ER, ES, ET FI, FJ, FK, FM, FO, FR, GA, GB, GD, GE GF, GG, GH, GI, GL, GM, GN, GP, GQ, GR GS, GT, GU, GW, GY, HK, HM, HN, HR, HT HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS IT, JE, JM, JO, JP, KE, KG, KH, KI, KM KN, KP, KR, KW, KY, KZ, LA, LB, LC, LI LK, LR, LS, LT, LU, LV, LY, MA, MC, MD ME, MF, MG, MH, MK, ML, MM, MN, MO, MP MQ, MR, MS, MT, MU, MV, MW, MX, MY, MZ NA, NC, NE, NF, NG, NI, NL, NO, NP, NR NU, NZ, OM, PA, PE, PF, PG, PH, PK, PL PM, PN, PR, PS, PT, PW, PY, QA, RE, RO RS, RU, RW, SA, SB, SC, SD, SE, SG, SH SI, SJ, SK, SL, SM, SN, SO, SR, SS, ST SV, SX, SY, SZ, TC, TD, TF, TG, TH, TJ TK, TL, TM, TN, TO, TR, TT, TV, TW, TZ UA, UG, UM, US, UY, UZ, VA, VC, VE, VG VI, VN, VU, WF, WS, XK, YE, YT, ZA, ZM ZW |

###### *Example payment confirmation body*

```json
{
  "currency": "USD",
  "payment_amount": 2000,
  "payment_transaction_reference": "partner-transaction-reference-4567",
  "supplementary_purchase_data": {
    "shipping": [
      {
        "recipient": {
          "given_name": "John",
          "family_name": "Doe",
          "email": "john.doe@klarna.com",
          "phone": "844-552-7621",
          "attention": "string"
        },
        "address": {
          "street_address": "800 N. High St",
          "street_address2": "Ste. 400",
          "postal_code": "43215",
          "city": "Columbus",
          "region": "OH",
          "country": "US"
        }
      }
    ]
  },
  "config": {
    "capture": false
  }
}
```

###### *Confirmation response*

```json
{
  "payment_request_id": "krn:payment:eu1:request:552603c0-fe8b-4ab1-aacb-41d55fafbdb4",
  "state": "AUTHORIZED",
  "state_expires_at": "2024-01-01T15:00:00Z",
  "state_context": {
    "payment_transaction_id": "krn:payment:eu1:transaction:6debe89e-98c0-486e-b7a5-08a4f6df94b0",
  },
  "expires_at": "2024-01-02T13:00:00Z",
  "created_at": "2024-01-01T12:00:00Z",
  "updated_at": "2024-01-01T13:00:00Z"
}
```

`payment_transaction_id`**payment_transaction_id has a krn format, for example krn:payment:eu1:request:ccbaba75-e287-414e-98ef-34ce53975ee7.** The UUID is the `order id` that you should use with the [Order management API](https://docs.klarna.com/api/ordermanagement/#operation/getOrder).

## Additional features

To enable additional KEC features like **Shipping Address Collection**, **Shipping Options**, and **Customer Information Collection**, include the `PaymentRequestConfig` object when creating the payment request. The following sections explain how to enable and manage each feature. Note that you can activate all features simultaneously if needed.

### Request customer profile

Defines whether the integrator will receive Klarna user account data at the end of the purchase flow, as well as which specific data points will be provided. Please ensure you have a valid legal basis under GDPR or other relevant regulations to request and handle customer identity information. To enable this feature, include the config property in the object passed to the initiate function, specifying `requestCustomerProfile` with the list of required customer data fields. The following customer information is available:

- `profile:email`
- `profile:name`
- `profile:phone`
- `profile:billing_address`
- `profile:locale`
- `profile:national_identification`
- `profile:date_of_birth`

```javascript
klarnaExpressCheckout.on("click", (paymentRequest) => {
  return paymentRequest.initiate({
    "paymentAmount": 1000,
    "currency": "EUR",
    "lineItems": [
      {
        name: 'Product 1',
        quantity: 1,
        totalAmount: 1000,
        totalTaxAmount: 100
       }
    ],
    "config": {
      "requestCustomerProfile": ["profile:email", "profile:name", "profile:phone", "profile:billing_address"]
    }
  }, {
    "interactionMode": "ON_PAGE"
  }
  );
});
```

###### *Example state context value with customer data*

```json
{
  "paymentRequestId": "krn:payment:eu1:request:ccb46f6a...",
  "state": "PENDING_CONFIRMATION",
  "stateContext": {
      "shipping": {},
      "paymentConfirmationToken": "krn:payment:eu1:confirmation-token:24b36821...",
      "klarnaCustomer": {
          "customerProfile": {
              "givenName": "Bob",
              "familyName": "Test",
              "email": "generated_email_de+1715945998626@example.com",
              "phone": "+49123456789"
          }
      }
  }
}
```

### Handle shipping addresses

KEC can handle shipping address collection on behalf of the integrator. To enable this feature, include the `PaymentRequestConfig` object with the attribute `"requestShippingData": ["SHIPPING_ADDRESS"]`. If you need to restrict the countries to which you ship, include the `allowedShippingCountries` attribute with a list of permitted countries. By default, all [Klarna-supported countries](https://docs.klarna.com/resources/legal-and-compliance/policies-and-term-of-service/ethical-instructions.md) are available unless specified otherwise.

```javascript
klarnaExpressCheckout.on('click', (paymentRequest) => {
  return paymentRequest.initiate(
    {
      paymentAmount: 1000,
      currency: 'EUR',
      supplementaryPurchaseData: {
        lineItems: [
          {
            name: 'Product 1',
            quantity: 1,
            totalAmount: 1000,
            totalTaxAmount: 100,
          },
        ],
      },
      config: {
        // Enable shipping address collection
        requestShippingData: ['SHIPPING_ADDRESS'],
        // List of merchant's allowed shipping countries
        allowedShippingCountries: ['DE', 'SE'],
      },
    },
    {
      interactionMode: 'ON_PAGE',
    }
  )
})
```

### Handle shipping options

KEC can handle shipping address and shipping options collection on behalf of the integrator. To enable this feature, include the `PaymentRequestConfig` object with the attribute `"requestShippingData": ["SHIPPING_ADDRESS", "SHIPPING_OPTION"]`. Note that shipping options cannot be collected without enabling the shipping address feature. If you need to restrict the countries where you ship, include the `allowedShippingCountries` attribute with a list of allowed countries. By default, all [Klarna-supported countries](https://docs.klarna.com/resources/legal-and-compliance/policies-and-term-of-service/ethical-instructions.md) are available unless specified otherwise.

```javascript
klarnaExpressCheckout.on('click', (paymentRequest) => {
  return paymentRequest.initiate(
    {
      paymentAmount: 100,
      currency: 'EUR',
      supplementaryPurchaseData: {
        lineItems: [
          {
            name: 'Product 1',
            quantity: 1,
            totalAmount: 1000,
            totalTaxAmount: 100,
          },
        ],
      },
      config: {
        // Enable shipping options
        requestShippingData: ['SHIPPING_ADDRESS', 'SHIPPING_OPTION'],
        // List of merchant's allowed shipping countries
        allowedShippingCountries: ['DE', 'SE'],
      },
    },
    {
      interactionMode: 'ON_PAGE',
    }
  )
})
```

To enable proper functionality of the shipping options integration, you, as the integrator, need to handle two event callbacks: `shippingaddresschange` and `shippingoptionselect`. These events allow you to communicate available shipping options after an address is selected, enabling the customer to choose from the provided options. The `shippingaddresschange` event is triggered each time a customer updates their shipping address during the purchase flow. You should respond by returning a list of available shipping options for the selected address. If no response is received within 5 seconds, the purchase flow will terminate with an error. Shipping address returned has the following format.

###### *Shipping address*

```json
{
  "streetAddress": "123 Main St",
  "streetAddress2": "Apt 4B",
  "city": "Springfield",
  "postalCode": "12345",
  "region": "IL",
  "country": "USA",
  "familyName": "Doe",
  "givenName": "John"
}
```

### Success response with multiple shipping options

```javascript
klarna.Payment.on("shippingaddresschange", async (paymentRequest, shippingAddress) => {
  // Fetch the shipping options
  return {
    shippingOptions: [{
      shippingOptionReference: "shipping-option-1",
      amount: 500,
      displayName: "Shipping option 1",
      description: "1 - 2 days",
      shippingType: "TO_DOOR"
    }]
  }
})
```

### Success response with one shipping option

```javascript
klarna.Payment.on("shippingaddresschange", async (paymentRequest, shippingAddress) => {
  // Fetch the shipping options
  // if there is one preselected/default shipping option you can send the updated order payload already in this event.
  return {
    paymentAmount: 1000 + 500,
    lineItems: [
      {
        name: 'Product 1',
        quantity: 1,
        totalAmount: 5000,
        totalTaxAmount: 100
      },
      {
        name: "shipping-option-1",
        quantity: 1,
        totalAmount: 500,
      }
    ],
    selectedShippingOptionReference: "shipping-option-1",
    shippingOptions: [
      {
        shippingOptionReference: "shipping-option-1",
        amount: 500,
        displayName: "Standard shipping",
        description: "1 - 3 working days",
        shippingType: "TO_DOOR",
      },
      {
        shippingOptionReference: "shipping-option-2",
        amount: 500,
        displayName: "Express shipping",
        description: "1 working day",
        shippingType: "TO_DOOR",
      }
    ]
  }
});
```

### Rejection response

```javascript
klarna.Payment.on("shippingaddresschange", async (paymentRequest, shippingAddress) => {
  // Fetch the shipping options
  return { rejection_reason: klarna.Payment.ShippingRejectionReason.COUNTRY_NOT_SUPPORTED }
});
```

The shipping options returned must follow this format.

###### *Shipping options*

```json
[
  {
    "shippingOptionReference": "shipping-option-1",
    "amount": 500,
    "displayName": "Standard shipping",
    "description": "1 - 3 working days",
    "shippingType": "TO_DOOR"
  },
  {
    "shippingOptionReference": "shipping-option-2",
    "amount": 1000,
    "displayName": "Express shipping",
    "description": "1 working day",
    "shippingType": "TO_DOOR"
  }
]
```

The `shippingoptionselect` event is triggered every time a customer selects a different shipping option. You should return an updated order data here. If nothing was received in 5 seconds, the purchase flow will end in an error state.

### Success response

```javascript
klarna.Payment.on("shippingoptionselect", async (paymentRequest, shippingOption) => {
  /*
  {
    shippingOptionReference: "shipping-option-1"
  }
   Verify on merchant side if the sipping option is valid
  */
  const result = await fetch("https://partner-backend.com/update", {
    body: {
      shippingOption
    }
  });
  // Update the paymentRequest with new amount and line items for shipping
  return {
    paymentAmount: 1000 + 500,
    lineItems: [
      ...,
      {
        name: "shipping-option-1",
        quantity: 1,
        totalAmount: 500,
        totalTaxAmount: 10
      }
    ]
  }
});
```

### Rejection response

```javascript
klarna.Payment.on("shippingoptionselect", async (paymentRequest, shippingOption) => {
  /*
  {
    shippingOptionReference: "shipping-option-1"
  }
   Verify on merchant side if the sipping option is valid
  */
  const result = await fetch("https://partner-backend.com/update", {
    body: {
      shippingOption
    }
  });
  // return invalid option message 
  return { rejection_reason: 'INVALID_OPTION'}
});
```

## Previous version

## Integration steps

### 1. Initialize and display the Express checkout button

Load the Klarna payments JavaScript library when the cart page or a product detail page is loaded. Ensure the library is included only once to prevent conflicts.

```html
<script defer="" src="https://x.klarnacdn.net/kp/lib/v1/api.js">
</script>
```

Then, implement the `klarnaAsyncCallback` function where you initialize Express checkout. Implement the `klarnaAsyncCallback` before importing the library. This way you ensure it will be invoked when the library is loaded. Within `klarnaAsyncCallback`, include the logic to:

1.  Initialize Klarna’s JavaScript SDK providing your client identifier as `client_id`. Get your `client_id` from the Merchant portal. Refer to the [Before you start](https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start.md) article for instructions.
2.  Load the button in a chosen container using a `load()` function. To help debug any issues that occur when loading the button, implement the \[load() callback\].
3.  Handle the `on_click` event, in which you start the payment authorization process by calling the `authorize()` function. Keep the following best practices in mind:

- When initiating the authorization, make sure that the format of the `orderPayload` is the same as the body of the request [to create a Klarna payments session.](https://docs.klarna.com/api/payments/#operation/createCreditSession) 
- Always invoke the `authorize()` callback that you receive in `on_click`. 
- Avoid having multiple nested asynchronous calls before invoking authorization.

The order payload object can contain all information allowed in the Klarna payments API, for example, merchant references, merchant URLs, and extra merchant data. Here’s an example of code that initializes the Klarna JavaScript library and renders the Express checkout button on a cart or a product detail page:

```html
<script defer="" src="https://x.klarnacdn.net/kp/lib/v1/api.js">
</script>
<script>
  window.klarnaAsyncCallback = function () {
    window.Klarna.Payments.Buttons.init({
      client_id: 'klarna_client_test...',
    }).load(
    {
      container: '#container',
      theme: 'default',
      shape: 'default',
      locale: 'es-ES',
      on_click: (authorize) => {
        // Here you should invoke authorize() with the order payload.
        authorize({ auto_finalize: true, collect_shipping_address: true }, orderPayload, (result) => {
          // The result, if successful, contains authorization_token.
        })
      },
    },
    function load_callback(loadResult) {
      // Here you can handle the result of loading the button
    }
  )
}
</script>
```

The table below lists the attributes of the `load()` function’s configuration object.

| Parameter | Description |
|---------|-----------|
| `container` required | `container` represents the location where you want the Express checkout button to be displayed. In this attribute, you can specify either: * a CSS selector, for example, #my-component-id, .my-component-class * an element-type object directly, for example, document.createElement('div') |
| `on_click` required | The function passed in this attribute will be executed when the Express checkout button is clicked. It will receive the `authorize()` function, which has to be invoked to start the Express checkout flow. The `authorize()` function acts similarly to `authorize()` in a standard [Klarna payments] integration. |
| `theme` | The color theme of the button. The possible values are `default` , `light` , and `dark` . If the value isn't specified, `default` is used. |
| `shape` | The shape of the button. The possible values are `default` , `rect` , and `pill` . If the value isn't specified, `default` is used. |
| `locale` | The language of the button text. If not specified, the browser's language will be used. |

The value of `locale` passed in the `authorize()` function’s configuration object defines the language of the button text. On the other hand, the value of `locale` passed to `authorize()` inside the `orderPayload` defines the language of the purchase flow. Learn more about [locale formats](https://docs.klarna.com/api/data-types/#locale--country) in Klarna APIs. The table below lists the attributes for the `authorize()` function’s configuration object.

| **Parameters** | **Description** |
|----|----|
| `collect_shipping_address` | Informs Express checkout whether you need the customer's shipping address from Klarna. The default value is false. |
| `auto_finalize` | Allows you to specify whether the authorization should automatically be finalized when the customer clicks the Express button. In one-step Express checkout, set `auto_finalize` to true. Otherwise, the purchase won’t be authorized automatically. The default value is true. If you omit this attribute, the order will be authorized automatically. |

### 2. Handle the authorization response

If the authorization is successful, you will receive the authorization_token from the client-side `authorize()` response, in the [authorization callback](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/other-actions/authorization-callback.md), or by [getting the payment details from Klarna payments API.](https://docs.klarna.com/api/payments/#operation/readCreditSession) Here’s an example of a response from the client-side authorize() call (one-step checkout):

```json
{
  "show_form": true,
  "approved": true,
  "finalize_required": false,
  "authorization_token": "1eddf502-f3a0-45bf-b1fd-f2e3a2758200",
  "session_id": "e4b81ca2-0aae-4c16-bcb2-29a0a088a35b", 
  "collected_shipping_address": { // if collect_shipping_address was set to true
    "attention": "Attn",
    "city": "London",
    "country": "GB",
    "email": "test.sam@test.com",
    "family_name": "Andersson",
    "given_name": "Adam",
    "organization_name": "string",
    "phone": "+44795465131",
    },
    "merchant_reference1": "" // if provided
    "merchant_reference2": "" // if provided
}
```

This example shows a response from the authorization callback.

```json
{
  "authorization_token": "1eddf502-f3a0-45bf-b1fd-f2e3a2758200",
  "session_id": "e4b81ca2-0aae-4c16-bcb2-29a0a088a35b",
  "merchant_reference1": "" // if provided
  "merchant_reference2": "" // if provided
}
```

For multi-step checkout, the authorization token is not passed here. If the merchant requires this to pre-populate the checkout, as a workaround the merchant can use GET session call to retrieve the customer's shipping address.

### 3. Create an order

Once you have the `authorization_token`, [create an order](https://docs.klarna.com/api/payments/#operation/createOrder). When creating the order, make sure the shipping address provided in the API request matches the collected shipping address returned alongside the `authorization_token`*.

### 4. Handle the authorization response

If the authorization is successful, you will receive the authorization_token from the client-side `authorize()` response, in the [authorization callback](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/other-actions/authorization-callback.md), or by [getting the payment details from Klarna payments API.](https://docs.klarna.com/api/payments/#operation/readCreditSession