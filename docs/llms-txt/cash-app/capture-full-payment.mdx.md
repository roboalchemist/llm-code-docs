# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/capture-full-payment.mdx

# Capture Full Payment

POST https://global-api-sandbox.afterpay.com/v2/payments/capture
Content-Type: application/json

This endpoint makes a payment capture for the full value of the payment plan.

This operation is idempotent based on the token, which allows for the safe retry of requests, guaranteeing the payment operation is only made once.

Since the idempotency of this endpoint is based on the token, the inclusion of a `requestId` is not required.

**Connection Timeouts**
| Timeout | Time (Seconds) |
|---------|----------------|
| Open    | 10             |
| Read    | 70             |


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/capture-full-payment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/payments/capture:
    post:
      operationId: capture-full-payment
      summary: Capture Full Payment
      description: >
        This endpoint makes a payment capture for the full value of the payment
        plan.


        This operation is idempotent based on the token, which allows for the
        safe retry of requests, guaranteeing the payment operation is only made
        once.


        Since the idempotency of this endpoint is based on the token, the
        inclusion of a `requestId` is not required.


        **Connection Timeouts**

        | Timeout | Time (Seconds) |

        |---------|----------------|

        | Open    | 10             |

        | Read    | 70             |
      tags:
        - ''
      parameters:
        - name: Authorization
          in: header
          description: Basic authentication
          required: true
          schema:
            type: string
        - name: User-Agent
          in: header
          required: true
          schema:
            type: string
        - name: Accept
          in: header
          required: false
          schema:
            type: string
            default: application/json
      responses:
        '201':
          description: >
            | Status | Description |

            | ----- | ----- |

            | `APPROVED` | If payment is approved by Cash App Afterpay, returns
            a Payment object in response, with a status of "APPROVED". |

            | `DECLINED` | If payment is declined by Cash App Afterpay, for
            example, if invalid card details were entered, returns a Payment
            object in response, with a status of "DECLINED". Please advise the
            customer to contact the Cash App Afterpay Customer Service team for
            more information. |
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Payment'
        '402':
          description: >-
            The checkout token is invalid, expired, or does not exist. Error
            code `invalid_token`.
          content:
            application/json:
              schema:
                description: Any type
        '412':
          description: >-
            The Consumer has not confirmed their payment for the order
            associated with this token. Error code
            `invalid_order_transaction_status`.
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: >-
            The checkout token was missing or empty. Error code
            `invalid_object`.
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                token:
                  type: string
                  description: The token returned in the Create Checkout request.
                merchantReference:
                  type: string
                  description: >-
                    The merchant’s order id/reference that this payment
                    corresponds to. This updates any value previously provided
                    in the Create Checkout request.
                amount:
                  $ref: '#/components/schemas/Money'
                  description: >-
                    **Required for express checkout only.** Amount to be checked
                    against the value in the create checkout request. If the
                    amounts do not match, then the request is rejected and an
                    error specific to this scenario is returned. 
                isCheckoutAdjusted:
                  type: boolean
                  description: >-
                    **Express checkout only.** The isCheckoutAdjusted field can
                    be used to allow the order amount to be changed after the
                    checkout flow.
                paymentScheduleChecksum:
                  type: string
                  description: >-
                    **Express checkout only.** A unique value representing the
                    payment schedule that must be provided when there have been
                    changes since the initial order creation (retrieved from
                    checkout widget).
                items:
                  $ref: '#/components/schemas/Item'
                  description: >-
                    **Express checkout only.** An array of order items that have
                    been updated. Provide if it has changed since the initial
                    order creation.
                shipping:
                  $ref: '#/components/schemas/Contact'
                  description: >-
                    **Express checkout only.** The shipping address if it has
                    changed since the initial order creation. 
                enrichments:
                  $ref: '#/components/schemas/Enrichments'
              required:
                - token
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    MoneyCurrency:
      type: string
      enum:
        - AUD
        - NZD
        - USD
        - CAD
        - GBP
      title: MoneyCurrency
    Money:
      type: object
      properties:
        amount:
          type: string
          description: >-
            The amount as a string representation of a decimal number, rounded
            to 2 decimal places.
        currency:
          $ref: '#/components/schemas/MoneyCurrency'
      required:
        - amount
        - currency
      description: Object containing amount and currency
      title: Money
    Item:
      type: object
      properties:
        name:
          type: string
        sku:
          type: string
        pageUrl:
          type: string
        imageUrl:
          type: string
        quantity:
          type: integer
        price:
          $ref: '#/components/schemas/Money'
        categories:
          type: array
          items:
            type: array
            items:
              type: string
        estimatedShipmentDate:
          type: string
          format: date
        preorder:
          type: boolean
          default: false
      required:
        - name
        - quantity
        - price
      description: >
        This data model is used to store crucial product details. The
        `price.amount` field represents the unit price of the individual item.
        The `quantity` field shows the number of units of the item. The `name`
        field denotes the name of the product, while `sku` holds the Stock
        Keeping Unit identifier. 100 is the maximum number of item objects in
        the items array.

        <Warning Title="Important Note">
          It is crucial that the `price.amount` represents the unit price of the individual item.
          **Never** populate the `price.amount` by multiplying the quantity by the unit cost. Always enter the price for a single unit to maintain data accuracy.
        </Warning>
      title: Item
    ContactCountryCode:
      type: string
      enum:
        - AU
        - NZ
        - US
        - CA
        - GB
      title: ContactCountryCode
    Contact:
      type: object
      properties:
        name:
          type: string
        line1:
          type: string
          description: First line of the address
        line2:
          type: string
          description: 'Second line of the address '
        area1:
          type: string
          description: |-
            - AU: Suburb
            - NZ: Town or City
            - UK: Postal Town
            - US: City
            - Canada: City
        area2:
          type: string
          description: |-
            - NZ: suburb
            - UK: village or local area.
        region:
          type: string
          description: |-
            - AU: State 
            - NZ: Region
            - UK: County
            - US: State
            - CA: Province or Territory
        postcode:
          type: string
        countryCode:
          $ref: '#/components/schemas/ContactCountryCode'
        phoneNumber:
          type: string
          description: >-
            The phone number, in [E.123](https://en.wikipedia.org/wiki/E.123)
            format.
      required:
        - name
        - line1
        - area1
        - region
        - postcode
        - countryCode
      description: >
        This data model is used for storing an individual's contact information.
        Mandatory fields such as **name**, **line1**, **area1**, **region**,
        **postcode**, and **countryCode** help in capturing vital information
        about a user's location. 


        The `line2` and `area2` fields provide additional space for extended
        addresses, while `phoneNumber` can be used to store the user's contact
        number.



        <Warning Title="Important Note">
          The `area1`, `area2` and `region` properties feature localized terminology based on country. Refer to the property descriptions for insights on each country's specific usage 
        </Warning>
      title: Contact
    InitiationActor:
      type: string
      enum:
        - CUSTOMER
        - MERCHANT
      description: The party who initiated the order
      title: InitiationActor
    Initiation:
      type: object
      properties:
        actor:
          $ref: '#/components/schemas/InitiationActor'
          description: The party who initiated the order
      required:
        - actor
      title: Initiation
    SubscriptionType:
      type: string
      enum:
        - FIXED
        - VARIABLE
      title: SubscriptionType
    SubscriptionInterval:
      type: string
      enum:
        - DAY
        - WEEK
        - MONTH
        - YEAR
      title: SubscriptionInterval
    Subscription:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/SubscriptionType'
        interval:
          $ref: '#/components/schemas/SubscriptionInterval'
        intervalCount:
          type: integer
      title: Subscription
    Enrichments:
      type: object
      properties:
        initiation:
          $ref: '#/components/schemas/Initiation'
          description: Who initiated the order
        subscription:
          $ref: '#/components/schemas/Subscription'
          description: Metadata on the subscription details
      required:
        - initiation
      title: Enrichments
    PaymentStatus:
      type: string
      enum:
        - APPROVED
        - DECLINED
      description: represents the status of the order
      title: PaymentStatus
    PaymentPaymentState:
      type: string
      enum:
        - AUTH_APPROVED
        - AUTH_DECLINED
        - PARTIALLY_CAPTURED
        - CAPTURED
        - CAPTURE_DECLINED
        - VOIDED
      description: is the current state for capturing payments
      title: PaymentPaymentState
    Refund:
      type: object
      properties:
        requestId:
          type: string
          description: Unique ID required for safe retries. Max length 64 (varchar).
        amount:
          $ref: '#/components/schemas/Money'
        merchantReference:
          type: string
          description: >-
            The merchant’s internal refund id/reference. This must be included
            along with the `requestId` to utilise idempotency. Max length 85
            (varchar).
        refundMerchantReference:
          type: string
          description: >-
            A unique reference for the individual refund event. Max length 128
            (varchar).
        refundId:
          type: string
          description: The unique, permanent, Cash App Afterpay-generated Refund ID.
        refundedAt:
          type: string
      description: >
        To guarantee safe retries, the merchant should offer their refund ID or
        reference, aligning with their internal records


        Unique values for the `requestID`  and `merchantReference` are required
        to guarantee safe retries. It is recommended that the merchant generates
        a UUID for each unique refund request. 


        The `refundMerchantReference` is a unique reference that when provided,
        will appear in the daily settlement file as "Payment Event Id". In most
        cases, this would hold the same value as the `merchantReference`.
      title: Refund
    Consumer:
      type: object
      properties:
        email:
          type: string
          format: email
        givenNames:
          type: string
          description: The consumer's first name
        surname:
          type: string
          description: The consumer's last name
        phoneNumber:
          type: string
      required:
        - email
      description: >-
        The consumer data model is used for gathering essential user
        information. It captures details such as the individual's first name,
        represented by `givenNames`, and their last name, captured under
        `surname`. In addition, it stores the user's contact number under
        `phoneNumber` and their email address under `email`. These fields
        collectively provide contact and identification details for a user.
      title: Consumer
    ShippingCourierPriority:
      type: string
      enum:
        - STANDARD
        - EXPRESS
      title: ShippingCourierPriority
    Shipping-Courier:
      type: object
      properties:
        shippedAt:
          type: string
          format: date-time
        name:
          type: string
        tracking:
          type: string
        priority:
          $ref: '#/components/schemas/ShippingCourierPriority'
      description: >-
        Essential information for tracking a shipment. The `shippedAt` key
        represents the date and time when the item was shipped. This value
        follows the [ISO 8601 standard
        format](https://www.iso.org/iso-8601-date-and-time-format.html) for date
        and time representations.


        The `name` field indicates the courier service employed to handle the
        shipment (e.g. FEDEX, UPS). For orders that are picked up in-store (also
        known as Buy-Online-Pickup-Instore), please use "INSTORE_PICKUP" as the
        `name` field value.


        The `tracking` key represents a unique tracking number provided by the
        courier service to monitor the shipment's progress. It's a valuable tool
        for customers and businesses to track and trace their packages.


        The `priority` field tracks the shipping speed or service level
        associated with the delivery. 
      title: Shipping-Courier
    Discount:
      type: object
      properties:
        displayName:
          type: string
        amount:
          $ref: '#/components/schemas/Money'
      description: Discount applied to an order
      title: Discount
    Order-Details:
      type: object
      properties:
        consumer:
          $ref: '#/components/schemas/Consumer'
        billing:
          $ref: '#/components/schemas/Contact'
        courier:
          $ref: '#/components/schemas/Shipping-Courier'
        items:
          type: array
          items:
            $ref: '#/components/schemas/Item'
        discounts:
          type: array
          items:
            $ref: '#/components/schemas/Discount'
        taxAmount:
          $ref: '#/components/schemas/Money'
        shippingAmount:
          $ref: '#/components/schemas/Money'
      description: >-
        This comprehensive schema is designed to store an entire transaction's
        detail, covering crucial aspects like consumer information, billing and
        shipping details, courier particulars, item list, discounts, tax, and
        shipping amount.
      title: Order-Details
    PaymentEventType:
      type: string
      enum:
        - AUTH_APPROVED
        - AUTH_DECLINED
        - CAPTURED
        - CAPTURE_DECLINED
        - VOIDED
        - EXPIRED
      title: PaymentEventType
    Payment-Event:
      type: object
      properties:
        id:
          type: string
        created:
          type: string
        expires:
          type: string
        type:
          $ref: '#/components/schemas/PaymentEventType'
        amount:
          $ref: '#/components/schemas/Money'
        paymentEventMerchantReference:
          type: string
      description: >-
        Each payment event has a unique ID, creation timestamp, and type (e.g.,
        "AUTH_APPROVED", "AUTH_DECLINED"). For "AUTH_APPROVED" events, an
        expiration timestamp is provided. The "payment event merchant reference"
        field, which can be used for payment capture events
      title: Payment-Event
    Payment:
      type: object
      properties:
        id:
          type: string
          description: The unique, permanent, Cash App Afterpay generated Order ID.
        token:
          type: string
          description: The token obtained from the checkout call
        status:
          $ref: '#/components/schemas/PaymentStatus'
          description: represents the status of the order
        created:
          type: string
          description: ' is the UTC timestamp of when the payment was completed.'
        originalAmount:
          $ref: '#/components/schemas/Money'
        openToCaptureAmount:
          $ref: '#/components/schemas/Money'
        paymentState:
          $ref: '#/components/schemas/PaymentPaymentState'
          description: is the current state for capturing payments
        merchantReference:
          type: string
          description: >-
            is the merchant's order id/reference that the payment corresponds
            to.
        refunds:
          type: array
          items:
            $ref: '#/components/schemas/Refund'
        orderDetails:
          $ref: '#/components/schemas/Order-Details'
        events:
          type: array
          items:
            $ref: '#/components/schemas/Payment-Event'
      description: Describes the schema for a (read-only) payment object
      title: Payment
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/payments/capture"

payload = {
    "token": "string",
    "merchantReference": "string",
    "amount": {
        "amount": "100.00",
        "currency": "AUD"
    },
    "isCheckoutAdjusted": True,
    "paymentScheduleChecksum": "string",
    "items": {
        "name": "Blue Carabiner",
        "quantity": 1,
        "price": {
            "amount": "40.00",
            "currency": "AUD"
        },
        "sku": "12341234",
        "pageUrl": "https://merchant.example.com/carabiner-354193.html",
        "imageUrl": "https://merchant.example.com/carabiner-7378-391453-1.jpg",
        "categories": [["Sporting Goods", "Climbing Equipment", "Climbing", "Climbing Carabiners"], ["Sale", "Climbing"]],
        "estimatedShipmentDate": "2023-08-01"
    },
    "shipping": {
        "name": "Joe Consumer",
        "line1": "Level 5",
        "area1": "Melbourne",
        "region": "VIC",
        "postcode": "3000",
        "countryCode": "AU",
        "line2": "390 Collins Street",
        "phoneNumber": "0400 000 000"
    }
}
headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/payments/capture';
const options = {
  method: 'POST',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"token":"string","merchantReference":"string","amount":{"amount":"100.00","currency":"AUD"},"isCheckoutAdjusted":true,"paymentScheduleChecksum":"string","items":{"name":"Blue Carabiner","quantity":1,"price":{"amount":"40.00","currency":"AUD"},"sku":"12341234","pageUrl":"https://merchant.example.com/carabiner-354193.html","imageUrl":"https://merchant.example.com/carabiner-7378-391453-1.jpg","categories":[["Sporting Goods","Climbing Equipment","Climbing","Climbing Carabiners"],["Sale","Climbing"]],"estimatedShipmentDate":"2023-08-01"},"shipping":{"name":"Joe Consumer","line1":"Level 5","area1":"Melbourne","region":"VIC","postcode":"3000","countryCode":"AU","line2":"390 Collins Street","phoneNumber":"0400 000 000"}}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://global-api-sandbox.afterpay.com/v2/payments/capture"

	payload := strings.NewReader("{\n  \"token\": \"string\",\n  \"merchantReference\": \"string\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"isCheckoutAdjusted\": true,\n  \"paymentScheduleChecksum\": \"string\",\n  \"items\": {\n    \"name\": \"Blue Carabiner\",\n    \"quantity\": 1,\n    \"price\": {\n      \"amount\": \"40.00\",\n      \"currency\": \"AUD\"\n    },\n    \"sku\": \"12341234\",\n    \"pageUrl\": \"https://merchant.example.com/carabiner-354193.html\",\n    \"imageUrl\": \"https://merchant.example.com/carabiner-7378-391453-1.jpg\",\n    \"categories\": [\n      [\n        \"Sporting Goods\",\n        \"Climbing Equipment\",\n        \"Climbing\",\n        \"Climbing Carabiners\"\n      ],\n      [\n        \"Sale\",\n        \"Climbing\"\n      ]\n    ],\n    \"estimatedShipmentDate\": \"2023-08-01\"\n  },\n  \"shipping\": {\n    \"name\": \"Joe Consumer\",\n    \"line1\": \"Level 5\",\n    \"area1\": \"Melbourne\",\n    \"region\": \"VIC\",\n    \"postcode\": \"3000\",\n    \"countryCode\": \"AU\",\n    \"line2\": \"390 Collins Street\",\n    \"phoneNumber\": \"0400 000 000\"\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Authorization", "Basic <username>:<password>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://global-api-sandbox.afterpay.com/v2/payments/capture")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"token\": \"string\",\n  \"merchantReference\": \"string\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"isCheckoutAdjusted\": true,\n  \"paymentScheduleChecksum\": \"string\",\n  \"items\": {\n    \"name\": \"Blue Carabiner\",\n    \"quantity\": 1,\n    \"price\": {\n      \"amount\": \"40.00\",\n      \"currency\": \"AUD\"\n    },\n    \"sku\": \"12341234\",\n    \"pageUrl\": \"https://merchant.example.com/carabiner-354193.html\",\n    \"imageUrl\": \"https://merchant.example.com/carabiner-7378-391453-1.jpg\",\n    \"categories\": [\n      [\n        \"Sporting Goods\",\n        \"Climbing Equipment\",\n        \"Climbing\",\n        \"Climbing Carabiners\"\n      ],\n      [\n        \"Sale\",\n        \"Climbing\"\n      ]\n    ],\n    \"estimatedShipmentDate\": \"2023-08-01\"\n  },\n  \"shipping\": {\n    \"name\": \"Joe Consumer\",\n    \"line1\": \"Level 5\",\n    \"area1\": \"Melbourne\",\n    \"region\": \"VIC\",\n    \"postcode\": \"3000\",\n    \"countryCode\": \"AU\",\n    \"line2\": \"390 Collins Street\",\n    \"phoneNumber\": \"0400 000 000\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/payments/capture")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"token\": \"string\",\n  \"merchantReference\": \"string\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"isCheckoutAdjusted\": true,\n  \"paymentScheduleChecksum\": \"string\",\n  \"items\": {\n    \"name\": \"Blue Carabiner\",\n    \"quantity\": 1,\n    \"price\": {\n      \"amount\": \"40.00\",\n      \"currency\": \"AUD\"\n    },\n    \"sku\": \"12341234\",\n    \"pageUrl\": \"https://merchant.example.com/carabiner-354193.html\",\n    \"imageUrl\": \"https://merchant.example.com/carabiner-7378-391453-1.jpg\",\n    \"categories\": [\n      [\n        \"Sporting Goods\",\n        \"Climbing Equipment\",\n        \"Climbing\",\n        \"Climbing Carabiners\"\n      ],\n      [\n        \"Sale\",\n        \"Climbing\"\n      ]\n    ],\n    \"estimatedShipmentDate\": \"2023-08-01\"\n  },\n  \"shipping\": {\n    \"name\": \"Joe Consumer\",\n    \"line1\": \"Level 5\",\n    \"area1\": \"Melbourne\",\n    \"region\": \"VIC\",\n    \"postcode\": \"3000\",\n    \"countryCode\": \"AU\",\n    \"line2\": \"390 Collins Street\",\n    \"phoneNumber\": \"0400 000 000\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/payments/capture', [
  'body' => '{
  "token": "string",
  "merchantReference": "string",
  "amount": {
    "amount": "100.00",
    "currency": "AUD"
  },
  "isCheckoutAdjusted": true,
  "paymentScheduleChecksum": "string",
  "items": {
    "name": "Blue Carabiner",
    "quantity": 1,
    "price": {
      "amount": "40.00",
      "currency": "AUD"
    },
    "sku": "12341234",
    "pageUrl": "https://merchant.example.com/carabiner-354193.html",
    "imageUrl": "https://merchant.example.com/carabiner-7378-391453-1.jpg",
    "categories": [
      [
        "Sporting Goods",
        "Climbing Equipment",
        "Climbing",
        "Climbing Carabiners"
      ],
      [
        "Sale",
        "Climbing"
      ]
    ],
    "estimatedShipmentDate": "2023-08-01"
  },
  "shipping": {
    "name": "Joe Consumer",
    "line1": "Level 5",
    "area1": "Melbourne",
    "region": "VIC",
    "postcode": "3000",
    "countryCode": "AU",
    "line2": "390 Collins Street",
    "phoneNumber": "0400 000 000"
  }
}',
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/payments/capture");
var request = new RestRequest(Method.POST);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"token\": \"string\",\n  \"merchantReference\": \"string\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"isCheckoutAdjusted\": true,\n  \"paymentScheduleChecksum\": \"string\",\n  \"items\": {\n    \"name\": \"Blue Carabiner\",\n    \"quantity\": 1,\n    \"price\": {\n      \"amount\": \"40.00\",\n      \"currency\": \"AUD\"\n    },\n    \"sku\": \"12341234\",\n    \"pageUrl\": \"https://merchant.example.com/carabiner-354193.html\",\n    \"imageUrl\": \"https://merchant.example.com/carabiner-7378-391453-1.jpg\",\n    \"categories\": [\n      [\n        \"Sporting Goods\",\n        \"Climbing Equipment\",\n        \"Climbing\",\n        \"Climbing Carabiners\"\n      ],\n      [\n        \"Sale\",\n        \"Climbing\"\n      ]\n    ],\n    \"estimatedShipmentDate\": \"2023-08-01\"\n  },\n  \"shipping\": {\n    \"name\": \"Joe Consumer\",\n    \"line1\": \"Level 5\",\n    \"area1\": \"Melbourne\",\n    \"region\": \"VIC\",\n    \"postcode\": \"3000\",\n    \"countryCode\": \"AU\",\n    \"line2\": \"390 Collins Street\",\n    \"phoneNumber\": \"0400 000 000\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = [
  "token": "string",
  "merchantReference": "string",
  "amount": [
    "amount": "100.00",
    "currency": "AUD"
  ],
  "isCheckoutAdjusted": true,
  "paymentScheduleChecksum": "string",
  "items": [
    "name": "Blue Carabiner",
    "quantity": 1,
    "price": [
      "amount": "40.00",
      "currency": "AUD"
    ],
    "sku": "12341234",
    "pageUrl": "https://merchant.example.com/carabiner-354193.html",
    "imageUrl": "https://merchant.example.com/carabiner-7378-391453-1.jpg",
    "categories": [["Sporting Goods", "Climbing Equipment", "Climbing", "Climbing Carabiners"], ["Sale", "Climbing"]],
    "estimatedShipmentDate": "2023-08-01"
  ],
  "shipping": [
    "name": "Joe Consumer",
    "line1": "Level 5",
    "area1": "Melbourne",
    "region": "VIC",
    "postcode": "3000",
    "countryCode": "AU",
    "line2": "390 Collins Street",
    "phoneNumber": "0400 000 000"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/payments/capture")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/payments/capture"

payload = {
    "token": "{{afterpay_checkout_token}}",
    "merchantReference": "{{merchant_order_number}}"
}
headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/payments/capture';
const options = {
  method: 'POST',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"token":"{{afterpay_checkout_token}}","merchantReference":"{{merchant_order_number}}"}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://global-api-sandbox.afterpay.com/v2/payments/capture"

	payload := strings.NewReader("{\n  \"token\": \"{{afterpay_checkout_token}}\",\n  \"merchantReference\": \"{{merchant_order_number}}\"\n}")

	req, _ := http.NewRequest("POST", url, payload)

	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Authorization", "Basic <username>:<password>")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://global-api-sandbox.afterpay.com/v2/payments/capture")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"token\": \"{{afterpay_checkout_token}}\",\n  \"merchantReference\": \"{{merchant_order_number}}\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/payments/capture")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"token\": \"{{afterpay_checkout_token}}\",\n  \"merchantReference\": \"{{merchant_order_number}}\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/payments/capture', [
  'body' => '{
  "token": "{{afterpay_checkout_token}}",
  "merchantReference": "{{merchant_order_number}}"
}',
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/payments/capture");
var request = new RestRequest(Method.POST);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"token\": \"{{afterpay_checkout_token}}\",\n  \"merchantReference\": \"{{merchant_order_number}}\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = [
  "token": "{{afterpay_checkout_token}}",
  "merchantReference": "{{merchant_order_number}}"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/payments/capture")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```