# Source: https://docs.together.ai/reference/deployments-secrets-update.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Secret

> Update an existing secret's value or metadata



## OpenAPI

````yaml PATCH /deployments/secrets/{id}
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /deployments/secrets/{id}:
    patch:
      tags:
        - Secrets
      summary: Update a secret
      description: Update an existing secret's value or metadata
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: Secret ID or name
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateSecretRequest'
        description: Updated secret configuration
        required: true
      responses:
        '200':
          description: Secret updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SecretResponseItem'
        '400':
          description: Invalid request
          content:
            application/json:
              schema:
                type: object
        '404':
          description: Secret not found
          content:
            application/json:
              schema:
                type: object
        '500':
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            from together import Together
            client = Together()

            client.beta.jig.secrets.update("my-secret", value="my-new-value")
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: >
            import Together from "together-ai";

            const client = new Together();


            await client.beta.jig.secrets.update("my-secret", { value:
            "my-new-value" });
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: >
            import Together from "together-ai";

            const client = new Together();


            await client.beta.jig.secrets.update("my-secret", { value:
            "my-new-value" });
        - lang: Shell
          label: cURL
          source: |
            curl -X PATCH \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  --data '{ "value": "my-new-value" }' \
                  https://api.together.ai/v1/deployments/secrets/my-secret
components:
  schemas:
    UpdateSecretRequest:
      properties:
        description:
          description: >-
            Description is an optional human-readable description of the
            secret's purpose (max 500 characters)
          maxLength: 500
          type: string
        name:
          description: >-
            Name is the new unique identifier for the secret. Can contain
            alphanumeric characters, underscores, hyphens, forward slashes, and
            periods (1-100 characters)
          maxLength: 100
          minLength: 1
          type: string
        project_id:
          description: >-
            ProjectID is ignored - the project is automatically determined from
            your authentication
          type: string
        value:
          description: >-
            Value is the new sensitive data to store securely. Updating this
            will replace the existing secret value
          minLength: 1
          type: string
      type: object
    SecretResponseItem:
      properties:
        created_at:
          description: CreatedAt is the ISO8601 timestamp when this secret was created
          type: string
        created_by:
          description: CreatedBy is the identifier of the user who created this secret
          type: string
        description:
          description: Description is a human-readable description of the secret's purpose
          type: string
        id:
          description: ID is the unique identifier for this secret
          type: string
        last_updated_by:
          description: >-
            LastUpdatedBy is the identifier of the user who last updated this
            secret
          type: string
        name:
          description: Name is the name/key of the secret
          type: string
        object:
          description: The object type, which is always `secret`.
          const: secret
        updated_at:
          description: UpdatedAt is the ISO8601 timestamp when this secret was last updated
          type: string
      type: object
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).