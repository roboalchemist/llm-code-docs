# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/buy-multiple-domains.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Buy multiple domains

> Buy multiple domains at once



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/registrar/domains/buy
openapi: 3.0.3
info:
  title: Vercel REST API & SDK
  description: >-
    The [`@vercel/sdk`](https://www.npmjs.com/package/@vercel/sdk) is a
    type-safe Typescript SDK that allows you to access the resources and methods
    of the Vercel REST API. Learn how to [install
    it](https://vercel.com/docs/rest-api/sdk#installing-vercel-sdk) and
    [authenticate](https://vercel.com/docs/rest-api/sdk#authentication) with a
    Vercel access token.
  contact:
    email: support@vercel.com
    name: Vercel Support
    url: https://vercel.com/support
  version: 0.0.1
servers:
  - url: https://api.vercel.com
    description: Production API
security: []
paths:
  /v1/registrar/domains/buy:
    post:
      tags:
        - domains-registrar
      summary: Buy multiple domains
      description: Buy multiple domains at once
      operationId: buyDomains
      parameters:
        - name: teamId
          in: query
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
          required: false
      requestBody:
        content:
          application/json:
            schema:
              type: object
              required:
                - domains
                - contactInformation
              properties:
                domains:
                  type: array
                  minItems: 1
                  items:
                    type: object
                    required:
                      - domainName
                      - autoRenew
                      - years
                      - expectedPrice
                    properties:
                      domainName:
                        $ref: '#/components/schemas/DomainName'
                      autoRenew:
                        type: boolean
                        description: >-
                          Whether the domain should be auto-renewed before it
                          expires. This can be configured later through the
                          Vercel Dashboard or the [Update auto-renew for a
                          domain](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/update-auto-renew-for-a-domain)
                          endpoint.
                      years:
                        type: number
                        description: The number of years to purchase the domain for.
                      expectedPrice:
                        type: number
                        minimum: 0.01
                    additionalProperties: false
                contactInformation:
                  type: object
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
                    additional:
                      type: object
                      properties: {}
                  additionalProperties: false
                  description: >-
                    The contact information for the domain. Some TLDs require
                    additional contact information. Use the [Get contact info
                    schema](https://vercel.com/docs/rest-api/reference/endpoints/domains-registrar/get-contact-info-schema)
                    endpoint to retrieve the required fields.
              additionalProperties: false
        required: true
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                required:
                  - orderId
                  - _links
                properties:
                  orderId:
                    $ref: '#/components/schemas/OrderId'
                  _links:
                    type: object
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
                additionalProperties: false
        '400':
          description: There was something wrong with the request
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/DomainTooShort'
                  - $ref: '#/components/schemas/OrderTooExpensive'
                  - $ref: '#/components/schemas/TooManyDomains'
                  - $ref: '#/components/schemas/InvalidAdditionalContactInfo'
                  - $ref: '#/components/schemas/AdditionalContactInfoRequired'
                  - $ref: '#/components/schemas/DuplicateDomains'
                  - $ref: '#/components/schemas/ExpectedPriceMismatch'
                  - $ref: '#/components/schemas/DomainNotAvailable'
                  - $ref: '#/components/schemas/TldNotSupported'
                  - $ref: '#/components/schemas/HttpApiDecodeError'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Unauthorized'
        '403':
          description: NotAuthorizedForScope
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/NotAuthorizedForScope'
                  - $ref: '#/components/schemas/Forbidden'
        '429':
          description: TooManyRequests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TooManyRequests'
        '500':
          description: InternalServerError
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/InternalServerError'
      security:
        - bearerToken: []
components:
  schemas:
    DomainName:
      type: string
      description: A valid domain name
    NonEmptyTrimmedString:
      type: string
      description: a non empty string
      title: nonEmptyString
      pattern: ^\S[\s\S]*\S$|^\S$|^$
      minLength: 1
    EmailAddress:
      type: string
      description: A valid RFC 5322 email address
      title: nonEmptyString
      minLength: 1
    E164PhoneNumber:
      type: string
      description: A valid E.164 phone number
      title: nonEmptyString
      minLength: 1
      pattern: ^(?=(?:\D*\d){8,15}$)\+[1-9]\d{0,2}\.?\d+$
    CountryCode:
      type: string
      description: A valid ISO 3166-1 alpha-2 country code
    OrderId:
      type: string
      description: A valid order ID
    DomainTooShort:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - domain_too_short
        message:
          type: string
      additionalProperties: false
      description: The domain name (excluding the TLD) is too short.
    OrderTooExpensive:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - order_too_expensive
        message:
          type: string
      additionalProperties: false
      description: The total price of the order is too high.
    TooManyDomains:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - too_many_domains
        message:
          type: string
      additionalProperties: false
      description: The number of domains in the order is too high.
    InvalidAdditionalContactInfo:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - invalid_additional_contact_info
        message:
          type: string
      additionalProperties: false
      description: Additional contact information provided for the TLD is invalid.
    AdditionalContactInfoRequired:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - additional_contact_info_required
        message:
          type: string
      additionalProperties: false
      description: Additional contact information is required for the TLD.
    DuplicateDomains:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - duplicate_domains
        message:
          type: string
      additionalProperties: false
      description: Duplicate domains were provided.
    ExpectedPriceMismatch:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - expected_price_mismatch
        message:
          type: string
      additionalProperties: false
      description: The expected price passed does not match the actual price.
    DomainNotAvailable:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - domain_not_available
        message:
          type: string
      additionalProperties: false
      description: The domain is not available.
    TldNotSupported:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 400
        code:
          type: string
          enum:
            - tld_not_supported
        message:
          type: string
      additionalProperties: false
      description: The TLD is not currently supported.
    HttpApiDecodeError:
      type: object
      required:
        - issues
        - message
      properties:
        issues:
          type: array
          items:
            $ref: '#/components/schemas/Issue'
        message:
          type: string
      additionalProperties: false
      description: The request did not match the expected schema
    Unauthorized:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 401
        code:
          type: string
          enum:
            - unauthorized
        message:
          type: string
      additionalProperties: false
    NotAuthorizedForScope:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 403
        code:
          type: string
          enum:
            - not_authorized_for_scope
        message:
          type: string
      additionalProperties: false
    Forbidden:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 403
        code:
          type: string
          enum:
            - forbidden
        message:
          type: string
      additionalProperties: false
    TooManyRequests:
      type: object
      required:
        - status
        - code
        - message
        - retryAfter
        - limit
      properties:
        status:
          type: number
          enum:
            - 429
        code:
          type: string
          enum:
            - too_many_requests
        message:
          type: string
        retryAfter:
          type: object
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
          type: object
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
      additionalProperties: false
    InternalServerError:
      type: object
      required:
        - status
        - code
        - message
      properties:
        status:
          type: number
          enum:
            - 500
        code:
          type: string
          enum:
            - internal_server_error
        message:
          type: string
      additionalProperties: false
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
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````