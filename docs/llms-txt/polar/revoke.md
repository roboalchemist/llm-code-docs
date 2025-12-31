# Source: https://polar.sh/docs/api-reference/subscriptions/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-seats/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-portal/seats/revoke.md

# Source: https://polar.sh/docs/api-reference/subscriptions/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-seats/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-portal/seats/revoke.md

# Source: https://polar.sh/docs/api-reference/subscriptions/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-seats/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-portal/seats/revoke.md

# Source: https://polar.sh/docs/api-reference/subscriptions/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-seats/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-portal/seats/revoke.md

# Revoke Seat

> **Scopes**: `customer_portal:write`

## OpenAPI

````yaml delete /v1/customer-portal/seats/{seat_id}
paths:
  path: /v1/customer-portal/seats/{seat_id}
  method: delete
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: customer session
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Customer session tokens are specific tokens that are used to
                authenticate customers on your organization. You can create
                those sessions programmatically using the [Create Customer
                Session
                endpoint](/api-reference/customer-portal/sessions/create).
          cookie: {}
    parameters:
      path:
        seat_id:
          schema:
            - type: string
              required: true
              title: Seat Id
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Go (SDK)
        lang: go
        source: "package main\n\nimport(\n\t\"context\"\n\tpolargo \"github.com/polarsource/polar-go\"\n\t\"os\"\n\t\"github.com/polarsource/polar-go/models/operations\"\n\t\"log\"\n)\n\nfunc main() {\n    ctx := context.Background()\n\n    s := polargo.New()\n\n    res, err := s.CustomerPortal.Seats.RevokeSeat(ctx, operations.CustomerPortalSeatsRevokeSeatSecurity{\n        CustomerSession: os.Getenv(\"POLAR_CUSTOMER_SESSION\"),\n    }, \"4b3d74b3-01ff-4aac-bd03-320535cd5ce4\")\n    if err != nil {\n        log.Fatal(err)\n    }\n    if res.CustomerSeat != nil {\n        // handle response\n    }\n}"
      - label: Python (SDK)
        lang: python
        source: |-
          import polar_sdk
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.customer_portal.seats.revoke_seat(security=polar_sdk.CustomerPortalSeatsRevokeSeatSecurity(
                  customer_session="<YOUR_BEARER_TOKEN_HERE>",
              ), seat_id="4b3d74b3-01ff-4aac-bd03-320535cd5ce4")

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.customerPortal.seats.revokeSeat({
              customerSession: process.env["POLAR_CUSTOMER_SESSION"] ?? "",
            }, {
              seatId: "4b3d74b3-01ff-4aac-bd03-320535cd5ce4",
            });

            console.log(result);
          }

          run();
      - label: PHP (SDK)
        lang: php
        source: >-
          declare(strict_types=1);


          require 'vendor/autoload.php';


          use Polar;

          use Polar\Models\Operations;


          $sdk = Polar\Polar::builder()->build();



          $requestSecurity = new
          Operations\CustomerPortalSeatsRevokeSeatSecurity(
              customerSession: '<YOUR_BEARER_TOKEN_HERE>',
          );


          $response = $sdk->customerPortal->seats->revokeSeat(
              security: $requestSecurity,
              seatId: '4b3d74b3-01ff-4aac-bd03-320535cd5ce4'

          );


          if ($response->customerSeat !== null) {
              // handle response
          }
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
                    description: Creation timestamp of the object.
              modified_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Modified At
                    description: Last modification timestamp of the object.
              id:
                allOf:
                  - type: string
                    format: uuid
                    title: Id
                    description: The seat ID
              subscription_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid
                      - type: 'null'
                    title: Subscription Id
                    description: The subscription ID (for recurring seats)
              order_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid
                      - type: 'null'
                    title: Order Id
                    description: The order ID (for one-time purchase seats)
              status:
                allOf:
                  - $ref: '#/components/schemas/SeatStatus'
                    description: Status of the seat
              customer_id:
                allOf:
                  - anyOf:
                      - type: string
                        format: uuid
                      - type: 'null'
                    title: Customer Id
                    description: The assigned customer ID
              customer_email:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Customer Email
                    description: The assigned customer email
              invitation_token_expires_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Invitation Token Expires At
                    description: When the invitation token expires
              claimed_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Claimed At
                    description: When the seat was claimed
              revoked_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Revoked At
                    description: When the seat was revoked
              seat_metadata:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Seat Metadata
                    description: Additional metadata for the seat
            title: CustomerSeat
            refIdentifier: '#/components/schemas/CustomerSeat'
            requiredProperties:
              - created_at
              - modified_at
              - id
              - status
        examples:
          example:
            value:
              created_at: '2023-11-07T05:31:56Z'
              modified_at: '2023-11-07T05:31:56Z'
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              subscription_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              order_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              status: pending
              customer_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              customer_email: <string>
              invitation_token_expires_at: '2023-11-07T05:31:56Z'
              claimed_at: '2023-11-07T05:31:56Z'
              revoked_at: '2023-11-07T05:31:56Z'
              seat_metadata: {}
        description: Successful Response
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Authentication required
        examples: {}
        description: Authentication required
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Not permitted or seat-based pricing not enabled
        examples: {}
        description: Not permitted or seat-based pricing not enabled
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Seat not found
        examples: {}
        description: Seat not found
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    SeatStatus:
      type: string
      enum:
        - pending
        - claimed
        - revoked
      title: SeatStatus
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````