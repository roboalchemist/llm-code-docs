# Source: https://vercel.mintlify-docs-rest-api-reference.com/docs/rest-api/reference/endpoints/aliases/assign-an-alias.md

> ## Documentation Index
> Fetch the complete documentation index at: https://vercel.mintlify.app/docs/rest-api/reference/llms.txt
> Use this file to discover all available pages before exploring further.

# Assign an Alias

> Creates a new alias for the deployment with the given deployment ID. The authenticated user or team must own this deployment. If the desired alias is already assigned to another deployment, then it will be removed from the old deployment and assigned to the new one.



## OpenAPI

````yaml https://spec.speakeasy.com/vercel/vercel-docs/vercel-oas-with-code-samples post /v2/deployments/{id}/aliases
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
  /v2/deployments/{id}/aliases:
    post:
      tags:
        - aliases
      summary: Assign an Alias
      description: >-
        Creates a new alias for the deployment with the given deployment ID. The
        authenticated user or team must own this deployment. If the desired
        alias is already assigned to another deployment, then it will be removed
        from the old deployment and assigned to the new one.
      operationId: assignAlias
      parameters:
        - name: id
          description: The ID of the deployment the aliases should be listed for
          in: path
          required: true
          schema:
            description: The ID of the deployment the aliases should be listed for
            example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
            oneOf:
              - type: string
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
              properties:
                alias:
                  description: >-
                    The alias we want to assign to the deployment defined in the
                    URL
                  example: my-alias.vercel.app
                  type: string
                redirect:
                  description: >-
                    The redirect property will take precedence over the
                    deployment id from the URL and consists of a hostname (like
                    test.com) to which the alias should redirect using status
                    code 307
                  example: null
                  type: string
                  nullable: true
              type: object
        required: true
      responses:
        '200':
          description: The alias was successfully assigned to the deployment
          content:
            application/json:
              schema:
                properties:
                  uid:
                    type: string
                    description: The unique identifier of the alias
                    example: 2WjyKQmM8ZnGcJsPWMrHRHrE
                  alias:
                    type: string
                    description: The assigned alias name
                    example: my-alias.vercel.app
                  created:
                    type: string
                    format: date-time
                    description: The date when the alias was created
                    example: '2017-04-26T23:00:34.232Z'
                  oldDeploymentId:
                    nullable: true
                    type: string
                    description: >-
                      The unique identifier of the previously aliased
                      deployment, only received when the alias was used before
                    example: dpl_FjvFJncQHQcZMznrUm9EoB8sFuPa
                required:
                  - alias
                  - created
                  - uid
                type: object
        '400':
          description: |-
            One of the provided values in the request body is invalid.
            One of the provided values in the request query is invalid.
            The cert for the provided alias is not ready
            The deployment is not READY and can not be aliased
            The supplied alias is invalid
        '401':
          description: The request is not authorized.
        '402':
          description: |-
            The account was soft-blocked for an unhandled reason.
            The account is missing a payment so payment method must be updated
        '403':
          description: |-
            You do not have permission to access this resource.
            If no .vercel.app alias exists then we fail (nothing to mirror)
        '404':
          description: |-
            The domain used for the alias was not found
            The deployment was not found
        '409':
          description: |-
            The provided alias is already assigned to the given deployment
            The domain is not allowed to be used
      security:
        - bearerToken: []
components:
  securitySchemes:
    bearerToken:
      type: http
      description: Default authentication mechanism
      scheme: bearer

````