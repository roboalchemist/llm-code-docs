# Source: https://docs.openpipe.ai/api-reference/get-listModels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Models

> List all models for a project.



## OpenAPI

````yaml get /models
openapi: 3.0.3
info:
  title: OpenPipe API
  description: The public API for reporting API calls to OpenPipe
  version: 0.1.1
servers:
  - url: https://api.openpipe.ai/api/v1
security: []
paths:
  /models:
    get:
      description: List all models for a project.
      operationId: listModels
      parameters: []
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  object:
                    type: string
                    enum:
                      - list
                  data:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                        object:
                          type: string
                          enum:
                            - model
                        description:
                          type: string
                          nullable: true
                        created:
                          type: string
                        updated:
                          type: string
                        openpipe:
                          type: object
                          properties:
                            baseModel:
                              type: string
                            hyperparameters:
                              type: object
                              additionalProperties: {}
                              nullable: true
                            status:
                              type: string
                              enum:
                                - PENDING
                                - TRAINING
                                - DEPLOYED
                                - ERROR
                                - DEPRECATED
                                - PENDING_DEPRECATION
                                - QUEUED
                                - PROVISIONING
                            datasetId:
                              type: string
                            errorMessage:
                              type: string
                              nullable: true
                          required:
                            - baseModel
                            - hyperparameters
                            - status
                            - datasetId
                            - errorMessage
                          additionalProperties: false
                        contextWindow:
                          type: number
                        maxCompletionTokens:
                          type: number
                        capabilities:
                          type: array
                          items:
                            type: string
                            enum:
                              - chat
                              - tools
                              - json
                        pricing:
                          type: object
                          properties:
                            chatIn:
                              type: number
                              description: $/million tokens
                            chatOut:
                              type: number
                              description: $/million tokens
                          required:
                            - chatIn
                            - chatOut
                          additionalProperties: false
                        owned_by:
                          type: string
                      required:
                        - id
                        - name
                        - object
                        - description
                        - created
                        - updated
                        - openpipe
                        - contextWindow
                        - maxCompletionTokens
                        - capabilities
                        - pricing
                        - owned_by
                      additionalProperties: false
                required:
                  - object
                  - data
                additionalProperties: false
        default:
          $ref: '#/components/responses/error'
      security:
        - Authorization: []
components:
  responses:
    error:
      description: Error response
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
              code:
                type: string
              issues:
                type: array
                items:
                  type: object
                  properties:
                    message:
                      type: string
                  required:
                    - message
                  additionalProperties: false
            required:
              - message
              - code
            additionalProperties: false
  securitySchemes:
    Authorization:
      type: http
      scheme: bearer

````