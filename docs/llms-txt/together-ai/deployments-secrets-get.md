# Source: https://docs.together.ai/reference/deployments-secrets-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Secret

> Retrieve details of a specific secret by its ID or name



## OpenAPI

````yaml GET /deployments/secrets/{id}
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
    get:
      tags:
        - Secrets
      summary: Get a secret by ID or name
      description: Retrieve details of a specific secret by its ID or name
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: Secret ID or name
            type: string
      responses:
        '200':
          description: Secret details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SecretResponseItem'
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

            secret = client.beta.jig.secrets.retrieve("my-secret")
            print(secret)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const secret = await client.beta.jig.secrets.retrieve("my-secret");
            console.log(secret);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const secret = await client.beta.jig.secrets.retrieve("my-secret");
            console.log(secret);
        - lang: Shell
          label: cURL
          source: |
            curl -X GET \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/deployments/secrets/my-secret
components:
  schemas:
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