# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/checks/rerequest-a-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Rerequest a check

> Rerequest a selected check that has failed.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v1/deployments/{deploymentId}/checks/{checkId}/rerequest
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
  /v1/deployments/{deploymentId}/checks/{checkId}/rerequest:
    post:
      tags:
        - checks
      summary: Rerequest a check
      description: Rerequest a selected check that has failed.
      operationId: rerequestCheck
      parameters:
        - name: deploymentId
          description: The deployment to rerun the check for.
          in: path
          required: true
          schema:
            description: The deployment to rerun the check for.
            example: dpl_2qn7PZrx89yxY34vEZPD31Y9XVj6
            type: string
        - name: checkId
          description: The check to rerun
          in: path
          required: true
          schema:
            description: The check to rerun
            example: check_2qn7PZrx89yxY34vEZPD31Y9XVj6
            type: string
        - name: autoUpdate
          description: Mark the check as running
          in: query
          required: false
          schema:
            description: Mark the check as running
            type: boolean
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
                type: object
        '400':
          description: One of the provided values in the request query is invalid.
        '401':
          description: The request is not authorized.
        '403':
          description: You do not have permission to access this resource.
        '404':
          description: |-
            The deployment was not found
            Check was not found
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````