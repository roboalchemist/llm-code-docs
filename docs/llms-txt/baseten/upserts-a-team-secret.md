# Source: https://docs.baseten.co/reference/management-api/teams/upserts-a-team-secret.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Upsert a team secret

> Creates a new secret or updates an existing secret if one with the provided name already exists. The name and creation date of the created or updated secret is returned. This secret belongs to the specified team



## OpenAPI

````yaml post /v1/teams/{team_id}/secrets
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
  /v1/teams/{team_id}/secrets:
    parameters:
      - $ref: '#/components/parameters/team_id'
    post:
      summary: Upserts a secret in a team
      description: >-
        Creates a new secret or updates an existing secret if one with the
        provided name already exists. The name and creation date of the created
        or updated secret is returned. This secret belongs to the specified team
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpsertSecretRequestV1'
        required: true
      responses:
        '200':
          description: >-
            A Baseten secret. Note that we do not support retrieving secret
            values.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SecretV1'
components:
  parameters:
    team_id:
      schema:
        type: string
      name: team_id
      in: path
      required: true
  schemas:
    UpsertSecretRequestV1:
      description: A request to create or update a Baseten secret by name.
      properties:
        name:
          description: Name of the new or existing secret
          examples:
            - my_secret
          title: Name
          type: string
        value:
          description: Value of the secret
          examples:
            - my_secret_value
          title: Value
          type: string
      required:
        - name
        - value
      title: UpsertSecretRequestV1
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