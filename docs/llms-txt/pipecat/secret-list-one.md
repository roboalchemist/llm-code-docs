# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/rest-reference/endpoint/secret-list-one.md

# Get Secret Set Details

> Retrieve key and value pairs for a specific secret set.



## OpenAPI

````yaml GET /secrets/{setName}
openapi: 3.0.0
info:
  title: Pipecat Cloud - Get Secret Set
  version: 1.0.0
  description: Get a specific secret set via Pipecat Cloud Private API
servers:
  - url: https://api.pipecat.daily.co/v1
    description: API server
security:
  - PrivateKeyAuth: []
paths:
  /secrets/{setName}:
    get:
      summary: Get a specific secret set
      description: >-
        Retrieve the keys (not values) of a specific secret set. Image pull
        secrets cannot be retrieved.
      operationId: getSecretSet
      parameters:
        - name: setName
          in: path
          required: true
          description: Name of the secret set to retrieve
          schema:
            type: string
            pattern: ^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$
            minLength: 3
            maxLength: 63
      responses:
        '200':
          description: Secret set details
          content:
            application/json:
              schema:
                type: object
                properties:
                  region:
                    type: string
                    description: The region where the secret set is stored
                  secrets:
                    type: array
                    items:
                      $ref: '#/components/schemas/SecretKey'
              example:
                region: us-west
                secrets:
                  - fieldName: API_KEY
                  - fieldName: DATABASE_URL
                  - fieldName: JWT_SECRET
        '400':
          description: Bad request - Cannot retrieve image pull secrets
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Cannot retrieve image pull secrets by name
                code: GENERIC_BAD_REQUEST
        '401':
          description: Unauthorized - Invalid or missing API key
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Unauthorized
                code: UNAUTHORIZED
        '404':
          description: Secret set not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              example:
                error: Set not found
                code: NOT_FOUND
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
    SecretKey:
      type: object
      properties:
        fieldName:
          type: string
          description: Name of the secret key (values are not returned for security)
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.pipecat.ai/llms.txt