# Transaction Search API Integration Guide

Use the Transaction Search API to get the history of transactions from your PayPal account.

## Note
- It takes a maximum of three hours for balances to appear in the list balances call.
- This call lists balances for up to the previous three years.

## Additional Information
- [Transaction Event Codes](/docs/integration/direct/transaction-search/transaction-event-codes/)
- [Transaction Search API Reference](/docs/api/transaction-search/v1/)

---

## Set up your development environment

Before you can integrate Transaction Search, you must set up your development environment. After you get a token that lets you access protected REST API resources, you create sandbox accounts to test your web and mobile apps. For details, see [Get started](/docs/multiparty/get-started/).

Then, return to this page to integrate Transaction Search.

- Enable transaction search:
  - **Log into Dashboard** and type your PayPal business account email and password.
  - On the **My Apps & Credentials** page, toggle to **Live** or **Sandbox**, then click the link for your REST app in the **REST API apps** section.
  - Select the **Transaction Search** option in the app settings section and click **Save**.

## Endpoints

To list transactions:

```http
GET <endpoint>/v1/reporting/transactions
```

Where `endpoint` is either:

| Endpoint | Environment | Description |
| --- | --- | --- |
| https://api-m.sandbox.paypal.com | Sandbox | Test. Use your test credentials to generate an access token to make calls to the sandbox URIs. |
| https://api-m.paypal.com | Live | Production. Use your live credentials to generate an access token to make calls to the live URIs. |

In the request, you must include the HTTP `Accept`, `Accept-Language`, `Auhorization`, and `Content-Type` [request headers](/api/rest/requests/#http-request-headers).

To limit the size of and filter the transactions that appear in the response, specify one or more optional pagination and query parameters.

The API combines all pagination and query parameters with an `and` operator. The more parameters that you specify, the narrower the result set in the response. For pagination and query parameter details, see [list transactions](/docs/api/transaction-search/v1/#transactions_get).

To get the next page of results in multiple-page result sets, you must make the same request with an incremented `page` pagination parameter. Continue to increment the `page` parameter value until you get the full result set.

The maximum page size is 500. The maximum supported date range is 31 days. The maximum number of records in a single request is 10,000. If the account has more than 10,000 records for a specified date range, shorten the date range.

**Notes:**
- The Transaction Search API accepts multiple query parameters and the `page` and `page_size` pagination parameters. For general information about query and pagination parameters, see [query parameters](/api/rest/requests/#query-parameters).
- If you specify one or more optional query parameters, the `ending_balance` response field is empty.
- It takes a maximum of three hours for executed transactions to appear in the list transactions call.
- This call lists transaction for the previous three years. However, a full three years of data will not be available until July 2018 because data has only been stored since July 2016.

## List transactions

This sample request lists transactions for a specified transaction ID.

**Note:** A transaction ID is not unique in the reporting system. The response can list two transactions with the same ID. One transaction can be balance affecting while the other is non-balance affecting.

```bash
curl -v -X GET https://api-m.sandbox.paypal.com/v1/reporting/transactions?transaction_id=5TY05013RG002845M&amp;fields=all&amp;page_size=100&amp;page=1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer &lt;Access-Token&gt;"
```

Because the request includes the `fields=all` query parameters, the sample response shows all fields for the listed transaction:

```json
{
  "transaction_details": [
    {
      "transaction_info": {
        "paypal_account_id": "6STWC2LSUYYYE",
        "transaction_id": "5TY05013RG002845M",
        "transaction_event_code": "T0006",
        "transaction_initiation_date": "2014-07-11T04:03:52+0000",
        "transaction_updated_date": "2014-07-11T04:03:52+0000",
        "transaction_amount": {
          "currency_code": "USD",
          "value": "465.00"
        },
        "fee_amount": {
          "currency_code": "USD",
          "value": "-13.79"
        },
        "insurance_amount": {
          "currency_code": "USD",
          "value": "15.00"
        },
        "shipping_amount": {
          "currency_code": "USD",
          "value": "30.00"
        },
        "shipping_discount_amount": {
          "currency_code": "USD",
          "value": "10.00"
        },
        "transaction_status": "S",
        "transaction_subject": "Bill for your purchase",
        "transaction_note": "Check out the latest sales",
        "invoice_id": "Invoice-005",
        "custom_field": "Thank you for your business",
        "protection_eligibility": "01"
      },
      "payer_info": {
        "account_id": "6STWC2LSUYYYE",
        "email_address": "consumer@example.com",
        "address_status": "Y",
        "payer_status": "Y",
        "payer_name": {
          "given_name": "test",
          "surname": "consumer",
          "alternate_full_name": "test consumer"
        },
        "country_code": "US"
      },
      "shipping_info": {
        "name": "Sowmith",
        "address": {
          "line1": "Eco Space, bellandur",
          "line2": "OuterRingRoad",
          "city": "Bangalore",
          "country_code": "IN",
          "postal_code": "560103"
        }
      },
      "cart_info": {
        "item_details": [
          {
            "item_code": "ItemCode-1",
            "item_name": "Item1 - radio",
            "item_description": "Radio",
            "item_quantity": "2",
            "item_unit_price": {
              "currency_code": "USD",
              "value": "50.00"
            },
            "item_amount": {
              "currency_code": "USD",
              "value": "100.00"
            },
            "tax_amounts": [
              {
                "tax_amount": {
                  "currency_code": "USD",
                  "value": "20.00"
                }
              }
            ],
            "total_item_amount": {
              "currency_code": "USD",
              "value": "120.00"
            },
            "invoice_number": "Invoice-005"
          },
          {
            "item_code": "ItemCode-2",
            "item_name": "Item2 - Headset",
            "item_description": "Headset",
            "item_quantity": "3",
            "item_unit_price": {
              "currency_code": "USD",
              "value": "100.00"
            },
            "item_amount": {
              "currency_code": "USD",
              "value": "300.00"
            },
            "tax_amounts": [
              {
                "tax_amount": {
                  "currency_code": "USD",
                  "value": "60.00"
                }
              }
            ],
            "total_item_amount": {
              "currency_code": "USD",
              "value": "360.00"
            },
            "invoice_number": "Invoice-005"
          },
          {
            "item_name": "3",
            "item_quantity": "1",
            "item_unit_price": {
              "currency_code": "USD",
              "value": "-50.00"
            },
            "item_amount": {
              "currency_code": "USD",
              "value": "-50.00"
            },
            "total_item_amount": {
              "currency_code": "USD",
              "value": "-50.00"
            },
            "invoice_number": "Invoice-005"
          }
        ]
      },
      "store_info": {},
      "auction_info": {},
      "incentive_info": {}
    }
  ],
  "account_number": "XZXSPECPDZHZU",
  "last_refreshed_datetime": "2017-01-02T06:59:59+0000",
  "page": 1,
  "total_items": 1,
  "total_pages": 1,
  "links": [
    {
      "href": "https://api-m.sandbox.paypal.com/v1/reporting/transactions?transaction_id=5TY05013RG002845M&amp;fields=all&amp;page_size=100&amp;page=1",
      "rel": "self",
      "method": "GET"
    }
  ]
}
```

## Check balances

To check the total, available, or withheld balances of a PayPal account, specify a date and time to filter your response. You can also filter your response by currency to get a balance for each holding currency.

**Note:**

- It takes a maximum of three hours for balances to appear in the list balances call.
- This call lists balances for up to the previous three years.

```bash
curl -v -X GET https://api-m.sandbox.paypal.com/v1/reporting/balances?currency_code=USD&amp;as_of_time=2016-10-15T06:07:00-0700 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer Access-Token"
```

A successful request returns the HTTP 200 OK status code and a JSON response body that lists balances.

```json
{
  "balance": {
    "currency": "USD",
    "primary": true,
    "total_balance": {
      "currency_code": "USD",
      "value": "300.00"
    },
    "available_balance": {
      "currency_code": "USD",
      "value": "100.00"
    },
    "withheld_balance": {
      "currency_code": "USD",
      "value": "200.00"
    }
  },
  "account_id": "QCXKLSS8GWT22",
  "as_of_time": "2016-10-15T13:07:00Z",
  "last_refresh_time": "2017-02-17T05:59:59Z"
}
```

## Additional information

- [Transaction Event Codes](/docs/integration/direct/transaction-search/transaction-event-codes/)
- [Transaction Search API Reference](/docs/api/transaction-search/v1/)