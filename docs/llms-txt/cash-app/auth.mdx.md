# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/auth.mdx

# Auth

POST https://global-api-sandbox.afterpay.com/v2/payments/auth
Content-Type: application/json

This endpoint requests a payment auth, which determines the order approval status. If approved, the auth has an expiration date and time, which is returned in the events list for the "AUTH_APPROVED" payment event. Authorization expires after 13 days.

This operation is idempotent based on the `requestId` (if provided), which allows for the safe retry of multiple requests, guaranteeing the payment operation is only made once.

The customer's payment plan starts at the time of auth approval.

**Note:** Authorization expires after 13 days and then the transaction is automatically voided. Voided transactions are frozen and cannot be reopened or changed in any way. In this case, use the `v2/checkouts` endpoint to create a new order.

**Connection Timeouts**
| Timeout | Time (Seconds) |
|---------|----------------|
| Open    | 10             |
| Read    | 70             |


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/auth

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/payments/auth:
    post:
      operationId: auth
      summary: Auth
      description: >
        This endpoint requests a payment auth, which determines the order
        approval status. If approved, the auth has an expiration date and time,
        which is returned in the events list for the "AUTH_APPROVED" payment
        event. Authorization expires after 13 days.


        This operation is idempotent based on the `requestId` (if provided),
        which allows for the safe retry of multiple requests, guaranteeing the
        payment operation is only made once.


        The customer's payment plan starts at the time of auth approval.


        **Note:** Authorization expires after 13 days and then the transaction
        is automatically voided. Voided transactions are frozen and cannot be
        reopened or changed in any way. In this case, use the `v2/checkouts`
        endpoint to create a new order.


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
          description: >-
            If the payment is approved by Cash App Afterpay, a Payment object is
            returned with a `status` of **APPROVED** and a `paymentState` of
            **AUTH_APPROVED**.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaymentAuth'
        '402':
          description: >
            If payment is declined by Cash App Afterpay, for example, if invalid
            card details were entered, returns a Payment object in response,
            with a `status` of "DECLINED" and a `paymentState` of
            "AUTH_DECLINED". advise the customer to contact the Cash App
            Afterpay Customer Service team for more information.


            As well, the following errorCodes are possible:

            | errorCode | Description |

            | --- | --- |

            | invalid_token | The checkout token is invalid, expired, or does
            not exist.
          content:
            application/json:
              schema:
                description: Any type
        '412':
          description: >-
            The customer has not confirmed their payment for the order
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
              $ref: '#/components/schemas/AuthorizePayment'
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
    AuthorizePayment:
      type: object
      properties:
        requestid:
          type: string
          format: uuid
          description: >-
            A unique request ID, required for idempotent retries. We recommend
            that merchants generate a Universally Unique Identifier (UUID) for
            each unique request.
        token:
          type: string
        merchantReference:
          type: string
          description: >-
            The reference/order ID that this payment corresponds to in the
            merchant's system.


            **Note:** Providing a new value updates any value previously set in
            the Create Checkout request.
        amount:
          $ref: '#/components/schemas/Money'
          description: >-
            **Required for express checkout only.** Amount to be checked against
            the value in the create checkout request. If the amounts do not
            match, then the request is rejected and an error specific to this
            scenario is returned.
        isCheckoutAdjusted:
          type: boolean
          description: >-
            **Express checkout only.** The isCheckoutAdjusted field can be used
            to allow the order amount to be changed after the checkout flow.
            Used for express checkout.
        paymentScheduleChecksum:
          type: string
          description: >-
            **Express checkout only.** A unique value representing the payment
            schedule that must be provided when there has been changes since the
            initial order creation (retrieved from checkout widget).
        items:
          type: array
          items:
            description: Any type
          description: >-
            **Express checkout only.** An array of order items that have been
            updated to be provided if it has changed since the initial order
            creation.
        shipping:
          $ref: '#/components/schemas/Contact'
          description: >-
            **Express checkout only.** The shipping address if it has changed
            since the initial order creation.
        enrichments:
          $ref: '#/components/schemas/Enrichments'
      required:
        - token
      title: AuthorizePayment
    PaymentAuthStatus:
      type: string
      enum:
        - APPROVED
        - DECLINED
      description: represents the status of the order
      title: PaymentAuthStatus
    PaymentAuthPaymentState:
      type: string
      enum:
        - AUTH_APPROVED
        - AUTH_DECLINED
        - PARTIALLY_CAPTURED
        - CAPTURED
        - CAPTURE_DECLINED
        - VOIDED
      description: is the current state for capturing payments
      title: PaymentAuthPaymentState
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
    PaymentAuth:
      type: object
      properties:
        id:
          type: string
          description: The unique, permanent, Cash App Afterpay generated Order ID.
        token:
          type: string
          description: The token obtained from the checkout call
        status:
          $ref: '#/components/schemas/PaymentAuthStatus'
          description: represents the status of the order
        created:
          type: string
          description: ' is the UTC timestamp of when the payment was completed.'
        originalAmount:
          $ref: '#/components/schemas/Money'
        openToCaptureAmount:
          $ref: '#/components/schemas/Money'
        paymentState:
          $ref: '#/components/schemas/PaymentAuthPaymentState'
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
      title: PaymentAuth
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/payments/auth"

payload = {
    "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
    "requestid": "d22f5305-05f3-48a0-9131-a4e6e5f58b9a",
    "merchantReference": "merchant-order-123",
    "amount": {
        "amount": "100.00",
        "currency": "AUD"
    },
    "isCheckoutAdjusted": True,
    "paymentScheduleChecksum": "string",
    "items": [None],
    "shipping": {
        "name": "Joe Consumer",
        "line1": "Level 5",
        "area1": "Melbourne",
        "region": "VIC",
        "postcode": "3000",
        "countryCode": "AU",
        "line2": "390 Collins Street",
        "phoneNumber": "0400 000 000"
    },
    "enrichments": { "initiation": { "actor": "MERCHANT" } }
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
const url = 'https://global-api-sandbox.afterpay.com/v2/payments/auth';
const options = {
  method: 'POST',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"token":"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2","requestid":"d22f5305-05f3-48a0-9131-a4e6e5f58b9a","merchantReference":"merchant-order-123","amount":{"amount":"100.00","currency":"AUD"},"isCheckoutAdjusted":true,"paymentScheduleChecksum":"string","items":[null],"shipping":{"name":"Joe Consumer","line1":"Level 5","area1":"Melbourne","region":"VIC","postcode":"3000","countryCode":"AU","line2":"390 Collins Street","phoneNumber":"0400 000 000"},"enrichments":{"initiation":{"actor":"MERCHANT"}}}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/payments/auth"

	payload := strings.NewReader("{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"requestid\": \"d22f5305-05f3-48a0-9131-a4e6e5f58b9a\",\n  \"merchantReference\": \"merchant-order-123\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"isCheckoutAdjusted\": true,\n  \"paymentScheduleChecksum\": \"string\",\n  \"items\": [\n    null\n  ],\n  \"shipping\": {\n    \"name\": \"Joe Consumer\",\n    \"line1\": \"Level 5\",\n    \"area1\": \"Melbourne\",\n    \"region\": \"VIC\",\n    \"postcode\": \"3000\",\n    \"countryCode\": \"AU\",\n    \"line2\": \"390 Collins Street\",\n    \"phoneNumber\": \"0400 000 000\"\n  },\n  \"enrichments\": {\n    \"initiation\": {\n      \"actor\": \"MERCHANT\"\n    }\n  }\n}")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/payments/auth")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"requestid\": \"d22f5305-05f3-48a0-9131-a4e6e5f58b9a\",\n  \"merchantReference\": \"merchant-order-123\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"isCheckoutAdjusted\": true,\n  \"paymentScheduleChecksum\": \"string\",\n  \"items\": [\n    null\n  ],\n  \"shipping\": {\n    \"name\": \"Joe Consumer\",\n    \"line1\": \"Level 5\",\n    \"area1\": \"Melbourne\",\n    \"region\": \"VIC\",\n    \"postcode\": \"3000\",\n    \"countryCode\": \"AU\",\n    \"line2\": \"390 Collins Street\",\n    \"phoneNumber\": \"0400 000 000\"\n  },\n  \"enrichments\": {\n    \"initiation\": {\n      \"actor\": \"MERCHANT\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/payments/auth")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"requestid\": \"d22f5305-05f3-48a0-9131-a4e6e5f58b9a\",\n  \"merchantReference\": \"merchant-order-123\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"isCheckoutAdjusted\": true,\n  \"paymentScheduleChecksum\": \"string\",\n  \"items\": [\n    null\n  ],\n  \"shipping\": {\n    \"name\": \"Joe Consumer\",\n    \"line1\": \"Level 5\",\n    \"area1\": \"Melbourne\",\n    \"region\": \"VIC\",\n    \"postcode\": \"3000\",\n    \"countryCode\": \"AU\",\n    \"line2\": \"390 Collins Street\",\n    \"phoneNumber\": \"0400 000 000\"\n  },\n  \"enrichments\": {\n    \"initiation\": {\n      \"actor\": \"MERCHANT\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/payments/auth', [
  'body' => '{
  "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
  "requestid": "d22f5305-05f3-48a0-9131-a4e6e5f58b9a",
  "merchantReference": "merchant-order-123",
  "amount": {
    "amount": "100.00",
    "currency": "AUD"
  },
  "isCheckoutAdjusted": true,
  "paymentScheduleChecksum": "string",
  "items": [
    null
  ],
  "shipping": {
    "name": "Joe Consumer",
    "line1": "Level 5",
    "area1": "Melbourne",
    "region": "VIC",
    "postcode": "3000",
    "countryCode": "AU",
    "line2": "390 Collins Street",
    "phoneNumber": "0400 000 000"
  },
  "enrichments": {
    "initiation": {
      "actor": "MERCHANT"
    }
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

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/payments/auth");
var request = new RestRequest(Method.POST);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"requestid\": \"d22f5305-05f3-48a0-9131-a4e6e5f58b9a\",\n  \"merchantReference\": \"merchant-order-123\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"isCheckoutAdjusted\": true,\n  \"paymentScheduleChecksum\": \"string\",\n  \"items\": [\n    null\n  ],\n  \"shipping\": {\n    \"name\": \"Joe Consumer\",\n    \"line1\": \"Level 5\",\n    \"area1\": \"Melbourne\",\n    \"region\": \"VIC\",\n    \"postcode\": \"3000\",\n    \"countryCode\": \"AU\",\n    \"line2\": \"390 Collins Street\",\n    \"phoneNumber\": \"0400 000 000\"\n  },\n  \"enrichments\": {\n    \"initiation\": {\n      \"actor\": \"MERCHANT\"\n    }\n  }\n}", ParameterType.RequestBody);
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
  "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
  "requestid": "d22f5305-05f3-48a0-9131-a4e6e5f58b9a",
  "merchantReference": "merchant-order-123",
  "amount": [
    "amount": "100.00",
    "currency": "AUD"
  ],
  "isCheckoutAdjusted": true,
  "paymentScheduleChecksum": "string",
  "items": [],
  "shipping": [
    "name": "Joe Consumer",
    "line1": "Level 5",
    "area1": "Melbourne",
    "region": "VIC",
    "postcode": "3000",
    "countryCode": "AU",
    "line2": "390 Collins Street",
    "phoneNumber": "0400 000 000"
  ],
  "enrichments": ["initiation": ["actor": "MERCHANT"]]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/payments/auth")! as URL,
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

url = "https://global-api-sandbox.afterpay.com/v2/payments/auth"

payload = {
    "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
    "requestid": "d22f5305-05f3-48a0-9131-a4e6e5f58b9a",
    "merchantReference": "merchant-order-123"
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
const url = 'https://global-api-sandbox.afterpay.com/v2/payments/auth';
const options = {
  method: 'POST',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"token":"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2","requestid":"d22f5305-05f3-48a0-9131-a4e6e5f58b9a","merchantReference":"merchant-order-123"}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/payments/auth"

	payload := strings.NewReader("{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"requestid\": \"d22f5305-05f3-48a0-9131-a4e6e5f58b9a\",\n  \"merchantReference\": \"merchant-order-123\"\n}")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/payments/auth")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"requestid\": \"d22f5305-05f3-48a0-9131-a4e6e5f58b9a\",\n  \"merchantReference\": \"merchant-order-123\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/payments/auth")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"requestid\": \"d22f5305-05f3-48a0-9131-a4e6e5f58b9a\",\n  \"merchantReference\": \"merchant-order-123\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/payments/auth', [
  'body' => '{
  "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
  "requestid": "d22f5305-05f3-48a0-9131-a4e6e5f58b9a",
  "merchantReference": "merchant-order-123"
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

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/payments/auth");
var request = new RestRequest(Method.POST);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"token\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"requestid\": \"d22f5305-05f3-48a0-9131-a4e6e5f58b9a\",\n  \"merchantReference\": \"merchant-order-123\"\n}", ParameterType.RequestBody);
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
  "token": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
  "requestid": "d22f5305-05f3-48a0-9131-a4e6e5f58b9a",
  "merchantReference": "merchant-order-123"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/payments/auth")! as URL,
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