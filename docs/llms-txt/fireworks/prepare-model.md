# Source: https://docs.fireworks.ai/api-reference/prepare-model.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prepare Model for different precisions



## OpenAPI

````yaml post /v1/accounts/{account_id}/models/{model_id}:prepare
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
  /v1/accounts/{account_id}/models/{model_id}:prepare:
    post:
      tags:
        - Gateway
      summary: Prepare Model for different precisions
      operationId: Gateway_PrepareModel
      parameters:
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GatewayPrepareModelBody'
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
    GatewayPrepareModelBody:
      type: object
      properties:
        precision:
          $ref: '#/components/schemas/DeploymentPrecision'
          title: the precision with which the model will be prepared
        readMask:
          type: string
          title: >-
            The fields to be returned in the response. If empty or "*", all
            fields will be returned.

            This is added as is used in getResource()
    DeploymentPrecision:
      type: string
      enum:
        - PRECISION_UNSPECIFIED
        - FP16
        - FP8
        - FP8_MM
        - FP8_AR
        - FP8_MM_KV_ATTN
        - FP8_KV
        - FP8_MM_V2
        - FP8_V2
        - FP8_MM_KV_ATTN_V2
        - NF4
        - FP4
        - BF16
        - FP4_BLOCKSCALED_MM
        - FP4_MX_MOE
      default: PRECISION_UNSPECIFIED
      title: >-
        - PRECISION_UNSPECIFIED: if left unspecified we will treat this as a
        legacy model created before

        self serve
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````