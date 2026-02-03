# Recurring payments module

## Overview
The recurring payment module helps you display recurring payment information to the payer before they commit to the payment. This can increase payer conversion by building customer trust through transparency.

Pay with PayPal supports saving payment methods so that you can charge payers on a recurring basis through two integration patterns:

- Save payment methods for purchase later: Collect and store payment information for future transactions without processing an immediate payment.
- Save payment methods during purchase: Save payment details while simultaneously processing an initial transaction.

To learn more about how to save payment methods, review the [Save PayPal for purchase later with the JavaScript SDK](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/js-sdk/paypal/) , [Save PayPal with the Orders API](http://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/orders-api/paypal/) , or [Save PayPal with the Payment Method Tokens API](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/) .

## Eligibility
- Available for buyers and merchants in the United States.
- To save for a purchase later, integrate using the Payment Methods Tokens v3 API.
- To save with a purchase, integrate using the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/) .
- Merchant must integrate using [Save PayPal with the JavaScript SDK](https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/js-sdk/paypal/) or have a server-side, direct-API integration with Orders API to provide the save payment method during the purchase experience.
- Merchant must integrate using [Save PayPal for purchase later with the JavaScript SDK](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/js-sdk/paypal/) or have a server-side, direct-API integration with [Payment Method Tokens API](https://developer.paypal.com/docs/checkout/save-payment-methods/purchase-later/payment-tokens-api/paypal/) to provide the save payment method for a later purchase experience.
- JavaScript SDK and API-only server-side integrations are supported.

## What are recurring payments?
Recurring payments are initiated by a merchant based on a schedule or other criteria. Examples of common recurring payments are:

- Subscriptions, such as streaming media or pet food delivery.
- Automatic bill payments, such as for utilities or mobile phone bills.
- Auto reloads, such as road tolls or prepaid cards.

Recurring payments are typically classified within the industry into one of the following types:

- Subscriptions
- Recurring
- Unscheduled account on file
- Merchant managed installments

These classifications are based on whether the amount or frequency will vary between payments and whether there is a fixed or open duration.

## How it works
When a payer signs up for your service and adds PayPal as a payment method, they will go through a PayPal flow where they are authenticated and consent to a billing agreement. You can configure the PayPal flow to include a recurring payment module that shows the payer details about the billing terms on the PayPal review page.

There are two types of information that you will provide:

- Recurring payment type: This flags the payment method token for future recurring payments and tailors content in the PayPal flow to show the payer that this will be a recurring payment.
- Recurring billing plan: This shows the payer a summary of the recurring payment agreement in PayPal.

When you save a payment method without purchase, the billing plan object is payment_source.paypal.billing_plan in the Create Setup Token API call.

When you save a payment method with purchase, pass the billing plan object in the Create Order API call using the purchase_units.items[] , purchase_units.items[].billing_plan , and payment_source.paypal.attributes.vault objects. For more details, see [Save payment methods for recurring payments](https://developer.paypal.com/docs/multiparty/checkout/standard/customize/save-payment-methods-for-recurring-payments/).

## Options for providing recurring payment type and recurring billing plan
PayPal’s recurring billing plan structure is designed to support use cases from simple to complex multi-tier arrangements. It is passed using the object billing_plan .

A merchant has 3 choices regarding passing recurring payment metadata:

| Merchant options | Payer experience | Use case |
| --- | --- | --- |
| Pass usage_pattern and paypal.billing_plan.name | Recurring approval flow hosted by PayPal is initiated for the payer. They see the plan details associated with the usage_pattern, paypal.billing_plan.name, and other billing plan details. | This helps show plan information to the payer at the time of checkout. Example use case: A buyer subscribing to a $5.99/month plan with a 14-day free trial starting today. |
| Pass usage_pattern only | Recurring approval flow hosted by PayPal is initiated for the payer, but they don't see plan details. | Complex plan structures can be hard to present on the checkout screen. The buyer sees a generic recurring checkout flow that does not contain the details of the plan. The merchant must clearly communicate plan terms on their site before signup. Example use case: The consumer signs up for a hybrid plan structure that involves usage-based billing at the end of each month, with automated billing within the month when certain thresholds are met. |
| Pass neither | Recurring approval flow hosted by PayPal has not started for the payer, and they see the non-recurring PayPal-hosted approval flow. | Transactions without a recurring component are not recommended for recurring transactions. Example use case: The consumer saves their payment information for a ride-share app. |

## User action button behavior without purchase
You can use the user action setting to control the message displayed on the PayPal button on the review page. There are two options for the button messaging:

| User action | Payer experience | Use case |
| --- | --- | --- |
| Setup Now | PayPal sends the payer to the merchant’s confirmation page after approval. | Use this option for the final approval step. This setting works best for typical flows. |
| Continue | PayPal redirects the payer to the merchant’s checkout page after approval. | Use this option when the buyer needs to complete additional steps or view more pages after approval. |

## User action button behavior with purchase
| User action | Payer experience | Use case |
| --- | --- | --- |
| Pay now | The payer completes the transaction on the PayPal review page. | Use this when you want to process payment immediately, such as when the order total is already known and fixed. This reduces steps for the customer and speeds up the checkout process. |
| Continue | The payer returns to the merchant site to complete the transaction. | Use this when the final order amount may change after the payer leaves PayPal. This can present a review page before completing the transaction. |

## Use payment method token with checkout
After you create a payment method token, and the buyer agrees to a payment schedule, you can use the token to create merchant-initiated purchases and capture recurring payments with the [Create orders](https://developer.paypal.com/docs/api/orders/v2/#orders_create) endpoint of the Orders v2 API. Use this to charge your buyers for their recurring payments.

### Tokenization payment method with purchase
Store the merchant payer ID aligned with your system to simplify the mapping of payer information between your system and PayPal. This is an optional field that returns the value shared in the response.

See [Save PayPal with the Orders API](https://developer.paypal.com/docs/checkout/save-payment-methods/during-purchase/orders-api/paypal/) and [Save payment methods for recurring payments](https://developer.paypal.com/docs/checkout/standard/customize/save-payment-methods-for-recurring-payments/) for more information.

### Modify the code
- Copy the code sample.
- Change ACCESS-TOKEN to your [sandbox access token](https://developer.paypal.com/api/rest/authentication) .
- Change REQUEST-ID to a set of unique alphanumeric characters, such as a timestamp.
- Use PayPal as the payment_source . Pass additional parameters in the paypal object for your use case and business.
- Add usage_pattern under the payment_source object and pass the billing_plan details. These are the details that the payer sees on the PayPal review page.
- Update the return_url value with the URL where the payer is redirected after they approve the flow.
- Update the cancel_url value with the URL where the payer is redirected after they cancel the flow.
- Update user_action value to confirm the agreement.

### Sample API request
```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders/ 
-H "Content-Type: application/json" 
-H "Authorization: Bearer ACCESS_TOKEN" 
-d '{ 
    "intent": "CAPTURE", 
    "purchase_units": [
        {
            "amount": {
                "currency_code": "USD",
                "value": "238",
                "breakdown": {
                    "item_total": {
                        "currency_code": "USD",
                        "value": "215"
                    },
                    "shipping": {
                        "currency_code": "USD",
                        "value": "3"
                    },
                    "tax_total": {
                        "currency_code": "USD",
                        "value": "20"
                    }
                }
            },
            "items": [
                {
                    "name": "iPhone 13",
                    "description": "iPhone 13 with Verizon plan",
                    "sku": "259483234816",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "200"
                    },
                    "tax": {
                        "currency_code": "USD",
                        "value": "20"
                    },
                    "quantity": "1",
                    "category": "DIGITAL_GOODS"
                },
                {
                    "name": "Billing Plan",
                    "description": "Billing plan for subscriptions",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "15"
                    },
                    "quantity": "1",
                    "billing_plan": {
                        "name": "Verizon",
                        "setup_fee": {
                            "value": "10",
                            "currency_code": "USD"
                        },
                        "billing_cycles": [
                            {
                                "tenure_type": "REGULAR",
                                "pricing_scheme": {
                                    "price": {
                                        "value": "5",
                                        "currency_code": "USD"
                                    },
                                    "pricing_model": "FIXED"
                                },
                                "frequency": {
                                    "interval_unit": "MONTH",
                                    "interval_count": 1
                                },
                                "total_cycles": 0,
                                "sequence": 1
                            }
                        ]
                    }
                }
            ],
            "payment_source": {
                "paypal": {
                    "attributes": {
                        "vault": {
                            "store_in_vault": "ON_SUCCESS",
                            "usage_type": "MERCHANT",
                            "usage_pattern": "SUBSCRIPTION_PREPAID"
                        }
                    },
                    "experience_context": {
                        "return_url": "https://example.com/returnUrl",
                        "cancel_url": "https://example.com/cancelUrl"
                    }
                }
            }
        }
    ],
    "payment_source": {
        "paypal": {}
    },
    "links": [{
        "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/SETUP-TOKEN-ID",
        "rel": "self",
        "method": "GET",
        "encType": "application/json"
    }, {
        "href": "https://sandbox.paypal.com/agreements/approve?approval_session_id=SETUP-TOKEN-ID",
        "rel": "approve",
        "method": "GET",
        "encType": "application/json"
    }]
}
```

### Sample API response
```javascript
{
  "id": "ORDER-ID",
  "intent": "CAPTURE",
  "status": "PAYER_ACTION_REQUIRED",
  "payment_source": {},
  "purchase_units": [
    {
      "items": [
        {
          "name": "iPhone 13",
          "description": "iPhone 13 with Verizon plan",
          "sku": "259483234816",
          "unit_amount": {
            "currency_code": "USD",
            "value": "200"
          },
          "tax": {
            "currency_code": "USD",
            "value": "20"
          },
          "quantity": "1",
          "category": "PHYSICAL_GOODS"
        },
        {
          "name": "Billing Plan",
          "description": "Billing plan for subscriptions",
          "unit_amount": {
            "currency_code": "USD",
            "value": "10"
          },
          "quantity": "1",
          "billing_plan": {
            "name": "Verizon",
            "setup_fee": {
              "value": "10",
              "currency_code": "USD"
            },
            "billing_cycles": [
              {
                "tenure_type": "REGULAR",
                "pricing_scheme": {
                  "price": {
                    "value": "5",
                    "currency_code": "USD"
                  },
                  "pricing_model": "FIXED"
                },
                "frequency": {
                  "interval_unit": "MONTH",
                  "interval_count": 1
                },
                "total_cycles": 0,
                "sequence": 1
              }
            ]
          }
        }
      ],
      "amount": {
        "currency_code": "USD",
        "value": "238.00",
        "breakdown": {
          "item_total": {
            "currency_code": "USD",
            "value": "215.00"
          },
          "tax_total": {
            "currency_code": "USD",
            "value": "20.00"
          },
          "shipping": {
            "currency_code": "USD",
            "value": "3"
          }
        }
      }
    }
  ],
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER-ID",
      "rel": "self",
      "method": "GET"
    },
    {
      "href": "https://www.paypal.com/checkoutnow?token=ORDER-ID",
      "rel": "payer-action",
      "method": "GET"
    }
  ]
}
```