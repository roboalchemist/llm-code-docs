# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/list-dispute-evidence.mdx

# List dispute evidence

GET https://api.cash.app/network/v1/disputes/{dispute_id}/evidence

Returns a list of all pieces of evidence associated with the given dispute.

**This endpoint is rate limited to 50 QPS.**

Scopes: `DISPUTES_READ`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/network-api/list-dispute-evidence

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /disputes/{dispute_id}/evidence:
    get:
      operationId: list-dispute-evidence
      summary: List dispute evidence
      description: >-
        Returns a list of all pieces of evidence associated with the given
        dispute.


        **This endpoint is rate limited to 50 QPS.**


        Scopes: `DISPUTES_READ`
      tags:
        - subpackage_disputes
      parameters:
        - name: dispute_id
          in: path
          required: true
          schema:
            type: string
        - name: cursor
          in: query
          description: >-
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the
            original query.
          required: false
          schema:
            type: string
        - name: limit
          in: query
          description: Maximum number of pieces of dispute evidence to return
          required: false
          schema:
            type: integer
            default: 50
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
                  #/components/schemas/Disputes_list-dispute-evidence_Response_200
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
servers:
  - url: https://api.cash.app/network/v1
  - url: https://sandbox.api.cash.app/network/v1
components:
  schemas:
    DisputeEvidenceCategory:
      type: string
      enum:
        - GENERIC_EVIDENCE
        - ONLINE_OR_APP_ACCESS_LOG
        - AUTHORIZATION_DOCUMENTATION
        - CANCELLATION_OR_REFUND_DOCUMENTATION
        - CARDHOLDER_COMMUNICATION
        - CARDHOLDER_INFORMATION
        - PURCHASE_ACKNOWLEDGEMENT
        - DUPLICATE_CHARGE_DOCUMENTATION
        - PRODUCT_OR_SERVICE_DESCRIPTION
        - RECEIPT
        - SERVICE_RECEIVED_DOCUMENTATION
        - PROOF_OF_DELIVERY_DOCUMENTATION
        - RELATED_TRANSACTION_DOCUMENTATION
        - REBUTTAL_EXPLANATION
        - TRACKING_NUMBER
      description: >-
        Describes what type of information is contained in this piece of
        evidence.


        Current values:


        - `GENERIC_EVIDENCE`: Default evidence type used if no other category
        applies.

        - `ONLINE_OR_APP_ACCESS_LOG`: Server or activity logs that show proof of
        the cardholder’s identity and that the cardholder successfully ordered
        and received the goods (digitally or otherwise). Example evidence
        includes IP addresses, corresponding timestamps/dates, cardholder’s name
        and email address linked to a cardholder profile held by the seller,
        proof the same device and card (used in dispute) were previously used in
        prior undisputed transaction, and any related detailed activity.

        - `AUTHORIZATION_DOCUMENTATION`: **[File Only]** Evidence that the
        cardholder did provide authorization for the charge. Example evidence
        includes a signed credit card authorization.

        - `CANCELLATION_OR_REFUND_DOCUMENTATION`: Evidence that the cardholder
        acknowledged your refund or cancellation policy. Example evidence
        includes a signature or checkbox showing the cardholder’s
        acknowledgement of your refund or cancellation policy.

        - `CARDHOLDER_COMMUNICATION`: **[File Only]** Evidence that shows
        relevant communication with the cardholder. Example evidence includes
        emails or texts that show the cardholder received goods/services or
        demonstrate cardholder satisfaction.

        - `CARDHOLDER_INFORMATION`: Evidence that validates the customer's
        identity. Example evidence includes personally identifiable details such
        as name, email address, purchaser IP address, and a copy of the
        cardholder ID.

        - `PURCHASE_ACKNOWLEDGEMENT`: Evidence that shows proof of the
        sale/transaction. Example evidence includes an invoice, contract, or
        other item showing the customer’s acknowledgement of the purchase and
        your terms.

        - `DUPLICATE_CHARGE_DOCUMENTATION`: **[File Only]** Evidence that shows
        the charges in question are valid and distinct from one another. Example
        evidence includes receipts, shipping labels, and invoices along with
        their distinct payment IDs.

        - `PRODUCT_OR_SERVICE_DESCRIPTION`: A description of the product or
        service sold.

        - `RECEIPT`: A receipt or message sent to the cardholder detailing the
        charge. Note: You do not need to upload the Square receipt; Square
        submits the receipt on your behalf.

        - `SERVICE_RECEIVED_DOCUMENTATION`: Evidence that the service was
        provided to the cardholder or the expected date that services will be
        rendered. Example evidence includes a signed delivery form, work order,
        expected delivery date, or other written agreements.

        - `PROOF_OF_DELIVERY_DOCUMENTATION`: Evidence that shows the product was
        provided to the cardholder or the expected date of delivery. Example
        evidence includes a signed delivery form or written agreement
        acknowledging receipt of the goods or services.

        - `RELATED_TRANSACTION_DOCUMENTATION`: Evidence that shows the
        cardholder previously processed transactions on the same card and did
        not dispute them.

        - `REBUTTAL_EXPLANATION`: An explanation of why the cardholder’s claim
        is invalid. Example evidence includes an explanation of why each
        distinct charge is a legitimate purchase, why the cardholder’s claim for
        credit owed due to their attempt to cancel, return, or refund is invalid
        per your stated policy and cardholder agreement, or an explanation of
        how the cardholder did not attempt to remedy the issue with you first to
        receive credit.

        - `TRACKING_NUMBER`: The tracking number for the order provided by the
        shipping carrier. If you have multiple numbers, they need to be
        submitted individually as separate pieces of evidence.
      title: DisputeEvidenceCategory
    DisputeEvidenceFileContentType:
      type: string
      enum:
        - application/pdf
        - image/heic
        - image/heif
        - image/jpeg
        - image/png
        - image/tiff
      description: |-
        The MIME type of the uploaded file.

        Current values:

        - `application/pdf`
        - `image/heic`
        - `image/heif`
        - `image/jpeg`
        - `image/png`
        - `image/tiff`
      title: DisputeEvidenceFileContentType
    DisputeEvidenceFile:
      type: object
      properties:
        filename:
          type: string
          description: >-
            Name of the uploaded file. It should be descriptive enough to
            indicate what type of information is contained in the uploaded file.
        content_type:
          $ref: '#/components/schemas/DisputeEvidenceFileContentType'
          description: |-
            The MIME type of the uploaded file.

            Current values:

            - `application/pdf`
            - `image/heic`
            - `image/heif`
            - `image/jpeg`
            - `image/png`
            - `image/tiff`
      required:
        - filename
        - content_type
      description: >-
        If the evidence is of type `FILE`, contains metadata about the binary
        file uploaded as evidence.
      title: DisputeEvidenceFile
    DisputeEvidenceType:
      type: string
      enum:
        - FILE
        - TEXT
      description: |-
        Indicates if the evidence is a file or plain text.

        Current values:
        - `TEXT`: The evidence is a blob of text under 500 characters.
        - `FILE`: The evidence is an uploaded binary file.
      title: DisputeEvidenceType
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
    DisputeEvidence:
      type: object
      properties:
        id:
          type: string
          description: |-
            A unique identifier for the dispute evidence issued by Cash App.

            Min length: `1`
            Max length: `128`
        dispute_id:
          type: string
          description: |-
            ID of the dispute this evidence is associated with.

            Min length: `1`
            Max length: `128`
        category:
          $ref: '#/components/schemas/DisputeEvidenceCategory'
          description: >-
            Describes what type of information is contained in this piece of
            evidence.


            Current values:


            - `GENERIC_EVIDENCE`: Default evidence type used if no other
            category applies.

            - `ONLINE_OR_APP_ACCESS_LOG`: Server or activity logs that show
            proof of the cardholder’s identity and that the cardholder
            successfully ordered and received the goods (digitally or
            otherwise). Example evidence includes IP addresses, corresponding
            timestamps/dates, cardholder’s name and email address linked to a
            cardholder profile held by the seller, proof the same device and
            card (used in dispute) were previously used in prior undisputed
            transaction, and any related detailed activity.

            - `AUTHORIZATION_DOCUMENTATION`: **[File Only]** Evidence that the
            cardholder did provide authorization for the charge. Example
            evidence includes a signed credit card authorization.

            - `CANCELLATION_OR_REFUND_DOCUMENTATION`: Evidence that the
            cardholder acknowledged your refund or cancellation policy. Example
            evidence includes a signature or checkbox showing the cardholder’s
            acknowledgement of your refund or cancellation policy.

            - `CARDHOLDER_COMMUNICATION`: **[File Only]** Evidence that shows
            relevant communication with the cardholder. Example evidence
            includes emails or texts that show the cardholder received
            goods/services or demonstrate cardholder satisfaction.

            - `CARDHOLDER_INFORMATION`: Evidence that validates the customer's
            identity. Example evidence includes personally identifiable details
            such as name, email address, purchaser IP address, and a copy of the
            cardholder ID.

            - `PURCHASE_ACKNOWLEDGEMENT`: Evidence that shows proof of the
            sale/transaction. Example evidence includes an invoice, contract, or
            other item showing the customer’s acknowledgement of the purchase
            and your terms.

            - `DUPLICATE_CHARGE_DOCUMENTATION`: **[File Only]** Evidence that
            shows the charges in question are valid and distinct from one
            another. Example evidence includes receipts, shipping labels, and
            invoices along with their distinct payment IDs.

            - `PRODUCT_OR_SERVICE_DESCRIPTION`: A description of the product or
            service sold.

            - `RECEIPT`: A receipt or message sent to the cardholder detailing
            the charge. Note: You do not need to upload the Square receipt;
            Square submits the receipt on your behalf.

            - `SERVICE_RECEIVED_DOCUMENTATION`: Evidence that the service was
            provided to the cardholder or the expected date that services will
            be rendered. Example evidence includes a signed delivery form, work
            order, expected delivery date, or other written agreements.

            - `PROOF_OF_DELIVERY_DOCUMENTATION`: Evidence that shows the product
            was provided to the cardholder or the expected date of delivery.
            Example evidence includes a signed delivery form or written
            agreement acknowledging receipt of the goods or services.

            - `RELATED_TRANSACTION_DOCUMENTATION`: Evidence that shows the
            cardholder previously processed transactions on the same card and
            did not dispute them.

            - `REBUTTAL_EXPLANATION`: An explanation of why the cardholder’s
            claim is invalid. Example evidence includes an explanation of why
            each distinct charge is a legitimate purchase, why the cardholder’s
            claim for credit owed due to their attempt to cancel, return, or
            refund is invalid per your stated policy and cardholder agreement,
            or an explanation of how the cardholder did not attempt to remedy
            the issue with you first to receive credit.

            - `TRACKING_NUMBER`: The tracking number for the order provided by
            the shipping carrier. If you have multiple numbers, they need to be
            submitted individually as separate pieces of evidence.
        file:
          $ref: '#/components/schemas/DisputeEvidenceFile'
          description: >-
            If the evidence is of type `FILE`, contains metadata about the
            binary file uploaded as evidence.
        text:
          type: string
          description: >-
            If the evidence is of type `TEXT`, contains the blob of text created
            as evidence.


            Min length: `1`

            Max length: `500`
        type:
          $ref: '#/components/schemas/DisputeEvidenceType'
          description: |-
            Indicates if the evidence is a file or plain text.

            Current values:
            - `TEXT`: The evidence is a blob of text under 500 characters.
            - `FILE`: The evidence is an uploaded binary file.
        created_at:
          type: string
          format: date-time
          description: >-
            When this evidence was created, in [RFC
            3339](https://datatracker.ietf.org/doc/html/rfc3339) format (UTC).
        metadata:
          $ref: '#/components/schemas/Metadata'
      required:
        - id
        - dispute_id
        - category
        - type
        - created_at
      title: DisputeEvidence
    Disputes_list-dispute-evidence_Response_200:
      type: object
      properties:
        evidence:
          type: array
          items:
            $ref: '#/components/schemas/DisputeEvidence'
          description: >-
            List of pieces of evidence for the dispute matching the given query
            parameters
        cursor:
          type: string
          description: >-
            The pagination cursor to be used in a subsequent request. If empty,
            this is the final response.
      required:
        - evidence
      title: Disputes_list-dispute-evidence_Response_200
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

url = "https://api.cash.app/network/v1/disputes/dispute_id/evidence"

headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent"
}

response = requests.get(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/network/v1/disputes/dispute_id/evidence';
const options = {
  method: 'GET',
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

	url := "https://api.cash.app/network/v1/disputes/dispute_id/evidence"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("https://api.cash.app/network/v1/disputes/dispute_id/evidence")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
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

HttpResponse<String> response = Unirest.get("https://api.cash.app/network/v1/disputes/dispute_id/evidence")
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

$response = $client->request('GET', 'https://api.cash.app/network/v1/disputes/dispute_id/evidence', [
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

var client = new RestClient("https://api.cash.app/network/v1/disputes/dispute_id/evidence");
var request = new RestRequest(Method.GET);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/network/v1/disputes/dispute_id/evidence")! as URL,
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