# Upgrade Your Checkout Integration

If you have previous checkout integrations, such as Express Checkout or checkout.js, PayPal recommends upgrading your integration with the [JavaScript SDK](/sdk/js/configuration/).

The JavaScript SDK has the following benefits:

- Dynamically renders payment buttons instead of using static images.
- Launches payment flow in a pop-up window instead of redirecting to a new page.
- Supports greater control over payment button styles.

**warning**
If you want to continue offering Pay Later at checkout, integrate Billing With Purchase, instead. It has the same features as Billing Agreement, but works with the payment options you already have.

## Know before you code

### Get sandbox account information
Complete the steps in [Get started](/docs/checkout/standard/upgrade-integration/) to get the following sandbox account information from the Developer Dashboard:
- Your client ID. Use your client ID when adding payment options to your website.
- Your personal and business sandbox accounts. Use sandbox accounts to test checkout options.

### Explore PayPal APIs with Postman
You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

## Payer experience
After the payer authorizes the transaction, the payment buttons call your JavaScript callback rather than redirecting the payer to a return URL.

The payer takes the following actions:
- Selects a payment button.
- Logs into PayPal.
- Approves the transaction on PayPal.
- Returns to your site where you show the payer a confirmation page.

![understanding-new-paypal-checkout-flow.svg](https://www.paypalobjects.com/devdoc/understanding-new-paypal-checkout-flow.svg)

## Add payment buttons
Add the JavaScript SDK and payment buttons to your page.

### **`Add payment buttons`**
```javascript
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Ensures optimal rendering on mobile devices. -->
</head>
<body>
    <script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID"
        // Replace YOUR_CLIENT_ID with your sandbox client ID
    ></script>
    <div id="paypal-button-container"></div>
</body>
</html>
```

### **`HTML createOrder example`**
```javascript
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <!-- Replace "TEST" with your own sandbox Business account app client ID -->
    <script src="https://www.paypal.com/sdk/js?client-id=TEST&currency=USD"></script>
    <!-- Set up a container element for the button -->
    <div id="paypal-button-container"></div>
    <script>
        paypal.Buttons({
            // Order is created on the server and the order id is returned
            createOrder() {
                return fetch("/my-server/create-paypal-order", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        // Use the "body" param to optionally pass additional order information
                        // such as product SKUs and quantities
                        body: JSON.stringify({
                            cart: [{
                                sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
                                quantity: "YOUR_PRODUCT_QUANTITY",
                            }],
                        }),
                    })
                    .then((response) => response.json())
                    .then((order) => order.id);
            }
        }).render('#paypal-button-container');
    </script>
</body>
</html>
```

### **`node.js createOrder example`**
```javascript
// For a working example, see:
// https://github.com/paypal-examples/docs-examples/tree/main/standard-integration
const {
    CLIENT_ID,
    APP_SECRET
} = process.env;
const baseURL = {
    sandbox: "https://api-m.sandbox.paypal.com",
    production: "https://api-m.paypal.com"
};
// Allow JSON body
app.use(express.json());
// Create a new order
app.post("/create-paypal-order", async(req, res) => {
    const order = await createOrder();
    res.json(order);
});
//////////////////////
// PayPal API helpers
/////////////////////////
// Use the orders API to create an order
async function createOrder() {
    const accessToken = await generateAccessToken();
    const url = `${baseURL.sandbox}/v2/checkout/orders`;
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
        body: JSON.stringify({
            intent: "CAPTURE",
            purchase_units: [{
                amount: {
                    currency_code: "USD",
                    value: "100.00",
                },
            }],
        }),
    });
    const data = await response.json();
    return data;
}
// Generate an access token using client ID and app secret
async function generateAccessToken() {
    const auth = Buffer.from(CLIENT_ID + ":" + APP_SECRET).toString("base64")
    const response = await fetch(`${baseURL.sandbox}/v1/oauth2/token`, {
        method: "POST",
        body: "grant_type=client_credentials",
        headers: {
            Authorization: `Basic ${auth}`,
        },
    });
    const data = await response.json();
    return data.access_token;
}
```

## Update script
Update the script tag to pass the [parameters you want for your integration](https://developer.paypal.com/sdk/js/configuration/), including:
- The currency of the transaction.
- The intent of the transaction.
- Whether the transaction has a **Pay Now** or a **Continue** button.
- Whether the transaction saves payment methods to the vault.

### **`HTML createOrder example`**
```javascript
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <!-- Replace "TEST" with your own sandbox Business account app client ID -->
    <script src="https://www.paypal.com/sdk/js?client-id=TEST&currency=USD"></script>
    <!-- Set up a container element for the button -->
    <div id="paypal-button-container"></div>
    <script>
        paypal.Buttons({
            // Order is created on the server and the order id is returned
            createOrder() {
                return fetch("/my-server/create-paypal-order", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        // Use the "body" param to optionally pass additional order information
                        // such as product SKUs and quantities
                        body: JSON.stringify({
                            cart: [{
                                sku: "YOUR_PRODUCT_STOCK_KEEPING_UNIT",
                                quantity: "YOUR_PRODUCT_QUANTITY",
                            }],
                        }),
                    })
                    .then((response) => response.json())
                    .then((order) => order.id);
            }
        }).render('#paypal-button-container');
    </script>
</body>
</html>
```

### **`node.js createOrder example`**
```javascript
// For a working example, see:
// https://github.com/paypal-examples/docs-examples/tree/main/standard-integration
const {
    CLIENT_ID,
    APP_SECRET
} = process.env;
const baseURL = {
    sandbox: "https://api-m.sandbox.paypal.com",
    production: "https://api-m.paypal.com"
};
// Allow JSON body
app.use(express.json());
// Capture payment & store order information or fulfill order
app.post("/capture-paypal-order", async(req, res) => {
    const {
        orderID
    } = req.params;
    const captureData = await capturePayment(orderID);
    // TODO: store payment information such as the transaction ID
    res.json(captureData);
});
//////////////////////
// PayPal API helpers
/////////////////////////
// Use the orders API to capture payment for an order
async function capturePayment(orderId) {
    const accessToken = await generateAccessToken();
    const url = `${baseURL.sandbox}/v2/checkout/orders/${orderId}/capture`;
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
    });
    const data = await response.json();
    return data;
}
// Generate an access token using client ID and app secret
async function generateAccessToken() {
    const auth = Buffer.from(CLIENT_ID + ":" + APP_SECRET).toString("base64")
    const response = await fetch(`${baseURL.sandbox}/v1/oauth2/token`, {
        method: "POST",
        body: "grant_type=client_credentials",
        headers: {
            Authorization: `Basic ${auth}`,
        },
    });
    const data = await response.json();
    return data.access_token;
}
```

## Set up transaction
When your payer selects the PayPal button, the script calls a createOrder() function that you define. In this function, return a promise for a token, payment ID, or order ID from the Orders v2 API.

**Note:** The createOrder() function in the JavaScript SDK integration replaces the payment() function in the checkout.js script.

Migrate the actions.payment.create() call to a server-side integration pattern with the create order endpoint.

API endpoint: [Create order](/docs/api/orders/v2/#orders_create)

### **`HTML captureOrder example`**
```javascript
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <!-- Replace "TEST" with your own sandbox Business account app client ID -->
    <script src="https://www.paypal.com/sdk/js?client-id=TEST&currency=USD"></script>
    <!-- Set up a container element for the button -->
    <div id="paypal-button-container"></div>
    <script>
        paypal.Buttons({
            // Finalize the transaction on the server after payer approval
            onApprove(data) {
                return fetch("/my-server/capture-paypal-order", {
                        method: "POST",
                        body: JSON.stringify({
                            orderID: data.orderID
                        })
                    })
                    .then((response) => response.json())
                    .then((orderData) => {
                        // Successful capture! For dev/demo purposes:
                        console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
                        const transaction = orderData.purchase_units[0].payments.captures[0];
                        alert(`Transaction ${transaction.status}: ${transaction.id}\\n\\nSee console for all available details`);
                        // When ready to go live, remove the alert and show a success message within this page. For example:
                        // const element = document.getElementById('paypal-button-container');
                        // element.innerHTML = '<h3>Thank you for your payment!</h3>';
                        // Or go to another URL:  window.location.href = 'thank_you.html';
                    });
            }
        }).render('#paypal-button-container');
    </script>
</body>
</html>
```

### **`node.js captureOrder example`**
```javascript
// For a working example, see:
// https://github.com/paypal-examples/docs-examples/tree/main/standard-integration
const {
    CLIENT_ID,
    APP_SECRET
} = process.env;
const baseURL = {
    sandbox: "https://api-m.sandbox.paypal.com",
    production: "https://api-m.paypal.com"
};
// Allow JSON body
app.use(express.json());
// Capture payment & store order information or fulfill order
app.post("/capture-paypal-order", async(req, res) => {
    const {
        orderID
    } = req.params;
    const captureData = await capturePayment(orderID);
    // TODO: store payment information such as the transaction ID
    res.json(captureData);
});
//////////////////////
// PayPal API helpers
/////////////////////////
// Use the orders API to capture payment for an order
async function capturePayment(orderId) {
    const accessToken = await generateAccessToken();
    const url = `${baseURL.sandbox}/v2/checkout/orders/${orderId}/capture`;
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
    });
    const data = await response.json();
    return data;
}
// Generate an access token using client ID and app secret
async function generateAccessToken() {
    const auth = Buffer.from(CLIENT_ID + ":" + APP_SECRET).toString("base64")
    const response = await fetch(`${baseURL.sandbox}/v1/oauth2/token`, {
        method: "POST",
        body: "grant_type=client_credentials",
        headers: {
            Authorization: `Basic ${auth}`,
        },
    });
    const data = await response.json();
    return data.access_token;
}
```

## Finalize payment
After your payer logs in to PayPal and approves the transaction, the script calls the onApprove() function to finalize the transaction.

**Note:** For server-side REST integrations, the onAuthorize() function from the checkout.js script is replaced by the onApprove() function in the JavaScript SDK integration.

Migrate the actions.payment.execute() to a server-side integration with the Orders Capture endpoint. For more information, see [Set up standard payments](/docs/checkout/standard/integrate/).

API endpoint: [Orders capture](/docs/api/orders/v2/#orders_capture)

### **`HTML captureOrder example`**
```javascript
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <!-- Replace "TEST" with your own sandbox Business account app client ID -->
    <script src="https://www.paypal.com/sdk/js?client-id=TEST&currency=USD"></script>
    <!-- Set up a container element for the button -->
    <div id="paypal-button-container"></div>
    <script>
        paypal.Buttons({
            // Finalize the transaction on the server after payer approval
            onApprove(data) {
                return fetch("/my-server/capture-paypal-order", {
                        method: "POST",
                        body: JSON.stringify({
                            orderID: data.orderID
                        })
                    })
                    .then((response) => response.json())
                    .then((orderData) => {
                        // Successful capture! For dev/demo purposes:
                        console.log('Capture result', orderData, JSON.stringify(orderData, null, 2));
                        const transaction = orderData.purchase_units[0].payments.captures[0];
                        alert(`Transaction ${transaction.status}: ${transaction.id}\\n\\nSee console for all available details`);
                        // When ready to go live, remove the alert and show a success message within this page. For example:
                        // const element = document.getElementById('paypal-button-container');
                        // element.innerHTML = '<h3>Thank you for your payment!</h3>';
                        // Or go to another URL:  window.location.href = 'thank_you.html';
                    });
            }
        }).render('#paypal-button-container');
    </script>
</body>
</html>
```

### **`node.js captureOrder example`**
```javascript
// For a working example, see:
// https://github.com/paypal-examples/docs-examples/tree/main/standard-integration
const {
    CLIENT_ID,
    APP_SECRET
} = process.env;
const baseURL = {
    sandbox: "https://api-m.sandbox.paypal.com",
    production: "https://api-m.paypal.com"
};
// Allow JSON body
app.use(express.json());
// Capture payment & store order information or fulfill order
app.post("/capture-paypal-order", async(req, res) => {
    const {
        orderID
    } = req.params;
    const captureData = await capturePayment(orderID);
    // TODO: store payment information such as the transaction ID
    res.json(captureData);
});
//////////////////////
// PayPal API helpers
/////////////////////////
// Use the orders API to capture payment for an order
async function capturePayment(orderId) {
    const accessToken = await generateAccessToken();
    const url = `${baseURL.sandbox}/v2/checkout/orders/${orderId}/capture`;
    const response = await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${accessToken}`,
        },
    });
    const data = await response.json();
    return data;
}
// Generate an access token using client ID and app secret
async function generateAccessToken() {
    const auth = Buffer.from(CLIENT_ID + ":" + APP_SECRET).toString("base64")
    const response = await fetch(`${baseURL.sandbox}/v1/oauth2/token`, {
        method: "POST",
        body: "grant_type=client_credentials",
        headers: {
            Authorization: `Basic ${auth}`,
        },
    });
    const data = await response.json();
    return data.access_token;
}
```