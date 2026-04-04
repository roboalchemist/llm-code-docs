# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/rolling-release/get-rolling-release-billing-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Get rolling release billing status

> Get the Rolling Releases billing status for a project. The team level billing status is used to determine if the project can be configured for rolling releases.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples get /v1/projects/{idOrName}/rolling-release/billing
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
  /v1/projects/{idOrName}/rolling-release/billing:
    get:
      tags:
        - rolling-release
      summary: Get rolling release billing status
      description: >-
        Get the Rolling Releases billing status for a project. The team level
        billing status is used to determine if the project can be configured for
        rolling releases.
      operationId: getRollingReleaseBillingStatus
      parameters:
        - name: idOrName
          description: Project ID or project name (URL-encoded)
          in: path
          required: true
          schema:
            description: Project ID or project name (URL-encoded)
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
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      availableSlots:
                        type: number
                        enum:
                          - 0
                      reason:
                        type: string
                        enum:
                          - plan_not_supported
                      message:
                        type: string
                    required:
                      - availableSlots
                      - message
                      - reason
                    type: object
                  - properties:
                      availableSlots:
                        type: string
                        enum:
                          - unlimited
                      reason:
                        type: string
                        enum:
                          - unlimited_slots
                      message:
                        type: string
                    required:
                      - availableSlots
                      - message
                      - reason
                    type: object
                  - properties:
                      availableSlots:
                        type: number
                        enum:
                          - 0
                      reason:
                        type: string
                        enum:
                          - no_available_slots
                      message:
                        type: string
                      enabledProjects:
                        items:
                          type: string
                        type: array
                    required:
                      - availableSlots
                      - enabledProjects
                      - message
                      - reason
                    type: object
                  - properties:
                      availableSlots:
                        type: number
                      reason:
                        type: string
                        enum:
                          - available_slots
                      message:
                        type: string
                    required:
                      - availableSlots
                      - message
                      - reason
                    type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
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