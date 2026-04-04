# Source: https://docs.fireworks.ai/api-reference/validate-model-upload.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Validate Model Upload



## OpenAPI

````yaml get /v1/accounts/{account_id}/models/{model_id}:validateUpload
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
  /v1/accounts/{account_id}/models/{model_id}:validateUpload:
    get:
      tags:
        - Gateway
      summary: Validate Model Upload
      operationId: Gateway_ValidateModelUpload
      parameters:
        - name: skipHfConfigValidation
          description: If true, skip the Hugging Face config validation.
          in: query
          required: false
          schema:
            type: boolean
        - name: trustRemoteCode
          description: If true, trusts remote code when validating the Hugging Face config.
          in: query
          required: false
          schema:
            type: boolean
        - name: configOnly
          description: If true, skip tokenizer and parameter name validation.
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
                $ref: '#/components/schemas/gatewayValidateModelUploadResponse'
components:
  schemas:
    gatewayValidateModelUploadResponse:
      type: object
      properties:
        warnings:
          type: array
          items:
            type: string
          title: Warnings generated during validation (e.g., unknown config fields)
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````