# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/creates-a-new-integration-log-drain-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Creates a new Integration Log Drain (deprecated)

> Creates an Integration log drain. This endpoint must be called with an OAuth2 client (integration), since log drains are tied to integrations. If it is called with a different token type it will produce a 400 error.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/integrations/log-drains
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
  /v2/integrations/log-drains:
    post:
      tags:
        - logDrains
      summary: Creates a new Integration Log Drain (deprecated)
      description: >-
        Creates an Integration log drain. This endpoint must be called with an
        OAuth2 client (integration), since log drains are tied to integrations.
        If it is called with a different token type it will produce a 400 error.
      operationId: createLogDrain
      parameters:
        - description: The Team identifier to perform the request on behalf of.
          in: query
          name: teamId
          schema:
            type: string
            example: team_1a2b3c4d5e6f7g8h9i0j1k2l
        - description: The Team slug to perform the request on behalf of.
          in: query
          name: slug
          schema:
            type: string
            example: my-team-url-slug
      requestBody:
        content:
          application/json:
            schema:
              properties:
                name:
                  description: The name of the log drain
                  example: My first log drain
                  maxLength: 100
                  pattern: ^[A-z0-9_ -]+$
                  type: string
                projectIds:
                  minItems: 1
                  maxItems: 50
                  type: array
                  items:
                    pattern: ^[a-zA-z0-9_]+$
                    type: string
                secret:
                  description: >-
                    A secret to sign log drain notification headers so a
                    consumer can verify their authenticity
                  example: a1Xsfd325fXcs
                  maxLength: 100
                  pattern: ^[A-z0-9_ -]+$
                  type: string
                deliveryFormat:
                  description: The delivery log format
                  example: json
                  enum:
                    - json
                    - ndjson
                url:
                  description: >-
                    The url where you will receive logs. The protocol must be
                    `https://` or `http://` when type is `json` and `ndjson`.
                  example: https://example.com/log-drain
                  format: uri
                  pattern: ^https?://
                  type: string
                sources:
                  type: array
                  uniqueItems: true
                  items:
                    type: string
                    enum:
                      - static
                      - lambda
                      - build
                      - edge
                      - external
                      - firewall
                  minItems: 1
                headers:
                  description: Headers to be sent together with the request
                  type: object
                  additionalProperties:
                    type: string
                environments:
                  type: array
                  uniqueItems: true
                  items:
                    type: string
                    enum:
                      - preview
                      - production
                  minItems: 1
              required:
                - name
                - url
              type: object
        required: true
      responses:
        '200':
          description: The log drain was successfully created
          content:
            application/json:
              schema:
                properties:
                  clientId:
                    type: string
                    description: >-
                      The oauth2 client application id that created this log
                      drain
                    example: oac_xRhY4LAB7yLhUADD69EvV7ct
                  configurationId:
                    type: string
                    description: The client configuration this log drain was created with
                    example: icfg_3bwCLgxL8qt5kjRLcv2Dit7F
                  createdAt:
                    type: number
                    description: A timestamp that tells you when the log drain was created
                    example: 1558531915505
                  id:
                    type: string
                    description: >-
                      The unique identifier of the log drain. Always prefixed
                      with `ld_`
                    example: ld_nBuA7zCID8g4QZ8g
                  deliveryFormat:
                    type: string
                    enum:
                      - json
                      - ndjson
                      - protobuf
                    description: The delivery log format
                    example: json
                  name:
                    type: string
                    description: The name of the log drain
                    example: My first log drain
                  ownerId:
                    type: string
                    description: >-
                      The identifier of the team or user whose events will
                      trigger the log drain
                    example: kr1PsOIzqEL5Xg6M4VZcZosf
                  projectId:
                    nullable: true
                    type: string
                    example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
                  projectIds:
                    items:
                      type: string
                    type: array
                    description: >-
                      The identifier of the projects this log drain is
                      associated with
                    example: AbCgVkqoxXeXCDWehVir51LHGrrcWL4mkYm14W6UBPWQeb
                  url:
                    type: string
                    description: The URL to call when logs are generated
                    example: https://example.com/log-drain
                  sources:
                    items:
                      type: string
                      enum:
                        - external
                        - build
                        - edge
                        - lambda
                        - static
                        - firewall
                        - redirect
                      description: >-
                        The sources from which logs are currently being
                        delivered to this log drain.
                      example:
                        - build
                        - edge
                    type: array
                    description: >-
                      The sources from which logs are currently being delivered
                      to this log drain.
                    example:
                      - build
                      - edge
                  createdFrom:
                    type: string
                    enum:
                      - integration
                      - self-served
                    description: >-
                      Whether the log drain was created by an integration or by
                      a user
                    example: integration
                  headers:
                    additionalProperties:
                      type: string
                    type: object
                    description: The headers to send with the request
                    example: '{"Authorization": "Bearer 123"}'
                  environments:
                    items:
                      type: string
                      enum:
                        - production
                        - preview
                      description: The environment of log drain
                      example:
                        - production
                    type: array
                    description: The environment of log drain
                    example:
                      - production
                  branch:
                    type: string
                    description: The branch regexp of log drain
                    example: feature/*
                  samplingRate:
                    type: number
                    description: The sampling rate of log drain
                    example: 0.5
                  source:
                    oneOf:
                      - properties:
                          kind:
                            type: string
                            enum:
                              - self-served
                        required:
                          - kind
                        type: object
                      - properties:
                          kind:
                            type: string
                            enum:
                              - integration
                          resourceId:
                            type: string
                          externalResourceId:
                            type: string
                          integrationId:
                            type: string
                          integrationConfigurationId:
                            type: string
                        required:
                          - integrationConfigurationId
                          - integrationId
                          - kind
                        type: object
                required:
                  - createdAt
                  - id
                  - name
                  - ownerId
                  - source
                  - url
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            The provided token is not from an OAuth2 Client
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````