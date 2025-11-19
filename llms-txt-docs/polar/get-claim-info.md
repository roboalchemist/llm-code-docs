# Source: https://polar.sh/docs/api-reference/customer-seats/get-claim-info.md

# Get Claim Info

## OpenAPI

````yaml get /v1/customer-seats/claim/{invitation_token}
paths:
  path: /v1/customer-seats/claim/{invitation_token}
  method: get
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
      path:
        invitation_token:
          schema:
            - type: string
              required: true
              title: Invitation Token
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Python (SDK)
        lang: python
        source: |-
          from polar_sdk import Polar


          with Polar() as polar:

              res = polar.customer_seats.get_claim_info(invitation_token="<value>")

              # Handle response
              print(res)
      - label: Typescript (SDK)
        lang: typescript
        source: |-
          import { Polar } from "@polar-sh/sdk";

          const polar = new Polar();

          async function run() {
            const result = await polar.customerSeats.getClaimInfo({
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
              product_name:
                allOf:
                  - type: string
                    title: Product Name
                    description: Name of the product
              product_id:
                allOf:
                  - type: string
                    format: uuid
                    title: Product Id
                    description: ID of the product
              organization_name:
                allOf:
                  - type: string
                    title: Organization Name
                    description: Name of the organization
              organization_slug:
                allOf:
                  - type: string
                    title: Organization Slug
                    description: Slug of the organization
              customer_email:
                allOf:
                  - type: string
                    title: Customer Email
                    description: Email of the customer assigned to this seat
              can_claim:
                allOf:
                  - type: boolean
                    title: Can Claim
                    description: Whether the seat can be claimed
            title: SeatClaimInfo
            description: |-
              Read-only information about a seat claim invitation.
              Safe for email scanners - no side effects when fetched.
            refIdentifier: '#/components/schemas/SeatClaimInfo'
            requiredProperties:
              - product_name
              - product_id
              - organization_name
              - organization_slug
              - customer_email
              - can_claim
        examples:
          example:
            value:
              product_name: <string>
              product_id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              organization_name: <string>
              organization_slug: <string>
              customer_email: <string>
              can_claim: true
        description: Successful Response
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Invalid or expired invitation token
        examples: {}
        description: Invalid or expired invitation token
    '403':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Seat-based pricing not enabled for organization
        examples: {}
        description: Seat-based pricing not enabled for organization
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