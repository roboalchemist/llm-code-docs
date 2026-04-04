# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/user/delete-user-account.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete User Account

> Initiates the deletion process for the currently authenticated User, by sending a deletion confirmation email. The email contains a link that the user needs to visit in order to proceed with the deletion process.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v1/user
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
  /v1/user:
    delete:
      tags:
        - user
      summary: Delete User Account
      description: >-
        Initiates the deletion process for the currently authenticated User, by
        sending a deletion confirmation email. The email contains a link that
        the user needs to visit in order to proceed with the deletion process.
      operationId: requestDelete
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              type: object
              additionalProperties: false
              properties:
                reasons:
                  type: array
                  description: >-
                    Optional array of objects that describe the reason why the
                    User account is being deleted.
                  items:
                    type: object
                    description: >-
                      An object describing the reason why the User account is
                      being deleted.
                    required:
                      - slug
                      - description
                    additionalProperties: false
                    properties:
                      slug:
                        type: string
                        description: >-
                          Idenitifier slug of the reason why the User account is
                          being deleted.
                      description:
                        type: string
                        description: >-
                          Description of the reason why the User account is
                          being deleted.
        required: true
      responses:
        '202':
          description: >-
            Response indicating that the User deletion process has been
            initiated, and a confirmation email has been sent.
          content:
            application/json:
              schema:
                properties:
                  id:
                    type: string
                    description: Unique identifier of the User who has initiated deletion.
                  email:
                    type: string
                    description: Email address of the User who has initiated deletion.
                  message:
                    type: string
                    description: User deletion progress status.
                    example: Verification email sent
                required:
                  - email
                  - id
                  - message
                type: object
        '400':
          description: One of the provided values in the request body is invalid.
        '401':
          description: ''
        '402':
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