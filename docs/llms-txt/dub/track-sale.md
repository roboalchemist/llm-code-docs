# Source: https://dub.co/docs/api-reference/endpoint/track-sale.md

# Track a sale

> Track a sale for a short link.

## OpenAPI

````yaml post /track/sale
paths:
  path: /track/sale
  method: post
  servers:
    - url: https://api.dub.co
      description: Production API
  request:
    security:
      - title: token
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              customerExternalId:
                allOf:
                  - type: string
                    minLength: 1
                    maxLength: 100
                    description: >-
                      The unique ID of the customer in your system. Will be used
                      to identify and attribute all future events to this
                      customer.
              amount:
                allOf:
                  - type: integer
                    minimum: 0
                    description: >-
                      The amount of the sale in cents (for all two-decimal
                      currencies). If the sale is in a zero-decimal currency,
                      pass the full integer value (e.g. `1437` JPY). Learn more:
                      https://d.to/currency
              currency:
                allOf:
                  - type: string
                    default: usd
                    description: >-
                      The currency of the sale. Accepts ISO 4217 currency codes.
                      Sales will be automatically converted and stored as USD at
                      the latest exchange rates. Learn more:
                      https://d.to/currency
              eventName:
                allOf:
                  - type: string
                    maxLength: 255
                    default: Purchase
                    description: >-
                      The name of the sale event. Recommended format: `Invoice
                      paid` or `Subscription created`.
                    example: Invoice paid
              paymentProcessor:
                allOf:
                  - type: string
                    enum:
                      - stripe
                      - shopify
                      - polar
                      - paddle
                      - revenuecat
                      - custom
                    default: custom
                    description: The payment processor via which the sale was made.
              invoiceId:
                allOf:
                  - type: string
                    nullable: true
                    default: null
                    description: >-
                      The invoice ID of the sale. Can be used as a idempotency
                      key – only one sale event can be recorded for a given
                      invoice ID.
              metadata:
                allOf:
                  - type: object
                    nullable: true
                    additionalProperties: {}
                    default: null
                    description: >-
                      Additional metadata to be stored with the sale event. Max
                      10,000 characters when stringified.
              leadEventName:
                allOf:
                  - type: string
                    nullable: true
                    default: null
                    description: >-
                      The name of the lead event that occurred before the sale
                      (case-sensitive). This is used to associate the sale event
                      with a particular lead event (instead of the latest lead
                      event for a link-customer combination, which is the
                      default behavior). For direct sale tracking, this field
                      can also be used to specify the lead event name.
                    example: Cloned template 1481267
              clickId:
                allOf:
                  - type: string
                    nullable: true
                    description: >-
                      [For direct sale tracking]: The unique ID of the click
                      that the sale conversion event is attributed to. You can
                      read this value from `dub_id` cookie.
              customerName:
                allOf:
                  - type: string
                    nullable: true
                    maxLength: 100
                    default: null
                    description: >-
                      [For direct sale tracking]: The name of the customer. If
                      not passed, a random name will be generated (e.g. “Big Red
                      Caribou”).
              customerEmail:
                allOf:
                  - type: string
                    nullable: true
                    format: email
                    maxLength: 100
                    default: null
                    description: >-
                      [For direct sale tracking]: The email address of the
                      customer.
              customerAvatar:
                allOf:
                  - type: string
                    nullable: true
                    default: null
                    description: >-
                      [For direct sale tracking]: The avatar URL of the
                      customer.
            requiredProperties:
              - customerExternalId
              - amount
        examples:
          example:
            value:
              customerExternalId: <string>
              amount: 1
              currency: usd
              eventName: Invoice paid
              paymentProcessor: custom
              invoiceId: null
              metadata: null
              leadEventName: Cloned template 1481267
              clickId: <string>
              customerName: null
              customerEmail: null
              customerAvatar: null
    codeSamples:
      - label: trackSale
        lang: python
        source: |-
          from dub import Dub


          with Dub(
              token="DUB_API_KEY",
          ) as d_client:

              res = d_client.track.sale(request={
                  "customer_external_id": "<id>",
                  "amount": 594903,
                  "event_name": "Invoice paid",
                  "lead_event_name": "Cloned template 1481267",
              })

              assert res is not None

              # Handle response
              print(res)
      - label: trackSale
        lang: php
        source: |-
          declare(strict_types=1);

          require 'vendor/autoload.php';

          use Dub;
          use Dub\Models\Operations;

          $sdk = Dub\Dub::builder()
              ->setSecurity(
                  'DUB_API_KEY'
              )
              ->build();

          $request = new Operations\TrackSaleRequestBody(
              customerExternalId: '<id>',
              amount: 594903,
              eventName: 'Invoice paid',
              leadEventName: 'Cloned template 1481267',
          );

          $response = $sdk->track->sale(
              request: $request
          );

          if ($response->object !== null) {
              // handle response
          }
      - label: trackSale
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tdubgo \"github.com/dubinc/dub-go\"\n\t\"github.com/dubinc/dub-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := dubgo.New(\n        dubgo.WithSecurity(\"DUB_API_KEY\"),\n    )\n\n    res, err := s.Track.Sale(ctx, &operations.TrackSaleRequestBody{\n        CustomerExternalID: \"<id>\",\n        Amount: 594903,\n        EventName: dubgo.Pointer(\"Invoice paid\"),\n        LeadEventName: dubgo.Pointer(\"Cloned template 1481267\"),\n    })\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res != nil {\n        // handle response\n    }\n}"
      - label: trackSale
        lang: ruby
        source: |-
          require 'dub'

          Models = ::OpenApiSDK::Models
          s = ::OpenApiSDK::Dub.new(
                security: Models::Shared::Security.new(
                  token: 'DUB_API_KEY',
                ),
              )

          req = Models::Operations::TrackSaleRequestBody.new(
            customer_external_id: '<id>',
            amount: 594_903,
            event_name: 'Invoice paid',
            lead_event_name: 'Cloned template 1481267',
          )

          res = s.track.sale(request: req)

          unless res.nil?
            # handle response
          end
      - label: trackSale
        lang: typescript
        source: |-
          import { Dub } from "dub";

          const dub = new Dub({
            token: "DUB_API_KEY",
          });

          async function run() {
            const result = await dub.track.sale();

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              eventName:
                allOf:
                  - type: string
              customer:
                allOf:
                  - type: object
                    nullable: true
                    properties:
                      id:
                        type: string
                      name:
                        type: string
                        nullable: true
                      email:
                        type: string
                        nullable: true
                      avatar:
                        type: string
                        nullable: true
                      externalId:
                        type: string
                        nullable: true
                    required:
                      - id
                      - name
                      - email
                      - avatar
                      - externalId
              sale:
                allOf:
                  - type: object
                    nullable: true
                    properties:
                      amount:
                        type: number
                      currency:
                        type: string
                      paymentProcessor:
                        type: string
                      invoiceId:
                        type: string
                        nullable: true
                      metadata:
                        type: object
                        nullable: true
                        additionalProperties: {}
                    required:
                      - amount
                      - currency
                      - paymentProcessor
                      - invoiceId
                      - metadata
            requiredProperties:
              - eventName
              - customer
              - sale
        examples:
          example:
            value:
              eventName: <string>
              customer:
                id: <string>
                name: <string>
                email: <string>
                avatar: <string>
                externalId: <string>
              sale:
                amount: 123
                currency: <string>
                paymentProcessor: <string>
                invoiceId: <string>
                metadata: {}
        description: A sale was tracked.
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - bad_request
                        description: A short code indicating the error code returned.
                        example: bad_request
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#bad-request
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: bad_request
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#bad-request
        description: >-
          The server cannot or will not process the request due to something
          that is perceived to be a client error (e.g., malformed request
          syntax, invalid request message framing, or deceptive request
          routing).
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - unauthorized
                        description: A short code indicating the error code returned.
                        example: unauthorized
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#unauthorized
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: unauthorized
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#unauthorized
        description: >-
          Although the HTTP standard specifies "unauthorized", semantically this
          response means "unauthenticated". That is, the client must
          authenticate itself to get the requested response.
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - forbidden
                        description: A short code indicating the error code returned.
                        example: forbidden
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#forbidden
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: forbidden
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#forbidden
        description: >-
          The client does not have access rights to the content; that is, it is
          unauthorized, so the server is refusing to give the requested
          resource. Unlike 401 Unauthorized, the client's identity is known to
          the server.
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - not_found
                        description: A short code indicating the error code returned.
                        example: not_found
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#not-found
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: not_found
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#not-found
        description: The server cannot find the requested resource.
    '409':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - conflict
                        description: A short code indicating the error code returned.
                        example: conflict
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: https://dub.co/docs/api-reference/errors#conflict
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: conflict
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#conflict
        description: >-
          This response is sent when a request conflicts with the current state
          of the server.
    '410':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - invite_expired
                        description: A short code indicating the error code returned.
                        example: invite_expired
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#invite-expired
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: invite_expired
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#invite-expired
        description: >-
          This response is sent when the requested content has been permanently
          deleted from server, with no forwarding address.
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - unprocessable_entity
                        description: A short code indicating the error code returned.
                        example: unprocessable_entity
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#unprocessable-entity
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: unprocessable_entity
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#unprocessable-entity
        description: >-
          The request was well-formed but was unable to be followed due to
          semantic errors.
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - rate_limit_exceeded
                        description: A short code indicating the error code returned.
                        example: rate_limit_exceeded
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#rate-limit_exceeded
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: rate_limit_exceeded
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#rate-limit_exceeded
        description: >-
          The user has sent too many requests in a given amount of time ("rate
          limiting")
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: string
                        enum:
                          - internal_server_error
                        description: A short code indicating the error code returned.
                        example: internal_server_error
                      message:
                        x-speakeasy-error-message: true
                        type: string
                        description: A human readable explanation of what went wrong.
                        example: The requested resource was not found.
                      doc_url:
                        type: string
                        description: >-
                          A link to our documentation with more details about
                          this error code
                        example: >-
                          https://dub.co/docs/api-reference/errors#internal-server_error
                    required:
                      - code
                      - message
            requiredProperties:
              - error
        examples:
          example:
            value:
              error:
                code: internal_server_error
                message: The requested resource was not found.
                doc_url: https://dub.co/docs/api-reference/errors#internal-server_error
        description: The server has encountered a situation it does not know how to handle.
  deprecated: false
  type: path
components:
  schemas: {}

````