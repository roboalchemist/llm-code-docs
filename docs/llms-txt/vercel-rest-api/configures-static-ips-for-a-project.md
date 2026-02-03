# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/connect/configures-static-ips-for-a-project.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Configures Static IPs for a project

> Allows configuring Static IPs for a project



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/shared-connect-links
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
  /v1/projects/{idOrName}/shared-connect-links:
    patch:
      tags:
        - connect
        - static-ips
      summary: Configures Static IPs for a project
      description: Allows configuring Static IPs for a project
      operationId: updateStaticIps
      parameters:
        - name: idOrName
          description: The unique project identifier or the project name
          in: path
          required: true
          schema:
            description: The unique project identifier or the project name
            type: string
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
              type: object
              anyOf:
                - required:
                    - builds
                - required:
                    - regions
              properties:
                builds:
                  type: boolean
                  description: Whether to use Static IPs for builds.
                regions:
                  type: array
                  items:
                    type: string
                    maxLength: 4
                    description: The region in which to enable Static IPs.
                    example: iad1
                  minItems: 0
                  maxItems: 3
                  uniqueItems: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                items:
                  properties:
                    envId:
                      oneOf:
                        - type: string
                        - type: string
                          enum:
                            - production
                            - preview
                    connectConfigurationId:
                      type: string
                    dc:
                      type: string
                    passive:
                      type: boolean
                      enum:
                        - false
                        - true
                    buildsEnabled:
                      type: boolean
                      enum:
                        - false
                        - true
                    aws:
                      properties:
                        subnetIds:
                          items:
                            type: string
                          type: array
                        securityGroupId:
                          type: string
                      required:
                        - securityGroupId
                        - subnetIds
                      type: object
                    createdAt:
                      type: number
                    updatedAt:
                      type: number
                  required:
                    - buildsEnabled
                    - connectConfigurationId
                    - createdAt
                    - envId
                    - passive
                    - updatedAt
                  type: object
                type: array
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '409':
          description: ''
        '500':
          description: ''
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````