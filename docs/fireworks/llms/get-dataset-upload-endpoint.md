# Source: https://docs.fireworks.ai/api-reference/get-dataset-upload-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Dataset Upload Endpoint



## OpenAPI

````yaml post /v1/accounts/{account_id}/datasets/{dataset_id}:getUploadEndpoint
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
  /v1/accounts/{account_id}/datasets/{dataset_id}:getUploadEndpoint:
    post:
      tags:
        - Gateway
      summary: Get Dataset Upload Endpoint
      operationId: Gateway_GetDatasetUploadEndpoint
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
              $ref: '#/components/schemas/GatewayGetDatasetUploadEndpointBody'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayGetDatasetUploadEndpointResponse'
components:
  schemas:
    GatewayGetDatasetUploadEndpointBody:
      type: object
      properties:
        filenameToSize:
          type: object
          additionalProperties:
            type: string
            format: int64
          description: A mapping from the file name to its size in bytes.
        readMask:
          type: string
          description: >-
            The fields to be returned in the response. If empty or "*", all
            fields will be returned.
      required:
        - filenameToSize
    gatewayGetDatasetUploadEndpointResponse:
      type: object
      properties:
        filenameToSignedUrls:
          type: object
          additionalProperties:
            type: string
          title: Signed URLs for uploading dataset files
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````