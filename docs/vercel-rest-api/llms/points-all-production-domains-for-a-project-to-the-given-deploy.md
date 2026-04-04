# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/projects/points-all-production-domains-for-a-project-to-the-given-deploy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Points all production domains for a project to the given deploy

> Allows users to rollback to a deployment.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/projects/{projectId}/rollback/{deploymentId}
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
  /v1/projects/{projectId}/rollback/{deploymentId}:
    post:
      tags:
        - projects
      summary: Points all production domains for a project to the given deploy
      description: Allows users to rollback to a deployment.
      operationId: requestRollback
      parameters:
        - name: projectId
          in: path
          required: true
          schema:
            type: string
        - name: deploymentId
          description: The ID of the deployment to rollback *to*
          in: path
          required: true
          schema:
            type: string
            description: The ID of the deployment to rollback *to*
        - name: description
          description: The reason for the rollback
          in: query
          required: false
          schema:
            type: string
            description: The reason for the rollback
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
        '201':
          description: ''
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '402':
          description: ''
        '403':
          description: You do not have permission to access this resource.
        '409':
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