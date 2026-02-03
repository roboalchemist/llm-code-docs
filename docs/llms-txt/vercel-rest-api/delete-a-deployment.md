# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/deployments/delete-a-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Deployment

> This API allows you to delete a deployment, either by supplying its `id` in the URL or the `url` of the deployment as a query parameter. You can obtain the ID, for example, by listing all deployments.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples delete /v13/deployments/{id}
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
  /v13/deployments/{id}:
    delete:
      tags:
        - deployments
      summary: Delete a Deployment
      description: >-
        This API allows you to delete a deployment, either by supplying its `id`
        in the URL or the `url` of the deployment as a query parameter. You can
        obtain the ID, for example, by listing all deployments.
      operationId: deleteDeployment
      parameters:
        - name: id
          description: The ID of the deployment to be deleted
          in: path
          required: true
          schema:
            description: The ID of the deployment to be deleted
            example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
            type: string
        - name: url
          description: >-
            A Deployment or Alias URL. In case it is passed, the ID will be
            ignored
          in: query
          required: false
          schema:
            description: >-
              A Deployment or Alias URL. In case it is passed, the ID will be
              ignored
            example: https://files-orcin-xi.vercel.app/
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
          description: The deployment was successfully deleted
          content:
            application/json:
              schema:
                properties:
                  uid:
                    type: string
                    description: The removed deployment ID.
                    example: dpl_5WJWYSyB7BpgTj3EuwF37WMRBXBtPQ2iTMJHJBJyRfd
                  state:
                    type: string
                    enum:
                      - DELETED
                    description: A constant with the final state of the deployment.
                required:
                  - state
                  - uid
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: The deployment was not found
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````