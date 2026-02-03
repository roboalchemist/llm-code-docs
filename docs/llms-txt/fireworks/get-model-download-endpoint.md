# Source: https://docs.fireworks.ai/api-reference/get-model-download-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Model Download Endpoint



## OpenAPI

````yaml get /v1/accounts/{account_id}/models/{model_id}:getDownloadEndpoint
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
  /v1/accounts/{account_id}/models/{model_id}:getDownloadEndpoint:
    get:
      tags:
        - Gateway
      summary: Get Model Download Endpoint
      operationId: Gateway_GetModelDownloadEndpoint
      parameters:
        - name: readMask
          description: >-
            The fields to be returned in the response. If empty or "*", all
            fields will be returned.
          in: query
          required: false
          schema:
            type: string
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: model_id
          in: path
          required: true
          description: The Model Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayGetModelDownloadEndpointResponse'
components:
  schemas:
    gatewayGetModelDownloadEndpointResponse:
      type: object
      properties:
        filenameToSignedUrls:
          type: object
          additionalProperties:
            type: string
          title: Signed URLs for for downloading model files
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````