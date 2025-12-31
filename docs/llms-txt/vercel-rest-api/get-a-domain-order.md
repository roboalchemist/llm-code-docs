# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-a-domain-order.md

# Get a domain order

> Get information about a domain order by its ID

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/orders/{orderId}
paths:
  path: /v1/registrar/orders/{orderId}
  method: get
  servers:
    - url: https://api.vercel.com
      description: Production API
  request:
    security:
      - title: bearerToken
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: Default authentication mechanism
          cookie: {}
    parameters:
      path:
        orderId:
          schema:
            - type: string
              required: true
      query:
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: getOrder
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getOrder({
              orderId: "<id>",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
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
              orderId:
                allOf:
                  - type: string
              domains:
                allOf:
                  - type: array
                    items:
                      anyOf:
                        - type: object
                          required:
                            - purchaseType
                            - autoRenew
                            - years
                            - domainName
                            - status
                            - price
                          properties:
                            purchaseType:
                              type: string
                              enum:
                                - purchase
                            autoRenew:
                              type: boolean
                            years:
                              type: number
                              description: >-
                                The number of years the domain is being
                                purchased for.
                            domainName:
                              $ref: '#/components/schemas/DomainName'
                            status:
                              type: string
                              enum:
                                - pending
                                - completed
                                - failed
                                - refunded
                                - refund-failed
                            price:
                              type: number
                              description: The price for the domain.
                              minimum: 0.01
                          additionalProperties: false
                        - type: object
                          required:
                            - purchaseType
                            - years
                            - domainName
                            - status
                            - price
                          properties:
                            purchaseType:
                              type: string
                              enum:
                                - renewal
                            years:
                              type: number
                              description: >-
                                The number of years the domain is being renewed
                                for.
                            domainName:
                              $ref: '#/components/schemas/DomainName'
                            status:
                              type: string
                              enum:
                                - pending
                                - completed
                                - failed
                                - refunded
                                - refund-failed
                            price:
                              type: number
                              description: The price for the domain.
                              minimum: 0.01
                          additionalProperties: false
                        - type: object
                          required:
                            - purchaseType
                            - autoRenew
                            - years
                            - domainName
                            - status
                            - price
                          properties:
                            purchaseType:
                              type: string
                              enum:
                                - transfer
                            autoRenew:
                              type: boolean
                            years:
                              type: number
                              description: >-
                                The number of years the domain is being
                                transferred for.
                            domainName:
                              $ref: '#/components/schemas/DomainName'
                            status:
                              type: string
                              enum:
                                - pending
                                - completed
                                - failed
                                - refunded
                                - refund-failed
                            price:
                              type: number
                              description: The price for the domain.
                              minimum: 0.01
                          additionalProperties: false
              status:
                allOf:
                  - type: string
                    enum:
                      - draft
                      - purchasing
                      - completed
                      - failed
              error:
                allOf:
                  - anyOf:
                      - type: object
                        required:
                          - code
                        properties:
                          code:
                            type: string
                            enum:
                              - payment-failed
                        additionalProperties: false
                      - type: object
                        required:
                          - code
                          - details
                        properties:
                          code:
                            type: string
                            enum:
                              - tld-outage
                          details:
                            type: object
                            required:
                              - tlds
                            properties:
                              tlds:
                                type: array
                                items:
                                  type: object
                                  required:
                                    - tldName
                                    - endsAt
                                  properties:
                                    tldName:
                                      type: string
                                    endsAt:
                                      type: string
                                  additionalProperties: false
                            additionalProperties: false
                        additionalProperties: false
                      - type: object
                        required:
                          - code
                          - details
                        properties:
                          code:
                            type: string
                            enum:
                              - price-mismatch
                          details:
                            type: object
                            required:
                              - expectedPrice
                            properties:
                              expectedPrice:
                                type: number
                              actualPrice:
                                type: number
                            additionalProperties: false
                        additionalProperties: false
                      - type: object
                        required:
                          - code
                        properties:
                          code:
                            type: string
                            enum:
                              - unexpected-error
                        additionalProperties: false
            requiredProperties:
              - orderId
              - domains
              - status
            additionalProperties: false
        examples:
          example:
            value:
              orderId: <string>
              domains:
                - purchaseType: purchase
                  autoRenew: true
                  years: 123
                  domainName: <string>
                  status: pending
                  price: 1.01
              status: draft
              error:
                code: payment-failed
        description: Success
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              issues:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/Issue'
              message:
                allOf:
                  - type: string
            description: The request did not match the expected schema
            refIdentifier: '#/components/schemas/HttpApiDecodeError'
            requiredProperties:
              - issues
              - message
            additionalProperties: false
        examples:
          example:
            value:
              issues:
                - path:
                    - <string>
                  message: <string>
              message: <string>
        description: There was something wrong with the request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 401
              code:
                allOf:
                  - type: string
                    enum:
                      - unauthorized
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Unauthorized'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 401
              code: unauthorized
              message: <string>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 403
              code:
                allOf:
                  - type: string
                    enum:
                      - not_authorized_for_scope
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/NotAuthorizedForScope'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 403
              code:
                allOf:
                  - type: string
                    enum:
                      - forbidden
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Forbidden'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 404
              code:
                allOf:
                  - type: string
                    enum:
                      - not_found
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/NotFound'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 404
              code: not_found
              message: <string>
        description: NotFound
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 429
              code:
                allOf:
                  - type: string
                    enum:
                      - too_many_requests
              message:
                allOf:
                  - type: string
              retryAfter:
                allOf:
                  - type: object
                    required:
                      - value
                      - str
                    properties:
                      value:
                        type: number
                      str:
                        type: string
                    additionalProperties: false
              limit:
                allOf:
                  - type: object
                    required:
                      - total
                      - remaining
                      - reset
                    properties:
                      total:
                        type: number
                      remaining:
                        type: number
                      reset:
                        type: number
                    additionalProperties: false
            refIdentifier: '#/components/schemas/TooManyRequests'
            requiredProperties:
              - status
              - code
              - message
              - retryAfter
              - limit
            additionalProperties: false
        examples:
          example:
            value:
              status: 429
              code: too_many_requests
              message: <string>
              retryAfter:
                value: 123
                str: <string>
              limit:
                total: 123
                remaining: 123
                reset: 123
        description: TooManyRequests
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 500
              code:
                allOf:
                  - type: string
                    enum:
                      - internal_server_error
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/InternalServerError'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
        examples:
          example:
            value:
              status: 500
              code: internal_server_error
              message: <string>
        description: InternalServerError
  deprecated: false
  type: path
components:
  schemas:
    Issue:
      type: object
      required:
        - path
        - message
      properties:
        path:
          type: array
          items:
            $ref: '#/components/schemas/PropertyKey'
          description: The path to the property where the issue occurred
        message:
          type: string
          description: A descriptive message explaining the issue
      additionalProperties: false
      description: >-
        Represents an error encountered while parsing a value to match the
        schema
    PropertyKey:
      anyOf:
        - type: string
        - type: number
        - type: object
          required:
            - _tag
            - key
          properties:
            _tag:
              type: string
              enum:
                - symbol
            key:
              type: string
          additionalProperties: false
          description: an object to be decoded into a globally shared symbol
    DomainName:
      type: string

````