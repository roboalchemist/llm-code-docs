# Source: https://docs.together.ai/reference/deployments-secrets-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Secret

> Delete an existing secret



## OpenAPI

````yaml DELETE /deployments/secrets/{id}
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
    delete:
      tags:
        - Secrets
      summary: Delete a secret
      description: Delete an existing secret
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: Secret ID or name
            type: string
      responses:
        '200':
          description: Secret deleted successfully
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

            client.beta.jig.secrets.delete("my-secret")
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            await client.beta.jig.secrets.delete("my-secret");
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            await client.beta.jig.secrets.delete("my-secret");
        - lang: Shell
          label: cURL
          source: |
            curl -X DELETE \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/deployments/secrets/my-secret
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).