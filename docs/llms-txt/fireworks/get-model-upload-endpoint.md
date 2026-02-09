# Source: https://docs.fireworks.ai/api-reference/get-model-upload-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Model Upload Endpoint



## OpenAPI

````yaml post /v1/accounts/{account_id}/models/{model_id}:getUploadEndpoint
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
  /v1/accounts/{account_id}/models/{model_id}:getUploadEndpoint:
    post:
      tags:
        - Gateway
      summary: Get Model Upload Endpoint
      operationId: Gateway_GetModelUploadEndpoint
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
              $ref: '#/components/schemas/GatewayGetModelUploadEndpointBody'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/gatewayGetModelUploadEndpointResponse'
components:
  schemas:
    GatewayGetModelUploadEndpointBody:
      type: object
      properties:
        filenameToSize:
          type: object
          additionalProperties:
            type: string
            format: int64
          description: A mapping from the file name to its size in bytes.
        enableResumableUpload:
          type: boolean
          description: If true, enable resumable upload instead of PUT.
        readMask:
          type: string
          description: >-
            The fields to be returned in the response. If empty or "*", all
            fields will be returned.
      required:
        - filenameToSize
    gatewayGetModelUploadEndpointResponse:
      type: object
      properties:
        filenameToSignedUrls:
          type: object
          additionalProperties:
            type: string
          title: Signed URLs for uploading model files
        filenameToUnsignedUris:
          type: object
          additionalProperties:
            type: string
          description: >-
            Unsigned URIs (e.g. s3://bucket/key, gs://bucket/key) for uploading
            model files.

            Returned when the caller has permission to upload to the URIs.
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````