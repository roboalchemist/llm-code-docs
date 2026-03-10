# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/checkouts/get-checkout.mdx

# Get Checkout

GET https://global-api-sandbox.afterpay.com/v2/checkouts/{token}

This endpoint retrieves an incomplete individual checkout by token.

Checkout details are only retained in this temporary format for up to 60 minutes. If a checkout token expires or has an order created against it, it can no longer be retrieved from this endpoint.
To retrieve a [Payment](../docs/ONLINE-API/Payment-object.md) record (Cash App Afterpay Order) along with its associated checkout details, see Get Payment By Token.


Reference: https://developers.cash.app/cash-app-afterpay/api-reference/reference/checkouts/get-checkout

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /v2/checkouts/{token}:
    get:
      operationId: get-checkout
      summary: Get Checkout
      description: >
        This endpoint retrieves an incomplete individual checkout by token.


        Checkout details are only retained in this temporary format for up to 60
        minutes. If a checkout token expires or has an order created against it,
        it can no longer be retrieved from this endpoint.

        To retrieve a [Payment](../docs/ONLINE-API/Payment-object.md) record
        (Cash App Afterpay Order) along with its associated checkout details,
        see Get Payment By Token.
      tags:
        - ''
      parameters:
        - name: token
          in: path
          description: The token of the checkout to be retrieved.
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
            type: string
            default: application/json
      responses:
        '200':
          description: >
            Returns an object combining the [Checkout
            Request](reference/Checkouts.v2.yaml/components/schemas/Checkout-Request)
            and [Checkout
            Response](reference/Checkouts.v2.yaml/components/schemas/Checkout-Response)
            for a provided token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/get-checkout_Response_200'
        '404':
          description: No checkout token was provided.
          content:
            application/json:
              schema:
                description: Any type
        '412':
          description: >-
            The checkout token is invalid, expired, completed, or does not
            exist.
          content:
            application/json:
              schema:
                description: Any type
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
    get-checkout_Response_200:
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
      title: get-checkout_Response_200
  securitySchemes:
    sec0:
      type: http
      scheme: basic

```

## SDK Code Examples

```python
import requests

url = "https://global-api-sandbox.afterpay.com/v2/checkouts/token"

headers = {
    "User-Agent": "User-Agent",
    "Authorization": "Basic <username>:<password>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://global-api-sandbox.afterpay.com/v2/checkouts/token';
const options = {
  method: 'GET',
  headers: {'User-Agent': 'User-Agent', Authorization: 'Basic <username>:<password>'}
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
	"net/http"
	"io"
)

func main() {

	url := "https://global-api-sandbox.afterpay.com/v2/checkouts/token"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Authorization", "Basic <username>:<password>")

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

url = URI("https://global-api-sandbox.afterpay.com/v2/checkouts/token")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["User-Agent"] = 'User-Agent'
request["Authorization"] = 'Basic <username>:<password>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://global-api-sandbox.afterpay.com/v2/checkouts/token")
  .header("User-Agent", "User-Agent")
  .header("Authorization", "Basic <username>:<password>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://global-api-sandbox.afterpay.com/v2/checkouts/token', [
  'headers' => [
    'Authorization' => 'Basic <username>:<password>',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://global-api-sandbox.afterpay.com/v2/checkouts/token");
var request = new RestRequest(Method.GET);
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Authorization", "Basic <username>:<password>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "User-Agent": "User-Agent",
  "Authorization": "Basic <username>:<password>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://global-api-sandbox.afterpay.com/v2/checkouts/token")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

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