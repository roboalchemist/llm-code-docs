# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/domains-registrar/get-contact-info-schema.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get contact info schema

> Some TLDs require additional contact information. Use this endpoint to get the schema for the tld-specific contact information for a domain.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/registrar/domains/{domain}/contact-info/schema
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
  /v1/registrar/domains/{domain}/contact-info/schema:
    get:
      tags:
        - domains-registrar
      summary: Get contact info schema
      description: >-
        Some TLDs require additional contact information. Use this endpoint to
        get the schema for the tld-specific contact information for a domain.
      operationId: getContactInfoSchema
      parameters:
        - name: domain
          in: path
          schema:
            $ref: '#/components/schemas/DomainName'
          required: true
        - name: teamId
          in: query
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
          required: false
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties: {}
        '400':
          description: There was something wrong with the request
          content:
            application/json:
              schema:
                anyOf:
                  - $ref: '#/components/schemas/BadRequest'
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
                $ref: '#/components/schemas/NotAuthorizedForScope'
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
    BadRequest:
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
            - bad_request
        message:
          type: string
      additionalProperties: false
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