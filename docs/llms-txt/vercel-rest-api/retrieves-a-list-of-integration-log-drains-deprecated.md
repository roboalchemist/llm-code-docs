# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/logdrains/retrieves-a-list-of-integration-log-drains-deprecated.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Retrieves a list of Integration log drains (deprecated)

> Retrieves a list of all Integration log drains that are defined for the authenticated user or team. When using an OAuth2 token, the list is limited to log drains created by the authenticated integration.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v2/integrations/log-drains
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
    get:
      tags:
        - logDrains
      summary: Retrieves a list of Integration log drains (deprecated)
      description: >-
        Retrieves a list of all Integration log drains that are defined for the
        authenticated user or team. When using an OAuth2 token, the list is
        limited to log drains created by the authenticated integration.
      operationId: getIntegrationLogDrains
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
      responses:
        '200':
          description: A list of log drains
          content:
            application/json:
              schema:
                items:
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
                      description: >-
                        A timestamp that tells you when the log drain was
                        created
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
                        The sources from which logs are currently being
                        delivered to this log drain.
                      example:
                        - build
                        - edge
                    createdFrom:
                      type: string
                      enum:
                        - integration
                        - self-served
                      description: >-
                        Whether the log drain was created by an integration or
                        by a user
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
                type: array
        '400':
          description: ''
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