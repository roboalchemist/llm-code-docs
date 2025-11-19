# Source: https://polar.sh/docs/api-reference/customer-seats/claim.md

# Claim Seat

## OpenAPI

````yaml post /v1/customer-seats/claim
paths:
  path: /v1/customer-seats/claim
  method: post
  servers:
    - url: https://api.polar.sh
      description: Production environment
    - url: https://sandbox-api.polar.sh
      description: Sandbox environment
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
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
              invitation_token:
                allOf:
                  - type: string
                    title: Invitation Token
                    description: Invitation token to claim the seat
            required: true
            title: SeatClaim
            refIdentifier: '#/components/schemas/SeatClaim'
            requiredProperties:
              - invitation_token
        examples:
          example:
            value:
              invitation_token: <string>
    codeSamples:
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.customer_seats.claim_seat(request={
                  "invitation_token": "<value>",
              })

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.customerSeats.claimSeat({
              invitationToken: "<value>",
            });

            console.log(result);
          }

          run();
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              seat:
                allOf:
                  - $ref: '#/components/schemas/CustomerSeat'
                    description: The claimed seat
              customer_session_token:
                allOf:
                  - type: string
                    title: Customer Session Token
                    description: Session token for immediate customer portal access
            title: CustomerSeatClaimResponse
            description: Response after successfully claiming a seat.
            refIdentifier: '#/components/schemas/CustomerSeatClaimResponse'
            requiredProperties:
              - seat
              - customer_session_token
        examples:
          example:
            value:
              seat:
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
              customer_session_token: <string>
        description: Successful Response
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Invalid, expired, or already claimed token
        examples: {}
        description: Invalid, expired, or already claimed token
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Seat-based pricing not enabled for organization
        examples: {}
        description: Seat-based pricing not enabled for organization
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
    CustomerSeat:
      properties:
        created_at:
          type: string
          format: date-time
          title: Created At
          description: Creation timestamp of the object.
        modified_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Modified At
          description: Last modification timestamp of the object.
        id:
          type: string
          format: uuid
          title: Id
          description: The seat ID
        subscription_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Subscription Id
          description: The subscription ID (for recurring seats)
        order_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Order Id
          description: The order ID (for one-time purchase seats)
        status:
          $ref: '#/components/schemas/SeatStatus'
          description: Status of the seat
        customer_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Customer Id
          description: The assigned customer ID
        customer_email:
          anyOf:
            - type: string
            - type: 'null'
          title: Customer Email
          description: The assigned customer email
        invitation_token_expires_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Invitation Token Expires At
          description: When the invitation token expires
        claimed_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Claimed At
          description: When the seat was claimed
        revoked_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Revoked At
          description: When the seat was revoked
        seat_metadata:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Seat Metadata
          description: Additional metadata for the seat
      type: object
      required:
        - created_at
        - modified_at
        - id
        - status
      title: CustomerSeat
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