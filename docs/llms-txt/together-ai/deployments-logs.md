# Source: https://docs.together.ai/reference/deployments-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Deployment Logs

> Retrieve logs from a deployment, optionally filtered by replica ID.



## OpenAPI

````yaml GET /deployments/{id}/logs
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
  /deployments/{id}/logs:
    get:
      tags:
        - Deployments
      summary: Get logs for a deployment
      description: Retrieve logs from a deployment, optionally filtered by replica ID.
      parameters:
        - name: id
          in: path
          required: true
          schema:
            description: Deployment ID or name
            type: string
        - name: replica_id
          in: query
          required: false
          schema:
            description: Replica ID to filter logs
            type: string
      responses:
        '200':
          description: Deployment logs
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeploymentLogs'
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

            deployment = client.beta.jig.logs("my-deployment")
            print(deployment)
        - lang: TypeScript
          label: Together AI SDK (TypeScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const deployment = await client.beta.jig.logs("my-deployment");
            console.log(deployment);
        - lang: JavaScript
          label: Together AI SDK (JavaScript)
          source: |
            import Together from "together-ai";
            const client = new Together();

            const deployment = await client.beta.jig.logs("my-deployment");
            console.log(deployment);
        - lang: Shell
          label: cURL
          source: |
            curl -X GET \
                  -H "Authorization: Bearer $TOGETHER_API_KEY" \
                  https://api.together.ai/v1/deployments/my-deployment/logs
components:
  schemas:
    DeploymentLogs:
      properties:
        lines:
          type: array
          items:
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