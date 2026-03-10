# Source: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/orders/get-order.mdx

# Get Order

GET https://api.webflow.com/sites/{site_id}/order/{order_id}

Retrieve a single product by its ID. All of its SKUs will also be retrieved. The `count`, `limit`, `offset`
and `total` values in the response represent the Product only and do not include SKUs.


Reference: https://developers.webflow.com/data/v1.0.0/reference/ecommerce/orders/get-order

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /sites/{site_id}/order/{order_id}:
    get:
      operationId: get-order
      summary: Get Order
      description: >
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved. The `count`, `limit`, `offset`

        and `total` values in the response represent the Product only and do not
        include SKUs.
      tags:
        - subpackage_orders
      parameters:
        - name: site_id
          in: path
          description: Unique identifier for a Site
          required: true
          schema:
            type: string
            format: uuid
        - name: order_id
          in: path
          description: Unique identifier for an Order
          required: true
          schema:
            type: string
            format: uuid
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
        - name: Accept-Version
          in: header
          description: The API version
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Request was successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Order'
        '400':
          description: >-
            Request body was incorrectly formatted. Likely invalid JSON being
            sent up.
          content:
            application/json:
              schema:
                description: Any type
        '401':
          description: >-
            Provided access token is invalid or does not have access to
            requested resource
          content:
            application/json:
              schema:
                description: Any type
        '404':
          description: Requested resource not found
          content:
            application/json:
              schema:
                description: Any type
        '429':
          description: >-
            The rate limit of the provided access_token has been reached. Please
            have your application respect the X-RateLimit-Remaining header we
            include on API responses.
          content:
            application/json:
              schema:
                description: Any type
        '500':
          description: We had a problem with our server. Try again later.
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: https://api.webflow.com
components:
  schemas:
    OrderStatus:
      type: string
      enum:
        - pending
        - unfulfilled
        - fulfilled
        - disputed
        - dispute-lost
        - refunded
      description: >
        One of `pending`, `unfulfilled`, `fulfilled`, `disputed`,
        `dispute-lost`, or `refunded`
      title: OrderStatus
    OrderAmount:
      type: object
      properties:
        unit:
          type: string
        value:
          type: string
        string:
          type: string
      description: The sum of all line items.
      title: OrderAmount
    OrderCustomerInfo:
      type: object
      properties:
        fullName:
          type: string
        email:
          type: string
          format: email
      description: An object with the keys `fullName` and `email`.
      title: OrderCustomerInfo
    OrderAddressType:
      type: string
      enum:
        - shipping
        - billing
      title: OrderAddressType
    OrderAddress:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OrderAddressType'
        addressee:
          type: string
        line1:
          type: string
        line2:
          type: string
        city:
          type: string
        state:
          type: string
        country:
          type: string
        postalCode:
          type: string
      description: A customer address
      title: OrderAddress
    OrderItemImage:
      type: object
      properties:
        fileId:
          type: string
          format: uuid
        url:
          type: string
          format: uri
      title: OrderItemImage
    OrderPurchasedItem:
      type: object
      properties:
        count:
          type: number
          format: double
          description: Number of item purchased.
        rowTotal:
          $ref: '#/components/schemas/OrderAmount'
        productId:
          type: string
          format: uuid
          description: String Product Id.
        productName:
          type: string
          description: Name of the product.
        productSlug:
          type: string
          description: Slug of the product.
        variantId:
          type: string
          format: uuid
          description: String Variant Id. (SKU)
        variantName:
          type: string
          description: Name of the variant. (SKU)
        variantSlug:
          type: string
          description: Slug of the variant. (SKU)
        variantImage:
          $ref: '#/components/schemas/OrderItemImage'
        variantPrice:
          $ref: '#/components/schemas/OrderAmount'
        height:
          type: number
          format: double
          description: The height of the variant if provided, 0 otherwise.
        length:
          type: number
          format: double
          description: The length of the variant if provided, 0 otherwise.
        width:
          type: number
          format: double
          description: The width of the variant if provided, 0 otherwise
        weight:
          type: number
          format: double
          description: The weight of the variant if provided, 0 otherwise.
        purchasedItemsCount:
          type: number
          format: double
          description: The sum of all 'count' fields in 'purchasedItems'.
      description: An item that was purchased
      title: OrderPurchasedItem
    StripeDetails:
      type: object
      properties:
        refundReason:
          type: string
          description: Stripe customer ID, or null.
        refundId:
          type: string
          format: uuid
          description: Stripe charge ID, or null.
        disputeId:
          type: string
          format: uuid
          description: Stripe dispute ID, or null.
        chargeId:
          type: string
          format: uuid
          description: Stripe refund ID, or null.
        customerId:
          type: string
          format: uuid
      description: >-
        An object with various Stripe IDs, useful for linking into the stripe
        dashboard.
      title: StripeDetails
    StripeCardBrand:
      type: string
      enum:
        - Visa
        - American Express
        - MasterCard
        - Discover
        - JCB
        - Diners Club
        - Unknown
      description: The card’s brand.
      title: StripeCardBrand
    StripeCardExpires:
      type: object
      properties:
        year:
          type: number
          format: double
        month:
          type: number
          format: double
      description: The card’s expiration date.
      title: StripeCardExpires
    StripeCard:
      type: object
      properties:
        last4:
          type: string
          description: The last 4 digits on the card.
        brand:
          $ref: '#/components/schemas/StripeCardBrand'
          description: The card’s brand.
        ownerName:
          type: string
          description: The name on the card.
        expires:
          $ref: '#/components/schemas/StripeCardExpires'
          description: The card’s expiration date.
      description: >
        Details on the card used to fulfill this order, if this order was
        finalized with Stripe.
      title: StripeCard
    OrderExtraType:
      type: string
      enum:
        - discount
        - discount-shipping
        - shipping
        - tax
      description: The type of extra item this is.
      title: OrderExtraType
    OrderExtra:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OrderExtraType'
          description: The type of extra item this is.
        name:
          type: string
          description: A human-readable (but English) name for this extra charge.
        description:
          type: string
          description: A human-readable (but English) description of this extra charge.
        price:
          $ref: '#/components/schemas/OrderAmount'
      description: Extra order items, includes discounts, shipping, and taxes.
      title: OrderExtra
    OrderTotals:
      type: object
      properties:
        subtotal:
          $ref: '#/components/schemas/OrderAmount'
        extras:
          type: array
          items:
            $ref: '#/components/schemas/OrderExtra'
          description: An array of extra items, includes discounts, shipping, and taxes.
        total:
          $ref: '#/components/schemas/OrderAmount'
      description: An object describing various pricing totals.
      title: OrderTotals
    OrderCustomDataItems:
      type: object
      properties: {}
      title: OrderCustomDataItems
    OrderDownloadedFile:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        url:
          type: string
          format: uri
      title: OrderDownloadedFile
    Order:
      type: object
      properties:
        orderId:
          type: string
          description: >
            The order ID. Will usually be 6 hex characters, but can also be 9
            hex characters if the site has a very large number of orders.
            Randomly assigned.
        status:
          $ref: '#/components/schemas/OrderStatus'
          description: >
            One of `pending`, `unfulfilled`, `fulfilled`, `disputed`,
            `dispute-lost`, or `refunded`
        comment:
          type: string
          description: >-
            A comment string for this order editable by API user (not used by
            Webflow).
        orderComment:
          type: string
          description: A comment that the customer left when making their order
        acceptedOn:
          type: string
          format: date-time
          description: The ISO8601 timestamp that an order was placed.
        disputedOn:
          type: string
          format: date-time
          description: >
            If an order was disputed by the customer, then this key will be set
            with the ISO8601 timestamp that Stripe notifies Webflow. Null if not
            disputed.
        disputeUpdatedOn:
          type: string
          description: >
            If an order was disputed by the customer, then this key will be set
            with the ISO8601 timestamp of the last time that we got an update.
            Null if not disputed.
        disputeLastStatus:
          type: string
          description: >
            If an order was disputed by the customer, then this key will be set
            with the [dispute's
            status](https://stripe.com/docs/api#dispute_object-status).
        fulfilledOn:
          type: string
          format: date-time
          description: >
            If an order was marked as 'fulfilled', then this is the ISO8601
            timestamp when that happened.
        refundedOn:
          type: string
          format: date-time
          description: If an order was refunded, this is the ISO8601 of when that happened.
        customerPaid:
          $ref: '#/components/schemas/OrderAmount'
        netAmount:
          $ref: '#/components/schemas/OrderAmount'
        requiresShipping:
          type: boolean
          description: >
            A boolean indicating whether the order contains one or more
            purchased items that require shipping.
        shippingProvider:
          type: string
          description: >
            A string editable by the API user to note the shipping provider used
            (not used by Webflow).
        shippingTracking:
          type: string
          description: >
            A string editable by the API user to note the shipping tracking
            number for the order (not used by Webflow).
        customerInfo:
          $ref: '#/components/schemas/OrderCustomerInfo'
        allAddresses:
          type: array
          items:
            $ref: '#/components/schemas/OrderAddress'
          description: All addresses provided by the customer during the ordering flow.
        shippingAddress:
          $ref: '#/components/schemas/OrderAddress'
        billingAddress:
          $ref: '#/components/schemas/OrderAddress'
        purchasedItems:
          type: array
          items:
            $ref: '#/components/schemas/OrderPurchasedItem'
          description: An array of all things that the customer purchased.
        stripeDetails:
          $ref: '#/components/schemas/StripeDetails'
        stripeCard:
          $ref: '#/components/schemas/StripeCard'
        totals:
          $ref: '#/components/schemas/OrderTotals'
        customData:
          type: array
          items:
            $ref: '#/components/schemas/OrderCustomDataItems'
          description: >
            An array of additional inputs for custom order data gathering. Each
            object in the array represents an input with a name, and a
            textInput, textArea, or checkbox value.
        downloadFiles:
          type: array
          items:
            $ref: '#/components/schemas/OrderDownloadedFile'
          description: An array of downloadable file objects.
      title: Order
  securitySchemes:
    OAuth2:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python
import requests

url = "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/order/5e8518516e147040726cc415"

headers = {
    "Accept-Version": "1.0.0",
    "Authorization": "Bearer <token>"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/order/5e8518516e147040726cc415';
const options = {
  method: 'GET',
  headers: {'Accept-Version': '1.0.0', Authorization: 'Bearer <token>'}
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

	url := "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/order/5e8518516e147040726cc415"

	req, _ := http.NewRequest("GET", url, nil)

	req.Header.Add("Accept-Version", "1.0.0")
	req.Header.Add("Authorization", "Bearer <token>")

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

url = URI("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/order/5e8518516e147040726cc415")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["Accept-Version"] = '1.0.0'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/order/5e8518516e147040726cc415")
  .header("Accept-Version", "1.0.0")
  .header("Authorization", "Bearer <token>")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/order/5e8518516e147040726cc415', [
  'headers' => [
    'Accept-Version' => '1.0.0',
    'Authorization' => 'Bearer <token>',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/order/5e8518516e147040726cc415");
var request = new RestRequest(Method.GET);
request.AddHeader("Accept-Version", "1.0.0");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept-Version": "1.0.0",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.webflow.com/sites/580e63e98c9a982ac9b8b741/order/5e8518516e147040726cc415")! as URL,
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