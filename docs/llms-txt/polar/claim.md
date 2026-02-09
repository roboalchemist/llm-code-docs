# Source: https://polar.sh/docs/api-reference/customer-seats/claim.md

> ## Documentation Index
> Fetch the complete documentation index at: https://polar.sh/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claim Seat



## OpenAPI

````yaml post /v1/customer-seats/claim
openapi: 3.1.0
info:
  title: Polar API
  summary: Polar HTTP and Webhooks API
  description: Read the docs at https://polar.sh/docs/api-reference
  version: 0.1.0
servers:
  - url: https://api.polar.sh
    description: Production environment
    x-speakeasy-server-id: production
  - url: https://sandbox-api.polar.sh
    description: Sandbox environment
    x-speakeasy-server-id: sandbox
security:
  - access_token: []
tags:
  - name: public
    description: >-
      Endpoints shown and documented in the Polar API documentation and
      available in our SDKs.
  - name: private
    description: >-
      Endpoints that should appear in the schema only in development to generate
      our internal JS SDK.
  - name: mcp
    description: Endpoints enabled in the MCP server.
paths:
  /v1/customer-seats/claim:
    post:
      tags:
        - customer-seats
        - public
      summary: Claim Seat
      operationId: customer-seats:claim_seat
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SeatClaim'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomerSeatClaimResponse'
        '400':
          description: Invalid, expired, or already claimed token
        '403':
          description: Seat-based pricing not enabled for organization
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - {}
components:
  schemas:
    SeatClaim:
      properties:
        invitation_token:
          type: string
          title: Invitation Token
          description: Invitation token to claim the seat
      type: object
      required:
        - invitation_token
      title: SeatClaim
    CustomerSeatClaimResponse:
      properties:
        seat:
          $ref: '#/components/schemas/CustomerSeat'
          description: The claimed seat
        customer_session_token:
          type: string
          title: Customer Session Token
          description: Session token for immediate customer portal access
      type: object
      required:
        - seat
        - customer_session_token
      title: CustomerSeatClaimResponse
      description: Response after successfully claiming a seat.
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
          description: >-
            The customer ID. When member_model_enabled is true, this is the
            billing customer (purchaser). When false, this is the seat member
            customer.
        member_id:
          anyOf:
            - type: string
              format: uuid
            - type: 'null'
          title: Member Id
          description: The member ID of the seat occupant
        email:
          anyOf:
            - type: string
            - type: 'null'
          title: Email
          description: Email of the seat member (set when member_model_enabled is true)
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
    SeatStatus:
      type: string
      enum:
        - pending
        - claimed
        - revoked
      title: SeatStatus
  securitySchemes:
    access_token:
      type: http
      scheme: bearer
      description: >-
        You can generate an **Organization Access Token** from your
        organization's settings.

````