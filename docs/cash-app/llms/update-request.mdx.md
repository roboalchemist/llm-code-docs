# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/customer-request-api/update-request.mdx

# Update request

PATCH https://api.cash.app/customer-request/v1/requests/{request_id}
Content-Type: application/json

Updates a customer request. The request must have its `status` in a `PENDING` state to successfully update.

To clear a field, set it to `null`. Fields that are not provided in the request will not be changed.
If updating an array field, the entire contents of the array must be passed.

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/customer-request-api/update-request

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /requests/{request_id}:
    patch:
      operationId: update-request
      summary: Update request
      description: >-
        Updates a customer request. The request must have its `status` in a
        `PENDING` state to successfully update.


        To clear a field, set it to `null`. Fields that are not provided in the
        request will not be changed.

        If updating an array field, the entire contents of the array must be
        passed.
      tags:
        - subpackage_requests
      parameters:
        - name: request_id
          in: path
          required: true
          schema:
            type: string
        - name: Accept
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
                $ref: '#/components/schemas/Requests_update-request_Response_200'
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
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                request:
                  $ref: >-
                    #/components/schemas/RequestsRequestIdPatchRequestBodyContentApplicationJsonSchemaRequest
                  description: Details about the request to update
              required:
                - request
servers:
  - url: https://api.cash.app/customer-request/v1
  - url: https://sandbox.api.cash.app/customer-request/v1
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
    Metadata:
      type: object
      additionalProperties:
        type: string
      description: >-
        Freeform key-value pairs of arbitrary data associated with this
        resource.


        Keys and values must be passed as strings and not contain any personally
        identifiable information (PII).


        Min keys: `0`

        Max keys: `50`


        > Note: Nested keys are not supported.
      title: Metadata
    RequestsRequestIdPatchRequestBodyContentApplicationJsonSchemaRequest:
      type: object
      properties:
        actions:
          type: array
          items:
            $ref: '#/components/schemas/Action'
          description: >-
            A list of the different actions a client intends to take on the
            customer if the request is approved.


            No duplicate action types allowed.


            Min number of items: `1`

            Max number of items: `5`
        reference_id:
          type:
            - string
            - 'null'
          description: >-
            A user-defined identifier for this request, typically used to
            associate the resource with a record in an external system.


            Min length: `1`

            Max length: `1024`
        metadata:
          $ref: '#/components/schemas/Metadata'
      description: Details about the request to update
      title: RequestsRequestIdPatchRequestBodyContentApplicationJsonSchemaRequest
    RequestStatus:
      type: string
      enum:
        - APPROVED
        - DECLINED
        - PENDING
        - PROCESSING
      default: PENDING
      description: >-
        Indicates if the state is approved, declined, or pending. Approved
        requests have grants, while pending and declined grants do not.


        Current values:


        - `PENDING`: The request has been created, but not responded to.

        - `PROCESSING`: The Cash App customer is actively responding to the
        request on their mobile device, and will require time to fill out
        information before the request is approved / declined.

        - `APPROVED`: The request was approved by the customer and grants have
        been created for the provided actions.

        - `DECLINED`: The request was denied by the customer. No grants were
        created.
      title: RequestStatus
    RequestAuthFlowTriggers:
      type: object
      properties:
        qr_code_image_url:
          type: string
          format: uri
          description: >-
            Link to a QR code customers can scan with Cash App to authorize the
            given action, encoded as a PNG file.


            Min length: `8`

            Max length: `1024`
        qr_code_svg_url:
          type: string
          format: uri
          description: >-
            Link to a QR code customers can scan with Cash App to authorize the
            given action, encoded as an SVG file.


            Min length: `8`

            Max length: `1024`
        mobile_url:
          type: string
          format: uri
          description: >-
            If on an Android or iOS device, the URL to redirect customers to in
            order to authorize the given action.


            Min length: `8`

            Max length: `1024`
        refreshes_at:
          type: string
          format: date-time
          description: >-
            When the QR code image URL will be rotated. Generally, it will
            rotate every ~20 seconds and become invalid after 30 seconds.
        desktop_url:
          type: string
          format: uri
          description: >-
            If on a desktop browser, the URL to redirect customers to in order
            to authorize the given action.


            Min length: `8`

            Max length: `1024`
      required:
        - qr_code_image_url
        - qr_code_svg_url
        - mobile_url
        - refreshes_at
      description: >-
        While the request is `PENDING`, contains different methods that can be
        used to start

        the authorization flow in the Cash App mobile application. Its contents
        refresh each time

        the `refreshes_at` timestamp passes. When the

        data refreshes, you should update any buttons

        or QR codes referring to it immediately.


        After a request has been scanned (and is no

        longer in the `PENDING` status), this

        field will no longer be returned.
      title: RequestAuthFlowTriggers
    RequestOriginType:
      type: string
      enum:
        - DIRECT
        - REQUEST_INITIATOR
      description: >-
        The method used to create the customer request.


        - `DIRECT` - the client or SDKs created this customer request by calling
        the "CreateCustomerRequest" endpoint

        - `REQUEST_INITIATOR` - a customer interacted with a request initiator
        and caused Cash App to create a customer request.
      title: RequestOriginType
    RequestOrigin:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/RequestOriginType'
          description: >-
            The method used to create the customer request.


            - `DIRECT` - the client or SDKs created this customer request by
            calling the "CreateCustomerRequest" endpoint

            - `REQUEST_INITIATOR` - a customer interacted with a request
            initiator and caused Cash App to create a customer request.
        id:
          type: string
          description: |-
            If present, is the ID of the initiator used to create this request.

            Min length: `1`
            Max length: `128`
      required:
        - type
      description: Metadata describing how the customer request was created.
      title: RequestOrigin
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
    RequestRequesterProfile:
      type: object
      properties:
        name:
          type: string
          description: |-
            Name of the brand to be shown in Cash App next to payments.

            Min length: `1`
            Max length: `1024`
        logo_url:
          type: string
          format: uri
          description: >-
            URL to the image of the entity (brand or client) that is requesting
            permission to perform the actions on the customer request.


            Formats:

            - `.jpg`

            - `.jpeg`

            - `.png`


            Min length: `8`

            Max length: `8000`
      required:
        - name
        - logo_url
      description: >-
        Details about the brand or client that are requesting permission to
        perform the actions on the customer request.
      title: RequestRequesterProfile
    RequestCustomerProfile:
      type: object
      properties:
        id:
          type: string
          description: |-
            Unique identifier for this customer issued by Cash App.

            Min length: `1`
            Max length: `128`
        cashtag:
          type: string
          description: >-
            Public identifier for the customer on Cash App. [Learn
            more](https://cash.app/help/us/en-us/3123-cashtags).


            Min length: `1`

            Max length: `1024`
      required:
        - id
        - cashtag
      description: >-
        If the customer request was approved, contains the identity of the Cash
        App customer that approved it.
      title: RequestCustomerProfile
    CustomerMetadata:
      type: object
      properties:
        reference_id:
          type: string
          description: >-
            The `reference_id` of the customer approving this request. When a
            customer approves this request, that customer will be associated
            with this `reference_id`.
      description: Metadata to associate with the customer that approves this request.
      title: CustomerMetadata
    Request:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the request issued by Cash App.

            Min length: `1`
            Max length: `128`
        status:
          $ref: '#/components/schemas/RequestStatus'
          description: >-
            Indicates if the state is approved, declined, or pending. Approved
            requests have grants, while pending and declined grants do not.


            Current values:


            - `PENDING`: The request has been created, but not responded to.

            - `PROCESSING`: The Cash App customer is actively responding to the
            request on their mobile device, and will require time to fill out
            information before the request is approved / declined.

            - `APPROVED`: The request was approved by the customer and grants
            have been created for the provided actions.

            - `DECLINED`: The request was denied by the customer. No grants were
            created.
        actions:
          type: array
          items:
            $ref: '#/components/schemas/Action'
          description: >-
            Represents what the client intends to do to a customer if given
            authorization.


            No duplicate action types allowed.


            Min number of items: `1`

            Max number of items: `5`
        auth_flow_triggers:
          $ref: '#/components/schemas/RequestAuthFlowTriggers'
          description: >-
            While the request is `PENDING`, contains different methods that can
            be used to start

            the authorization flow in the Cash App mobile application. Its
            contents refresh each time

            the `refreshes_at` timestamp passes. When the

            data refreshes, you should update any buttons

            or QR codes referring to it immediately.


            After a request has been scanned (and is no

            longer in the `PENDING` status), this

            field will no longer be returned.
        redirect_url:
          type: string
          format: uri
          description: >-
            If this request is responded to via mobile redirect, this field
            specifies the URL that Cash App will open for a customer in the
            mobile device's default browser after the request is approved or
            declined.
        created_at:
          type: string
          format: date-time
          description: >-
            When this customer request was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        updated_at:
          type: string
          format: date-time
          description: >-
            When the customer request was last updated, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        expires_at:
          type: string
          format: date-time
          description: >-
            When this customer request will be automatically declined by Cash
            App, in [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339)
            format (UTC).
        origin:
          $ref: '#/components/schemas/RequestOrigin'
          description: Metadata describing how the customer request was created.
        channel:
          $ref: '#/components/schemas/Channel'
        grants:
          type: array
          items:
            $ref: '#/components/schemas/Grant'
          description: >-
            If present, contains grants that can be used to perform actions
            specified in the request using the Network API.


            Each grant corresponds directly to an action on the request.


            Min number of items: `1`

            Max number of items: `5`
        reference_id:
          type: string
          description: >-
            A user-defined identifier for this request, typically used to
            associate the resource with a record in an external system.


            Min length: `1`

            Max length: `1024`
        requester_profile:
          $ref: '#/components/schemas/RequestRequesterProfile'
          description: >-
            Details about the brand or client that are requesting permission to
            perform the actions on the customer request.
        customer_profile:
          $ref: '#/components/schemas/RequestCustomerProfile'
          description: >-
            If the customer request was approved, contains the identity of the
            Cash App customer that approved it.
        metadata:
          $ref: '#/components/schemas/Metadata'
        customer_metadata:
          $ref: '#/components/schemas/CustomerMetadata'
      required:
        - id
        - status
        - actions
        - redirect_url
        - created_at
        - updated_at
        - expires_at
        - origin
        - channel
      description: >-
        Describes a request from a client to perform a given action on a
        customer's account.
      title: Request
    Requests_update-request_Response_200:
      type: object
      properties:
        request:
          $ref: '#/components/schemas/Request'
      required:
        - request
      title: Requests_update-request_Response_200
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

```python Request with One Time Payment Action
import requests

url = "https://api.cash.app/customer-request/v1/requests/request_id"

headers = {
    "Accept": "Accept",
    "User-Agent": "User-Agent",
    "Content-Type": "application/json"
}

response = requests.patch(url, headers=headers)

print(response.json())
```

```javascript Request with One Time Payment Action
const url = 'https://api.cash.app/customer-request/v1/requests/request_id';
const options = {
  method: 'PATCH',
  headers: {
    Accept: 'Accept',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: undefined
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Request with One Time Payment Action
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/customer-request/v1/requests/request_id"

	req, _ := http.NewRequest("PATCH", url, nil)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Request with One Time Payment Action
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/customer-request/v1/requests/request_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Accept"] = 'Accept'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'

response = http.request(request)
puts response.read_body
```

```java Request with One Time Payment Action
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.cash.app/customer-request/v1/requests/request_id")
  .header("Accept", "Accept")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .asString();
```

```php Request with One Time Payment Action
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.cash.app/customer-request/v1/requests/request_id', [
  'headers' => [
    'Accept' => 'Accept',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp Request with One Time Payment Action
using RestSharp;

var client = new RestClient("https://api.cash.app/customer-request/v1/requests/request_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Accept", "Accept");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
IRestResponse response = client.Execute(request);
```

```swift Request with One Time Payment Action
import Foundation

let headers = [
  "Accept": "Accept",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/customer-request/v1/requests/request_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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

```python Request with On File Payment Action
import requests

url = "https://api.cash.app/customer-request/v1/requests/request_id"

headers = {
    "Accept": "Accept",
    "User-Agent": "User-Agent",
    "Content-Type": "application/json"
}

response = requests.patch(url, headers=headers)

print(response.json())
```

```javascript Request with On File Payment Action
const url = 'https://api.cash.app/customer-request/v1/requests/request_id';
const options = {
  method: 'PATCH',
  headers: {
    Accept: 'Accept',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: undefined
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Request with On File Payment Action
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/customer-request/v1/requests/request_id"

	req, _ := http.NewRequest("PATCH", url, nil)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Request with On File Payment Action
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/customer-request/v1/requests/request_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Accept"] = 'Accept'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'

response = http.request(request)
puts response.read_body
```

```java Request with On File Payment Action
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.cash.app/customer-request/v1/requests/request_id")
  .header("Accept", "Accept")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .asString();
```

```php Request with On File Payment Action
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.cash.app/customer-request/v1/requests/request_id', [
  'headers' => [
    'Accept' => 'Accept',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp Request with On File Payment Action
using RestSharp;

var client = new RestClient("https://api.cash.app/customer-request/v1/requests/request_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Accept", "Accept");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
IRestResponse response = client.Execute(request);
```

```swift Request with On File Payment Action
import Foundation

let headers = [
  "Accept": "Accept",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/customer-request/v1/requests/request_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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

```python Request with Link Account Action
import requests

url = "https://api.cash.app/customer-request/v1/requests/request_id"

headers = {
    "Accept": "Accept",
    "User-Agent": "User-Agent",
    "Content-Type": "application/json"
}

response = requests.patch(url, headers=headers)

print(response.json())
```

```javascript Request with Link Account Action
const url = 'https://api.cash.app/customer-request/v1/requests/request_id';
const options = {
  method: 'PATCH',
  headers: {
    Accept: 'Accept',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: undefined
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Request with Link Account Action
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/customer-request/v1/requests/request_id"

	req, _ := http.NewRequest("PATCH", url, nil)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Request with Link Account Action
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/customer-request/v1/requests/request_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Accept"] = 'Accept'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'

response = http.request(request)
puts response.read_body
```

```java Request with Link Account Action
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.cash.app/customer-request/v1/requests/request_id")
  .header("Accept", "Accept")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .asString();
```

```php Request with Link Account Action
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.cash.app/customer-request/v1/requests/request_id', [
  'headers' => [
    'Accept' => 'Accept',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp Request with Link Account Action
using RestSharp;

var client = new RestClient("https://api.cash.app/customer-request/v1/requests/request_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Accept", "Accept");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
IRestResponse response = client.Execute(request);
```

```swift Request with Link Account Action
import Foundation

let headers = [
  "Accept": "Accept",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/customer-request/v1/requests/request_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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

```python Sample request with metadata
import requests

url = "https://api.cash.app/customer-request/v1/requests/request_id"

payload = { "request": {
        "actions": [
            {
                "amount": 2500,
                "currency": "USD",
                "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
                "type": "ONE_TIME_PAYMENT"
            }
        ],
        "reference_id": "string",
        "metadata": { "key": "value" }
    } }
headers = {
    "Accept": "Accept",
    "User-Agent": "User-Agent",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript Sample request with metadata
const url = 'https://api.cash.app/customer-request/v1/requests/request_id';
const options = {
  method: 'PATCH',
  headers: {
    Accept: 'Accept',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"request":{"actions":[{"amount":2500,"currency":"USD","scope_id":"MMI_4vxs5egfk7hmta3qx2h6rp91x","type":"ONE_TIME_PAYMENT"}],"reference_id":"string","metadata":{"key":"value"}}}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Sample request with metadata
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/customer-request/v1/requests/request_id"

	payload := strings.NewReader("{\n  \"request\": {\n    \"actions\": [\n      {\n        \"amount\": 2500,\n        \"currency\": \"USD\",\n        \"scope_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n        \"type\": \"ONE_TIME_PAYMENT\"\n      }\n    ],\n    \"reference_id\": \"string\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Sample request with metadata
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/customer-request/v1/requests/request_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Accept"] = 'Accept'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"request\": {\n    \"actions\": [\n      {\n        \"amount\": 2500,\n        \"currency\": \"USD\",\n        \"scope_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n        \"type\": \"ONE_TIME_PAYMENT\"\n      }\n    ],\n    \"reference_id\": \"string\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java Sample request with metadata
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.cash.app/customer-request/v1/requests/request_id")
  .header("Accept", "Accept")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"request\": {\n    \"actions\": [\n      {\n        \"amount\": 2500,\n        \"currency\": \"USD\",\n        \"scope_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n        \"type\": \"ONE_TIME_PAYMENT\"\n      }\n    ],\n    \"reference_id\": \"string\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}")
  .asString();
```

```php Sample request with metadata
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.cash.app/customer-request/v1/requests/request_id', [
  'body' => '{
  "request": {
    "actions": [
      {
        "amount": 2500,
        "currency": "USD",
        "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
        "type": "ONE_TIME_PAYMENT"
      }
    ],
    "reference_id": "string",
    "metadata": {
      "key": "value"
    }
  }
}',
  'headers' => [
    'Accept' => 'Accept',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp Sample request with metadata
using RestSharp;

var client = new RestClient("https://api.cash.app/customer-request/v1/requests/request_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Accept", "Accept");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"request\": {\n    \"actions\": [\n      {\n        \"amount\": 2500,\n        \"currency\": \"USD\",\n        \"scope_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n        \"type\": \"ONE_TIME_PAYMENT\"\n      }\n    ],\n    \"reference_id\": \"string\",\n    \"metadata\": {\n      \"key\": \"value\"\n    }\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Sample request with metadata
import Foundation

let headers = [
  "Accept": "Accept",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]
let parameters = ["request": [
    "actions": [
      [
        "amount": 2500,
        "currency": "USD",
        "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
        "type": "ONE_TIME_PAYMENT"
      ]
    ],
    "reference_id": "string",
    "metadata": ["key": "value"]
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/customer-request/v1/requests/request_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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

```python Sample request without metadata
import requests

url = "https://api.cash.app/customer-request/v1/requests/request_id"

payload = { "request": {
        "actions": [
            {
                "amount": 2500,
                "currency": "USD",
                "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
                "type": "ONE_TIME_PAYMENT"
            }
        ],
        "reference_id": "string"
    } }
headers = {
    "Accept": "Accept",
    "User-Agent": "User-Agent",
    "Content-Type": "application/json"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript Sample request without metadata
const url = 'https://api.cash.app/customer-request/v1/requests/request_id';
const options = {
  method: 'PATCH',
  headers: {
    Accept: 'Accept',
    'User-Agent': 'User-Agent',
    'Content-Type': 'application/json'
  },
  body: '{"request":{"actions":[{"amount":2500,"currency":"USD","scope_id":"MMI_4vxs5egfk7hmta3qx2h6rp91x","type":"ONE_TIME_PAYMENT"}],"reference_id":"string"}}'
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go Sample request without metadata
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/customer-request/v1/requests/request_id"

	payload := strings.NewReader("{\n  \"request\": {\n    \"actions\": [\n      {\n        \"amount\": 2500,\n        \"currency\": \"USD\",\n        \"scope_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n        \"type\": \"ONE_TIME_PAYMENT\"\n      }\n    ],\n    \"reference_id\": \"string\"\n  }\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("User-Agent", "User-Agent")
	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby Sample request without metadata
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/customer-request/v1/requests/request_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
request["Accept"] = 'Accept'
request["User-Agent"] = 'User-Agent'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"request\": {\n    \"actions\": [\n      {\n        \"amount\": 2500,\n        \"currency\": \"USD\",\n        \"scope_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n        \"type\": \"ONE_TIME_PAYMENT\"\n      }\n    ],\n    \"reference_id\": \"string\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java Sample request without metadata
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("https://api.cash.app/customer-request/v1/requests/request_id")
  .header("Accept", "Accept")
  .header("User-Agent", "User-Agent")
  .header("Content-Type", "application/json")
  .body("{\n  \"request\": {\n    \"actions\": [\n      {\n        \"amount\": 2500,\n        \"currency\": \"USD\",\n        \"scope_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n        \"type\": \"ONE_TIME_PAYMENT\"\n      }\n    ],\n    \"reference_id\": \"string\"\n  }\n}")
  .asString();
```

```php Sample request without metadata
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'https://api.cash.app/customer-request/v1/requests/request_id', [
  'body' => '{
  "request": {
    "actions": [
      {
        "amount": 2500,
        "currency": "USD",
        "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
        "type": "ONE_TIME_PAYMENT"
      }
    ],
    "reference_id": "string"
  }
}',
  'headers' => [
    'Accept' => 'Accept',
    'Content-Type' => 'application/json',
    'User-Agent' => 'User-Agent',
  ],
]);

echo $response->getBody();
```

```csharp Sample request without metadata
using RestSharp;

var client = new RestClient("https://api.cash.app/customer-request/v1/requests/request_id");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Accept", "Accept");
request.AddHeader("User-Agent", "User-Agent");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"request\": {\n    \"actions\": [\n      {\n        \"amount\": 2500,\n        \"currency\": \"USD\",\n        \"scope_id\": \"MMI_4vxs5egfk7hmta3qx2h6rp91x\",\n        \"type\": \"ONE_TIME_PAYMENT\"\n      }\n    ],\n    \"reference_id\": \"string\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift Sample request without metadata
import Foundation

let headers = [
  "Accept": "Accept",
  "User-Agent": "User-Agent",
  "Content-Type": "application/json"
]
let parameters = ["request": [
    "actions": [
      [
        "amount": 2500,
        "currency": "USD",
        "scope_id": "MMI_4vxs5egfk7hmta3qx2h6rp91x",
        "type": "ONE_TIME_PAYMENT"
      ]
    ],
    "reference_id": "string"
  ]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/customer-request/v1/requests/request_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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