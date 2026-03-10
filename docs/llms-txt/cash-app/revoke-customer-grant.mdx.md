# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/revoke-customer-grant.mdx

# Revoke customer grant

POST https://api.cash.app/network/v1/customers/{customer_id}/grants/{grant_id}/revoke

Revokes a customer grant, rendering it unusable. Other endpoints will no longer be able to use the grant to perform its associated action.

<Note> 
You cannot un-revoke a grant. Use with caution.
</Note>

**This endpoint is not rate limited.**

Scopes: `GRANTS_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/revoke-customer-grant

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /customers/{customer_id}/grants/{grant_id}/revoke:
    post:
      operationId: revoke-customer-grant
      summary: Revoke customer grant
      description: >-
        Revokes a customer grant, rendering it unusable. Other endpoints will no
        longer be able to use the grant to perform its associated action.


        <Note> 

        You cannot un-revoke a grant. Use with caution.

        </Note>


        **This endpoint is not rate limited.**


        Scopes: `GRANTS_WRITE`
      tags:
        - subpackage_customers
      parameters:
        - name: customer_id
          in: path
          required: true
          schema:
            type: string
        - name: grant_id
          in: path
          required: true
          schema:
            type: string
        - name: Accept
          in: header
          required: true
          schema:
            type: string
        - name: X-Region
          in: header
          required: true
          schema:
            type: string
        - name: X-Signature
          in: header
          required: true
          schema:
            type: string
        - name: User-Agent
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Customers_revoke-customer-grant_Response_200
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.cash.app/network/v1
  - url: https://sandbox.api.cash.app/network/v1
components:
  schemas:
    Currency:
      type: string
      enum:
        - USD
      description: >-
        Indicates the country associated with an entity. Values are from the
        [ISO-4217 Alpha-3](https://www.iso.org/iso-4217-currency-codes.html)
        specification.


        Current values:


        - `USD`: United States Dollar
      title: Currency
    OneTimePaymentActionType:
      type: string
      enum:
        - ONE_TIME_PAYMENT
      description: The type of the action (`ONE_TIME_PAYMENT`).
      title: OneTimePaymentActionType
    OneTimePaymentAction:
      type: object
      properties:
        amount:
          type: integer
          description: >-
            Amount to charge the customer, in the lowest unit of the associated
            currency.


            Min value: `1`
        currency:
          $ref: '#/components/schemas/Currency'
        scope_id:
          type: string
          description: >-
            ID of the client, brand, or merchant that will charge the customer.


            If a client ID is passed, the grant from this action can be used to
            create a payment for any merchant owned by the client.


            If a brand ID is passed, the grant from this action can be used to
            create a payment for any merchant that has a matching brand ID.


            If a merchant ID is passed, the grant from this action can be used
            to create a payment for the merchant with a matching ID.


            Min length: `1`

            Max length: `128`
        type:
          $ref: '#/components/schemas/OneTimePaymentActionType'
          description: The type of the action (`ONE_TIME_PAYMENT`).
      required:
        - scope_id
        - type
      description: >-
        Describes an intent for a client to charge a customer a given amount.


        Note the following restrictions when using this action:


        - If no amount is provided to the action, the payment charged may be
        **any** amount.

        - If `amount` is provided, `currency` must be provided too (and vice
        versa).
      title: OneTimePaymentAction
    OnFilePaymentActionType:
      type: string
      enum:
        - ON_FILE_PAYMENT
      default: ON_FILE_PAYMENT
      description: The type of the action (`ON_FILE_PAYMENT`).
      title: OnFilePaymentActionType
    OnFilePaymentAction:
      type: object
      properties:
        scope_id:
          type: string
          description: >-
            ID of the client or brand that will charge customers.


            If a client ID is passed, the grant from this action can be used to
            create a payment for any merchant owned by the client.


            If a brand ID is passed, the grant from this action can be used to
            create a payment for any merchant that has a matching brand ID.


            Merchant IDs may *not* be passed.


            Min length: `1`

            Max length: `128`
        type:
          $ref: '#/components/schemas/OnFilePaymentActionType'
          description: The type of the action (`ON_FILE_PAYMENT`).
        account_reference_id:
          type: string
          description: >-
            Identifier of the account or customer associated to the on file
            action.
      required:
        - scope_id
        - type
      description: "Describes an\_intent for a client to store a customer's account, allowing a client to create payments or issue refunds for it on a recurring basis."
      title: OnFilePaymentAction
    OnFileDepositActionType:
      type: string
      enum:
        - ON_FILE_DEPOSIT
      description: The type of the action (`ON_FILE_DEPOSIT`).
      title: OnFileDepositActionType
    OnFileDepositAction:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/OnFileDepositActionType'
          description: The type of the action (`ON_FILE_DEPOSIT`).
        scope_id:
          type: string
          description: >-
            ID of the client or brand that indicates the set of merchants that
            will deposit to customers.


            If a client ID is passed, the grant from this action can be used to
            create a deposit for any merchant owned by the client.


            If a brand ID is passed, the grant from this action can be used to
            create a deposit for any merchant that has a matching brand ID.

            Min length: `1`

            Max length: `128`
        account_reference_id:
          type: string
          description: >-
            Identifier of the account or customer associated to the on file
            action.
      required:
        - type
        - scope_id
        - account_reference_id
      description: >-
        Describes an intent for a client to deposit funds into the Cash App
        account balances in perpetuity until the Cash App account revokes the
        grant.
      title: OnFileDepositAction
    LinkAccountActionType:
      type: string
      enum:
        - LINK_ACCOUNT
      description: The type of the action (`LINK_ACCOUNT`).
      title: LinkAccountActionType
    LinkAccountAction:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/LinkAccountActionType'
          description: The type of the action (`LINK_ACCOUNT`).
      required:
        - type
      description: "Describes an\_intent for a client to manage a customer's merchant profiles in Cash App."
      title: LinkAccountAction
    Action:
      oneOf:
        - $ref: '#/components/schemas/OneTimePaymentAction'
        - $ref: '#/components/schemas/OnFilePaymentAction'
        - $ref: '#/components/schemas/OnFileDepositAction'
        - $ref: '#/components/schemas/LinkAccountAction'
      description: >-
        Represents what the client intends to do to a customer if given
        authorization.
      title: Action
    GrantStatus:
      type: string
      enum:
        - ACTIVE
        - CONSUMED
        - REVOKED
        - EXPIRED
      description: >-
        Describes whether or not this grant can be used to perform the action
        associated with it.


        If `ACTIVE`, it can be used to perform the action.


        If `EXPIRED`, it may no longer be used to perform the action due to the
        current time being past the "expires_at" time.


        If `CONSUMED`, it was already redeemed to perform the action and cannot
        be used again.


        If `REVOKED`, the customer or merchant explicitly unauthorized the
        grant, preventing it from being used to perform the action.
      title: GrantStatus
    GrantType:
      type: string
      enum:
        - ONE_TIME
        - EXTENDED
      description: >-
        Describes whether this grant can be only be used once (`ONE_TIME`) or
        repeatedly (`EXTENDED`).
      title: GrantType
    Channel:
      type: string
      enum:
        - IN_PERSON
        - ONLINE
        - IN_APP
      description: >-
        How the customer is expected to interact with the request.


        - `IN_PERSON`: The customer presents or scans a QR code at a physical
        location to approve the request.

        - `ONLINE`: The customer scans a QR code or is redirected to Cash App
        from a browser context.

        - `IN_APP`: The customer scans a QR code or is redirected to Cash App
        from a native mobile application context.
      title: Channel
    Grant:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this grant issued by Cash App.

            Min length: `1`
            Max length: `256`
        customer_id:
          type: string
          description: |-
            ID of the customer that approved this grant.

            Min length: `1`
            Max length: `128`
        request_id:
          type: string
          description: >-
            A unique identifier issued by Cash App for the customer request that
            resulted in the creation of this grant.


            Min length: `1`

            Max length: `128`
        action:
          $ref: '#/components/schemas/Action'
        status:
          $ref: '#/components/schemas/GrantStatus'
          description: >-
            Describes whether or not this grant can be used to perform the
            action associated with it.


            If `ACTIVE`, it can be used to perform the action.


            If `EXPIRED`, it may no longer be used to perform the action due to
            the current time being past the "expires_at" time.


            If `CONSUMED`, it was already redeemed to perform the action and
            cannot be used again.


            If `REVOKED`, the customer or merchant explicitly unauthorized the
            grant, preventing it from being used to perform the action.
        type:
          $ref: '#/components/schemas/GrantType'
          description: >-
            Describes whether this grant can be only be used once (`ONE_TIME`)
            or repeatedly (`EXTENDED`).
        channel:
          $ref: '#/components/schemas/Channel'
        created_at:
          type: string
          format: date-time
          description: >-
            When this grant was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When this grant was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        expires_at:
          type: string
          format: date-time
          description: >-
            If present, indicates when the grant's status will become `EXPIRED`,
            preventing a client from using it to create payments or refunds.


            The timestamp is in the [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
      required:
        - id
        - customer_id
        - request_id
        - action
        - status
        - type
        - channel
        - created_at
        - updated_at
      description: >-
        Describes a grant that can be used to perform actions specified in a
        customer request using the Network API.
      title: Grant
    Customers_revoke-customer-grant_Response_200:
      type: object
      properties:
        grant:
          $ref: '#/components/schemas/Grant'
      required:
        - grant
      title: Customers_revoke-customer-grant_Response_200
    ErrorCategory:
      type: string
      enum:
        - API_ERROR
        - AUTHENTICATION_ERROR
        - BRAND_ERROR
        - DISPUTE_ERROR
        - MERCHANT_ERROR
        - INVALID_REQUEST_ERROR
        - PAYMENT_PROCESSING_ERROR
        - RATE_LIMIT_ERROR
        - WEBHOOK_ERROR
        - API_KEY_ERROR
        - GRANT_ERROR
      description: The high-level reason the error occurred
      title: ErrorCategory
    Error:
      type: object
      properties:
        category:
          $ref: '#/components/schemas/ErrorCategory'
          description: The high-level reason the error occurred
        code:
          type: string
          description: >-
            A unique identifier for the specific type of error that occurred.
            See the Error Code Reference for more information.


            Min length: `1`
        detail:
          type: string
          description: >-
            Human-readable description of why the error occurred and how to
            resolve it.


            Min length: `1`
        field:
          type: string
          description: >-
            The field in the request that caused the error, using array and
            object dot notation.


            Min length: `1`
      required:
        - category
        - code
      description: Represents an error encountered during a request to the API.
      title: Error
    ErrorResponse:
      type: object
      properties:
        errors:
          type: array
          items:
            $ref: '#/components/schemas/Error'
          description: |-
            A list of errors that occurred while processing the request.

            Min number of items: `1`
      required:
        - errors
      title: ErrorResponse

```

## SDK Code Examples

```python
import requests

url = "https://api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke"

headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent"
}

response = requests.post(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke';
const options = {
  method: 'POST',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent'
  }
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

	url := "https://api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke"

	req, _ := http.NewRequest("POST", url, nil)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("X-Region", "X-Region")
	req.Header.Add("X-Signature", "X-Signature")
	req.Header.Add("User-Agent", "User-Agent")

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

url = URI("https://api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("https://api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke', [
  'headers' => [
    'Accept' => 'Accept',
    'User-Agent' => 'User-Agent',
    'X-Region' => 'X-Region',
    'X-Signature' => 'X-Signature',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke");
var request = new RestRequest(Method.POST);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/customers/customer_id/grants/grant_id/revoke")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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