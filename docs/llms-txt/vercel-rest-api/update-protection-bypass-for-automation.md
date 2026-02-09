# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/update-protection-bypass-for-automation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Protection Bypass for Automation

> Update the deployment protection automation bypass for a project



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples patch /v1/projects/{idOrName}/protection-bypass
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
  /v1/projects/{idOrName}/protection-bypass:
    patch:
      tags:
        - projects
      summary: Update Protection Bypass for Automation
      description: Update the deployment protection automation bypass for a project
      operationId: updateProjectProtectionBypass
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
              properties:
                revoke:
                  description: >-
                    Optional instructions for revoking and regenerating a
                    automation bypass
                  type: object
                  properties:
                    secret:
                      description: Automation bypass to revoked
                      type: string
                    regenerate:
                      description: >-
                        Whether or not a new automation bypass should be created
                        after the provided secret is revoked
                      type: boolean
                  required:
                    - secret
                    - regenerate
                generate:
                  description: >-
                    Generate a new secret. If neither generate or revoke are
                    provided, a new random secret will be generated.
                  type: object
                  properties:
                    secret:
                      description: >-
                        Optional value of the secret to generate, don't send it
                        for oauth2 tokens
                      type: string
                      pattern: ^[a-zA-Z0-9]{32}$
                    note:
                      type: string
                      description: Note to be displayed in the UI for this bypass
                      maxLength: 100
                update:
                  description: Update an existing bypass
                  type: object
                  required:
                    - secret
                  properties:
                    secret:
                      description: Automation bypass to updated
                      type: string
                    isEnvVar:
                      type: boolean
                      description: >-
                        Whether or not this bypass is set as the
                        VERCEL_AUTOMATION_BYPASS_SECRET environment variable on
                        deployments
                    note:
                      type: string
                      description: Note to be displayed in the UI for this bypass
                      maxLength: 100
              additionalProperties: false
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                properties:
                  protectionBypass:
                    additionalProperties:
                      oneOf:
                        - properties:
                            createdAt:
                              type: number
                            createdBy:
                              type: string
                            scope:
                              type: string
                              enum:
                                - integration-automation-bypass
                            integrationId:
                              type: string
                            configurationId:
                              type: string
                          required:
                            - configurationId
                            - createdAt
                            - createdBy
                            - integrationId
                            - scope
                          type: object
                        - properties:
                            createdAt:
                              type: number
                            createdBy:
                              type: string
                            scope:
                              type: string
                              enum:
                                - automation-bypass
                            isEnvVar:
                              type: boolean
                              enum:
                                - false
                                - true
                              description: >-
                                When there was only one bypass, it was
                                automatically set as an env var on deployments.
                                With multiple bypasses, there is always one
                                bypass that is selected as the default, and gets
                                set as an env var on deployments. As this is a
                                new field, undefined means that the bypass is
                                the env var. If there are any automation
                                bypasses, exactly one must be the env var.
                            note:
                              type: string
                              description: >-
                                Optional note about the bypass to be displayed
                                in the UI
                          required:
                            - createdAt
                            - createdBy
                            - scope
                          type: object
                    type: object
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: ''
        '409':
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