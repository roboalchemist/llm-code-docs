# Source: https://docs.fireworks.ai/api-reference/get-evaluator-build-log-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Evaluator Build Log Endpoint

> Returns a signed URL to download the evaluator's build logs. Useful for
debugging `BUILD_FAILED` state.



## OpenAPI

````yaml get /v1/accounts/{account_id}/evaluators/{evaluator_id}:getBuildLogEndpoint
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
  /v1/accounts/{account_id}/evaluators/{evaluator_id}:getBuildLogEndpoint:
    get:
      tags:
        - Gateway
      summary: Get Evaluator Build Log Endpoint
      description: |-
        Returns a signed URL to download the evaluator's build logs. Useful for
        debugging `BUILD_FAILED` state.
      operationId: Gateway_GetEvaluatorBuildLogEndpoint
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
                  #/components/schemas/gatewayGetEvaluatorBuildLogEndpointResponse
components:
  schemas:
    gatewayGetEvaluatorBuildLogEndpointResponse:
      type: object
      properties:
        buildLogSignedUri:
          type: string
          title: Signed URL for the build log
  securitySchemes:
    BearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>
      bearerFormat: API_KEY

````