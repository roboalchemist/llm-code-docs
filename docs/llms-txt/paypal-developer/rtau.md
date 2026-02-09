# Real-time account updater for direct merchants

Use real-time account updates to reduce declined card payments. Real-time account updater increases payment success by asking the card issuer for updates about the buyer's card, and applying any changes to the current card.

Use this integration guide if you are a merchant and have a direct integration with PayPal.

## What is real-time account updater?

A buyer's credit or debit card can be declined for many reasons. When a card on file expires, is lost or stolen, or changes for any other reason, payments using that saved card are declined. A declined card can interrupt or prevent a transaction and impact your relationship with that customer.

Only cards that the customer has saved on PayPal's Commerce Platform for future payments are eligible for real-time updates. When triggered, real-time account updater obtains the updated card information to use for the payment. The API response includes data about the card used to complete the payment. For details on how to save a card for future payments, visit [Save payment methods](/docs/checkout/save-payment-methods/).

Examples of payments using a card on file include:

- Recurring payments on a subscription for a service or a product.
- Online or mobile checkout using a previously saved credit or debit card.

Real-time account updater doesn't apply to mobile payments from a digital wallet, such as Apple Pay, Google Pay, and Samsung Pay.

**info**
**Note:** Even cards that qualify for real-time updates may not be updated during a transaction. [Read PayPal's Online Card Payment Services Agreement](https://www.paypal.com/us/legalhub/pocpsa-full?locale.x=en_US#pocpsa-full-11) for details.

## Eligibility

Real-time account updater is a limited early access program for all merchants with the following integrations enabled:

- [Advanced credit and debit card payments](/docs/checkout/advanced/)
- [Save payment methods](/docs/checkout/save-payment-methods/)

Real-time account updates only occur on subsequent card payments using a card on file. For examples of subsequent payment scenarios, see the [Strong Customer Authentication payment indicators page](/docs/checkout/advanced/customize/sca-payment-indicators/#link-usecases).

Real-time account updater works when issuers agree to share card updates via card networks. PayPal can’t provide a card update when the card issuer or cardholder opts out of automatic updates. When a card account doesn’t support real-time account updates, request a card update directly from the cardholder.

If you're interested in using real-time account updater, go to [our article about Real-Time Account Updater and integration](https://www.paypal.com/us/cshelp/article/what-is-real-time-account-updater-and-what-do-i-need-to-do-to-prepare-my-integration-ts2271).

## Supported countries

The following table shows the card types and countries that real-time account updater supports.

| Card network | Card type | Issuing country | Merchant country |
| --- | --- | --- | --- |
| Mastercard | Credit and debit cards | AT, AU, BE, BG, CA, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK, UK, US | AT, AU, BE, BG, CA, CN, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HU, IE, IT, LI, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK, UK, US |
| Visa | Credit and debit cards | AT, AU, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HK, HU, IE, IT, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SG, SI, SK, UK, US | AT, AU, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GR, HK, HU, IE, IT, LT, LU, LV, MT, NL, NO, PL, PT, RO, SE, SI, SK, UK, US |

## How it works

PayPal works with Mastercard and Visa to reduce declined payments using real-time account updates.

### Mastercard

When a partner or direct merchant has real-time account updater enabled for their account, PayPal checks if the card information is current and eligible for updates.

![Real-time,account,updater,workflow,for,Mastercard](https://www.paypalobjects.com/devdoc/rtau_diagram_mastercard.png)

- A merchant has a card on file that was saved for future payments with the customer's consent.
- The buyer makes a purchase using the saved card on file, or the merchant uses the card on file for a recurring payment.
- PayPal processes the payment as an advanced credit or debit transaction.
- Mastercard sends the payment to the card issuer, but the card on file has expired, has been cancelled, or is otherwise not available for payment.
- Mastercard notifies PayPal that the issuer declined the card.
- PayPal checks to see if the card on file is eligible for real-time account updater.
- PayPal sends a request to Mastercard to check whether the card's information is current.
- Mastercard confirms that the card has changed, and sends the updated card information.
- PayPal resubmits the payment on the merchant's behalf using the updated card information.
- PayPal returns the updated card information to the merchant. If the card on file was a vaulted token, PayPal updates the card on file in the PayPal Complete Payments Platform vault.

### Visa

When a partner or direct merchant has real-time account updater enabled for their account, PayPal flags the card for Visa to verify and update card information.

![Real-time,account,updater,workflow,for,Visa](https://www.paypalobjects.com/devdoc/rtau_diagram_visa.png)

- A merchant has a card on file that was saved for future payments with the customer's consent.
- The buyer makes a purchase using the saved card on file, or the merchant uses the card on file for a recurring payment.
- PayPal processes the payment as an advanced credit or debit card transaction.
- PayPal checks to see if the card on file is eligible for real-time account updater.
- PayPal flags the payment so that Visa checks for card updates.
- The card on file has expired, has been cancelled, or is otherwise not available for payment.
- If an update is available, Visa submits the payment to the issuer using the updated card information.
- After the issuer approves the payment, Visa returns the updated card information to PayPal.
- PayPal returns the updated card information to the merchant. If the card on file was a vaulted token, PayPal updates the card on file in the PayPal Complete Payments Platform vault.

**info**
**Note:** If an update isn't available, Visa submits the payment using the original card information. The issuer approves or declines the payment.

## Postman collection

[Download the Postman collection](https://www.paypalobjects.com/devdoc/postman/Targeted_RTAU_SBX_Use_Cases_Collection.postman_collection.json) for real-time account updater to test making updates to cards.

## Sample card change scenarios

This section shows how real-time account updater responds to 3 different card changes.

**info**
**Note:** The payment token id in these code samples is a placeholder. Generate and use your own payment token.

### Expired token

This sample shows what happens when a token for an expired card is used for a payment. The response returns the updated expiration date for the same card.

If you call GET /v3/vault/payment-tokens/{id} using the token before you submit the order using POST /v2/checkout/orders , the POST response includes the updated values that PayPal used to complete the payment. Compare the expiry returned by the GET call to the expiry returned by the POST call.

API endpoint: /v2/checkout/orders

### Request

```curl
{
    "intent": "CAPTURE",
    "payment_source": {
        "token": {
            "id": "0rjdehvx",
            "type": "PAYMENT_METHOD_TOKEN"
        }
    },
    "payer": {
        "name": {
            "given_name": "kakashi Hatakae",
            "surname": "user"
        },
        "address": {
            "address_line_1": "123 Main St.",
            "address_line_2": "Floor 6",
            "admin_area_2": "Anytown",
            "admin_area_1": "CA",
            "postal_code": "12345",
            "country_code": "US"
        }
    },
    "purchase_units": [
        {
            "description": "Item bought at Hemm Store",
            "custom_id": "1111",
            "soft_descriptor": "",
            "amount": {
                "currency_code": "USD",
                "value": "45.00"
            },
            "shipping": {
                "address": {
                    "address_line_1": "123 Main St.",
                    "address_line_2": "Building 17",
                    "admin_area_2": "Anytown",
                    "admin_area_1": "CA",
                    "postal_code": "12345",
                    "country_code": "US"
                }
            }
        }
    ]
}
```

### Response

```curl
{
    "id": "7YS401589T475863H",
    "status": "COMPLETED",
    "payment_source": {
        "card": {
            "last_digits": "9855",
            "expiry": "2040-12",
            "brand": "VISA",
            "type": "CREDIT"
        }
    },
    "purchase_units": [
        {
            "reference_id": "default",
            "shipping": {
                "address": {
                    "address_line_1": "123 Main St.",
                    "address_line_2": "Floor 6",
                    "admin_area_2": "Anytown",
                    "admin_area_1": "CA",
                    "postal_code": "12345",
                    "country_code": "US"
                }
            },
            "payments": {
                "captures": [
                    {
                        "id": "1MJ8142177130444J",
                        "status": "COMPLETED",
                        "amount": {
                            "currency_code": "USD",
                            "value": "45.00"
                        },
                        "final_capture": true,
                        "seller_protection": {
                            "status": "NOT_ELIGIBLE"
                        },
                        "seller_receivable_breakdown": {
                            "gross_amount": {
                                "currency_code": "USD",
                                "value": "45.00"
                            },
                            "paypal_fee": {
                                "currency_code": "USD",
                                "value": "1.66"
                            },
                            "net_amount": {
                                "currency_code": "USD",
                                "value": "43.34"
                            }
                        },
                        "custom_id": "1111",
                        "links": [
                            {
                                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/1MJ8142177130444J",
                                "rel": "self",
                                "method": "GET"
                            },
                            {
                                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/1MJ8142177130444J/refund",
                                "rel": "refund",
                                "method": "POST"
                            },
                            {
                                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/7YS401589T475863H",
                                "rel": "up",
                                "method": "GET"
                            }
                        ],
                        "create_time": "2023-03-12T17:53:18Z",
                        "update_time": "2023-03-12T17:53:18Z",
                        "processor_response": {
                            "avs_code": "A",
                            "cvv_code": "M",
                            "response_code": "0000"
                        }
                    }
                ]
            }
        }
    ],
    "links": [
        {
            "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/7YS401589T475863H",
            "rel": "self",
            "method": "GET"
        }
    ]
}
```

### Updated token

This sample shows what happens when a token for an unexpired card is used for a payment. The response returns details about the new card issued.

If you call GET /v3/vault/payment-tokens/{id} using the token before you submit the order using POST /v2/checkout/orders , the POST response includes the updated values that PayPal used to complete the payment. Compare the expiry and last_digits returned by the GET call to the values returned by the POST call.

API endpoint: /v2/checkout/orders

### Request

```curl
{
    "intent": "CAPTURE",
    "payment_source": {
        "token": {
            "id": "n3wrbawh",
            "type": "PAYMENT_METHOD_TOKEN"
        }
    },
    "payer": {
        "name": {
            "given_name": "kakashi Hatakae",
            "surname": "user"
        },
        "address": {
            "address_line_1": "123 Main St.",
            "address_line_2": "Floor 6",
            "admin_area_2": "Anytown",
            "admin_area_1": "CA",
            "postal_code": "12345",
            "country_code": "US"
        }
    },
    "purchase_units": [
        {
            "description": "Item bought at Hemm Store",
            "custom_id": "1111",
            "soft_descriptor": "",
            "amount": {
                "currency_code": "USD",
                "value": "45.00"
            },
            "shipping": {
                "address": {
                    "address_line_1": "123 Main St.",
                    "address_line_2": "Building 17",
                    "admin_area_2": "Anytown",
                    "admin_area_1": "CA",
                    "postal_code": "12345",
                    "country_code": "US"
                }
            }
        }
    ]
}
```

### Response

```curl
{
    "id": "3N479859GX821113M",
    "status": "COMPLETED",
    "payment_source": {
        "card": {
            "last_digits": "2211",
            "expiry": "2040-12",
            "brand": "MASTERCARD",
            "type": "CREDIT"
        }
    },
    "purchase_units": [
        {
            "reference_id": "default",
            "shipping": {
                "address": {
                    "address_line_1": "123 Main St.",
                    "address_line_2": "Floor 6",
                    "admin_area_2": "Anytown",
                    "admin_area_1": "CA",
                    "postal_code": "12345",
                    "country_code": "US"
                }
            },
            "payments": {
                "captures": [
                    {
                        "id": "1WA02572C51593351",
                        "status": "COMPLETED",
                        "amount": {
                            "currency_code": "USD",
                            "value": "45.00"
                        },
                        "final_capture": true,
                        "seller_protection": {
                            "status": "NOT_ELIGIBLE"
                        },
                        "seller_receivable_breakdown": {
                            "gross_amount": {
                                "currency_code": "USD",
                                "value": "45.00"
                            },
                            "paypal_fee": {
                                "currency_code": "USD",
                                "value": "1.66"
                            },
                            "net_amount": {
                                "currency_code": "USD",
                                "value": "43.34"
                            }
                        },
                        "custom_id": "1111",
                        "links": [
                            {
                                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/1WA02572C51593351",
                                "rel": "self",
                                "method": "GET"
                            },
                            {
                                "href": "https://api-m.sandbox.paypal.com/v2/payments/captures/1WA02572C51593351/refund",
                                "rel": "refund",
                                "method": "POST"
                            },
                            {
                                "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/3N479859GX821113M",
                                "rel": "up",
                                "method": "GET"
                            }
                        ],
                        "create_time": "2023-03-12T18:01:36Z",
                        "update_time": "2023-03-12T18:01:36Z",
                        "processor_response": {
                            "response_code": "0000"
                        }
                    }
                ]
            }
        }
    ],
    "links": [
        {
            "href": "https://api-m.sandbox.paypal.com/v2/checkout/orders/3N479859GX821113M",
            "rel": "self",
            "method": "GET"
        }
    ]
}
```

### Closed token

This sample shows what happens when a token for a closed card is used for a payment. The issuer no longer provides the linked card to the cardholder, so the updater can't get new token information. The response shows that the card is closed.

API endpoint: /v2/checkout/orders

### Request

```curl
{
    "intent": "CAPTURE",
    "payment_source": {
        "token": {
            "id": "09pae77b",
            "type": "PAYMENT_METHOD_TOKEN"
        }
    },
    "payer": {
        "name": {
            "given_name": "kakashi Hatakae",
            "surname": "user"
        },
        "address": {
            "address_line_1": "123 Main St.",
            "address_line_2": "Floor 6",
            "admin_area_2": "Anytown",
            "admin_area_1": "CA",
            "postal_code": "12345",
            "country_code": "US"
        }
    },
    "purchase_units": [
        {
            "description": "Item bought at Hemm Store",
            "custom_id": "1111",
            "soft_descriptor": "",
            "amount": {
                "currency_code": "USD",
                "value": "45.00"
            },
            "shipping": {
                "address": {
                    "address_line_1": "123 Main St.",
                    "address_line_2": "Building 17",
                    "admin_area_2": "Anytown",
                    "admin_area_1": "CA",
                    "postal_code": "12345",
                    "country_code": "US"
                }
            }
        }
    ]
}
```

### Response

```curl
{
    "name": "UNPROCESSABLE_ENTITY",
    "details": [
        {
            "field": "payment_source/card",
            "location": "body",
            "issue": "CARD_CLOSED",
            "description": "The card is closed."
        }
    ],
    "message": "The requested action could not be performed, semantically incorrect, or failed business validation.",
    "debug_id": "7381a9a790cc7",
    "links": [
        {
            "href": "https://developer.paypal.com/docs/api/orders/v2/#error-CARD_CLOSED",
            "rel": "information_link",
            "method": "GET"
        }
    ]
}
```