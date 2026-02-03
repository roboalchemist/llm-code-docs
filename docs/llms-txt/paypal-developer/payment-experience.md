# Customize Payment Flow with Payment Experience API

As a merchant, you can use the Payment Experience API to create web experience profiles to customize payment flow experiences. You can create multiple product-agnostic web experience profiles. These profiles are decoupled from the core Payments API and your general merchant profile settings and preferences, which enables you to use them across products and integration types.

When you create a payment, you can reference a web experience profile that provides your customers with a seamless experience from your merchant cart to the payment flow.

## Integration steps

| 1. | Required | [Set up your development environment](/docs/payment-experience/#set-up-your-development-environment). |
| 2. | Required | [Create web experience profile](/docs/payment-experience/#create-web-experience-profile). |
| 3. | Required | [Create PayPal payment with web profile](/docs/payment-experience/#create-paypal-payment-with-web-profile). |
| 4. | Required | [Get customer approval](/docs/payment-experience/#get-customer-approval). When a customer clicks the approval link, their payment experience is customized with your company brand, logo, and so on. |
| 5. | Optional | Make other [Payment Experience API calls](/docs/payment-experience/#other-payment-experience-api-calls). |

## Set up your development environment

Before you can integrate Payment Experience, you must set up your development environment. After you get a token that lets you access protected REST API resources, you create sandbox accounts to test your web and mobile apps. For details, see [Get started](/docs/multiparty/get-started/).

Then, return to this page to integrate Payment Experience.

## Create web experience profile

When you create a web experience profile, you provide a name for each that is unique only among your merchant profiles. You can specify these parameters in your profiles:

- [Flow configuration](/docs/payment-experience/#flow-configuration)
- [Customer fields](/docs/payment-experience/#customer-fields)
- [Style and presentation overrides](/docs/payment-experience/#style-and-presentation-overrides)

### Flow configuration

Your profile can configure these flow details:

- landing_page_type. Defines the type of page to display when a user lands on the PayPal site for checkout. You can display either the non-PayPal account landing page or the PayPal account login landing page.
- bank_txn_pending_url. Defines the URL on the merchant site to which to redirect the user after a bank transfer payment.
- return_uri_http_method. Defines the HTTP method to use to redirect the user to a return URL. Value is GET or POST.
- useraction. Defines which checkout flow to present to the buyer. You include this parameter in the URL query string. For example: https://www.paypal.com/cgi-bin/webscr?cmd=_express-checkout/useraction=commit/token=[token]
- checkout flows include:
  - Pay Now. If you set useraction=commit in the query string, the flow redirects the buyer to the PayPal payment page and displays a Pay Now button. When the buyer clicks Pay Now, call DoExpressCheckoutPayment to complete the payment without additional interaction from the buyer. Choose this flow when you know the final payment amount when you initiate the checkout flow.
  - Continue. If you omit useraction from the query string, this default flow redirects the buyer to the PayPal payment page and displays the Continue button. When the buyer clicks Continue, the buyer can edit the payment amount. Choose this flow when you do not know the final payment amount when you initiate the checkout flow.

### Customer fields

Your profile can define the behavior for these customer fields:

- allow_note. Enables a customer to enter a note to the merchant on the PayPal page during checkout.
- shipping_address. A shipping address. You can choose whether to display the customer shipping address on the payment experience pages. If you display the address, you can define from where PayPal gets the address.

### Style and presentation overrides

You can include:

- brand_name. A brand name label to override the business name in the PayPal account on the PayPal pages.
- logo_image. A URL to a logo image.
- locale_code. The locale in which to display PayPal payment experience pages.

## Example

This sample request creates a web experience profile:

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v1/payment-experience/web-profiles/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <Access-Token>" \
  -d '{ \
    "name": "ebayProfile", \
    "presentation": { \
      "logo_image": "https://www.paypal.com" \
    }, \
    "input_fields": { \
      "no_shipping": 1, \
      "address_override": 1 \
    }, \
    "flow_config": { \
      "landing_page_type": "billing", \
      "bank_txn_pending_url": "https://www.paypal.com" \
    } \
  }'
```

A successful call returns a web experience profile ID that you can reference when you create a payment:

```json
{
  "id": "XP-RFV4-PVD8-AGHJ-8E5J",
  "name": "ebayProfile",
  "temporary": false,
  "presentation": {
    "logo_image": "https://www.paypal.com"
  },
  "input_fields": {
    "no_shipping": 1,
    "address_override": 1
  },
  "flow_config": {
    "landing_page_type": "billing",
    "bank_txn_pending_url": "https://www.paypal.com"
  }
}
```

When you [create a PayPal payment](/docs/integration/direct/payments/paypal-payments/), you reference your web experience profile, by ID.

Use paypal as the payment method and pass the experience_profile_id in the JSON request body:

```curl
curl -v POST https://api-m.sandbox.paypal.com/v1/payments/payment \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <Access-Token>" \
  -d '{ \
    "intent": "authorize", \
    "experience_profile_id": "XP-RFV4-PVD8-AGHJ-8E5J", \
    "payer": { \
      "payment_method": "paypal" \
    }, \
    "transactions": [{ \
      "amount": { \
        "currency": "DKK", \
        "total": "41.15", \
        "details": { \
          "shipping": "11", \
          "subtotal": "30", \
          "tax": "0.15" \
        } \
      }, \
      "payee": { \
        "email": "merchant@example.com" \
      }, \
      "description": "This is the payment transaction description.", \
      "item_list": { \
        "items": [{ \
          "name": "Basketball Team Jersey", \
          "quantity": "5", \
          "price": "3", \
          "sku": "1", \
          "currency": "DKK" \
        }, { \
          "name": "Sequined Shirt", \
          "quantity": "1", \
          "price": "15", \
          "sku": "product34", \
          "currency": "DKK" \
        }] \
      }, \
      "shipping_address": { \
        "recipient_name": "Betsy customer", \
        "line1": "111 First Street", \
        "city": "Saratoga", \
        "country_code": "US", \
        "postal_code": "95070", \
        "phone": "0116519999164", \
        "state": "CA" \
      } \
    }] \
  }, \
  "redirect_urls": { \
    "return_url": "https://example.com", \
    "cancel_url": "https://example.com" \
  } \
}'
```

A successful call returns an approval URL:

```json
{
  "id": "PAY-51M20283MV166772CKQM3TAI",
  "create_time": "2014-09-17T16:40:33Z",
  "update_time": "2014-09-17T16:40:34Z",
  "state": "created",
  "intent": "authorize",
  "payer": {
    "payment_method": "paypal",
    "payer_info": {
      "shipping_address": {}
    }
  },
  "transactions": [{
    "amount": {
      "total": "41.15",
      "currency": "DKK",
      "details": {
        "subtotal": "30.00",
        "tax": "0.15",
        "shipping": "11.00"
      }
    },
    "description": "This is the payment transaction description.",
    "item_list": {
      "items": [{
        "name": "Basketball Team Jersey",
        "sku": "1",
        "price": "3.00",
        "currency": "DKK",
        "quantity": "5"
      }, {
        "name": "Sequined Shirt",
        "sku": "product34",
        "price": "15.00",
        "currency": "DKK",
        "quantity": "1"
      }]
    },
    "shipping_address": {
      "recipient_name": "Betsy customer",
      "line1": "111 First Street",
      "city": "Saratoga",
      "state": "CA",
      "phone": "0116519999164",
      "postal_code": "95070",
      "country_code": "US"
    }
  }],
  "links": [{
    "href": "https://api-m.sandbox.paypal.com/v1/payments/payment/PAY-51M20283MV166772CKQM3TAI",
    "rel": "self",
    "method": "GET"
  }, {
    "href": "https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout/token=EC-13203752FN674472X",
    "rel": "approval_url",
    "method": "REDIRECT"
  }, {
    "href": "https://api-m.sandbox.paypal.com/v1/payments/payment/PAY-51M20283MV166772CKQM3TAI/execute",
    "rel": "execute",
    "method": "POST"
  }]
}
```

In this sample response, the approval URL is https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout/token=EC-13203752FN674472X. Use this approval URL to get customer approval.

## Get customer approval

When you use the PayPal payment method, you redirect the payer to the approval URL.

**Note:** The approval URL is the href value associated with "rel": "approval_url" in the links object in the previous response.

When a customer clicks the approval link, their payment experience is customized with your company brand, logo, and so on. Then, you can execute or capture the payment as usual.

## Other Payment Experience API calls

Use the Payment Experience API to:

- [Show web experience profile details](/docs/api/payment-experience/v1/#web-profiles_get)
- [List web experience profiles](/docs/api/payment-experience/v1/#web-profiles_get-list)
- [Update web experience profile](/docs/api/payment-experience/v1/#web-profiles_update)
- [Partially update web experience profile](/docs/api/payment-experience/v1/#web-profiles_partial-update)
- [Delete web experience profile](/docs/api/payment-experience/v1/#web-profiles_delete)

## Additional information

- [Payment Experience API reference](/docs/api/payment-experience/v1/)