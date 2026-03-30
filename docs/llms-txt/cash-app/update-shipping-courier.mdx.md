# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/update-shipping-courier.mdx

# Update Shipping Courier

PUT https://global-api-sandbox.afterpay.com/v2/payments/{orderId}/courier
Content-Type: application/json

This endpoint updates an order with shipping courier information. The Cash App Afterpay team may use this information when providing support.

**Connection Timeouts**
| Timeout | Time (Seconds) |
|---------|----------------|
| Open    | 10             |
| Read    | 20             |


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/payments/update-shipping-courier

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/payments/{orderId}/courier:
    put:
      operationId: update-shipping-courier
      summary: Update Shipping Courier
      description: >
        This endpoint updates an order with shipping courier information. The
        Cash App Afterpay team may use this information when providing support.


        **Connection Timeouts**

        | Timeout | Time (Seconds) |

        |---------|----------------|

        | Open    | 10             |

        | Read    | 20             |
      tags:
        - ''
      parameters:
        - name: orderId
          in: path
          description: The unique Cash App Afterpay Order ID to update.
          required: true
          schema:
            type: string
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
            $ref: '#/components/schemas/V2PaymentsOrderIdCourierPutParametersAccept'
      responses:
        '200':
          description: Returns a Payment object in response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Payment'
        '412':
          description: >-
            No Cash App Afterpay Order was found matching the `orderId`
            provided. Error code `precondition_failed`.
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: >-
            A value for shippedAt was provided, but not a valid [ISO
            8601](https://www.iso.org/iso-8601-date-and-time-format.html) date.
            Or, a value for priority was provided, but wasn't one of "STANDARD"
            or "EXPRESS". Error code `invalid_object`.
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Shipping-Courier'
servers:
  - url: https://global-api-sandbox.afterpay.com
  - url: https://global-api.afterpay.com
components:
  schemas:
    V2PaymentsOrderIdCourierPutParametersAccept:
      type: string
      enum:
        - application/json
      title: V2PaymentsOrderIdCourierPutParametersAccept
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
    PaymentStatus:
      type: string
      enum:
        - APPROVED
        - DECLINED
      description: represents the status of the order
      title: PaymentStatus
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

url = "https://global-api-sandbox.afterpay.com/v2/payments/orderId/courier"

payload = {}
headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/payments/orderId/courier';
const options = {
  method: 'PUT',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/payments/orderId/courier"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PUT", url, payload)

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

url = URI("https://global-api-sandbox.afterpay.com/v2/payments/orderId/courier")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Put.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("https://global-api-sandbox.afterpay.com/v2/payments/orderId/courier")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'https://global-api-sandbox.afterpay.com/v2/payments/orderId/courier', [
  'body' => '{}',
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

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/payments/orderId/courier");
var request = new RestRequest(Method.PUT);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/payments/orderId/courier")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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