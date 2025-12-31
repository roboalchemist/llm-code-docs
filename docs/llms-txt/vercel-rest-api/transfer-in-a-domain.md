# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/transfer-in-a-domain.md

# Transfer-in a domain

> Transfer a domain in from another registrar

## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/{domain}/transfer
paths:
  path: /v1/registrar/domains/{domain}/transfer
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
      path:
        domain:
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              authCode:
                allOf:
                  - type: string
              autoRenew:
                allOf:
                  - type: boolean
                    description: >-
                      Whether the domain should be auto-renewed before it
                      expires. This can be configured later through the Vercel
                      Dashboard or the [Update auto-renew for a
                      domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain)
                      endpoint.
              years:
                allOf:
                  - type: number
                    description: >-
                      The number of years to renew the domain for once it is
                      transferred in. This must be a valid number of transfer
                      years for the TLD.
              expectedPrice:
                allOf:
                  - type: number
                    description: >-
                      The expected price for the domain. Use the [Get price data
                      for a
                      domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-price-data-for-a-domain)
                      endpoint to retrieve the price data for a domain.
                    minimum: 0.01
              contactInformation:
                allOf:
                  - type: object
                    required:
                      - firstName
                      - lastName
                      - email
                      - phone
                      - address1
                      - city
                      - state
                      - zip
                      - country
                    properties:
                      firstName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      lastName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      email:
                        $ref: '#/components/schemas/EmailAddress'
                      phone:
                        $ref: '#/components/schemas/E164PhoneNumber'
                      address1:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      address2:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      city:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      state:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      zip:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      country:
                        $ref: '#/components/schemas/CountryCode'
                      companyName:
                        $ref: '#/components/schemas/NonEmptyTrimmedString'
                      fax:
                        $ref: '#/components/schemas/E164PhoneNumber'
                    additionalProperties: false
            required: true
            requiredProperties:
              - authCode
              - autoRenew
              - years
              - expectedPrice
              - contactInformation
            additionalProperties: false
        examples:
          example:
            value:
              authCode: <string>
              autoRenew: true
              years: 123
              expectedPrice: 1.01
              contactInformation:
                firstName: <string>
                lastName: <string>
                email: <string>
                phone: <string>
                address1: <string>
                address2: <string>
                city: <string>
                state: <string>
                zip: <string>
                country: <string>
                companyName: <string>
                fax: <string>
    codeSamples:
      - label: transferInDomain
        lang: typescript
        source: |-
          import { Vercel } from "@vercel/sdk";

          const vercel = new Vercel({
            bearerToken: "<YOUR_BEARER_TOKEN_HERE>",
          });

          async function run() {
            const result = await vercel.domainsRegistrar.transferInDomain({
              domain: "silky-fund.org",
              teamId: "team_1a2b3c4d5e6f7g8h9i0j1k2l",
              requestBody: {
                authCode: "<value>",
                autoRenew: true,
                years: 298.08,
                expectedPrice: 5092.5,
                contactInformation: {
                  firstName: "Gabrielle",
                  lastName: "Hackett",
                  email: "Keshawn99@yahoo.com",
                  phone: "(758) 385-1802 x13762",
                  address1: "<value>",
                  city: "Pattiestead",
                  state: "Idaho",
                  zip: "64653-9022",
                  country: "Bolivia",
                },
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
              orderId:
                allOf:
                  - type: string
              _links:
                allOf:
                  - type: object
                    additionalProperties:
                      type: object
                      required:
                        - href
                        - method
                      properties:
                        href:
                          type: string
                        method:
                          type: string
                          enum:
                            - GET
                            - POST
                            - PUT
                            - DELETE
                            - PATCH
                      additionalProperties: false
            requiredProperties:
              - orderId
              - _links
            additionalProperties: false
        examples:
          example:
            value:
              orderId: <string>
              _links: {}
        description: Success
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: number
                    enum:
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - bad_request
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/BadRequest'
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
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_already_owned
              message:
                allOf:
                  - type: string
            description: The domain is already owned by another team or user.
            refIdentifier: '#/components/schemas/DomainAlreadyOwned'
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
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_too_short
              message:
                allOf:
                  - type: string
            description: The domain name (excluding the TLD) is too short.
            refIdentifier: '#/components/schemas/DomainTooShort'
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
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - dnssec_enabled
              message:
                allOf:
                  - type: string
            description: >-
              The operation cannot be completed because DNSSEC is enabled for
              the domain.
            refIdentifier: '#/components/schemas/DNSSECEnabled'
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
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - expected_price_mismatch
              message:
                allOf:
                  - type: string
            description: The expected price passed does not match the actual price.
            refIdentifier: '#/components/schemas/ExpectedPriceMismatch'
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
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - domain_not_available
              message:
                allOf:
                  - type: string
            description: The domain is not available.
            refIdentifier: '#/components/schemas/DomainNotAvailable'
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
                      - 400
              code:
                allOf:
                  - type: string
                    enum:
                      - tld_not_supported
              message:
                allOf:
                  - type: string
            description: The TLD is not currently supported.
            refIdentifier: '#/components/schemas/TldNotSupported'
            requiredProperties:
              - status
              - code
              - message
            additionalProperties: false
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
              status: 400
              code: bad_request
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
    NonEmptyTrimmedString:
      type: string
      description: a non empty string
      title: nonEmptyString
      pattern: ^\S[\s\S]*\S$|^\S$|^$
      minLength: 1
    EmailAddress:
      type: string
      description: a non empty string
      title: nonEmptyString
      minLength: 1
    E164PhoneNumber:
      type: string
      description: A valid E.164 phone number
      title: nonEmptyString
      minLength: 1
      pattern: ^(?=(?:\D*\d){7,15}$)\+[1-9]\d{0,2}\.?\d+$
    CountryCode:
      type: string
      description: A valid ISO 3166-1 alpha-2 country code
      title: nonEmptyString
      minLength: 1
      pattern: ^[A-Z]{2}$

````