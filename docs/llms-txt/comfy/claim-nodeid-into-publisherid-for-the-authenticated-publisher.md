# Source: https://docs.comfy.org/api-reference/registry/claim-nodeid-into-publisherid-for-the-authenticated-publisher.md

# Claim nodeId into publisherId for the authenticated publisher

> This endpoint allows a publisher to claim an unclaimed node that they own the repo, which is identified by the nodeId. The unclaimed node's repository must be owned by the authenticated user.


## OpenAPI

````yaml https://api.comfy.org/openapi post /publishers/{publisherId}/nodes/{nodeId}/claim-my-node
paths:
  path: /publishers/{publisherId}/nodes/{nodeId}/claim-my-node
  method: post
  servers:
    - url: https://api.comfy.org
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        publisherId:
          schema:
            - type: string
              required: true
        nodeId:
          schema:
            - type: string
              required: true
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              GH_TOKEN:
                allOf:
                  - description: >-
                      GitHub token to verify if the user owns the repo of the
                      node
                    type: string
            required: true
            refIdentifier: '#/components/schemas/ClaimMyNodeRequest'
            requiredProperties:
              - GH_TOKEN
        examples:
          example:
            value:
              GH_TOKEN: <string>
  response:
    '204':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Node claimed successfully
        examples: {}
        description: Node claimed successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
              message:
                allOf:
                  - &ref_1
                    type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: &ref_2
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Bad request, invalid input data
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: |
          Forbidden - various authorization and permission issues
          Includes:
          - The authenticated user does not have permission to claim the node
          - The node is already claimed by another publisher
          - The GH_TOKEN is invalid
          - The repository is not owned by the authenticated GitHub user
    '429':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Too many requests - GitHub API rate limit exceeded
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Internal server error
    '503':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties: *ref_2
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Service unavailable - GitHub API is currently unavailable
  deprecated: false
  type: path
components:
  schemas: {}

````