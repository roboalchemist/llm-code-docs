# Source: https://docs.fireworks.ai/api-reference/delete-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Deployment



## OpenAPI

````yaml delete /v1/accounts/{account_id}/deployments/{deployment_id}
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.21.6
servers:
  - url: https://api.fireworks.ai
security:
  - BearerAuth: []
tags:
  - name: Gateway
paths:
  /v1/accounts/{account_id}/deployments/{deployment_id}:
    delete:
      tags:
        - Gateway
      summary: Delete Deployment
      operationId: Gateway_DeleteDeployment
      parameters:
        - name: hard
          description: If true, this will perform a hard deletion.
          in: query
          required: false
          schema:
            type: boolean
        - name: ignoreChecks
          description: >-
            If true, this will ignore checks and force the deletion of a
            deployment that is currently

            deployed and is in use.
          in: query
          required: false
          schema:
            type: boolean
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: deployment_id
          in: path
          required: true
          description: The Deployment Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                type: object
                properties: {}
components:
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````