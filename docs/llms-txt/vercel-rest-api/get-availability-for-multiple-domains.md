# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-availability-for-multiple-domains.md

# Get availability for multiple domains

> Get availability for multiple domains. If the domains are available, they can be purchased using the [Buy a domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-a-domain) endpoint or the [Buy multiple domains](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains) endpoint.

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/availability
paths:
  path: /v1/registrar/domains/availability
  method: post
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
      path: {}
      query:
        teamId:
          schema:
            - type: string
              required: false
              example: team_1a2b3c4d5e6f7g8h9i0j1k2l
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              domains:
                allOf:
                  - type: array
                    minItems: 1
                    items:
                      $ref: '#/components/schemas/DomainName'
                    description: an array of at most 50 item(s)
                    title: maxItems(50)
                    maxItems: 50
            required: true
            requiredProperties:
              - domains
            additionalProperties: false
        examples:
          example:
            value:
              domains:
                - <string>
    codeSamples:
      - label: getBulkAvailability
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.getBulkAvailability({
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                domains: [
                  "<value 1>",
                ],
              },
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
              results:
                allOf:
                  - type: array
                    items:
                      type: object
                      required:
                        - domain
                        - available
                      properties:
                        domain:
                          $ref: '#/components/schemas/DomainName'
                        available:
                          type: boolean
                      additionalProperties: false
            requiredProperties:
              - results
            additionalProperties: false
        examples:
          example:
            value:
              results:
                - domain: <string>
                  available: true
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
        examples:
          example:
            value:
              status: 403
              code: not_authorized_for_scope
              message: <string>
        description: NotAuthorizedForScope
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