# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/accept-project-transfer-request.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Accept project transfer request

> Accept a project transfer request initated by another team. <br/> The `code` is generated using the `POST /projects/:idOrName/transfer-request` endpoint.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples put /projects/transfer-request/{code}
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
  /projects/transfer-request/{code}:
    put:
      tags:
        - projects
      summary: Accept project transfer request
      description: >-
        Accept a project transfer request initated by another team. <br/> The
        `code` is generated using the `POST
        /projects/:idOrName/transfer-request` endpoint.
      operationId: acceptProjectTransferRequest
      parameters:
        - name: code
          description: The code of the project transfer request.
          in: path
          required: true
          schema:
            type: string
            description: The code of the project transfer request.
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
              additionalProperties: false
              properties:
                newProjectName:
                  description: The desired name for the project
                  example: a-project-name
                  type: string
                  maxLength: 100
                paidFeatures:
                  type: object
                  additionalProperties: false
                  properties:
                    concurrentBuilds:
                      type: integer
                      nullable: true
                    passwordProtection:
                      type: boolean
                      nullable: true
                    previewDeploymentSuffix:
                      type: boolean
                      nullable: true
                acceptedPolicies:
                  type: object
                  additionalProperties:
                    type: object
                    additionalProperties:
                      type: string
                      format: date-time
                    required:
                      - eula
                      - privacy
                    properties:
                      eula:
                        type: string
                        format: date-time
                      privacy:
                        type: string
                        format: date-time
      responses:
        '202':
          description: The project has been transferred successfully.
          content:
            application/json:
              schema:
                oneOf:
                  - properties:
                      partnerCalls:
                        items:
                          properties:
                            installationId:
                              type: string
                            resourceIds:
                              items:
                                type: string
                              type: array
                            result:
                              properties:
                                status:
                                  type: string
                                  enum:
                                    - errored
                                    - fulfilled
                                error:
                                  type: object
                                code:
                                  type: string
                              required:
                                - status
                              type: object
                          required:
                            - installationId
                            - resourceIds
                            - result
                          type: object
                        type: array
                      resourceTransferErrors:
                        items:
                          type: object
                        type: array
                      transferredStoreIds:
                        items:
                          type: string
                        type: array
                    required:
                      - partnerCalls
                      - resourceTransferErrors
                      - transferredStoreIds
                    type: object
                  - type: object
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
        '422':
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