# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/teams/create-a-team.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Team

> Create a new Team under your account. You need to send a POST request with the desired Team slug, and optionally the Team name.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/teams
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
  /v1/teams:
    post:
      tags:
        - teams
      summary: Create a Team
      description: >-
        Create a new Team under your account. You need to send a POST request
        with the desired Team slug, and optionally the Team name.
      operationId: createTeam
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              required:
                - slug
              properties:
                slug:
                  example: a-random-team
                  description: The desired slug for the Team
                  type: string
                  maxLength: 48
                name:
                  example: A Random Team
                  description: >-
                    The desired name for the Team. It will be generated from the
                    provided slug if nothing is provided
                  type: string
                  maxLength: 256
                attribution:
                  type: object
                  description: Attribution information for the session or current page
                  properties:
                    sessionReferrer:
                      type: string
                      description: Session referrer
                    landingPage:
                      type: string
                      description: Session landing page
                    pageBeforeConversionPage:
                      type: string
                      description: Referrer to the signup page
                    utm:
                      type: object
                      properties:
                        utmSource:
                          type: string
                          description: UTM source
                        utmMedium:
                          type: string
                          description: UTM medium
                        utmCampaign:
                          type: string
                          description: UTM campaign
                        utmTerm:
                          type: string
                          description: UTM term
        required: true
      responses:
        '200':
          description: The team was created successfully
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                    description: Id of the created team
                    example: team_nLlpyC6RE1qxqglFKbrMxlud
                  slug:
                    type: string
                required:
                  - id
                  - slug
                type: object
                description: The team was created successfully
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            The slug is already in use
        '401':
          description: ''
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