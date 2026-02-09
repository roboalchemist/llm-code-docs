# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/rest-reference/endpoint/secret-list-all.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pipecat.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List All Secret Sets

> Retrieve a list of all secret sets in your organization with their name and secret type.



## OpenAPI

````yaml GET /secrets
openapi: 3.0.0
info:
  title: Pipecat Cloud - List Secret Sets
  version: 1.0.0
  description: List all secret sets via Pipecat Cloud Private API
servers:
  - url: https://api.pipecat.daily.co/v1
    description: API server
security:
  - PrivateKeyAuth: []
paths:
  /secrets:
    get:
      summary: List all secret sets
      description: Retrieve a list of all secret sets for the organization.
      operationId: listSecretSets
      responses:
        '200':
          description: List of secret sets
          content:
            application/json:
              schema:
                type: object
                properties:
                  sets:
                    type: array
                    items:
                      $ref: '#/components/schemas/SecretSetSummary'
              example:
                sets:
                  - name: my-app-secrets
                    type: secret
                    region: us-west
                  - name: dockerhub-credentials
                    type: imagePullSecret
                    region: us-west
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Unauthorized
                code: UNAUTHORIZED
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - PrivateKeyAuth: []
components:
  schemas:
    SecretSetSummary:
      type: object
      properties:
        name:
          type: string
          description: Name of the secret set
        type:
          type: string
          enum:
            - secret
            - imagePullSecret
          description: Type of the secret set
        region:
          type: string
          description: The region where the secret set is stored
    ErrorResponse:
      type: object
      properties:
        error:
          type: string
          description: Error message
        code:
          type: string
          description: Error code
  securitySchemes:
    PrivateKeyAuth:
      type: http
      scheme: bearer
      description: >-
        Authentication requires a Pipecat Cloud Private API token.


        Generate a Private API key from your Dashboard (Settings > API Keys >
        Private > Create key) and include it as a Bearer token in the
        Authorization header.

````