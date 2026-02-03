# Pass a buyer identifier to streamline buyer login

You can pass a buyer’s email address as the buyer identifier to PayPal through the Create Order request. During one-time checkout, PayPal uses this email address to prefill the buyer's PayPal login page. This streamlines and quickens the buyer authentication process for an effortless login.

## How it works

In your app, when you [Create an order](https://developer.paypal.com/studio/checkout/standard/integrate#create-order), as part of the request body, send the buyer’s email address in the `payment_source.paypal.email_address` field. For more information, see [Create Order API](https://developer.paypal.com/docs/api/orders/v2/#orders_create!ct=application/json&path=payment_source/paypal/email_address&t=request) request.

After a successful request, the passed email address is used to prepopulate the PayPal login page when the buyer pays with PayPal.

```
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: REQUEST-ID' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-d '{ \
    "intent": "CAPTURE", \
    "payment_source": { \
        "paypal": { \
            "email_address": "customer@example.com", \
            "experience_context": { \
                "shipping_preference": "GET_FROM_FILE", \
                "user_action": "PAY_NOW", \
                "return_url": "https://example.com/returnUrl", \
                "cancel_url": "https://example.com/cancelUrl" \
            } \
        } \
    }, \
    "purchase_units": [ \
        { \
            "invoice_id": "005384", \
            "amount": { \
                "currency_code": "USD", \
                "value": "40.00" \
            } \
        } \
    ] \
}'
```

```
if (false && true && (navigator && !navigator.cookieEnabled)) { reason = 'cookies are disabled'; } else if (sessionStorage.getItem("isUserAccepted")) { reason = 'User accepted or declined'; } else if (sessionStorage.getItem("isBannerClosed")) { reason = 'Banner Closed'; } else if (sessionStorage.getItem("isInvisibleBanner")) { reason = 'Invisible banner loaded'; } } else { reason = ''; }