# Source: https://docs.fireworks.ai/api-reference/get-evaluator-source-code-endpoint.md

# Get Evaluator Source Code Endpoint

> Returns a signed URL to download the evaluator's source code archive.
Useful for debugging or reviewing the uploaded code.



## OpenAPI

````yaml get /v1/accounts/{account_id}/evaluators/{evaluator_id}:getSourceCodeSignedUrl
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.15.25
servers:
  - url: https://api.fireworks.ai
security:
  - BearerAuth: []
tags:
  - name: Gateway
paths:
  /v1/accounts/{account_id}/evaluators/{evaluator_id}:getSourceCodeSignedUrl:
    get:
      tags:
        - Gateway
      summary: Get Evaluator Source Code Endpoint
      description: |-
        Returns a signed URL to download the evaluator's source code archive.
        Useful for debugging or reviewing the uploaded code.
      operationId: Gateway_GetEvaluatorSourceCodeEndpoint
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
        - name: evaluator_id
          in: path
          required: true
          description: The Evaluator Id
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/gatewayGetEvaluatorSourceCodeEndpointResponse
components:
  schemas:
    gatewayGetEvaluatorSourceCodeEndpointResponse:
      type: object
      properties:
        filenameToSignedUrls:
          type: object
          additionalProperties:
            type: string
          title: Mapping from filename to signed URL for downloading the source code
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.fireworks.ai/llms.txt