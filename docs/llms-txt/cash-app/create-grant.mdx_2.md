# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/orders/create-grant.mdx

# Create Order

POST https://global-api-sandbox.afterpay.com/v2/orders
Content-Type: application/json

This is the first step in the on file grant purchase process. Use the token in the response to initiate the payment


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/orders/create-grant

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/orders:
    post:
      operationId: create-grant
      summary: Create Order
      description: >
        This is the first step in the on file grant purchase process. Use the
        token in the response to initiate the payment
      tags:
        - ''
      parameters:
        - name: Authorization
          in: header
          description: Basic authentication
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
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateOrderResponse'
        '415':
          description: Unsupported Media Type
          content:
            application/json:
              schema:
                description: Any type
        '422':
          description: >
            | errorCode | Description |

            | --- | --- |

            | invalid_object             | One or more required fields were
            missing or invalid.                     |

            | unsupported_payment_type   | The amount is outside of the
            merchant's payment limits, as returned by Get Configuration. |

            | unsupported_currency       | The amount is outside of the
            merchant's payment limits, as returned by Get Configuration. |
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/OrderRequest'
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
    OrderRequest:
      type: object
      properties:
        requestId:
          type: string
          format: uuid
          description: A unique identifier for the request, used for idempotency
        grantId:
          type: string
          description: ID of the grant used to create this order
        amount:
          $ref: '#/components/schemas/Money'
          description: The total amount of the order
        enrichments:
          $ref: '#/components/schemas/Enrichments'
          description: Describes additional fields beyond core payment information.
        consumer:
          $ref: '#/components/schemas/Consumer'
        billing:
          $ref: '#/components/schemas/Contact'
        shipping:
          $ref: '#/components/schemas/Contact'
        items:
          type: array
          items:
            $ref: '#/components/schemas/Item'
        discounts:
          type: array
          items:
            $ref: '#/components/schemas/Discount'
        merchantReference:
          type: string
          description: The reference/order ID in the merchant's system
        shippingAmount:
          $ref: '#/components/schemas/Money'
          description: The shipping cost amount
        taxAmount:
          $ref: '#/components/schemas/Money'
          description: The tax amount
        courier:
          $ref: '#/components/schemas/Shipping-Courier'
      required:
        - requestId
        - grantId
        - amount
        - enrichments
      title: OrderRequest
    CreateOrderResponse:
      type: object
      properties:
        token:
          type: string
        expires:
          type: string
          format: date-time
      required:
        - token
        - expires
      title: CreateOrderResponse
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/orders"

payload = {
    "requestId": "123e4567-e89b-12d3-a456-426614174000",
    "grantId": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
    "amount": {
        "amount": "100.00",
        "currency": "AUD"
    },
    "enrichments": { "initiation": { "actor": "CUSTOMER" } }
}
headers = {
    "Authorization": "Basic <username>:<password>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/orders';
const options = {
  method: 'POST',
  headers: {
    Authorization: 'Basic <username>:<password>',
    'Content-Type': 'application/json'
  },
  body: '{"requestId":"123e4567-e89b-12d3-a456-426614174000","grantId":"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2","amount":{"amount":"100.00","currency":"AUD"},"enrichments":{"initiation":{"actor":"CUSTOMER"}}}'
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

	url := "https://global-api-sandbox.afterpay.com/v2/orders"

	payload := strings.NewReader("{\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"grantId\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"enrichments\": {\n    \"initiation\": {\n      \"actor\": \"CUSTOMER\"\n    }\n  }\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("https://global-api-sandbox.afterpay.com/v2/orders")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Authorization"] = 'Basic <username>:<password>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"grantId\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"enrichments\": {\n    \"initiation\": {\n      \"actor\": \"CUSTOMER\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://global-api-sandbox.afterpay.com/v2/orders")
  .header("Authorization", "Basic <username>:<password>")
  .header("Content-Type", "application/json")
  .body("{\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"grantId\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"enrichments\": {\n    \"initiation\": {\n      \"actor\": \"CUSTOMER\"\n    }\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://global-api-sandbox.afterpay.com/v2/orders', [
  'body' => '{
  "requestId": "123e4567-e89b-12d3-a456-426614174000",
  "grantId": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
  "amount": {
    "amount": "100.00",
    "currency": "AUD"
  },
  "enrichments": {
    "initiation": {
      "actor": "CUSTOMER"
    }
  }
}',
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/orders");
var request = new RestRequest(Method.POST);
request.AddHeader("Authorization", "Basic <username>:<password>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"requestId\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"grantId\": \"005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2\",\n  \"amount\": {\n    \"amount\": \"100.00\",\n    \"currency\": \"AUD\"\n  },\n  \"enrichments\": {\n    \"initiation\": {\n      \"actor\": \"CUSTOMER\"\n    }\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Authorization": "Basic <username>:<password>",
  "Content-Type": "application/json"
]
let parameters = [
  "requestId": "123e4567-e89b-12d3-a456-426614174000",
  "grantId": "005.2fkv5o963b132z8ppa34srlh60987y87d55re237wsg9tr4q2",
  "amount": [
    "amount": "100.00",
    "currency": "AUD"
  ],
  "enrichments": ["initiation": ["actor": "CUSTOMER"]]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/orders")! as URL,
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