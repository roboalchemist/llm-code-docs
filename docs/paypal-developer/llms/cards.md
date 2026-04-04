# Save Cards with JavaScript SDK

If you accept cookies, we’ll use them to improve and customize your experience and enable our partners to show you personalized PayPal ads when you visit other sites. [Manage cookies and learn more](https://www.paypal.com/myaccount/privacy/cookiePrefs?_ga=1.14097599.947497879.1704302180)

After customers save their credit or debit card, they can select it for faster checkout. Customers won't have to enter payment details for future transactions.

Use the JavaScript SDK to save a payer's card if you aren't [PCI Compliant - SAQ A](https://www.pcisecuritystandards.org/pci_security/completing_self_assessment) but want to save credit or debit cards during checkout.

Set up your sandbox and live business accounts to save payment methods:

- Log in to the Developer Dashboard.
- Under **REST API apps**, select your app name.
- Under **Sandbox App Settings** \> **App Feature Options**, check **Accept payments** .
- Expand **Advanced options** . Confirm that **Vault** is selected.

Add a checkbox element grouped with your card collection fields to give payers the option to save their card.

#### **`Code`**

```javascript
<div>
  <input type="checkbox" id="save" name="save">
  <label for="save">Save your card</label>
</div>
```

Pass document.getElementById("save").checked to your server with the following details in the createOrder() method:

- Value of the checkbox
- Optional: Card name
- Optional: Billing address

#### No Verification

#### **`Code`**

```javascript
      const cardFields = paypal.CardFields({
  createOrder: async (data) => {
    // Create the order on your server and return the order ID
    const saveCheckbox = document.getElementById("save");
    return fetch("/api/paypal/order/create/", {
      method: "POST",
      body: JSON.stringify({
        // Include the saveCheckbox.checked value
        // Optionally, include the card name and billing address
      }),
    }).then((res) => {
      return res.json();
    }).then((orderData) => {
      // Return the order ID that was created on your server
      return orderData.id;
    });
  },
  onApprove: function (data) {
    // Authorize or capture the order on your server
    const { liabilityshift, orderID } = data;
      if(liabilityShift) {
         /* Handle liability shift. More information in the response parameters */
        }
    return fetch('/api/paypal/orders/${orderID}/capture/', {
      method: "POST"
    }).then((res) => {
      return res.json();
    }).then((orderData) => {
      // Retrieve vault details from the response
      const vault = orderData?.paymentSource?.card?.attributes?.vault;
      if (vault) {
        // Save the vault.id and vault.customer.id for future use
      }
      // Handle successful transaction
    });
  },
  onError: function (error) {
    // Handle any error that may occur
  }
});
if (cardFields.isEligible()) {
  cardFields.NameField().render("#card-name-field-container");
  cardFields.NumberField().render("#card-number-field-container");
  cardFields.ExpiryField().render("#card-expiry-field-container");
  cardFields.CVVField().render("#card-cvv-field-container");
} else {
  // Handle the workflow when credit and debit cards are not available
}
const submitButton = document.getElementById("submit-button");
submitButton.addEventListener("click", () => {
  cardFields
    .submit()
    .then(() => {
      // Handle successful transaction
    }).catch((error) => {
      // Handle any error that may occur
    });
});
```

#### 3D Secure
To trigger the authentication, pass the required contingency with the verification method in the create orders payload. The verification method can be contingencies parameter with SCA_ALWAYS or SCA_WHEN_REQUIRED .

SCA_ALWAYSTriggers an authentication for every transaction, whileSCA_WHEN_REQUIREDtriggers an authentication only when a regional compliance mandate such as PSD2 is required. 3D Secure is supported only in countries with a[PSD2 compliance mandate](https://www.paypal.com/uk/webapps/mpp/PSD2?_ga=1.51925228.43968804.1640649786PSD2).

#### **`Code`**
```javascript
      const cardFields = paypal.CardFields({
  createOrder: (data) => {
    // Create the order on your server and return the order ID
    const saveCheckbox = document.getElementById("save");
    return fetch("/api/paypal/order/create/", {
      method: "POST",
      body: JSON.stringify({
        // Include the saveCheckbox.checked value
        // Optionally, include the card name and billing address
        // Pass in the 3DS contingency as a verification attribute along with the payment source
        ...
          card: {
            attributes: {
              verification: {
                        method: "SCA_ALWAYS",//SCA_WHEN_REQUIRED is also another option for the verification method
                    },\n
                },\n
            experience_context: {
                shipping_preference: "NO_SHIPPING",
                return_url: "https://example.com/returnUrl",
                cancel_url: "https://example.com/cancelUrl",
              },\n
            },\n
          },
        },
      }),
    }).then((res) => {
      return res.json();
    }).then((orderData) => {
      // Return the order ID that was created on your server
      return orderData.id;
    });
  },
  onApprove: function (data) {
    // Authorize or capture the order on your server
    const { liabilityshift, orderID } = data;
      if(liabilityShift) {
         /* Handle liability shift. More information in the response parameters */
        }
    return fetch('/api/paypal/orders/${orderID}/capture/', {
      method: "POST"
    }).then((res) => {
      return res.json();
    }).then((orderData) => {
      // Retrieve vault details from the response
      const vault = orderData?.paymentSource?.card?.attributes?.vault;
      if (vault) {
        // Save the vault.id and vault.customer.id for future use
      }
      // Handle successful transaction
    });
  },
  onError: function (error) {
    // Handle any error that may occur
  }
});
if (cardFields.isEligible()) {
  cardFields.NameField().render("#card-name-field-container");
  cardFields.NumberField().render("#card-number-field-container");
  cardFields.ExpiryField().render("#card-expiry-field-container");
  cardFields.CVVField().render("#card-cvv-field-container");
} else {
  // Handle the workflow when credit and debit cards are not available
}
const submitButton = document.getElementById("submit-button");
submitButton.addEventListener("click", () => {
  cardFields
    .submit()
    .then(() => {
      // Handle successful transaction
    }).catch((error) => {
      // Handle any error that may occur
    });
});
```

#### **`Code`**
```javascript
  {
    "id": "WH-1KN88282901968003-82E75604WM969463F",
    "event_version":"1.0",
    "create_time":"2022-08-15T14:13:48.978Z",
    "resource_type":"payment_token",
    "resource_version":"3.0",
    "event_type":"VAULT.PAYMENT-TOKEN.CREATED",
    "summary":"A payment token has been created.",
    "resource":{
      "time_created":"2022-08-15T07:13:48.964PDT",
      "links":[
           {
              "href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/9n6724m",
              "rel":"self",
              "method":"GET",
              "encType":"application/json"
           },\n
           {
              "href":"https://api-m.sandbox.paypal.com/v3/vault/payment-tokens/9n6724m",
              "rel":"delete",
              "method":"DELETE",
              "encType":"application/json"
           }
        ],
      "id":"nkq2y9g",
      "payment_source":{\n\n            "card":{\n               "last_digits":"1111",\n               "brand":"VISA",\n               "expiry":"2027-02",\n               "billing_address":{\n                  "address_line_1":"123 Main St.",\n                  "address_line_2":"Unit B",\n                  "admin_area_2":"Anytown",\n                  "admin_area_1":"CA",\n                  "postal_code":"12345",\n                  "country_code":"US"\n               }\n            }\n         },\n         "customer":{\n            "id":"695922590\"\n         }\n      },\n      "links":[\n         {\n            "href":"https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1KN88282901968003-82E75604WM969463F",
            "rel":"self",
            "method":"GET"
         },\n         {\n            "href":"https://api-m.sandbox.paypal.com/v1/notifications/webhooks-events/WH-1KN88282901968003-82E75604WM969463F/resend",
            "rel":"resend",
            "method":"POST"
         }\n      ]\n  }\n\n```