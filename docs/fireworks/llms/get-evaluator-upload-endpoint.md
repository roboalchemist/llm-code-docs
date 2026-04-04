# Source: https://docs.fireworks.ai/api-reference/get-evaluator-upload-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Evaluator Upload Endpoint

> Returns signed URLs for uploading evaluator source code (**step 3** in the
[Create Evaluator](/api-reference/create-evaluator) workflow). After receiving
the signed URL, upload your `.tar.gz` archive using HTTP `PUT` with
`Content-Type: application/octet-stream` header.



## OpenAPI

````yaml post /v1/accounts/{account_id}/evaluators/{evaluator_id}:getUploadEndpoint
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
  /v1/accounts/{account_id}/evaluators/{evaluator_id}:getUploadEndpoint:
    post:
      tags:
        - Gateway
      summary: Get Evaluator Upload Endpoint
      description: >-
        Returns signed URLs for uploading evaluator source code (**step 3** in
        the

        [Create Evaluator](/api-reference/create-evaluator) workflow). After
        receiving

        the signed URL, upload your `.tar.gz` archive using HTTP `PUT` with

        `Content-Type: application/octet-stream` header.
      operationId: Gateway_GetEvaluatorUploadEndpoint
      parameters:
        - name: account_id
          in: path
          required: true
          description: The Account Id
          schema:
            type: string
        - name: evaluator_id
          in: path
          required: true
          description: The Evaluator Id
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GatewayGetEvaluatorUploadEndpointBody'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayGetEvaluatorUploadEndpointResponse'
components:
  schemas:
    GatewayGetEvaluatorUploadEndpointBody:
      type: object
      properties:
        filenameToSize:
          type: object
          additionalProperties:
            type: string
            format: int64
        readMask:
          type: string
      required:
        - filenameToSize
    gatewayGetEvaluatorUploadEndpointResponse:
      type: object
      properties:
        filenameToSignedUrls:
          type: object
          additionalProperties:
            type: string
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````