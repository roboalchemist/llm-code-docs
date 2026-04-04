# Pay another account

By default, money is paid to the application owner in their own account. The account receiving funds is known as the payee.

To specify a different payee when you create an order:

1. Add the [payee object](/docs/api/orders/v2/#definition-purchase_unit_request/) to the transaction payload.
2. Include the `email_address` or `merchant_id` of the account to receive the payment.

## Sample request

### **`Pay another account`**

```javascript
async function createOrder() {
    // Create accessToken using your clientID and clientSecret
    // For the full stack example, please see the Standard Integration guide at
    // https://developer.paypal.com/docs/checkout/standard/integrate/
    const accessToken = "REPLACE_WITH_YOUR_ACCESS_TOKEN"
    return fetch("https://api-m.sandbox.paypal.com/v2/checkout/orders", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${accessToken}`,
            },
            body: JSON.stringify({
                intent: "CAPTURE",
                purchase_units: [{
                    amount: {
                        value: "15.00",
                        currency_code: "USD",
                    },
                    payee: {
                        email_address: "payee@exmple.com",
                    },
                }],
            }),
        })
        .then((response) => response.json())
        .then((data) => console.log(data));
}
```