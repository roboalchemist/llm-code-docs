# Source: https://polar.sh/docs/api-reference/subscriptions/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-seats/revoke.md

# Source: https://polar.sh/docs/api-reference/customer-portal/seats/revoke.md

> ## Documentation Index
> Fetch the complete documentation index at: https://polar.sh/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke Seat



## OpenAPI

````yaml delete /v1/customer-portal/seats/{seat_id}
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
  /v1/customer-portal/seats/{seat_id}:
    delete:
      tags:
        - customer_portal
        - seats
        - public
      summary: Revoke Seat
      operationId: customer_portal:seats:revoke_seat
      parameters:
        - name: seat_id
          in: path
          required: true
          schema:
            type: string
            format: uuid4
            title: Seat Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CustomerSeat'
        '401':
          description: Authentication required
        '403':
          description: Not permitted or seat-based pricing not enabled
        '404':
          description: Seat not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - customer_session:
            - customer_portal:write
        - member_session:
            - customer_portal:write
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
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
  securitySchemes:
    access_token:
      type: http
      scheme: bearer
      description: >-
        You can generate an **Organization Access Token** from your
        organization's settings.
    customer_session:
      type: http
      description: >-
        Customer session tokens are specific tokens that are used to
        authenticate customers on your organization. You can create those
        sessions programmatically using the [Create Customer Session
        endpoint](/api-reference/customer-portal/sessions/create).
      scheme: bearer
    member_session:
      type: http
      description: >-
        Member session tokens are specific tokens that are used to authenticate
        members on your organization. You can create those sessions
        programmatically using the [Create Member Session
        endpoint](/api-reference/member-portal/sessions/create).
      scheme: bearer

````