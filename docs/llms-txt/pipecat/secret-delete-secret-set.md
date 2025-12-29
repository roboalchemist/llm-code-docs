# Source: https://docs.pipecat.ai/deployment/pipecat-cloud/rest-reference/endpoint/secret-delete-secret-set.md

# Delete Entire Secret Set

> Delete an entire secret set by its name. This operation removes the secret set and all associated key-value pairs.



## OpenAPI

````yaml DELETE /secrets/{setName}
openapi: 3.0.0
info:
  title: Pipecat Cloud - Delete Secret Set
  version: 1.0.0
  description: Delete an entire secret set via Pipecat Cloud Private API
servers:
  - url: https://api.pipecat.daily.co/v1
    description: API server
security:
  - PrivateKeyAuth: []
paths:
  /secrets/{setName}:
    delete:
      summary: Delete an entire secret set
      description: Permanently removes a secret set and all its associated secrets.
      operationId: deleteSecretSet
      parameters:
        - name: setName
          in: path
          required: true
          description: Name of the secret set to delete
          schema:
            type: string
            pattern: ^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$
            minLength: 3
            maxLength: 63
      responses:
        '200':
          description: Secret set successfully deleted
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    enum:
                      - OK
              example:
                status: OK
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