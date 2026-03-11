# Source: https://docs.together.ai/reference/deleteendpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Endpoint

> Permanently deletes an endpoint. This action cannot be undone.



## OpenAPI

````yaml DELETE /endpoints/{endpointId}
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
  /endpoints/{endpointId}:
    delete:
      tags:
        - Endpoints
      summary: Delete endpoint
      description: Permanently deletes an endpoint. This action cannot be undone.
      operationId: deleteEndpoint
      parameters:
        - name: endpointId
          in: path
          required: true
          schema:
            type: string
            description: The ID of the endpoint to delete
            example: endpoint-d23901de-ef8f-44bf-b3e7-de9c1ca8f2d7
      responses:
        '204':
          description: No Content - Endpoint successfully deleted
        '403':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Internal error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
      x-codeSamples:
        - lang: Python
          label: Together AI SDK (v2)
          source: |
            # Docs for v1 can be found by changing the above selector ^
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            endpoint = client.endpoints.delete("endpoint-id")

            print(endpoint)
        - lang: Python
          label: Together AI SDK (v1)
          source: |
            from together import Together
            import os

            client = Together(
                api_key=os.environ.get("TOGETHER_API_KEY"),
            )

            endpoint = client.endpoints.delete(
                endpoint_id="endpoint-id",
            )

            print(endpoint)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const endpoint = await client.endpoints.delete("endpoint-id");

            console.log(endpoint);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";

            const client = new Together({
              apiKey: process.env.TOGETHER_API_KEY,
            });

            const endpoint = await client.endpoints.delete("endpoint-id");

            console.log(endpoint);
        - lang: Shell
          label: cURL
          source: >
            curl -X "DELETE" "https://api.together.xyz/v1/endpoints/endpoint-id"
            \
                 -H "Authorization: Bearer $TOGETHER_API_KEY"
components:
  schemas:
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

Built with [Mintlify](https://mintlify.com).