# Source: https://docs.together.ai/reference/deployments-secrets-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Secrets

> Retrieve all secrets in your project



## OpenAPI

````yaml GET /deployments/secrets
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
  /deployments/secrets:
    get:
      tags:
        - Secrets
      summary: Get the list of project secrets
      description: Retrieve all secrets in your project
      responses:
        '200':
          description: List of secrets
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListSecretsResponse'
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

            secrets = client.beta.jig.secrets.list()
            print(secrets)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const secrets = await client.beta.jig.secrets.list();
            console.log(secrets);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const secrets = await client.beta.jig.secrets.list();
            console.log(secrets);
components:
  schemas:
    ListSecretsResponse:
      properties:
        data:
          description: Data is the array of secret items
          items:
            $ref: '#/components/schemas/SecretResponseItem'
          type: array
        object:
          description: The object type, which is always `list`.
          const: list
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