# Source: https://docs.fireworks.ai/api-reference/validate-dataset-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Validate Dataset Upload



## OpenAPI

````yaml post /v1/accounts/{account_id}/datasets/{dataset_id}:validateUpload
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
  /v1/accounts/{account_id}/datasets/{dataset_id}:validateUpload:
    post:
      tags:
        - Gateway
      summary: Validate Dataset Upload
      operationId: Gateway_ValidateDatasetUpload
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: dataset_id
          in: path
          required: true
          description: The Dataset Id
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GatewayValidateDatasetUploadBody'
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
    GatewayValidateDatasetUploadBody:
      type: object
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````