# Source: https://docs.together.ai/reference/deployments-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Deployment

> Delete an existing deployment



## OpenAPI

````yaml DELETE /deployments/{id}
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
  /deployments/{id}:
    delete:
      tags:
        - Deployments
      summary: Delete a deployment
      description: Delete an existing deployment
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: Deployment ID or name
            type: string
      responses:
        '200':
          description: Deployment deleted successfully
          content:
            application/json:
              schema:
                type: object
        '404':
          description: Deployment not found
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

            deployment = client.beta.jig.destroy("my-deployment")
            print(deployment)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const deployment = await client.beta.jig.destroy("my-deployment");
            console.log(deployment);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const deployment = await client.beta.jig.destroy("my-deployment");
            console.log(deployment);
        - lang: Shell
          label: cURL
          source: |
            curl -X DELETE \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/deployments/my-deployment
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).