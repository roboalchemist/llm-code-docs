# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1.mdx

# Create Checkout

POST https://global-api-sandbox.afterpay.com/v2/checkouts
Content-Type: application/json

The `checkouts` endpoint is responsible for creating a new checkout and returning the associated checkout token.


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/checkouts:
    post:
      operationId: create-checkout-1
      summary: Create Checkout
      description: >
        The `checkouts` endpoint is responsible for creating a new checkout and
        returning the associated checkout token.
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
          description: Returns a token, expiry date/time, and checkout URL if successful.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Checkout-Response'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: >
            | errorCode | Description |

            | --- | --- |

            | invalid_object | One or more required fields were missing or
            invalid. |

            | unsupported_payment_type | The `amount` is outside of the
            merchant's payment limits, as returned by GET Configuration. |

            | unsupported_currency | One or more Money objects contained a
            currency that differs from the merchant's account currency. |
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        description: ''
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Checkout-Request'
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
    CheckoutRequestMerchant:
      type: object
      properties:
        redirectConfirmUrl:
          type: string
        redirectCancelUrl:
          type: string
        popupOriginUrl:
          type: string
          description: >-
            The URL location from which Cash App Afterpay is initiated (required
            for express checkout). Optional for standard checkout when a
            `redirectConfirmURL` is provided.
        name:
          type: string
          description: >-
            The merchant name displayed in the Cash App Afterpay checkout flow,
            confirmation & refund emails, and the consumer portal
      required:
        - redirectConfirmUrl
        - redirectCancelUrl
      title: CheckoutRequestMerchant
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
    Checkout-Request:
      type: object
      properties:
        amount:
          $ref: '#/components/schemas/Money'
        consumer:
          $ref: '#/components/schemas/Consumer'
        merchantReference:
          type: string
        billing:
          $ref: '#/components/schemas/Contact'
        shipping:
          $ref: '#/components/schemas/Contact'
        merchant:
          $ref: '#/components/schemas/CheckoutRequestMerchant'
        items:
          type: array
          items:
            $ref: '#/components/schemas/Item'
        courier:
          $ref: '#/components/schemas/Shipping-Courier'
        taxAmount:
          $ref: '#/components/schemas/Money'
        shippingAmount:
          $ref: '#/components/schemas/Money'
        discounts:
          type: array
          items:
            $ref: '#/components/schemas/Discount'
        description:
          type: string
        mode:
          type: string
          default: standard
          description: |-
            Must be set to `express` to enable express checkout. 
            Allowed values: `express` `standard`
      required:
        - amount
        - consumer
      description: Individual Checkout
      title: Checkout-Request
    Checkout-Response:
      type: object
      properties:
        token:
          type: string
          description: Checkout token to be used to complete payment.
        expires:
          type: string
          description: >-
            The UTC timestamp of when the checkout token will expire, in ISO
            8601 format.
        redirectCheckoutUrl:
          type: string
          description: >-
            A URL that can be used to redirect the customer to the Cash App
            Afterpay screenflow directly from the merchant backend.
      title: Checkout-Response
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/checkouts"

payload = {
    "amount": {
        "amount": "100.00",
        "currency": "AUD"
    },
    "consumer": { "email": "test@example.com" }
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
const url = 'https://global-api-sandbox.afterpay.com/v2/checkouts';
const options = {
  method: 'POST',
  headers: {
    'User-Agent': 'User-Agent',
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"amount":{"amount":"100.00","currency":"AUD"},"consumer":{"email":"test@example.com"}}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/checkouts"

	payload := strings.NewReader("{\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"consumer\": {\n    \"email\": \"test@example.com\"\n  }\n}")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/checkouts")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"consumer\": {\n    \"email\": \"test@example.com\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/checkouts")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"consumer\": {\n    \"email\": \"test@example.com\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/checkouts', [
  'body' => '{
  "amount": {
    "amount": "100.00",
    "currency": "AUD"
  },
  "consumer": {
    "email": "test@example.com"
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

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/checkouts");
var request = new RestRequest(Method.POST);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"consumer\": {\n    \"email\": \"test@example.com\"\n  }\n}", ParameterType.RequestBody);
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
  "amount": [
    "amount": "100.00",
    "currency": "AUD"
  ],
  "consumer": ["email": "test@example.com"]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/checkouts")! as URL,
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