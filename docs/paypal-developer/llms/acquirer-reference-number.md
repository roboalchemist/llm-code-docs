# Track transactions using an acquirer reference number

The acquirer reference number (ARN) is a unique value assigned to a credit or debit card transaction after the card has been processed. The ARN tracks the transaction's movement, which helps card brands, card issuing banks, and processors locate the transaction and confirm its handling.

Customers can use the ARN to confirm that a refund was processed. If you provide your customer with the ARN, their bank can trace the transaction using this value. The ARN is passed as part of the response object.

Without an ARN, if a customer's card has been lost, stolen, or closed since the original transaction, the issuing bank can have trouble routing a refund to the customer's account. When this happens, the bank reroutes the money to the appropriate account, mails the customer a check, or returns the money to your merchant account.

## Know before you code

### This integration requires an Expanded Checkout integration.

## Availability

This integration is available:

- In the US, UK, Canada, Australia, and the EU.
- For credit and debit card purchases, including those made with digital wallets or mobile devices.

You can retrieve the ARN for orders, captured payments, or refunded transactions. Make a GET call to the `v2/checkout/orders/ORDER-ID`, `v2/payments/captures/CAPTURE-ID`, or `v2/payments/refunds/REFUND-ID` endpoints to retrieve a transaction's ARN. If the ARN is available, it is listed in the response.

**Note:** After you capture a payment or refund a transaction, the ARN is available after a few days.

### Orders API

API endpoint used: [Show order details](https://developer.paypal.com/docs/api/orders/v2/#orders_get)

#### Sample request

```curl
"request": {
"method": "GET",
"path": "v2/checkout/orders/ORDER-ID?fields=payment_source",
"headers": {
  "Authorization: Bearer ACCESS-TOKEN"
}
},
```

#### Sample response

```curl
"response": {
    "status": "200 OK",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": {
        "id": "5O190127TN364715T",
        "status": "COMPLETED",
        "intent": "CAPTURE",
        "payment_source": {
            "card": {
                "last_digits": "2643",
                "expiry": "2021-01",
                "brand": "VISA"
            }
        },
        "purchase_units": [
            {
                "reference_id": "REFERENCE-ID",
                "amount": {
                    "currency_code": "USD",
                    "value": "107.14",
                    "breakdown": {
                        "item_total": {
                            "currency_code": "USD",
                            "value": "107.14"
                        },
                        "shipping": {
                            "currency_code": "USD",
                            "value": "0.00"
                        },
                        "handling": {
                            "currency_code": "USD",
                            "value": "0.00"
                        },
                        "tax_total": {
                            "currency_code": "USD",
                            "value": "0.00"
                        },
                        "shipping_discount": {
                            "currency_code": "USD",
                            "value": "0.00"
                        }
                    }
                },
                "description": "Description of PU1",
                "custom_id": "custom_id_1001",
                "soft_descriptor": "PP*soft_descr_107.14",
                "payments": {
                    "captures": [
                        {
                            "id": "CAPTURE-ID",
                            "status": "COMPLETED",
                            "amount": {
                                "currency_code": "USD",
                                "value": "107.14"
                            },
                            "seller_protection": {
                                "status": "NOT_ELIGIBLE"
                            },
                            "final_capture": true,
                            "network_transaction_reference": {
                                "id": "TRANSACTION-ID",
                                "network": "VISA",
                                "acquirer_reference_number": "ACQUIRER-REFERENCE-NUMBER"
                            },
                        }
                    ],
                    "refunds": [
                        {
                            "id": "REFUND-ID",
                            "status": "COMPLETED",
                            "amount": {
                                "currency_code": "USD",
                                "value": "107.14"
                            },
                            "note": "Defective product",
                            "acquirer_reference_number": "ACQUIRER-REFERENCE-NUMBER",
                }
            ]
        ],
        "payer": {
            "name": {
                "given_name": "Firstname",
                "surname": "Lastname"
            },
            "email_address": "customer@example.com",
            "payer_id": "PAYER-ID",
            "phone": {
                "phone_number": {
                    "country_code": "1",
                    "national_number": "18882211161"
                }
            },
            "address": {
                "address_line_1": "123 Main St",
                "address_line_2": "Suite 1",
                "admin_area_2": "Anytown",
                "admin_area_1": "CA",
                "postal_code": "12345",
                "country_code": "US"
            }
        },
        "create_time": "2018-04-01T21:18:49Z",
        "update_time": "2018-04-01T21:20:49Z",
        "links": [
            {
                "href": "https://api-m.paypal.com/v2/checkout/orders/5O190127TN364715T",
                "rel": "self",
                "method": "GET"
            }
        ]
    }
}
```

**Step result**

A successful request results in the following:

- A return status code of HTTP 200 OK.
- A JSON response body that contains the ARN.

### Refund API

API endpoint used: [Show refund details](/docs/api/payments/v2/#refunds_get)

#### Sample request

```curl
"request": {
"method": "GET",
"path": "v2/payments/refunds/REFUND-ID",
"headers": {
  "Authorization: Bearer ACCESS-TOKEN"
}
},
```

#### Sample response

```curl
"response": {
    "status": "200 OK",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": {
        "id": "REFUND-ID",
        "amount": {
            "value": "10.99",
            "currency_code": "USD"
        },
        "status": "COMPLETED",
        "note_to_payer": "Defective product",
        "seller_payable_breakdown": {
            "gross_amount": {
                "value": "10.99",
                "currency_code": "USD"
            },
            "paypal_fee": {
                "value": "0",
                "currency_code": "USD"
            },
            "net_amount": {
                "value": "10.99",
                "currency_code": "USD"
            },
            "total_refunded_amount": {
                "value": "10.99",
                "currency_code": "USD"
            }
        },
        "acquirer_reference_number": "ACQUIRER-REFERENCE-NUMBER",
        "invoice_id": "INVOICE-123",
        "create_time": "2023-05-11T23:24:19Z",
        "update_time": "2023-05-11T23:24:19Z",
        "links": [{
                "rel": "self",
                "method": "GET",
                "href": "https://api-m.paypal.com/v2/payments/refunds/1JU08902781691411"
            },
            {
                "rel": "up",
                "method": "GET",
                "href": "https://api-m.paypal.com/v2/payments/captures/2GG279541U471931P"
            }
        ]
    }
}
```

**Step result**

A successful request results in the following:

- A return status code of HTTP 200 OK.
- A JSON response body that contains the ARN.

### Capture API

API endpoint used: [Show captured payment details](https://developer.paypal.com/docs/api/payments/v2/#captures_get)

#### Sample request

```curl
"request": {
"method": "GET",
"path": "v2/payments/captures/CAPTURE-ID",
"headers": {
  "Authorization: Bearer ACCESS-TOKEN"
}
},
```

#### Sample response

```curl
"response": {
    "status": "200 OK",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": {
        "id": "CAPTURE-ID",
        "status": "COMPLETED",
        "amount": {
            "value": "10.99",
            "currency_code": "USD"
        },
        "final_capture": true,
        "network_transaction_reference": {
            "id": "REFERENCE-ID",
            "network": "VISA",
            "acquirer_reference_number": "ACQUIRER-REFERENCE-NUMBER"
        },
        "seller_protection": {
            "status": "ELIGIBLE",
            "dispute_categories": [
                "ITEM_NOT_RECEIVED",
                "UNAUTHORIZED_TRANSACTION"
            ]
        },
        "seller_receivable_breakdown": {
            "gross_amount": {
                "value": "10.99",
                "currency_code": "USD"
            },
            "paypal_fee": {
                "value": "0.33",
                "currency_code": "USD"
            },
            "net_amount": {
                "value": "10.66",
                "currency_code": "USD"
            }
        },
        "invoice_id": "INVOICE-123",
        "processor_response": {
            "avs_code": "A",
            "cvv_code": "M",
            "response_code": "0000"
        },
        "supplementary_data": {
            "related_ids": {
                "order_id": "ORDER-ID"
            }
        },
        "create_time": "2017-09-11T23:24:01Z",
        "update_time": "2017-09-11T23:24:01Z",
        "links": [{
                "href": "https://api-m.paypal.com/v2/payments/captures/2GG279541U471931P",
                "rel": "self",
                "method": "GET"
            },
            {
                "href": "https://api-m.paypal.com/v2/payments/captures/2GG279541U471931P/refund",
                "rel": "refund",
                "method": "POST"
            },
            {
                "href": "https://api-m.paypal.com/v2/payments/authorizations/0VF52814937998046",
                "rel": "up",
                "method": "GET"
            }
        ]
    }
}
```

**Step result**

A successful request results in the following:

- A return status code of HTTP 200 OK.
- A JSON response body that contains the ARN.