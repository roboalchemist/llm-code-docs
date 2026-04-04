# Source: https://docs.fireworks.ai/api-reference/scale-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scale Deployment to a specific number of replicas or to zero



## OpenAPI

````yaml patch /v1/accounts/{account_id}/deployments/{deployment_id}:scale
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
  /v1/accounts/{account_id}/deployments/{deployment_id}:scale:
    patch:
      tags:
        - Gateway
      summary: Scale Deployment to a specific number of replicas or to zero
      operationId: Gateway_ScaleDeployment
      parameters:
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GatewayScaleDeploymentBody'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                type: object
                properties: {}
components:
  schemas:
    GatewayScaleDeploymentBody:
      type: object
      properties:
        replicaCount:
          type: integer
          format: int32
          description: The desired number of replicas.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````