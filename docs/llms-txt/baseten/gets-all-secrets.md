# Source: https://docs.baseten.co/reference/management-api/secrets/gets-all-secrets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Get all secrets



## OpenAPI

````yaml get /v1/secrets
openapi: 3.1.0
info:
  description: REST API for management of Baseten resources
  title: Baseten management API
  version: 1.0.0
servers:
  - url: https://api.baseten.co
security:
  - ApiKeyAuth: []
paths:
  /v1/secrets:
    get:
      summary: Gets all secrets
      responses:
        '200':
          description: A list of Baseten secrets.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SecretsV1'
components:
  schemas:
    SecretsV1:
      description: A list of Baseten secrets.
      properties:
        secrets:
          items:
            $ref: '#/components/schemas/SecretV1'
          title: Secrets
          type: array
      required:
        - secrets
      title: SecretsV1
      type: object
    SecretV1:
      description: A Baseten secret. Note that we do not support retrieving secret values.
      properties:
        created_at:
          description: Time the secret was created in ISO 8601 format
          format: date-time
          title: Created At
          type: string
        name:
          description: Name of the secret
          title: Name
          type: string
        team_name:
          description: Name of the team the secret belongs to
          title: Team Name
          type: string
      required:
        - created_at
        - name
        - team_name
      title: SecretV1
      type: object
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Authorization
      description: >-
        You must specify the scheme 'Api-Key' in the Authorization header. For
        example, `Authorization: Api-Key <Your_Api_Key>`

````